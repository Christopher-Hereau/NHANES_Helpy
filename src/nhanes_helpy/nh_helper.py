import math
import pandas as pd
import re
from pathlib import Path

from .code_details_demo import (
    CYCLES,
    # DEMO_VARS,
    DEMO_CATALOG,
    # SAS_TO_SHORT_DEMO,
    SDDSRVYR_TO_CYCLE,
)
from .code_details_diet import (
    DIET_CATALOG,
)
from .code_details_lab import LAB_CATALOG, LAB_GROUPS, LAB_FILES, LAB_REPLICATE_COLUMNS
from .code_details_questions import (
    QUESTION_CATALOG,
    mask_sentinels,
    kind_for as q_kind_for,
    sentinel_codes,
    DRUG_LOOKUP_TABLE,
    DRUG_CODE_COLUMNS,
    DRUG_NAME_COLUMN,
    DRUG_GRAIN,
)
from .code_details_exam import EXAM_CATALOG, mask_sentinels as exam_mask_sentinels



YEAR_RE = re.compile(r"(?P<y1>\d{4})-(?P<y2>\d{4})", re.IGNORECASE)
YEAR_PREFIX = re.compile(
    r"^(?P<y1>\d{4})-(?P<y2>\d{4})\s*(?P<name>.+)$",
    re.IGNORECASE,
)
DATA_FOLDER_RE = re.compile(r"^(?P<cat>.+?)_data$", re.IGNORECASE)
# Jackknife replicates are prefix + 01–52, not analysis weights like
# WTSPH2YR, WTANA6YR, or WTSSCB2Y. drop_replicates drops only the replicates.
JACKKNIFE_COL_RE = re.compile(
    r"^(?:WT[A-Z]*|wt_jk_[a-z0-9_]+?)(?:0[1-9]|[1-4]\d|5[0-2])$",
    re.IGNORECASE,
)

DEMO_REPLICATE_COLUMNS = (
    ["SDJ1REPN"]
    + [f"WTIREP{i:02d}" for i in range(1, 53)]
    + [f"WTMREP{i:02d}" for i in range(1, 53)]
)
REPLICATE_COLUMNS = list(dict.fromkeys(
    DEMO_REPLICATE_COLUMNS + list(LAB_REPLICATE_COLUMNS)
))


def _cycle_from_years(y1: str, y2: str) -> str:
    return f"{y1[-2:]}-{y2[-2:]}"


def _cycle_sort_key(cycle: str) -> tuple[int, int]:
    """Store cycles in asc year order"""
    a, b = cycle.split("-")
    y1 = 1900 + int(a) if int(a) >= 50 else 2000 + int(a)
    y2 = 1900 + int(b) if int(b) >= 50 else 2000 + int(b)
    return (y1, y2)


def _find_cycle(path: Path) -> str | None:
    for part in (path.stem, *reversed(path.parts)):
        m = YEAR_RE.search(part)
        if m:
            return _cycle_from_years(m["y1"], m["y2"])
    return None


def _find_category(path: Path) -> str:
    for part in reversed(path.parts[:-1]):
        m = DATA_FOLDER_RE.match(part)
        if m:
            return m["cat"]
    return path.parent.name


def _table_name(path: Path) -> str:
    m = YEAR_PREFIX.match(path.stem)
    if not m:
        return path.stem
    name = m["name"].strip()
    # 1999-2000_DIET.csv leaves a leading separator; the tag is DIET.
    name = name.lstrip("_- ")
    if "~ " in name:
        name = name.split("~ ", 1)[1].strip()
    return name


def _has_seqn(df: pd.DataFrame) -> bool:
    return any(col.upper() == "SEQN" for col in df.columns)

def _decode_sas_bytes(df: pd.DataFrame) -> pd.DataFrame:
    """Turn SAS bytes (b'GIN', b'10001567', b'') into str / None."""
    df = df.copy()
    df.columns = [
        c.decode("latin-1") if isinstance(c, bytes) else str(c)
        for c in df.columns
    ]

    def _cell(val):
        if isinstance(val, bytes):
            text = val.decode("latin-1")
            return None if text == "" else text
        if val is None or (isinstance(val, float) and pd.isna(val)):
            return None
        if isinstance(val, str) and val == "":
            return None
        return val

    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].map(_cell)

    return df

def _seqn_col(df: pd.DataFrame) -> str | None:
    for col in df.columns:
        if str(col).upper() == "SEQN":
            return str(col)
    return None


def _is_jackknife_column(name: str) -> bool:
    """True only for jackknife replicate weights (WT*01-52 and listed reps).

    Analysis weights of every kind are kept: WTMEC2YR, WTSPH2YR, WTANA6YR,
    WTSSCB2Y, WTSSMC4Y, and so on. Surplus columns in compressed data are
    identified by the _SP suffix and dropped by surplus=False, not here.
    """
    text = str(name)
    if text in REPLICATE_COLUMNS or text.upper() in {c.upper() for c in REPLICATE_COLUMNS}:
        return True
    return bool(JACKKNIFE_COL_RE.fullmatch(text))


