# nhanes-helpy

A lightweight Python helper for loading, stacking, cleaning, and decoding NHANES data files (XPT or CSV). It is designed as a comprehensive tool for working with NHANES data, with column descriptions and decoding for any categorical field.

It indexes a local tree of cycle folders, loads only the files a request needs, outer-merges person-level tables on `SEQN`, and applies codebook labels for demographics, diet, laboratory, examination, and questionnaire variables.

## Features

- Decodes SAS names → short names and numeric codes → labels
- Handles surplus columns, jackknife replicates, and imputation flags
- Includes food-code, modification-code, and drug-name lookups
- Indexes XPT or CSV files without loading them until requested
- Stacks any combination of cycles for a category (`set`)
- Outer-merges person-level tables on `SEQN` (with optional grain/day filters)
- Supports a compressed “Zenodo-style” flat CSV layout and decompression back to a cycle tree

## Installation

```bash
pip install nhanes-helpy
```

**Dependencies:** `pandas` (and `pyreadstat` if you read `.xpt` files).

## Download Data

[https://zenodo.org/records/23602819](https://zenodo.org/records/23602819)


## Quick Start

```python
from nhanes_helpy import NHANES_Helper

# Sample data included with the module — fully functional without a data download (100 rows per dataset per cycle)
nh = NHANES_Helper(data_dir=None)

# Decompress Zenodo files into a memory-efficient folder structure
nh.Decompress_Data(
    compressed_dir="path/to/zenodo_csv_files",
    destination="destination/folder",
)

# Point at a folder that contains cycle subfolders
# (e.g. 1999-2000_data/, 2001-2002_data/, …)
nh = NHANES_Helper(data_dir="path/to/decompressed")
```

```python
# Load all available cycles of demographics (person-level).
# decode_rows accepts True, False, or a list of columns to label.
demo = nh.get_df(
    cycle="all",
    set="Demographics",
    decode_rows=["gender", "hhref_age", "race_ethnicity", "interview_exam_status"],
    log=True,
)
```

```
Loading Demographics:
Cycle 99-00 rows: 100 columns: 38
Cycle 01-02 rows: 100 columns: 38
Cycle 03-04 rows: 100 columns: 45
Cycle 05-06 rows: 100 columns: 44
Cycle 07-08 rows: 100 columns: 44
Cycle 09-10 rows: 100 columns: 44
Cycle 11-12 rows: 100 columns: 49
Cycle 13-14 rows: 100 columns: 48
Cycle 15-16 rows: 100 columns: 48
Cycle 17-18 rows: 100 columns: 47
Cycle 17-20 rows: 100 columns: 30
Cycle 21-23 rows: 100 columns: 28
```

```python
print(demo[demo.columns[:10]])
```

| seqn  | cycle | release_cycle | interview_exam_status             | exam_6mo_period | gender | age_years | age_months_screen | age_months_exam | race_ethnicity   |
| ----- | ----- | ------------- | --------------------------------- | --------------- | ------ | --------- | ----------------- | --------------- | ---------------- |
| 53.0  | 99-00 | 1             | Both Interviewed and MEC examined | 1               | Female | 18.0      | 222.0             | 223.0           | Mexican American |
| 88.0  | 99-00 | 1             | Both Interviewed and MEC examined | 1               | Female | 19.0      | 231.0             | 232.0           | Mexican American |
| 126.0 | 99-00 | 1             | Both Interviewed and MEC examined | 1               | Female | 33.0      | 397.0             | 398.0           | Mexican American |
| 143.0 | 99-00 | 1             | Both Interviewed and MEC examined | 1               | Female | 22.0      | 275.0             | 276.0           | Mexican American |
| 169.0 | 99-00 | 1             | Both Interviewed and MEC examined | 1               | Female | 23.0      | 276.0             | 276.0           | Mexican American |

```python
# Lab data for selected cycles. Keep only columns present in ≥3 cycles.
labs = nh.get_df(
    set="lab",
    cycle=["11-12", "13-14", "15-16"],
    decode_columns=False,
    cycle_min=3,
    log=False,
)
```

| SEQN    | cycle | URXUMA | URXUCR | LBXBPB | LBDBPBSI | LBXBCD | LBDBCDSI | LBXTHG | LBDTHGSI |
| ------- | ----- | ------ | ------ | ------ | -------- | ------ | -------- | ------ | -------- |
| 62218.0 | 11-12 | 13.3   | 80.0   | 1.03   | 0.050    | 1.20   | 10.68    | 0.61   | 3.0      |
| 62449.0 | 11-12 | 8.6    | 110.0  | 0.43   | 0.021    | 0.21   | 1.87     | 0.67   | 3.3      |
| 62501.0 | 11-12 | 8.2    | 89.0   | 0.32   | 0.015    | 0.29   | 2.58     | 0.11   | 0.5      |
| 62596.0 | 11-12 | 11.5   | 150.0  | 1.25   | 0.060    | 0.64   | 5.69     | 3.80   | 19.0     |
| 62764.0 | 11-12 | 7.1    | 74.0   | 0.70   | 0.034    | 0.24   | 2.14     | 2.81   | 14.0     |


Most columns that represent slight changes in column id between cycles are not merged or changed when the difference was caused by a change in method or calculation. 
Some columns are merged on a best-effort basis to stay true to scientific rigor when the change was due to a cycle delimiter or file artifact. 
A complete list of all coerced/merged columns for a given dataset can be output and reviewed by checking the SAS name and SAS aliases:

```python
sas_map = nh.sas_coerced("Laboratory")
```

```
Column:      glucose_fasting_si
SAS name:    LBXGLUSI
Kind:        continuous
Cycle:       (default / all)
Target:      Both males and females 12 YEARS - 150 YEARS
Definition:  Fasting plasma glucose (mmol/L)
SAS aliases: 03-04=LBDGLUSI, 05-06=LBDGLUSI, 07-08=LBDGLUSI, 09-10=LBDGLUSI, 11-12=LBDGLUSI, 13-14=LBDGLUSI, 15-16=LBDGLUSI, 17-18=LBDGLUSI, 17-20=LBDGLUSI, 21-23=LBDGLUSI
Notes:       Diabetes mellitus will be assessed by measures of plasma glucose, insulin, and C-peptide in participants aged 12 years and over in the morning examination session only. 
Fasting plasma glucose is a diabetes / glycemia measure from the morning subsample; do not use random BIOPRO glucose in its place.
...
```


```python
labs_decoded = nh.get_df(
    set="lab",
    cycle=["11-12", "13-14", "15-16"],
    decode_columns=True,
    decode_rows=False,
    cycle_min=3,
    log=False,
)
```

| seqn    | cycle | albumin_urine | urine_creatinine | blood_lead_lbxbpb | blood_lead | blood_cadmium_lbxbcd | blood_cadmium | mercury_total | blood_mercury_total |
| ------- | ----- | ------------- | ---------------- | ----------------- | ---------- | -------------------- | ------------- | ------------- | ------------------- |
| 62218.0 | 11-12 | 13.3          | 80.0             | 1.03              | 0.050      | 1.20                 | 10.68         | 0.61          | 3.0                 |
| 62449.0 | 11-12 | 8.6           | 110.0            | 0.43              | 0.021      | 0.21                 | 1.87          | 0.67          | 3.3                 |
| 62501.0 | 11-12 | 8.2           | 89.0             | 0.32              | 0.015      | 0.29                 | 2.58          | 0.11          | 0.5                 |
| 62596.0 | 11-12 | 11.5          | 150.0            | 1.25              | 0.060      | 0.64                 | 5.69          | 3.80          | 19.0                |
| 62764.0 | 11-12 | 7.1           | 74.0             | 0.70              | 0.034      | 0.24                 | 2.14          | 2.81          | 14.0                |

```python
# Look up any variable from any dataset
nh.describe("LBXBCD")
```

```
Column:      blood_cadmium_lbxbcd
SAS name:    LBXBCD
Kind:        continuous
Cycle:       (default / all)
Target:      Both males and females 1 YEARS - 150 YEARS
Definition:  Blood cadmium (ug/L)
Notes:       Blood cadmium (ug/L). Cadmium is a nephrotoxin and carcinogen; major sources are cigarette smoke and some industrial exposures.
Codebook bins (original labels):
    0.1: Below Limit of Detection
```

`describe()` works with either the SAS name or the short name for every column in every dataset.

```python
nh.describe("blood_cadmium_lbxbcd")
```

```python
demo_raw = nh.get("Demographics")  # completely raw, lossless data
```

| SEQN  | cycle | SDDSRVYR | RIDSTATR | RIDEXMON | RIAGENDR | RIDAGEYR | RIDAGEMN | RIDAGEEX | RIDRETH1 |
| ----- | ----- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 53.0  | 99-00 | 1.0      | 2.0      | 1.0      | 2.0      | 18.0     | 222.0    | 223.0    | 1.0      |
| 88.0  | 99-00 | 1.0      | 2.0      | 1.0      | 2.0      | 19.0     | 231.0    | 232.0    | 1.0      |
| 126.0 | 99-00 | 1.0      | 2.0      | 1.0      | 2.0      | 33.0     | 397.0    | 398.0    | 1.0      |
| 143.0 | 99-00 | 1.0      | 2.0      | 1.0      | 2.0      | 22.0     | 275.0    | 276.0    | 1.0      |
| 169.0 | 99-00 | 1.0      | 2.0      | 1.0      | 2.0      | 23.0     | 276.0    | 276.0    | 1.0      |

```python
demo_raw_decoded = nh.decode(demo_raw)  # previously loaded frames can still be decoded later
```

| seqn  | cycle | release_cycle                   | interview_exam_status             | exam_6mo_period             | gender | age_years | age_months_screen | age_months_exam | race_ethnicity   |
| ----- | ----- | ------------------------------- | --------------------------------- | --------------------------- | ------ | --------- | ----------------- | --------------- | ---------------- |
| 53.0  | 99-00 | NHANES 1999-2000 Public Release | Both Interviewed and MEC examined | November 1 through April 30 | Female | 18.0      | 222.0             | 223.0           | Mexican American |
| 88.0  | 99-00 | NHANES 1999-2000 Public Release | Both Interviewed and MEC examined | November 1 through April 30 | Female | 19.0      | 231.0             | 232.0           | Mexican American |
| 126.0 | 99-00 | NHANES 1999-2000 Public Release | Both Interviewed and MEC examined | November 1 through April 30 | Female | 33.0      | 397.0             | 398.0           | Mexican American |
| 143.0 | 99-00 | NHANES 1999-2000 Public Release | Both Interviewed and MEC examined | November 1 through April 30 | Female | 22.0      | 275.0             | 276.0           | Mexican American |
| 169.0 | 99-00 | NHANES 1999-2000 Public Release | Both Interviewed and MEC examined | November 1 through April 30 | Female | 23.0      | 276.0             | 276.0           | Mexican American |

## All available data sets

Multi-row-per-SEQN tables are selected with `grain`. `person` means one SEQN per row.

```python
# Usage for all available datasets
demo = nh.get_df(
    cycle="all",
    set="Demographics",
    decode_rows=["gender", "hhref_age", "race_ethnicity", "interview_exam_status"],
    log=False,
)
labs = nh.get_df(cycle="all", set="Laboratory", table="all", grain="person", cycle_min=5)  # keep columns present in at least N cycles
lab_pools = nh.get_df(cycle="all", set="Laboratory", table="all", grain="pool")
questions = nh.get_df(cycle="all", set="Questionnaire", grain="person")  # one SEQN per row
activity = nh.get_df(cycle="all", set="Questionnaire", grain="activity")  # multiple rows per SEQN
drugs = nh.get_df(cycle="all", set="Questionnaire", grain="drugs")
diet = nh.get_df(cycle="all", set="Dietary", grain="person", decode_rows=False)
foods = nh.get_df(cycle="all", set="Dietary", grain="food", decode_rows=True)
exam = nh.get_df(cycle="all", set="Exam", grain="person",)
```

## Main API

### `NHANES_Helper(data_dir=None, drop_replicates=True, drop_impute_flags=True, surplus=True)`

Indexes the given directory. No data frames are loaded until a method is called.

| Parameter           | Default | Description                                                   |
| ------------------- | ------- | ------------------------------------------------------------- |
| `data_dir`          | `None`  | Root folder containing cycle data                             |
| `drop_replicates`   | `True`  | Drop jackknife replicate weights (`WT*01`–`52`, etc.)         |
| `drop_impute_flags` | `True`  | Drop imputation-flag columns                                  |
| `surplus`           | `True`  | Keep surplus-sample columns (suffix `_SP` in compressed data) |

### `get_df(...)` → `DataFrame`

The primary loader.

| Argument         | Default          | Description                                                      |
| ---------------- | ---------------- | ---------------------------------------------------------------- |
| `cycle`          | `"all"`          | `"all"`, a cycle string (`"15-16"`), or a list of cycles         |
| `set`            | `"demographics"` | Category: `demographics`, `diet`, `lab`, `exam`, `questionnaire` |
| `table`          | `None`           | Specific table name (optional)                                   |
| `grain`          | `None`           | `person`, `food`, `drugs`, `activity`, `pool`, …                 |
| `day`            | `1`              | Recall day for diet tables                                       |
| `decode_rows`    | `None`           | `True` / `False` / list of columns to label                      |
| `decode_columns` | `True`           | Rename SAS names to short names                                  |
| `cycle_min`      | `None`           | Drop columns present in fewer than this many cycles              |
| `log`            | `True`           | Print progress (`False` or `"off"` to silence)                   |

A `cycle` column is always inserted immediately after `SEQN`.


### Other useful methods

- `cycles()` – indexed cycles
- `categories(cycle=None)` – available sets
- `tables(category, cycle=None)` – tables in a set
- `get(cycle, tables=..., grain=..., set=...)` – load without stacking/decoding
- `decode(df, ...)` / `encode(df, ...)` – convert codes ↔ labels
- `describe(column, category=None, cycle=None)` – print (or return) codebook info
- `Decompress_Data(compressed_dir, destination)` – expand a flat compressed CSV folder into a cycle tree

## Catalogs

Codebook definitions live in the companion `code_details_*.py` modules (demographics, diet, lab, examination, questionnaire). They supply:

- SAS name ↔ short name maps
- Value labels and cycle-specific codes
- Grain / day metadata
- Food, modification, and drug lookups

`decode_rows=True` applies these maps (and masks common questionnaire sentinels).

## Disclaimer

This package is not affiliated with the CDC or NCHS. NHANES data are public domain; users are responsible for following CDC usage guidelines.

Built from data originally scraped by Michael Amato and stored at https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/WYIIQ1&version=1.0