def drop_replicate_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Drop demographic and lab jackknife replicate weights."""
    drop = [c for c in df.columns if _is_jackknife_column(str(c))]
    if not drop:
        return df
    return df.drop(columns=drop)


def _merge_frames_by_seqn(frames: list[pd.DataFrame]) -> pd.DataFrame:
    """Outer-join person tables on SEQN; coalesce overlapping columns."""
    out = None
    for df in frames:
        key = _seqn_col(df)
        if not key:
            continue
        part = df
        if key != "SEQN":
            part = part.rename(columns={key: "SEQN"})
        if part["SEQN"].duplicated().any():
            part = part.drop_duplicates(subset=["SEQN"], keep="first")
        if out is None:
            out = part.copy()
            continue
        overlap = [c for c in part.columns if c != "SEQN" and c in out.columns]
        merged = out.merge(part, on="SEQN", how="outer", suffixes=("", "__new"))
        for col in overlap:
            new = f"{col}__new"
            if new in merged.columns:
                merged[col] = merged[col].where(merged[col].notna(), merged[new])
                merged.drop(columns=[new], inplace=True)
        out = merged
    if out is None:
        raise KeyError("No SEQN columns to merge")
    return out


def _insert_cycle(df: pd.DataFrame, cycle: str) -> pd.DataFrame:
    """Put the source cycle string in a column immediately after SEQN."""
    out = df.copy()
    out["cycle"] = cycle
    key = next((c for c in out.columns if str(c).upper() == "SEQN"), None)
    ordered = [c for c in out.columns if c != "cycle"]
    if key is None:
        ordered = ["cycle"] + ordered
    else:
        at = ordered.index(key) + 1
        ordered = ordered[:at] + ["cycle"] + ordered[at:]
    return out[ordered]


def _want_all_tables(table: str | None) -> bool:
    return table is not None and str(table).strip().lower() in {"all", "*", "every"}


def _years_from_cycle(cycle: str) -> str:
    """Rebuild a YYYY-YYYY token that index_nhanes_xpt maps back to cycle."""
    a, b = str(cycle).split("-")
    y1 = 1900 + int(a) if int(a) >= 50 else 2000 + int(a)
    y2 = 1900 + int(b) if int(b) >= 50 else 2000 + int(b)
    return f"{y1}-{y2}"


# Layout tags written flat by compress_layouts. Decompress_Data rebuilds
# the *_data folders from these names.
_LAYOUT_FOLDERS = {
    "DEMO": "Demographics_data",
    "DIET": "Dietary_data",
    "IFF": "Dietary_data",
    "EXAM": "Examination_data",
    "LABS": "Laboratory_data",
    "POOL": "Laboratory_data",
    "QUESTIONS": "Questionnaire_data",
    "PAQIAF": "Questionnaire_data",
    "RXQ_RX": "Questionnaire_data",
}


def index_nhanes_xpt(data_dir: str | Path) -> tuple[list[dict], set[str]]:
    """Index XPT and CSV paths. Does not read file contents."""
    data_dir = Path(data_dir)
    paths = sorted(
        (
            p for p in data_dir.rglob("*")
            if p.is_file() and p.suffix.lower() in {".xpt", ".csv"}
        ),
        key=lambda p: p.as_posix().lower(),
    )
    records: list[dict] = []
    demo_cycles: set[str] = set()
    for path in paths:
        cycle = _find_cycle(path)
        if not cycle:
            print(f"skip (no year prefix): {path}")
            continue
        category = _find_category(path)
        table = _table_name(path)
        records.append({
            "path": path,
            "cycle": cycle,
            "category": category,
            "table": table,
        })
        if category.lower() == "demographics":
            demo_cycles.add(cycle)
    return records, demo_cycles


def _read_csv(path: Path, drop_replicates: bool = True, drop_impute_flags: bool = True) -> pd.DataFrame:
    """Read one layout CSV written by compress_layouts or Decompress_Data."""
    df = pd.read_csv(path, low_memory=False)
    if drop_impute_flags:
        drop = [c for c in ("DMAETHN", "DMARACE") if c in df.columns]
        if drop:
            df = df.drop(columns=drop)
    if drop_replicates:
        df = drop_replicate_columns(df)
    return df


def _read_frame(path: Path, drop_replicates: bool = True, drop_impute_flags: bool = True) -> pd.DataFrame:
    """Read an XPT or CSV layout file."""
    if Path(path).suffix.lower() == ".csv":
        return _read_csv(path, drop_replicates=drop_replicates, drop_impute_flags=drop_impute_flags)
    return _read_xpt(path, drop_replicates=drop_replicates, drop_impute_flags=drop_impute_flags)


def _read_xpt(path: Path, drop_replicates: bool = True, drop_impute_flags: bool = True) -> pd.DataFrame:
    """Read one XPT, decode SAS bytes, and apply the same column drops as before.

    CDC files are classic XPORT and pandas reads them. Sample files written by
    pyreadstat are SAS V8 transport (LIBV8), which pandas rejects, so fall back.
    """
    try:
        df = pd.read_sas(path, format="xport")
    except ValueError as exc:
        if "XPORT" not in str(exc) and "xport" not in str(exc).lower():
            raise
        try:
            import pyreadstat
        except ImportError as missing:
            raise ValueError(
                f"{path} is not classic XPORT. Install pyreadstat to read "
                "SAS V8 transport sample files."
            ) from missing
        df, _meta = pyreadstat.read_xport(path)
    df = _decode_sas_bytes(df)
    if drop_impute_flags:
        drop = [c for c in ("DMAETHN", "DMARACE") if c in df.columns]
        if drop:
            df = df.drop(columns=drop)
    if drop_replicates:
        df = drop_replicate_columns(df)
    return df


def load_nhanes_xpt(data_dir: str | Path, drop_replicates: bool = True, drop_impute_flags: bool = True)-> dict:
    """Eager load. Prefer the helper index; this remains for callers that want every frame."""
    records, demo_cycles = index_nhanes_xpt(data_dir)
    data: dict = {}
    info: dict = {}
    for rec in records:
        try:
            df = _read_frame(rec["path"], drop_replicates=drop_replicates, drop_impute_flags=drop_impute_flags)
        except Exception as e:
            print(f"skip (read failed): {rec['path']} ({e})")
            continue
        use_info = (not _has_seqn(df)) or (rec["cycle"] not in demo_cycles)
        target = info if use_info else data
        target.setdefault(rec["cycle"], {}).setdefault(rec["category"], {})[rec["table"]] = df

    out: dict = {}
    for cycle in sorted(data, key=_cycle_sort_key):
        out[cycle] = {
            cat: {
                name: data[cycle][cat][name]
                for name in sorted(data[cycle][cat])
            }
            for cat in sorted(data[cycle])
        }
    out["Info"] = {}
    for cycle in sorted(info, key=_cycle_sort_key):
        out["Info"][cycle] = {
            cat: {
                name: info[cycle][cat][name]
                for name in sorted(info[cycle][cat])
            }
            for cat in sorted(info[cycle])
        }
    return out





def _build_sas_to_short(vars_map: dict) -> dict:
    out = {}
    for spec in vars_map.values():
        sas = spec.get("sas")
        if sas:
            out[str(sas)] = spec["short"]
        for alias in (spec.get("sas_by_cycle") or {}).values():
            if alias:
                out[str(alias)] = spec["short"]
        for alias in spec.get("aliases") or []:
            if alias:
                out[str(alias)] = spec["short"]
        day_pair = spec.get("day_pair")
        if day_pair:
            out[str(day_pair)] = spec["short"]
    return out


def sas_name(spec: dict, cycle: str | None = None) -> str | None:
    if cycle and cycle in (spec.get("sas_by_cycle") or {}):
        return spec["sas_by_cycle"][cycle]
    return spec.get("sas")


def codes_for(spec: dict, cycle: str | None = None) -> dict | None:
    if cycle and cycle in (spec.get("codes_by_cycle") or {}):
        return spec["codes_by_cycle"][cycle]
    return spec.get("codes")


def raw_codes_for(spec: dict, cycle: str | None = None) -> dict | None:
    raw_by = spec.get("raw_codes_by_cycle") or {}
    if cycle and cycle in raw_by:
        return raw_by[cycle]
    if spec.get("raw_codes"):
        return spec["raw_codes"]
    return codes_for(spec, cycle)


def kind_for(spec: dict, cycle: str | None = None) -> str:
    by = spec.get("kind_by_cycle") or {}
    if cycle and cycle in by:
        return by[cycle]
    if spec.get("short") == "hhref_age" and cycle in {"17-18", "21-23"}:
        return "categorical"
    return spec["kind"]


def target_for(spec: dict, cycle: str | None = None) -> str:
    tgt_by = spec.get("target_by_cycle") or {}
    if cycle and cycle in tgt_by:
        return tgt_by[cycle]
    return spec.get("target") or ""


def definition_for(spec: dict, cycle: str | None = None) -> str:
    def_by = spec.get("definition_by_cycle") or {}
    if cycle and cycle in def_by:
        return def_by[cycle]
    return spec.get("definition") or spec.get("text") or ""


def notes_for(spec: dict) -> str:
    return spec.get("notes") or ""


def _short_names(vars_map: dict) -> set[str]:
    return {spec["short"] for spec in vars_map.values()}


def _norm_table(name: str) -> str:
    n = str(name).upper()
    n = re.sub(r"\.(XPT|CSV|SAS7BDAT)$", "", n)
    n = re.sub(r"^P_", "", n)
    n = re.sub(r"_[A-Z]$", "", n)
    return n

def _component_grain(name: str) -> str | None:
    """Grain from a codebook component title, for files not named by SAS stem."""
    key = " ".join(str(name).casefold().split())
    return _COMPONENT_GRAIN.get(key)


def _grain_from_name(name: str, columns=None) -> str | None:
    """Name- or column-based grain when the catalog key does not match the loaded file."""
    raw = re.sub(r"[^A-Z0-9_]", "", str(name).upper())
    stem = _norm_table(name)
    titled = _component_grain(name)
    if titled:
        return titled
    if (
        stem.startswith("RXQ_RX")
        or stem.startswith("RXQANA")
        or "RXQ_RX" in raw
        or "RXQRX" in raw
        or raw.startswith("RXQANA")
    ):
        return "drugs"
    if stem.startswith("PAQIAF") or "PAQIAF" in raw:
        return "activity"
    if stem in {"RXQ_DRUG", "RXQDRUG"} or "RXQ_DRUG" in raw:
        return "lookup"
    if columns is None:
        cols = set()
    else:
        cols = {str(c).upper() for c in list(columns)}
    if "RXDDRUG" in cols or "RXDDRGID" in cols:
        return "drugs"
    return None


def _normalize_grain(grain: str | None) -> str | None:
    """Map user grain names onto catalog grains. drugs is the RXQ_RX event grain."""
    if grain is None:
        return None
    g = str(grain).lower().strip()
    return {
        "total": "person",
        "totals": "person",
        "person-level": "person",
        "foods": "food",
        "iff": "food",
        "item": "food",
        "items": "food",
        "drug": "drugs",
        "drugs": "drugs",
        "medication": "drugs",
        "medications": "drugs",
        "rx": "drugs",
        "prescription": "drugs",
        "activity": "activity",
        "activities": "activity",
        "paqiaf": "activity",
    }.get(g, g)


def _infer_table_kind(name: str) -> dict:
    raw = str(name).upper()
    stem = _norm_table(name)
    grain = None
    day = None
    # Layout tags written by compress_layouts / Decompress_Data.
    tag = stem.lstrip("_")
    if tag in {"IFF"} or "IFF" in stem or "INDIVIDUAL FOOD" in raw:
        grain = "food"
    elif tag in {"POOL"} or "POL" in stem or "POOL" in raw:
        grain = "pool"
    elif tag in {"PAQIAF"} or stem.startswith("PAQIAF"):
        grain = "activity"
    elif tag in {"RXQ_RX", "RXQRX"} or stem.startswith("RXQ_RX"):
        grain = "drugs"
    elif tag in {"DIET", "DEMO", "EXAM", "LABS", "QUESTIONS"}:
        grain = "person"
    elif "FCD" in stem or "MCD" in stem or "FOOD CODE" in raw or "MODIFICATION CODE" in raw:
        grain = "support"
    elif "TOT" in stem or "TOTAL NUTRIENT" in raw:
        grain = "person"
    if stem.startswith("DR2") or "SECOND DAY" in raw or "DAY 2" in raw:
        day = 2
    elif stem.startswith("DR1") or stem.startswith("DRX") or "FIRST DAY" in raw or "DAY 1" in raw:
        day = 1
    return {"grain": grain, "day": day}




_KNOWN_CATALOGS = (DEMO_CATALOG, DIET_CATALOG, LAB_CATALOG, QUESTION_CATALOG, EXAM_CATALOG)


def _catalog_record(raw: dict) -> dict:
    vars_map = raw["vars"]
    return {
        "name": raw["name"].lower(),
        "aliases": tuple(a.lower() for a in raw.get("aliases") or (raw["name"],)),
        "vars": vars_map,
        "sas_to_short": raw.get("sas_to_short") or _build_sas_to_short(vars_map),
        "grain": raw.get("grain") or "person",
        "tables": dict(raw.get("tables") or {}),
    }


CATALOGS = {c["name"]: c for c in (_catalog_record(x) for x in _KNOWN_CATALOGS)}


def _build_component_grain() -> dict[str, str]:
    """Component title -> grain. Skip titles that map to more than one grain."""
    found: dict[str, set[str]] = {}
    for cat in CATALOGS.values():
        for meta in (cat.get("tables") or {}).values():
            title = meta.get("component")
            grain = (meta.get("grain") or "").lower()
            if not title or not grain:
                continue
            key = " ".join(str(title).casefold().split())
            found.setdefault(key, set()).add(grain)
    return {key: next(iter(grains)) for key, grains in found.items() if len(grains) == 1}


_COMPONENT_GRAIN = _build_component_grain()


def _state(df: pd.DataFrame) -> dict:
    return dict(
        df.attrs.get("nhanes_state")
        or df.attrs.get("demo_state")
        or {"columns": "sas", "rows": "codes", "cycle": None, "category": None}
    )


def _set_state(df: pd.DataFrame, **kwargs) -> None:
    st = _state(df)
    st.update(kwargs)
    df.attrs["nhanes_state"] = st
    df.attrs["demo_state"] = st


def _guess_column_state(df: pd.DataFrame, sas_to_short: dict, short_names: set[str]) -> str:
    cols = {str(c) for c in df.columns}
    bases = {_base_col(c) for c in cols}
    n_sas = len((cols | bases) & set(sas_to_short))
    n_short = len((cols | bases) & short_names)
    if n_short > n_sas:
        return "short"
    return "sas"


_NEAR_ZERO = 1e-8
_NEAR_INT = 1e-6
# Denormal / export underflow. Real NHANES weights and lab results are not this small.
_NEAR_ZERO_NUMERIC = 1e-10


def _canonicalize_code(val, keys: set | None = None):
    """Collapse export artifacts (denormals, 1.0) onto codebook integers."""
    if pd.isna(val):
        return val
    if isinstance(val, str):
        return val
    try:
        f = float(val)
    except (TypeError, ValueError):
        return val
    if not math.isfinite(f):
        return val
    if abs(f) < _NEAR_ZERO:
        snapped = 0
    else:
        nearest = round(f)
        snapped = int(nearest) if abs(f - nearest) <= _NEAR_INT else val
    if keys is None:
        return snapped
    if snapped in keys:
        return snapped
    best, best_d = None, _NEAR_INT
    for key in keys:
        try:
            d = abs(f - float(key))
        except (TypeError, ValueError):
            continue
        if d < best_d:
            best, best_d = key, d
    return best if best is not None else val


def _clean_categorical_series(s: pd.Series, codes: dict | None = None) -> pd.Series:
    """Fix denormal / float codes on a categorical column before label mapping."""
    if s.empty:
        return s.astype(object)
    keys = set(codes) if codes else None
    num = pd.to_numeric(s, errors="coerce")
    cleaned = []
    for raw, nval in zip(s.tolist(), num.tolist()):
        if pd.isna(raw):
            cleaned.append(pd.NA)
            continue
        if pd.isna(nval):
            cleaned.append(raw)
            continue
        cleaned.append(_canonicalize_code(nval, keys))
    return pd.Series(cleaned, index=s.index, dtype="object")


def _snap_near_zero_series(s: pd.Series, thresh: float = _NEAR_ZERO_NUMERIC) -> pd.Series:
    """Coerce |x| < thresh to 0 on a numeric-like column. Leaves labels alone."""
    if s.empty:
        return s
    num = pd.to_numeric(s, errors="coerce")
    if not num.notna().any():
        return s
    snapped = num.mask(num.abs() < thresh, 0.0)
    if pd.api.types.is_numeric_dtype(s) and not pd.api.types.is_bool_dtype(s):
        return snapped
    # Mixed / string storage of numbers: only replace rows that parsed as numeric.
    out = pd.Series(s.tolist(), index=s.index, dtype="object")
    mask = num.notna()
    out.loc[mask] = snapped.loc[mask].tolist()
    return out


def _base_col(name: str) -> str:
    """Strip compression suffixes so catalog lookup still matches.

    Removes a __<table> suffix and a trailing _SP. Does not strip a
    trailing number: SSJO_1, SSMI_2, and SSPL_12 are real SAS names.
    """
    text = str(name)
    if "__" in text:
        text = text.split("__", 1)[0]
    if text.upper().endswith("_SP"):
        text = text[:-3]
    return text


def _strip_enum(name: str):
    """Split a trailing _<digits> without regex. Returns (base, n) or (name, None)."""
    text = str(name)
    cut = text.rfind("_")
    if cut <= 0:
        return text, None
    tail = text[cut + 1:]
    if tail.isdigit():
        return text[:cut], int(tail)
    return text, None


def _values_agree(left: pd.Series, right: pd.Series) -> bool:
    """True when overlapping non-null values match. Complementary nulls are ok."""
    both = left.notna() & right.notna()
    if not both.any():
        return True
    a = left[both]
    b = right[both]
    if pd.api.types.is_numeric_dtype(a) and pd.api.types.is_numeric_dtype(b):
        import numpy as np
        return bool(np.allclose(
            a.to_numpy(dtype=float),
            b.to_numpy(dtype=float),
            rtol=1e-5,
            atol=1e-8,
            equal_nan=True,
        ))
    return bool(a.astype(str).equals(b.astype(str)))


def _is_surplus_column(name: str) -> bool:
    """True for columns compress_layouts marked as surplus (_SP)."""
    return str(name).upper().endswith("_SP")


def drop_surplus_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Drop surplus columns identified by the _SP suffix."""
    drop = [c for c in df.columns if _is_surplus_column(str(c))]
    if not drop:
        return df
    return df.drop(columns=drop)


def collapse_surplus_duplicates(
    df: pd.DataFrame,
    known: set[str] | None = None,
) -> pd.DataFrame:
    """Merge identical enumerated surplus copies of the same column.

    Only NAME_SP / NAME_2_SP / NAME_3_SP are a group, and only when NAME_2
    is not itself a SAS name. SSJO_1, SSPL_7, SSPL_12 stay separate even if
    every row is the same non-detect fill. A group is merged only when the
    overlapping values agree. The first column is kept as NAME_SP.
    """
    if df is None or not len(df.columns):
        return df
    known_up = {str(name).upper() for name in (known or set()) if name}
    # stem (without _SP) -> column, for columns that are real SAS names
    # or plain surplus copies.
    plain: dict[str, str] = {}
    copies: dict[str, list[tuple[int, str, str]]] = {}
    for col in df.columns:
        text = str(col)
        if not text.upper().endswith("_SP"):
            continue
        stem = text[:-3]
        stem_up = stem.upper()
        if stem_up in known_up:
            plain[stem_up] = text
            continue
        base, n = _strip_enum(stem)
        if n is None or n < 2:
            continue
        base_up = base.upper()
        # Numbered form is a real analyte (SSPL_7), not a collision copy.
        if stem_up in known_up or f"{base}_{n}".upper() in known_up:
            continue
        # Only an enumeration of this exact main name.
        if base_up not in known_up and base_up not in plain:
            continue
        copies.setdefault(base_up, []).append((n, text, base))
    if not copies:
        return df
    out = df.copy()
    drop: list[str] = []
    for base_up, items in copies.items():
        items = sorted(items)
        anchor = plain.get(base_up) or items[0][1]
        if not all(_values_agree(out[anchor], out[col]) for _, col, _ in items):
            continue
        base_case = next((base for _, _, base in items), base_up)
        target = plain.get(base_up) or f"{base_case}_SP"
        series = None
        cols = ([plain[base_up]] if base_up in plain else []) + [col for _, col, _ in items]
        for col in cols:
            cur = out[col]
            series = cur.copy() if series is None else series.combine_first(cur)
        if target not in out.columns:
            loc = int(out.columns.get_loc(items[0][1]))
            out.insert(loc, target, series)
        else:
            out[target] = series
        for col in cols:
            if col != target:
                drop.append(col)
    if drop:
        out = out.drop(columns=list(dict.fromkeys(drop)))
    return out


def _matching_columns(df: pd.DataFrame, name: str) -> list[str]:
    """Columns that are exactly name, or name__TABLE from a compressed layout."""
    if name not in df.columns and not any(str(c).startswith(name + "__") for c in df.columns):
        return []
    return [
        c for c in df.columns
        if str(c) == name or str(c).startswith(name + "__")
    ]


def _snap_near_zero_frame(
    out: pd.DataFrame,
    vars_map: dict | None,
    cycle: str | None,
    col_state: str,
    thresh: float = _NEAR_ZERO_NUMERIC,
) -> None:
    """Zero-out denormals on continuous / weight columns (and uncatalogued numerics)."""
    handled = set()
    if vars_map:
        for spec in vars_map.values():
            kind = kind_for(spec, cycle)
            if kind not in {"continuous", "weight", "flag"}:
                continue
            name = _active_name(spec, cycle, col_state)
            targets = _matching_columns(out, name)
            if not targets:
                alt = spec.get("short") if col_state != "short" else spec.get("sas")
                if alt:
                    targets = _matching_columns(out, alt)
            for name in targets:
                out[name] = _snap_near_zero_series(out[name], thresh)
                handled.add(name)
    skip = handled | {"seqn", "SEQN"}
    for col in out.columns:
        if col in skip:
            continue
        s = out[col]
        if pd.api.types.is_numeric_dtype(s) and not pd.api.types.is_bool_dtype(s):
            out[col] = _snap_near_zero_series(s, thresh)


def _map_value(val, lookup: dict):
    if pd.isna(val):
        return val
    keys = set(lookup)
    val = _canonicalize_code(val, keys)
    if val in lookup:
        return lookup[val]
    try:
        ival = int(val)
    except (TypeError, ValueError):
        return val
    return lookup.get(ival, val)


def _active_name(spec: dict, cycle: str | None, col_state: str) -> str:
    if col_state == "short":
        return spec["short"]
    return sas_name(spec, cycle)


def _row_col_requested(name: str, spec: dict, cycle: str, wanted: set[str]) -> bool:
    aliases = {str(name), str(spec["short"])}
    sas = sas_name(spec, cycle)
    if sas:
        aliases.add(str(sas))
    for extra in (spec.get("sas_by_cycle") or {}).values():
        if extra:
            aliases.add(str(extra))
    for extra in spec.get("aliases") or []:
        if extra:
            aliases.add(str(extra))
    day_pair = spec.get("day_pair")
    if day_pair:
        aliases.add(str(day_pair))
    return not wanted.isdisjoint(aliases)


def infer_cycle(df: pd.DataFrame, cycle: str | None = None) -> str | None:
    if cycle:
        return cycle
    state = _state(df)
    if state.get("cycle"):
        return state["cycle"]
    if "SDDSRVYR" in df.columns:
        col = "SDDSRVYR"
    elif "sddsrvyr" in df.columns:
        col = "sddsrvyr"
    elif "release_cycle" in df.columns:
        col = "release_cycle"
    else:
        return None
    vals = pd.to_numeric(df[col], errors="coerce").dropna().unique()
    found = set()
    for val in vals:
        try:
            mapped = SDDSRVYR_TO_CYCLE.get(int(val))
        except (TypeError, ValueError):
            continue
        if mapped:
            found.add(mapped)
    if len(found) == 1:
        return next(iter(found))
    return None


def _cycle_series(df: pd.DataFrame, vars_map: dict) -> pd.Series | None:
    if "SDDSRVYR" in df.columns:
        raw = pd.to_numeric(df["SDDSRVYR"], errors="coerce")
    elif "sddsrvyr" in df.columns:
        raw = pd.to_numeric(df["sddsrvyr"], errors="coerce")
    elif "release_cycle" in df.columns:
        raw = df["release_cycle"]
        spec = vars_map.get("release_cycle")
        if spec and spec.get("codes") and raw.dtype == object:
            inv = {label: code for code, label in spec["codes"].items()}
            raw = raw.map(lambda v, m=inv: _map_value(v, m))
        raw = pd.to_numeric(raw, errors="coerce")
    else:
        return None
    return raw.map(lambda v: SDDSRVYR_TO_CYCLE.get(int(v)) if pd.notna(v) else None)


def _ensure_object(df: pd.DataFrame, name: str) -> None:
    if name not in df.columns:
        return
    if str(df[name].dtype) != "object":
        df[name] = df[name].astype(object)


def _apply_row_map(out, spec, cycle, col_state, row_cols, to_labels: bool, indexer=None) -> bool:
    name = _active_name(spec, cycle, col_state)
    targets = _matching_columns(out, name)
    if not targets:
        return False
    if row_cols is not None and not _row_col_requested(name, spec, cycle or "", row_cols):
        return False
    if kind_for(spec, cycle) != "categorical":
        return False
    codes = codes_for(spec, cycle)
    if not codes:
        return False
    lookup = codes if to_labels else {label: code for code, label in codes.items()}
    for name in targets:
        # loc assignment will not upcast a numeric column. Convert first so
        # label strings and <NA> can be written into cycle-sliced rows.
        if to_labels:
            _ensure_object(out, name)
            cleaned = _clean_categorical_series(
                out.loc[indexer, name] if indexer is not None else out[name],
                codes,
            )
            if indexer is None:
                out[name] = cleaned
            else:
                out.loc[indexer, name] = cleaned
        _ensure_object(out, name)
        if indexer is None:
            out[name] = out[name].map(lambda v, m=lookup: _map_value(v, m))
        else:
            out.loc[indexer, name] = out.loc[indexer, name].map(
                lambda v, m=lookup: _map_value(v, m)
            )
    return True


def _map_rows(out, vars_map, cycle, col_state, row_cols, to_labels: bool) -> None:
    series = None if cycle else _cycle_series(out, vars_map)
    if cycle is not None:
        groups = [(cycle, None)]
    elif series is None:
        groups = [(None, None)]
    else:
        valid = series.dropna()
        uniq = valid.unique().tolist()
        if len(uniq) <= 1:
            groups = [(uniq[0] if uniq else None, None)]
        else:
            groups = [
                (cyc, idx)
                for cyc, idx in series.groupby(series, dropna=True).groups.items()
            ]
    for cyc, indexer in groups:
        for spec in vars_map.values():
            _apply_row_map(out, spec, cyc, col_state, row_cols, to_labels, indexer=indexer)


def _as_catalog_list(catalog, sas_to_short, catalogs) -> list[dict]:
    if catalogs:
        out = []
        for cat in catalogs:
            if not cat:
                continue
            vars_map = cat["vars"] if "vars" in cat else cat
            out.append(
                {
                    "vars": vars_map,
                    "sas_to_short": cat.get("sas_to_short") or _build_sas_to_short(vars_map),
                }
            )
        return out
    if catalog:
        return [{"vars": catalog, "sas_to_short": sas_to_short or _build_sas_to_short(catalog)}]
    return []


def _sanitize_frame_categoricals(out, vars_map, cycle, col_state, row_cols=None) -> None:
    """Snap denormal / float codes on categorical columns in place."""
    for spec in vars_map.values():
        if kind_for(spec, cycle) != "categorical":
            continue
        name = _active_name(spec, cycle, col_state)
        targets = _matching_columns(out, name)
        if not targets:
            continue
        if row_cols is not None and not _row_col_requested(name, spec, cycle or "", row_cols):
            continue
        codes = codes_for(spec, cycle)
        for name in targets:
            out[name] = _clean_categorical_series(out[name], codes)


def decode_frame(
    df: pd.DataFrame,
    cycle: str | None = None,
    rows: bool | list[str] = True,
    columns: bool = True,
    inplace: bool = False,
    catalog: dict | None = None,
    sas_to_short: dict | None = None,
    catalogs: list[dict] | None = None,
    category: str | None = None,
) -> pd.DataFrame:
    cat_list = _as_catalog_list(catalog, sas_to_short, catalogs)
    out = df if inplace else df.copy()
    st = _state(out)
    cycle = infer_cycle(out, cycle)
    merged_sas, merged_short, merged_vars = {}, set(), {}
    for cat in cat_list:
        merged_sas.update(cat["sas_to_short"])
        merged_short |= _short_names(cat["vars"])
        merged_vars.update(cat["vars"])
    col_state = st.get("columns") or (
        _guess_column_state(out, merged_sas, merged_short) if merged_vars else "sas"
    )
    row_state = st.get("rows") or "codes"
    row_cols = None if isinstance(rows, bool) else {str(c) for c in rows}
    if columns and merged_sas and col_state != "short":
        rename, taken = {}, set(map(str, out.columns))
        for col in list(out.columns):
            raw = str(col)
            base = _base_col(raw)
            short = merged_sas.get(raw) or merged_sas.get(base)
            if not short:
                continue
            # Surplus stays surplus: WTSSBI2Y_SP -> <short>_SP, never the
            # non-surplus short. A __<table> suffix is still preserved.
            surplus = _is_surplus_column(raw)
            if "__" in raw and raw != base:
                suffix = raw.split("__", 1)[1]
                new_name = f"{short}__{suffix}"
            else:
                new_name = f"{short}_SP" if surplus else short
            if new_name not in taken:
                rename[col] = new_name
                taken.add(new_name)
        if rename:
            out.rename(columns=rename, inplace=True)
        col_state = "short"
    if merged_vars:
        _sanitize_frame_categoricals(out, merged_vars, cycle, col_state, row_cols)
    if rows and merged_vars:
        _map_rows(out, merged_vars, cycle, col_state, row_cols, to_labels=True)
        row_state = "labels" if row_cols is None else "mixed"
    _set_state(out, columns=col_state, rows=row_state, cycle=cycle, category=category)
    return out


def encode_frame(
    df: pd.DataFrame,
    cycle: str | None = None,
    rows: bool | list[str] = True,
    columns: bool = True,
    inplace: bool = False,
    catalog: dict | None = None,
    sas_to_short: dict | None = None,
    catalogs: list[dict] | None = None,
    category: str | None = None,
) -> pd.DataFrame:
    cat_list = _as_catalog_list(catalog, sas_to_short, catalogs)
    out = df if inplace else df.copy()
    st = _state(out)
    cycle = infer_cycle(out, cycle)
    merged_sas, merged_short, merged_vars = {}, set(), {}
    for cat in cat_list:
        merged_sas.update(cat["sas_to_short"])
        merged_short |= _short_names(cat["vars"])
        merged_vars.update(cat["vars"])
    col_state = st.get("columns") or (
        _guess_column_state(out, merged_sas, merged_short) if merged_vars else "short"
    )
    row_state = st.get("rows") or "labels"
    row_cols = None if isinstance(rows, bool) else {str(c) for c in rows}
    if rows and merged_vars:
        _map_rows(out, merged_vars, cycle, col_state, row_cols, to_labels=False)
        row_state = "codes" if row_cols is None else "mixed"
    if columns and merged_vars and col_state != "sas":
        rename, taken = {}, set(map(str, out.columns))
        for spec in merged_vars.values():
            short = spec["short"]
            sas = sas_name(spec, cycle)
            if not sas:
                continue
            if short in out.columns and sas not in taken:
                rename[short] = sas
                taken.add(sas)
            surplus_short = f"{short}_SP"
            surplus_sas = f"{sas}_SP"
            if surplus_short in out.columns and surplus_sas not in taken:
                rename[surplus_short] = surplus_sas
                taken.add(surplus_sas)
        if rename:
            out.rename(columns=rename, inplace=True)
        col_state = "sas"
    _set_state(out, columns=col_state, rows=row_state, cycle=cycle, category=category)
    return out


def _mask_question_sentinels(df, category, cycle, rows):
    """Null refused/don't-know on questionnaire or exam numerics when rows are labels."""
    if rows != "labels":
        return df
    cat = str(category or "").lower()
    if cat in {"questionnaire", "questions", "question", "questionaire", "interview", "q"}:
        return mask_sentinels(df, cycle=cycle, vars_map=QUESTION_CATALOG["vars"])
    if cat in {"examination", "exam", "exams", "examinations", "mec exam", "mec examination", "sp exam"}:
        return exam_mask_sentinels(df, cycle=cycle, vars_map=EXAM_CATALOG["vars"])
    return df


class _SasCoerced(dict):
    """Dict of coerced short -> SAS names.

    Missing-key lookup returns a status string instead of raising:
    "present (not coerced)" if the short exists in the catalog,
    "not present" otherwise. Lookup is case-insensitive on the short name.
    """

    _PRESENT = "present (not coerced)"
    _ABSENT = "not present"

    def __init__(self, coerced: dict, known: set):
        super().__init__(coerced)
        self._known = {str(k) for k in known}
        self._known_upper = {k.upper(): k for k in self._known}
        self._upper = {str(k).upper(): k for k in coerced}

    def _resolve(self, key):
        s = str(key)
        if s in self:
            return s, True
        up = s.upper()
        if up in self._upper:
            return self._upper[up], True
        return s, False

    def __contains__(self, key) -> bool:
        _, found = self._resolve(key)
        return found

    def __getitem__(self, key):
        real, found = self._resolve(key)
        if found:
            return super().__getitem__(real)
        up = str(key).upper()
        if up in self._known_upper:
            return self._PRESENT
        return self._ABSENT

    def get(self, key, default=None):
        real, found = self._resolve(key)
        if found:
            return super().__getitem__(real)
        up = str(key).upper()
        if up in self._known_upper:
            return self._PRESENT
        return default if default is not None else self._ABSENT


class NHANES_Helper:
    """Index NHANES XPTs and load only the files a call needs.

    Init stores paths, cycle, category, and table name. It does not read
    the CSV/XPT contents. raw_data() and get_df() read the matching files and
    do not keep them on the instance.

    Replicates: jackknife replicates and the like are dropped by default
    Impute Flags:  are dropped by default, these are rare and generally related to categorical columns with inferred entries that are filled in their own columns
    Surplus: surplus samples are dropped by default, typically related to laboratory testing where person-specific tests were later replaced by testing pooled groups of serum.
    this method makes them incompatible with the same historical per-individual tests.

    
    """

    def __init__(
        self,
        data_dir: str | Path | None = None,
        drop_replicates: bool = True,
        drop_impute_flags: bool = True,
        surplus: bool = False,
        data: dict | None = None,
    ):
        self.catalogs = {k: dict(v) for k, v in CATALOGS.items()}
        self.drop_replicates = drop_replicates
        self.drop_impute_flags = drop_impute_flags
        self.surplus = surplus
        self.index: list[dict] = []
        self.demo_cycles: set[str] = set()
        self._eager = None
        if data is not None:
            # Backward compatible: a preloaded frame tree still works.
            self._eager = data
        elif data_dir is not None:
            self.index, self.demo_cycles = index_nhanes_xpt(data_dir)
        else:
            default = Path(__file__).resolve().parent / "sample_data"
            if default.is_dir():
                self.index, self.demo_cycles = index_nhanes_xpt(default)

    def Decompress_Data(
        self,
        compressed_dir: str | Path = "",
        destination: str | Path = "",
        log: bool = True,
    ) -> pd.DataFrame:
        """Split combined layout CSVs into one CSV per cycle per layout.

        compressed_dir is a flat Zenodo folder (DEMO.csv, LABS.csv,
        Info_Dietary.csv). destination receives the per-cycle tree:
        *_data/YYYY-YYYY_TAG.csv and Info/<set>/. Streams each layout file;
        grouped info files are split by their __info_stem tag.
        log=False silences progress prints.
        """
        import shutil

        compressed_dir = Path(compressed_dir)
        destination = Path(destination)
        if not compressed_dir.is_dir():
            raise FileNotFoundError(f"No compressed directory at {compressed_dir}")
        log_rows = []
        for src in sorted(compressed_dir.rglob("*")):
            if not src.is_file() or src.suffix.lower() != ".csv":
                continue
            if src.name.startswith("_"):
                continue
            # Grouped info: Info_<set>.csv (set name has no underscore)
            if re.match(r"^Info_[^_]+\.csv$", src.name):
                log_rows.extend(self._split_info_group(src, destination, log=log))
                continue
            rel_parts = src.relative_to(compressed_dir).parts
            info_dest = self._info_dest(src, destination, rel_parts)
            if info_dest is not None:
                info_dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, info_dest)
                log_rows.append({
                    "source": str(src),
                    "target": str(info_dest),
                    "cycle": None,
                    "rows": None,
                    "status": "copied",
                })
                if log:
                    print(f"info -> {info_dest}")
                continue
            folder = _LAYOUT_FOLDERS.get(src.stem.upper())
            if folder is None and src.parent.name.endswith("_data"):
                folder = src.parent.name
            if folder is None:
                if log:
                    print(f"skip (unknown layout tag): {src.name}")
                log_rows.append({
                    "source": str(src),
                    "target": None,
                    "cycle": None,
                    "rows": None,
                    "status": "skipped: unknown tag",
                })
                continue
            log_rows.extend(self._split_layout_csv(src, destination, folder, log=log))
        return pd.DataFrame(log_rows)

    def _info_dest(self, src: Path, destination: Path, rel_parts: tuple) -> Path | None:
        """Where an info file goes, or None if this is a layout file."""
        if "Info" in rel_parts:
            return destination / Path(*rel_parts[rel_parts.index("Info"):])
        name = src.name
        if not name.startswith("Info_"):
            return None
        rest = name[len("Info_"):]
        set_name, _, stem = rest.partition("_")
        if not set_name or not stem:
            return destination / "Info" / name
        return destination / "Info" / set_name / stem

    def _split_info_group(self, src: Path, destination: Path, log: bool = True) -> list[dict]:
        """Split a grouped Info_<set>.csv back into one file per original stem.

        Source rows are tagged with __info_stem. Each group is written to
        Info/<set>/<stem>.csv with the tag columns removed and all-NaN
        columns dropped, restoring the original frames.
        """
        m = re.match(r"^Info_([^_]+)\.csv$", src.name)
        if not m:
            return []
        set_name = m.group(1)
        try:
            df = pd.read_csv(src, low_memory=False)
        except Exception as exc:
            if log:
                print(f"skip info group (read failed): {src} ({exc})")
            return [{
                "source": str(src),
                "target": None,
                "cycle": None,
                "rows": None,
                "status": f"read failed: {exc}",
            }]
        if "__info_stem" not in df.columns:
            if log:
                print(f"skip info group (no __info_stem): {src}")
            return [{
                "source": str(src),
                "target": None,
                "cycle": None,
                "rows": None,
                "status": "skipped: no __info_stem",
            }]
        log_rows = []
        info_dir = destination / "Info" / set_name
        info_dir.mkdir(parents=True, exist_ok=True)
        tag_cols = [c for c in df.columns if str(c).startswith("__info_")]
        for stem, group in df.groupby("__info_stem", sort=False):
            sub = group.drop(columns=tag_cols, errors="ignore")
            sub = sub.dropna(axis=1, how="all")
            dest = info_dir / f"{stem}.csv"
            try:
                sub.to_csv(dest, index=False)
                status = "wrote"
            except Exception as exc:
                if log:
                    print(f"skip info (write failed): {dest} ({exc})")
                status = f"write failed: {exc}"
            log_rows.append({
                "source": str(src),
                "target": str(dest),
                "cycle": None,
                "rows": len(sub),
                "status": status,
            })
            if log:
                print(f"info {set_name}/{stem} -> {dest}")
        if not log_rows and log:
            print(f"info group empty: {src}")
        return log_rows

    def _split_layout_csv(self, src: Path, destination: Path, folder: str | None = None, log: bool = True) -> list[dict]:
        """Stream one combined CSV into one file per cycle. Constant memory.

        The combined header is every column from every cycle. A first pass
        records which columns are non-empty in each cycle. The second pass
        writes only those columns, so a cycle file does not carry columns
        that cycle never had.
        """
        import csv

        folder = folder or _LAYOUT_FOLDERS.get(src.stem.upper()) or src.parent.name
        tag = src.stem
        with src.open(newline="", encoding="utf-8") as fh:
            reader = csv.reader(fh)
            try:
                header = next(reader)
            except StopIteration:
                if log:
                    print(f"skip (empty): {src}")
                return [{
                    "source": str(src),
                    "target": None,
                    "cycle": None,
                    "rows": 0,
                    "status": "skipped: empty",
                }]
            if "cycle" not in header:
                if log:
                    print(f"skip (no cycle column): {src}")
                return [{
                    "source": str(src),
                    "target": None,
                    "cycle": None,
                    "rows": None,
                    "status": "skipped: no cycle column",
                }]
            cycle_idx = header.index("cycle")
            present: dict[str, set[int]] = {}
            counts: dict[str, int] = {}
            if log:
                print(f"scanning {src.name} for columns used by each cycle")
            for row in reader:
                if len(row) <= cycle_idx:
                    continue
                cycle = row[cycle_idx]
                used = present.get(cycle)
                if used is None:
                    used = {cycle_idx}
                    present[cycle] = used
                    counts[cycle] = 0
                counts[cycle] += 1
                for i, value in enumerate(row):
                    if value != "" and i not in used:
                        used.add(i)
        if not present:
            if log:
                print(f"skip (no rows): {src}")
            return [{
                "source": str(src),
                "target": None,
                "cycle": None,
                "rows": 0,
                "status": "skipped: no rows",
            }]

        keep = {
            cycle: sorted(indexes)
            for cycle, indexes in present.items()
        }
        writers: dict[str, csv.writer] = {}
        handles: dict[str, object] = {}
        log_rows = []
        try:
            with src.open(newline="", encoding="utf-8") as fh:
                reader = csv.reader(fh)
                next(reader, None)
                if log:
                    print(f"splitting {src.name}")
                seen = 0
                for row in reader:
                    if len(row) <= cycle_idx:
                        continue
                    seen += 1
                    cycle = row[cycle_idx]
                    writer = writers.get(cycle)
                    if writer is None:
                        years = _years_from_cycle(cycle)
                        dest = destination / folder / f"{years}_{tag}.csv"
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        out = dest.open("w", newline="", encoding="utf-8")
                        handles[cycle] = out
                        writer = csv.writer(out)
                        cols = keep[cycle]
                        writer.writerow([header[i] for i in cols])
                        writers[cycle] = writer
                    cols = keep[cycle]
                    writer.writerow([
                        row[i] if i < len(row) else ""
                        for i in cols
                    ])
                    if seen % 250000 == 0 and log:
                        print(f"  {seen} rows")
        finally:
            for handle in handles.values():
                handle.close()
        for cycle, n in counts.items():
            years = _years_from_cycle(cycle)
            dest = destination / folder / f"{years}_{tag}.csv"
            log_rows.append({
                "source": str(src),
                "target": str(dest),
                "cycle": cycle,
                "rows": n,
                "columns": len(keep[cycle]),
                "status": "wrote",
            })
            if log:
                print(
                    f"{cycle} {folder}/{tag}: {n} rows, "
                    f"{len(keep[cycle])} cols -> {dest.name}"
                )
        return log_rows

    def _using_eager(self) -> bool:
        return self._eager is not None

    def cycles(self) -> list[str]:
        if self._using_eager():
            return [c for c in self._eager if c != "Info"]
        found = {rec["cycle"] for rec in self.index}
        return [c for c in sorted(found, key=_cycle_sort_key)]

    def categories(self, cycle: str | None = None) -> list[str]:
        if self._using_eager():
            if cycle:
                return list(self._eager.get(cycle, {}))
            found = set()
            for c in self.cycles():
                found.update(self._eager[c])
            return sorted(found)
        if cycle:
            return sorted({rec["category"] for rec in self.index if rec["cycle"] == cycle})
        return sorted({rec["category"] for rec in self.index})

    def tables(self, category: str, cycle: str | None = None) -> list[str]:
        cat = self._match_category_name(category, cycle)
        if self._using_eager():
            if cycle:
                return list(self._eager.get(cycle, {}).get(cat, {}))
            names = set()
            for c in self.cycles():
                names.update(self._eager[c].get(cat, {}))
            return sorted(names)
        names = {
            rec["table"] for rec in self.index
            if rec["category"] == cat and (cycle is None or rec["cycle"] == cycle)
        }
        return sorted(names)

    def _records(self, cycle: str | None = None, category: str | None = None) -> list[dict]:
        out = []
        for rec in self.index:
            if cycle and rec["cycle"] != cycle:
                continue
            if category and rec["category"] != category:
                continue
            out.append(rec)
        return out

    def _read_record(self, rec: dict) -> pd.DataFrame:
        df = _read_frame(
            rec["path"],
            drop_replicates=self.drop_replicates,
            drop_impute_flags=self.drop_impute_flags,
        )
        if not self.surplus:
            df = drop_surplus_columns(df)
        return df

    def _load_tables(self, cycle: str, category: str) -> dict:
        """Read the XPTs for one cycle/category. Caller owns the frames."""
        if self._using_eager():
            return self._eager.get(cycle, {}).get(category, {})
        tables = {}
        for rec in self._records(cycle, category):
            try:
                tables[rec["table"]] = self._read_record(rec)
            except Exception as e:
                print(f"skip (read failed): {rec['path']} ({e})")
        return tables

    def raw_data(
        self,
        cycle: str | list[str] = "all",
        tables: str | list[str] = "all",
        grain: str | None = "person",
        set: str | None = None,
        day: int = 1,
    ) -> dict:
        """Load matching XPTs into {cycle: {category: {table: DataFrame}}}.

        Does not store the frames on the helper. cycle='All' and tables='All'
        are accepted. Pass set='Questionnaire' (or Exam, Dietary, Laboratory)
        to limit the category. grain filters person / food / drugs / activity / pool.
        """
        cycles = self._normalize_cycles(cycle)
        wanted_tables = None
        # `set` is a parameter, so it shadows the builtin type.
        seq_types = (list, tuple, type({}))
        if isinstance(tables, seq_types):
            wanted_tables = {str(t) for t in tables}
        elif tables is not None and str(tables).strip().lower() not in {"all", "*", "every"}:
            wanted_tables = {str(tables)}
        wanted_grain = _normalize_grain(grain) if grain else None
        if wanted_grain in {"all", "any"}:
            wanted_grain = None
        out: dict = {}
        categories = [self._match_category_name(set, None)] if set else None
        for cyc in cycles:
            cats = categories or self.categories(cyc)
            for cat_name in cats:
                loaded = self._load_tables(cyc, cat_name)
                if not loaded:
                    continue
                kept = {}
                for name, df in self._iter_merge_tables(cat_name, loaded, grain=wanted_grain, day=day):
                    if wanted_tables and name not in wanted_tables and _norm_table(name) not in {_norm_table(t) for t in wanted_tables}:
                        continue
                    kept[name] = df
                if kept:
                    out.setdefault(cyc, {})[cat_name] = kept
        if not out:
            raise KeyError(
                f"No raw tables for cycle={cycle!r}, set={set!r}, "
                f"tables={tables!r}, grain={grain!r}."
            )
        return out

    def available_cycles(
        self,
        set: str,
        grain: str | None = None,
        table: str | None = None,
        day: int = 1,
    ) -> list[str]:
        """Cycles that can serve this set/grain/table request."""
        found = []
        for c in self.cycles():
            try:
                self._one_table(set, c, table, grain=grain, day=day)
            except KeyError:
                continue
            found.append(c)
        return found

    def get(
        self,
        category: str = "demographics",
        cycle: str | None = None,
        table: str | None = None,
        grain: str | None = None,
        day: int = 1,
        columns: str = "sas",
        rows: str = "codes",
        copy: bool = True,
    ) -> pd.DataFrame:
        if cycle:
            df = self._one_table(category, cycle, table, grain=grain, day=day)
            out = df.copy() if copy else df
            _set_state(out, columns="sas", rows="codes", cycle=cycle, category=category)
            out = self._apply_view(out, category, cycle, columns, rows)
            out = _mask_question_sentinels(out, category, cycle, rows)
            if self.drop_replicates:
                out = drop_replicate_columns(out)
            if not self.surplus:
                out = drop_surplus_columns(out)
            return out

        frames = []
        for c in self.cycles():
            try:
                raw = self._one_table(category, c, table, grain=grain, day=day)
            except KeyError:
                continue
            part = raw.copy()
            _set_state(part, columns="sas", rows="codes", cycle=c, category=category)
            part = self._apply_view(part, category, c, columns, rows)
            part = _mask_question_sentinels(part, category, c, rows)
            frames.append(part)
        if not frames:
            raise KeyError(f"No tables found for category={category!r}")
        out = pd.concat(frames, ignore_index=True)
        if self.drop_replicates:
            out = drop_replicate_columns(out)
        if not self.surplus:
            out = drop_surplus_columns(out)
        _set_state(out, columns=columns, rows=rows, cycle=None, category=category)
        return out

    def get_df(
        self,
        cycle: str | list[str] = "all",
        set: str = "demographics",
        table: str | None = None,
        grain: str | None = None,
        day: int = 1,
        decode_rows: bool | list[str] | None = None,
        decode_columns: bool = True,
        encode_rows: bool = False,
        encode_columns: bool = False,
        cycle_min: int | None = None,
        log: bool | str = True,
    ) -> pd.DataFrame:
        """Load and stack cycles for one set.

        cycle_min drops any column present in fewer than that many loaded
        cycles. None keeps every column. SEQN and cycle are always kept.
        log=False (or "off"/"false"/"0"/"no"/"none") silences progress prints.
        """
        cycles = self._normalize_cycles(cycle)
        frames, skipped = [], []
        col_cycles: dict[str, int] = {}
        if isinstance(log, str):
            log = log.strip().lower() not in {"off", "false", "0", "no", "none"}
        else:
            log = bool(log)
        title = str(set).strip()
        if title:
            title = title[:1].upper() + title[1:]
        grain_txt = f" ({grain})" if grain else ""
        if log:
            print(f"Loading {title}{grain_txt}:")
        for c in cycles:
            try:
                raw = self._one_table(set, c, table, grain=grain, day=day)
            except KeyError as exc:
                skipped.append(f"{c}: {exc}")
                continue
            part = raw.copy()
            _set_state(part, columns="sas", rows="codes", cycle=c, category=set)
            part = self.clean_numeric(part, category=set, cycle=c)
            part = self.clean_categorical(part, category=set, cycle=c)
            if decode_rows or decode_columns:
                part = self.decode(
                    part,
                    category=set,
                    cycle=c,
                    rows=False if not decode_rows else decode_rows,
                    columns=bool(decode_columns),
                )
                if decode_rows is True:
                    part = _mask_question_sentinels(part, set, c, "labels")
                    if _normalize_grain(grain) == "drugs":
                        part = self._apply_drug_names(part)
                    part = self._apply_diet_lookups(part, cycle=c)
            if encode_rows or encode_columns:
                part = self.encode(
                    part,
                    category=set,
                    cycle=c,
                    rows=bool(encode_rows),
                    columns=bool(encode_columns),
                )
            for col in part.columns:
                col_cycles[str(col)] = col_cycles.get(str(col), 0) + 1
            frames.append(_insert_cycle(part, c))
            if log:
                print(f"Cycle {c} rows: {len(part)}  columns: {part.shape[1]}")
        if not frames:
            detail = " | ".join(skipped[:8]) if skipped else "no cycles loaded"
            available = self.available_cycles(set, grain=grain, table=table, day=day)
            avail_txt = ", ".join(available) if available else "none"
            raise KeyError(
                f"No data found for set={set!r}, cycle={cycle!r}, "
                f"grain={grain!r}, day={day!r}, table={table!r}. "
                f"Available cycles for this request: {avail_txt}. {detail}"
            )
        out = frames[0] if len(frames) == 1 else pd.concat(frames, ignore_index=True)
        if self.drop_replicates:
            out = drop_replicate_columns(out)
        if not self.surplus:
            out = drop_surplus_columns(out)
        if cycle_min is not None and int(cycle_min) > 0:
            keep = []
            for col in out.columns:
                name = str(col)
                if name.upper() == "SEQN" or name == "cycle":
                    keep.append(col)
                elif col_cycles.get(name, 0) >= int(cycle_min):
                    keep.append(col)
            dropped = out.shape[1] - len(keep)
            out = out[keep]
            if log and dropped:
                print(
                    f"cycle_min={int(cycle_min)}: dropped {dropped} columns "
                    f"present in fewer than {int(cycle_min)} cycles"
                )
        if decode_rows is True:
            row_state = "labels"
        elif decode_rows:
            row_state = "mixed"
        else:
            row_state = "codes"
        _set_state(
            out,
            columns="short" if decode_columns and not encode_columns else "sas",
            rows=row_state,
            cycle=None if len(cycles) != 1 else cycles[0],
            category=set,
        )
        return out

    def decode(
        self,
        df: pd.DataFrame | None = None,
        category: str | None = None,
        cycle: str | None = None,
        table: str | None = None,
        rows: bool | list[str] = True,
        columns: bool = True,
        inplace: bool = False,
    ) -> pd.DataFrame:
        if df is None:
            category = category or "demographics"
            df = self.get(category, cycle=cycle, table=table, columns="sas", rows="codes")
            inplace = False
        category = category or _state(df).get("category")
        cats = self._catalogs_for(df, category)
        return decode_frame(
            df, cycle=cycle, rows=rows, columns=columns, inplace=inplace,
            catalogs=cats, category=category,
        )

    def clean_categorical(
        self,
        df: pd.DataFrame,
        category: str | None = None,
        cycle: str | None = None,
        inplace: bool = False,
    ) -> pd.DataFrame:
        """Snap denormal / float codes on catalog categorical columns."""
        out = df if inplace else df.copy()
        category = category or _state(out).get("category")
        cats = self._catalogs_for(out, category)
        cycle = infer_cycle(out, cycle)
        merged_sas, merged_short, merged_vars = {}, set(), {}
        for cat in cats:
            merged_sas.update(cat["sas_to_short"])
            merged_short |= _short_names(cat["vars"])
            merged_vars.update(cat["vars"])
        col_state = _state(out).get("columns") or _guess_column_state(
            out, merged_sas, merged_short
        )
        if merged_vars:
            _sanitize_frame_categoricals(out, merged_vars, cycle, col_state)
        return out

    def clean_numeric(
        self,
        df: pd.DataFrame,
        category: str | None = None,
        cycle: str | None = None,
        thresh: float = _NEAR_ZERO_NUMERIC,
        inplace: bool = False,
    ) -> pd.DataFrame:
        """Coerce |x| < thresh to 0 on continuous / weight columns (default 1e-10)."""
        out = df if inplace else df.copy()
        category = category or _state(out).get("category")
        cats = self._catalogs_for(out, category)
        cycle = infer_cycle(out, cycle)
        merged_sas, merged_short, merged_vars = {}, set(), {}
        for cat in cats:
            merged_sas.update(cat.get("sas_to_short") or {})
            merged_short |= _short_names(cat.get("vars") or {})
            merged_vars.update(cat.get("vars") or {})
        col_state = _state(out).get("columns") or _guess_column_state(
            out, merged_sas, merged_short
        )
        _snap_near_zero_frame(out, merged_vars or None, cycle, col_state, thresh)
        return out

    def encode(
        self,
        df: pd.DataFrame | None = None,
        category: str | None = None,
        cycle: str | None = None,
        table: str | None = None,
        rows: bool | list[str] = True,
        columns: bool = True,
        inplace: bool = False,
    ) -> pd.DataFrame:
        if df is None:
            category = category or "demographics"
            df = self.get(category, cycle=cycle, table=table, columns="short", rows="labels")
            inplace = False
        category = category or _state(df).get("category")
        cats = self._catalogs_for(df, category)
        return encode_frame(
            df, cycle=cycle, rows=rows, columns=columns, inplace=inplace,
            catalogs=cats, category=category,
        )

    def describe(
        self,
        column: str,
        category: str | None = None,
        cycle: str | None = None,
        as_dict: bool = False
    ):
        try:
            spec, _cat_key = self._resolve_spec(column, category)
        except KeyError:
            stem = _base_col(column).upper()
            close = self._close_names(stem, category)
            hint = f" Close catalog names: {', '.join(close)}." if close else ""
            msg = f"Column {column!r} is not in any catalog.{hint}"
            if as_dict:
                return {
                    "column": str(column),
                    "missing": True,
                    "notes": msg,
                    "close": close,
                }
            print(msg)
            return None
        info = self._spec_info(spec, cycle)
        if _is_surplus_column(column):
            extra = (
                "Part of surplus/pooled data. Identical enumerated copies "
                "(NAME_2_SP, NAME_3_SP, ...) from the same cycle are combined "
                "into this column."
            )
            note = info.get("notes") or ""
            info["notes"] = f"{note} {extra}".strip() if note else extra
        if as_dict:
            return info
        return print(self._format_spec(info))

    info = describe

    def sas_coerced(self, set: str) -> "_SasCoerced":
        """Map short names that absorb more than one SAS name.

        Returns a dict-like of {short: [sas, ...]} sorted by short name.
        Only shorts that resolve to two or more distinct SAS names are
        stored. Each list is unique (case-insensitive) and sorted. Sources
        are the primary SAS name, cycle-specific names from sas_by_cycle,
        aliases, and day_pair.

        Looking up a short that is not coerced does not raise KeyError:
        - if the short exists in the catalog but has only one SAS name,
          the result is the string "present (not coerced)"
        - if the short is unknown, the result is the string "not present"

        This is the inverse of the internal SAS-to-short coercion used by
        get_df. Different original SAS names (often reflecting method or
        labeling changes across cycles) can land on the same short name.
        """
        cat = self._catalog(set)
        if cat is None:
            raise KeyError(
                f"Unknown set {set!r}. Known: {sorted(self.catalogs)}"
            )

        def _collect(spec: dict) -> list[str]:
            # Parameter name "set" shadows the builtin; collect then unique.
            raw: list[str] = []
            if spec.get("sas"):
                raw.append(str(spec["sas"]))
            for alias in (spec.get("sas_by_cycle") or {}).values():
                if alias:
                    raw.append(str(alias))
            for alias in spec.get("aliases") or []:
                if alias:
                    raw.append(str(alias))
            if spec.get("day_pair"):
                raw.append(str(spec["day_pair"]))
            seen: dict[str, str] = {}
            for name in raw:
                seen.setdefault(name.upper(), name)
            return sorted(seen.values(), key=str.upper)

        coerced = {
            short: names
            for short, spec in cat["vars"].items()
            if len(names := _collect(spec)) > 1
        }
        known = {str(short) for short in cat["vars"]}
        return _SasCoerced(dict(sorted(coerced.items())), known)

    def _catalog(self, category: str | None) -> dict | None:
        if not category:
            return None
        wanted = category.lower().strip()
        direct = self.catalogs.get(wanted)
        if direct:
            return direct
        for cat in self.catalogs.values():
            if wanted in cat.get("aliases", ()):
                return cat
        return None

    def _catalogs_for(self, df: pd.DataFrame, category: str | None) -> list[dict]:
        if category:
            cat = self._catalog(category)
            return [cat] if cat else []
        cols = set(map(str, df.columns))
        scored = []
        for cat in self.catalogs.values():
            sas = set(cat.get("sas_to_short") or ())
            shorts = _short_names(cat.get("vars") or {})
            n = len(cols & sas) + len(cols & shorts)
            if n:
                scored.append((n, cat))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [cat for _, cat in scored]

    def _normalize_cycles(self, cycle: str | list[str]) -> list[str]:
        if cycle is None or str(cycle).lower() == "all":
            loaded = set(self.cycles())
            return [c for c in CYCLES if c in loaded] or self.cycles()
        known = set(self.cycles())
        if isinstance(cycle, str):
            if cycle not in known:
                raise KeyError(f"Cycle {cycle!r} not indexed. Have: {sorted(known)}")
            return [cycle]
        missing = [c for c in cycle if c not in known]
        if missing:
            raise KeyError(f"Cycles not indexed: {missing}")
        return list(cycle)

    def _category_pool(self, cycle: str | None = None) -> list[str]:
        if self._using_eager():
            if cycle and cycle in self._eager:
                return list(self._eager[cycle])
            pool = []
            for c in self.cycles():
                pool.extend(self._eager.get(c, {}))
            return list(dict.fromkeys(pool))
        if cycle:
            return sorted({rec["category"] for rec in self.index if rec["cycle"] == cycle})
        return sorted({rec["category"] for rec in self.index})

    def _match_category_name(self, category: str, cycle: str | None = None) -> str:
        wanted = category.lower()
        cat = self._catalog(category)
        alias_pool = {wanted}
        if cat:
            alias_pool.update(cat.get("aliases") or ())

        pool = self._category_pool(cycle)
        unique_pool = list(dict.fromkeys(pool))

        exact = [n for n in unique_pool if n.lower() == wanted]
        if exact:
            return exact[0]
        alias_exact = [n for n in unique_pool if n.lower() in alias_pool]
        if alias_exact:
            return alias_exact[0]
        partial = [
            n for n in unique_pool
            if any(a in n.lower() or n.lower() in a for a in alias_pool)
        ]
        if len(partial) == 1:
            return partial[0]

        # Match by table stems when folder names differ from catalog names.
        if cat and cat.get("tables"):
            stems = {_norm_table(t) for t in cat["tables"]}
            hits = []
            cycles = [cycle] if cycle else self.cycles()
            for cyc in cycles:
                for cat_name in self._category_pool(cyc):
                    if self._using_eager():
                        names = self._eager.get(cyc, {}).get(cat_name, {})
                    else:
                        names = [rec["table"] for rec in self.index if rec["cycle"] == cyc and rec["category"] == cat_name]
                    if any(_norm_table(t) in stems for t in names):
                        hits.append(cat_name)
            hits = list(dict.fromkeys(hits))
            if len(hits) == 1:
                return hits[0]
            if hits and cycle:
                return hits[0]
        if cat:
            return category
        raise KeyError(f"Category {category!r} not found. Have: {unique_pool}")

    def _table_meta(self, catalog: dict | None, table_name: str, columns=None) -> dict:
        inferred = _infer_table_kind(table_name)
        if not catalog:
            out = dict(inferred)
            named = _grain_from_name(table_name, columns)
            if named:
                out["grain"] = named
            return out
        raw = catalog.get("tables") or {}
        stem = _norm_table(table_name)
        meta = raw.get(table_name) or raw.get(stem) or {}
        if not meta:
            for key, val in raw.items():
                if _norm_table(key) == stem or _norm_table(key) in stem or stem in _norm_table(key):
                    meta = val
                    break
        out = dict(inferred)
        out.update(meta or {})
        named = _grain_from_name(table_name, columns)
        if named:
            out["grain"] = named
        return out

    def _match_table_name(
        self,
        tables: dict,
        table: str | None,
        category: str,
        grain: str | None = None,
        day: int = 1,
    ) -> str:
        if not isinstance(tables, dict):
            raise KeyError(f"{category!r} is not a table map: {type(tables).__name__}")

        if table and table in tables:
            return table
        if table:
            want = _norm_table(table)
            hits = [
                n for n in tables
                if n.lower() == table.lower() or _norm_table(n) == want or want in _norm_table(n)
            ]
            if len(hits) == 1:
                return hits[0]
            if hits:
                return hits[0]
            raise KeyError(f"Table {table!r} not in {sorted(tables)}")

        cat = self._catalog(category)
        wanted_grain = _normalize_grain(grain or (cat.get("grain") if cat else None) or "person")
        if wanted_grain in {"total", "totals", "person-level"}:
            wanted_grain = "person"

        scored = []
        for name in tables:
            meta = self._table_meta(cat, name)
            g = (meta.get("grain") or "").lower()
            d = meta.get("day")
            if g in {"support", "lookup"}:
                continue
            if g and g != wanted_grain:
                continue
            if d is not None and int(d) != int(day):
                continue
            if g == wanted_grain:
                scored.append(name)

        if scored:
            return scored[0]
        if len(tables) == 1:
            return next(iter(tables))
        raise KeyError(
            f"No {wanted_grain!r} day-{day} table in {category!r}. Have: {sorted(tables)}"
        )

    def _is_questionnaire(self, category: str | None) -> bool:
        wanted = str(category or "").lower().strip()
        if wanted in {
            "questionnaire", "questions", "question", "questionaire",
            "interview", "sp questionnaire", "q",
        }:
            return True
        cat = self._catalog(category)
        if not cat:
            return False
        return cat.get("name") == "questionnaire" or "questionnaire" in (cat.get("aliases") or ())

    def _is_exam(self, category: str | None) -> bool:
        wanted = str(category or "").lower().strip()
        if wanted in {
            "examination", "exam", "exams", "examinations",
            "mec exam", "mec examination", "sp exam",
        }:
            return True
        cat = self._catalog(category)
        if not cat:
            return False
        return cat.get("name") == "examination" or "exam" in (cat.get("aliases") or ())

    def _drug_code_to_name(self) -> dict:
        """RXQ_DRUG lexicon: generic drug code -> generic drug name."""
        cached = getattr(self, "_drug_name_map", None)
        if cached is not None:
            return cached
        mapping = {
            "55555": "Unknown",
            "77777": "Refused",
            "99999": "Don't know",
        }
        data = self._eager if self._using_eager() else {}
        buckets = []
        if data:
            for cycle, cats in data.items():
                if cycle == "Info" or not isinstance(cats, dict):
                    continue
                buckets.append(cats)
            info = data.get("Info")
            if isinstance(info, dict):
                for cats in info.values():
                    if isinstance(cats, dict):
                        buckets.append(cats)
        else:
            # Read only the drug lexicon, not the whole survey.
            for rec in self.index:
                if "RXQ_DRUG" not in str(rec["table"]).upper() and _norm_table(rec["table"]) != _norm_table(DRUG_LOOKUP_TABLE):
                    continue
                try:
                    df = self._read_record(rec)
                except Exception:
                    continue
                buckets.append({rec["category"]: {rec["table"]: df}})
        for cats in buckets:
            for tables in cats.values():
                if not isinstance(tables, dict):
                    continue
                for name, df in tables.items():
                    if not hasattr(df, "columns"):
                        continue
                    if _norm_table(name) != _norm_table(DRUG_LOOKUP_TABLE) and "RXQ_DRUG" not in str(name).upper():
                        continue
                    cols = {str(c).upper(): c for c in df.columns}
                    code_col = cols.get(DRUG_CODE_COLUMNS[0])
                    name_col = cols.get(DRUG_NAME_COLUMN)
                    if not code_col or not name_col:
                        continue
                    for code, label in zip(df[code_col].tolist(), df[name_col].tolist()):
                        if code is None or label is None or pd.isna(code) or pd.isna(label):
                            continue
                        key = str(code).strip()
                        if key:
                            mapping[key] = str(label).strip()
        self._drug_name_map = mapping
        return mapping

    def _apply_drug_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """Replace RXDDRGID (and a coded RXDDRUG) with the RXQ_DRUG name."""
        mapping = self._drug_code_to_name()
        if len(mapping) <= 3 or df is None or df.empty:
            return df
        out = df.copy()
        code_names = set(DRUG_CODE_COLUMNS) | {DRUG_NAME_COLUMN}
        # short names after decode_columns=True
        cat = self._catalog("questionnaire") or {}
        for spec in (cat.get("vars") or {}).values():
            if spec.get("sas") in code_names:
                code_names.add(spec["short"])
        for col in list(out.columns):
            if str(col).upper() not in {c.upper() for c in code_names} and str(col) not in code_names:
                continue
            # Only rewrite the code column, plus a name column that still holds codes.
            is_code = str(col).upper() == DRUG_CODE_COLUMNS[0] or str(col).lower().startswith("rxddrgid")
            is_name = str(col).upper() == DRUG_NAME_COLUMN or str(col).lower().startswith("rxddrug")
            if not (is_code or is_name):
                continue

            def _label(val):
                if val is None or (isinstance(val, float) and pd.isna(val)):
                    return val
                key = str(val).strip()
                if key.endswith(".0") and key[:-2].isdigit():
                    key = key[:-2]
                return mapping.get(key, val)

            out[col] = out[col].map(_label)
        return out

    def _apply_diet_lookups(self, df: pd.DataFrame, cycle: str | None = None) -> pd.DataFrame:
        """Replace food, modification, FFQ, and supplement codes with names.

        Food and modification maps are cycle-specific. Supplement ids become
        the product name, and a supp_ingredients column is added from the
        1999-2023 ingredient file.
        """
        try:
            from .code_details_diet_lookups import (
                FFQ_FOOD,
                FFQ_VAR,
                FOOD_BY_CYCLE,
                FOOD_LATEST,
                MOD_BY_CYCLE,
                MOD_LATEST,
                SUPP_BY_PID,
                SUPP_BY_SUPID,
                SUPP_INGREDIENTS,
            )
        except ImportError:
            return df
        if df is None or df.empty:
            return df
        out = df.copy()
        cycle = infer_cycle(out, cycle)
        food = FOOD_BY_CYCLE.get(cycle or "", FOOD_LATEST)
        mod = MOD_BY_CYCLE.get(cycle or "", MOD_LATEST)

        def _key(val):
            if val is None or (isinstance(val, float) and pd.isna(val)):
                return None
            text = str(val).strip()
            if text.endswith(".0") and text[:-2].isdigit():
                text = text[:-2]
            return text or None

        def _map_col(col, primary, fallback):
            def _label(val):
                key = _key(val)
                if key is None:
                    return val
                return primary.get(key) or fallback.get(key) or val
            out[col] = out[col].map(_label)

        food_cols = {
            "DR1IFDCD", "DR2IFDCD", "DRDIFDCD", "DRXFDCD", "FOOD_CODE",
        }
        mod_cols = {"DR1MC", "DR2MC", "DRXMC", "MOD_CODE"}
        supp_cols = {"DSDSUPID", "DSDPID", "SUPP_ID"}
        supp_src = None
        for col in list(out.columns):
            name = str(col).upper()
            if name in food_cols or name.startswith("DR1IFDCD") or name.startswith("DR2IFDCD"):
                _map_col(col, food, FOOD_LATEST)
            elif name in mod_cols or name.startswith("DR1MC") or name.startswith("DR2MC"):
                _map_col(col, mod, MOD_LATEST)
            elif name == "FFQ_FOOD":
                _map_col(col, FFQ_FOOD, FFQ_FOOD)
            elif name == "FFQ_VAR":
                _map_col(col, FFQ_VAR, FFQ_VAR)
            elif name in supp_cols or name.startswith("DSDSUPID") or name.startswith("DSDPID"):
                if supp_src is None:
                    supp_src = col
                primary = SUPP_BY_PID if "PID" in name else SUPP_BY_SUPID
                fallback = SUPP_BY_SUPID if primary is SUPP_BY_PID else SUPP_BY_PID
                _map_col(col, primary, fallback)
        if supp_src is not None and "supp_ingredients" not in out.columns:
            def _ings(val):
                key = _key(val)
                if key is None:
                    return None
                return SUPP_INGREDIENTS.get(key)
            out["supp_ingredients"] = df[supp_src].map(_ings)
        return out

    def _close_names(self, stem: str, category: str | None = None) -> list[str]:
        """Catalog SAS/short names that start with stem, for a failed lookup."""
        stem = str(stem).upper()
        if not stem:
            return []
        cats = [self._catalog(category)] if category else list(self.catalogs.values())
        found = []
        for cat in cats:
            if not cat:
                continue
            for spec in (cat.get("vars") or {}).values():
                for key in ("sas", "short"):
                    val = spec.get(key)
                    if not val:
                        continue
                    up = str(val).upper()
                    if up == stem or up.startswith(stem + "_"):
                        found.append(str(val))
        return sorted(set(found))[:8]

    def _known_column_names(self) -> set[str]:
        """SAS names, shorts, and aliases. Used to tell SSJO_1 from NAME_2."""
        names: set[str] = set()
        for cat in self.catalogs.values():
            for spec in (cat.get("vars") or {}).values():
                for key in ("sas", "short", "day_pair"):
                    val = spec.get(key)
                    if val:
                        names.add(str(val).upper())
                for alias in (spec.get("sas_by_cycle") or {}).values():
                    if alias:
                        names.add(str(alias).upper())
                for alias in spec.get("aliases") or []:
                    if alias:
                        names.add(str(alias).upper())
        return names

    def _one_table(
        self,
        category: str,
        cycle: str,
        table: str | None,
        grain: str | None = None,
        day: int = 1,
    ) -> pd.DataFrame:
        if cycle not in self.cycles():
            raise KeyError(f"Cycle {cycle!r} not indexed")
        cat_name = self._match_category_name(category, cycle)
        tables = self._load_tables(cycle, cat_name)
        if not tables:
            raise KeyError(f"Category {category!r} not in cycle {cycle}")
        grain_norm = _normalize_grain(grain)
        # Questionnaire and examination person pulls merge one-row-per-SEQN files.
        if table is None and grain_norm in {None, "person"} and (
            self._is_questionnaire(category) or self._is_exam(category)
        ):
            table = "all"
        known = self._known_column_names()
        if grain_norm in {"drugs", "activity"} and (table is None or _want_all_tables(table)):
            return collapse_surplus_duplicates(
                self._concat_grain_tables(category, tables, grain_norm),
                known,
            )
        if _want_all_tables(table):
            return collapse_surplus_duplicates(self._merge_category_by_seqn(
                category, cycle, tables, grain=grain, day=day,
            ), known)
        name = self._match_table_name(tables, table, category, grain=grain, day=day)
        return collapse_surplus_duplicates(tables[name], known)

    def _concat_grain_tables(self, category: str, tables: dict, grain: str) -> pd.DataFrame:
        """Stack event tables. Do not collapse duplicate SEQN rows."""
        frames = [df for _, df in self._iter_merge_tables(category, tables, grain=grain)]
        if not frames:
            have = ", ".join(sorted(map(str, tables))) or "(none)"
            raise KeyError(
                f"No {grain!r} tables to stack for {category!r}. Tables present: {have}"
            )
        if len(frames) == 1:
            return frames[0].copy()
        return pd.concat(frames, ignore_index=True)

    def _iter_merge_tables(
        self,
        category: str,
        tables: dict,
        grain: str | None = None,
        day: int = 1,
    ):
        cat = self._catalog(category)
        raw_grain = grain
        if grain is None:
            wanted = (cat.get("grain") if cat else None) or "person"
        else:
            wanted = grain
        wanted = _normalize_grain(wanted) or "person"
        if wanted in {"all", "any"}:
            wanted = None
        for name, df in tables.items():
            meta = self._table_meta(cat, name, getattr(df, "columns", None))
            g = (meta.get("grain") or "").lower()
            d = meta.get("day")
            if g in {"support", "lookup"}:
                continue
            if wanted == "person" and g in {"pool", "drugs", "activity", "event"}:
                continue
            # A requested event grain must match. Unknown-grain tables are
            # person files and must not be stacked into drugs/activity.
            if wanted in {"drugs", "activity", "food", "pool", "event"} and g != wanted:
                continue
            if wanted and g and g != wanted:
                continue
            if wanted == "food" and d is not None and int(d) != int(day):
                continue
            if raw_grain is None and wanted == "person" and not _has_seqn(df):
                continue
            if wanted == "person" and not _has_seqn(df):
                continue
            yield name, df

    def _merge_category_by_seqn(
        self,
        category: str,
        cycle: str,
        tables: dict,
        grain: str | None = None,
        day: int = 1,
    ) -> pd.DataFrame:
        frames = [df for _, df in self._iter_merge_tables(category, tables, grain=grain, day=day)]
        if not frames:
            raise KeyError(
                f"No SEQN tables to merge for {category!r} in cycle {cycle}"
            )
        out = _merge_frames_by_seqn(frames)
        if getattr(self, "drop_replicates", True):
            out = drop_replicate_columns(out)
        if not getattr(self, "surplus", True):
            out = drop_surplus_columns(out)
        return out

    def _apply_view(self, df, category, cycle, columns, rows):
        cats = self._catalogs_for(df, category)
        if not cats:
            return df
        if columns == "short" or rows == "labels":
            df = decode_frame(
                df, cycle=cycle, rows=(rows == "labels"), columns=(columns == "short"),
                catalogs=cats, category=category,
            )
        st = _state(df)
        need_cols = columns == "sas" and st.get("columns") != "sas"
        need_rows = rows == "codes" and st.get("rows") not in {"codes", None}
        if need_cols or need_rows:
            df = encode_frame(
                df, cycle=cycle, rows=need_rows, columns=need_cols,
                catalogs=cats, category=category,
            )
        return df

    def _resolve_spec(self, column: str, category: str | None) -> tuple[dict, str]:
        key = str(column)
        base = _base_col(key)
        candidates = [key]
        if base != key:
            candidates.append(base)
        # Collision copies are NAME_2_SP. Also try the un-numbered stem so
        # describe("WTSSBI2Y_2_SP") still finds WTSSBI2Y. Real names such as
        # SSMI_2 are tried first and win when they exist.
        stem, n = _strip_enum(base)
        if n is not None:
            candidates.append(stem)
        candidates = tuple(dict.fromkeys(candidates))
        search = []
        cat = self._catalog(category) if category else None
        if cat:
            search.append((cat["name"], cat))
        for extra_key, extra in self.catalogs.items():
            if extra_key not in [k for k, _ in search]:
                search.append((extra_key, extra))
        for candidate in candidates:
            for cat_key, cat in search:
                vars_map = cat["vars"]
                sas_map = cat["sas_to_short"]
                if candidate in vars_map:
                    return vars_map[candidate], cat_key
                if candidate in sas_map:
                    return vars_map[sas_map[candidate]], cat_key
                upper = {str(s).upper(): short for s, short in sas_map.items()}
                if candidate.upper() in upper:
                    return vars_map[upper[candidate.upper()]], cat_key
                lower = {str(s).lower(): spec for s, spec in vars_map.items()}
                if candidate.lower() in lower:
                    return lower[candidate.lower()], cat_key
        raise KeyError(f"Column {column!r} not found in {category or 'any catalog'}")

    def _spec_info(self, spec: dict, cycle: str | None) -> dict:
        codes = codes_for(spec, cycle)
        raw = raw_codes_for(spec, cycle)
        return {
            "short": spec["short"],
            "sas": sas_name(spec, cycle),
            "sas_default": spec.get("sas"),
            "sas_by_cycle": dict(spec.get("sas_by_cycle") or {}),
            "kind": kind_for(spec, cycle),
            "kind_stored": spec.get("kind"),
            "label": spec.get("label") or spec.get("text"),
            "definition": definition_for(spec, cycle),
            "target": target_for(spec, cycle),
            "target_default": spec.get("target"),
            "target_by_cycle": dict(spec.get("target_by_cycle") or {}),
            "codes": dict(codes) if codes else None,
            "raw_codes": dict(raw) if raw and raw != codes else None,
            "notes": notes_for(spec),
            "cycle": cycle,
        }

    def _format_spec(self, info: dict) -> str:
        lines = [
            f"Column:      {info['short']}",
            f"SAS name:    {info['sas']}",
            f"Kind:        {info['kind']}",
            f"Cycle:       {info['cycle'] or '(default / all)'}",
            f"Target:      {info['target']}",
            f"Definition:  {info['definition']}",
        ]
        if info["sas_by_cycle"]:
            alias = ", ".join(f"{c}={s}" for c, s in info["sas_by_cycle"].items())
            lines.append(f"SAS aliases: {alias}")
        if info["notes"]:
            lines.append(f"Notes:       {info['notes']}")
        if info["codes"]:
            lines.append("Codes:")
            for code, label in info["codes"].items():
                lines.append(f"    {code}: {label}")
        if info["raw_codes"] and info["raw_codes"] != info["codes"]:
            lines.append("Codebook bins (original labels):")
            for code, label in info["raw_codes"].items():
                lines.append(f"    {code}: {label}")
        return "\n".join(lines)
