from __future__ import annotations

# Shared cycle maps live in the demographics catalog. Re-declared here so this
# file can stand alone; drop these if you import them from demo.
CYCLES = [
    "99-00", "01-02", "03-04", "05-06", "07-08", "09-10",
    "11-12", "13-14", "15-16", "17-18", "17-20", "21-23",
]

T_ALL = "Both males and females 0 YEARS - 150 YEARS"
T_1_150 = "Both males and females 1 YEARS - 150 YEARS"
T_F_16_49 = "Females only 16 YEARS - 49 YEARS"

YES_NO = {1: "Yes", 2: "No", 7: "Refused", 9: "Don't know"}
YES_NO_ONLY = {1: "Yes", 2: "No"}

AMOUNT_VS_USUAL = {
    1: "Much more than usual",
    2: "Usual",
    3: "Much less than usual",
    7: "Refused",
    9: "Don't know",
}
AMOUNT_VS_USUAL_9900 = {
    1: "Usual",
    2: "Less than usual",
    3: "More than usual",
    9: "Don't know",
}

COMPLETE_PARTIAL = {1: "Complete", 2: "Partial", 3: "Not done"}
SALT_ADJ = {
    1: "No sodium adjustment done",
    2: "Total sodium intake adjusted for salt use in food preparation",
}

SALT_ADJ_IFF = {
    1: "No sodium adjustment done",
    2: "Sodium value adjusted for salt use in food preparation",
}

# ---------------------------------------------------------------------------
# Code maps
# ---------------------------------------------------------------------------

# 1999-2000 only. Code 2 ("reliable but not minimum") and 3 ("not reliable")
# were collapsed into a single "not reliable / not minimum" code starting 01-02.
RECALL_STATUS_9900 = {
    1: "Reliable and meet minimum criteria",
    2: "Reliable but not meet minimum criteria",
    3: "Not reliable",
    4: "Breast-fed infant or child",
    5: "Not done",
}

# 2001-2002 onward (DRDDRSTZ / DR1DRSTZ / DR2DRSTZ). Code 3 unused.
RECALL_STATUS = {
    1: "Reliable and met the minimum criteria",
    2: "Not reliable or not met the minimum criteria",
    4: "Reported consuming breast-milk",
    5: "Not done",
}

RECALL_STATUS_BY_CYCLE = {"99-00": RECALL_STATUS_9900}

DAY_OF_WEEK = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday",
}

COMBO_FLAG = {0: "Single component food", 1: "Combo food"}
MODIFIED_RECIPE = {0: "Non-modified recipe", 1: "Modified recipe"}

# Early files allow mixed / other. Later DR1LANG / DR2LANG are usually 1/2.
DIET_LANG_EARLY = {1: "English", 2: "Spanish", 3: "English and Spanish", 4: "Other"}
DIET_LANG = {1: "English", 2: "Spanish", 3: "English and Spanish", 4: "Other", 5: "Other", 6: "Other"}

INTERVIEW_MODE = {1: "In-person", 2: "Telephone"}

INTAKE_DAYS = {1: "Day 1 only", 2: "Day 1 and Day 2"}

BREASTFED = {1: "Yes", 2: "No"}

COMPARE_USUAL = dict(AMOUNT_VS_USUAL)

# 01-02 DRDRESP (3-cat). 03-14 used relationship codes under DR1MNRSP.
RESPONDENT_3CAT = {1: "SP", 2: "Proxy", 3: "SP and proxy"}

RESPONDENT_REL = {
    1: "SP",
    2: "Mother of SP",
    3: "Father of SP",
    4: "Wife of SP",
    5: "Husband of SP",
    6: "Daughter of SP",
    7: "Son of SP",
    8: "Grandparent of SP",
    9: "Friend, partner, non-relative",
    10: "Translator, not a HH member",
    11: "Child care provider, caretaker",
    12: "Other relative",
    13: "No one",          # used on HELPD; unused on MNRSP
    14: "Other specify",
    77: "Refused",
    99: "Don't know",
}

# 99-00 coded meal name (DRD030). Not 1:1 with later DR1_030Z.
EAT_OCC_9900 = {
    1: "Breakfast",
    2: "Brunch",
    3: "Lunch",
    4: "Snack/beverage",
    5: "Dinner/supper",
    6: "Infant feeding",
    7: "Extended consumption",
    8: "Other",
    9: "Desayuno",
    10: "Almuerzo",
    11: "Comida",
    12: "Merienda",
    13: "Cena",
    14: "Entre comida/bebida",
    15: "Bocadillo",
    16: "Botana",
    99: "Don't know",
}

MEAL_PLACE_9900 = {
    1: "Boat",
    2: "Self serve buffet",
    3: "Cafeteria",
    4: "Car",
    5: "Community feeding program",
    6: "Deli",
    7: "Fast food",
    8: "Friend's house",
    9: "Home",
    11: "Plane",
    12: "Restaurant",
    13: "School",
    14: "Someone else's house",
    15: "Store",
    16: "Take out",
    17: "Work",
    18: "Day camp",
    19: "Day care",
    90: "Other",
}

# 01-02+ eating occasion (DRD030Z / DR1_030Z / DR2_030Z).
EAT_OCC = {
    1: "Breakfast",
    2: "Lunch",
    3: "Dinner",
    4: "Supper",
    5: "Brunch",
    6: "Snack",
    7: "Drink",
    8: "Infant feeding",
    9: "Extended consumption",
    10: "Desayuno",
    11: "Almuerzo",
    12: "Comida",
    13: "Merienda",
    14: "Cena",
    15: "Entre comida",
    16: "Botana",
    17: "Bocadillo",
    18: "Tentempie",
    19: "Bebida",
    91: "Other",
    99: "Don't know",
}

# Food source. Added 03-04 as DR1FS. Labels refined over time; codes are stable.
FOOD_SOURCE = {
    1: "Store - grocery/supermarket",
    2: "Restaurant with waiter/waitress",
    3: "Restaurant fast food/pizza",
    4: "Bar/tavern/lounge",
    5: "Restaurant, no additional information",
    6: "Cafeteria not in a K-12 school",
    7: "Cafeteria in a K-12 school",
    8: "Child/adult care center",
    9: "Child/adult home care",
    10: "Soup kitchen/shelter/food pantry",
    11: "Meals on Wheels program",
    12: "Community food program - other",
    13: "Community program, no additional info",
    14: "Vending machine",
    15: "Common coffee pot or snack tray",
    16: "From someone else/gift",
    17: "Mail order purchase",
    18: "Residential dining facility",
    19: "Grown or caught by you or someone you know",
    20: "Fish caught by you or someone you know",
    24: "Sport, recreation, or entertainment",
    25: "Street vendor, vending truck",
    26: "Fundraiser sales",
    27: "Store - convenience type",
    28: "Store - no additional information",
    91: "Other, specify",
    99: "Don't know",
}

# 99-00 combination types are NOT comparable to later codes.
COMBO_TYPE_9900 = {
    0: "Non-combination food",
    1: "Baby food combo",
    2: "Dried beans w/ adds",
    3: "Beverage combo",
    4: "Bread/baked products w/ adds",
    5: "Cereal mix/cereal w/ adds",
    6: "Chips w/ adds",
    7: "Crackers w/ adds",
    8: "Desserts w/ adds",
    9: "Eggs w/ adds",
    10: "Fish w/ adds",
    11: "Frozen meal",
    12: "Fruit combo",
    13: "Grains w/ adds",
    14: "Meat w/ adds",
    15: "Mixed dish",
    17: "Poultry w/ adds",
    18: "Salads (greens based)",
    19: "Salads (non-greens based)",
    20: "Sandwiches",
    21: "Soup combo",
    22: "Tortilla w/ adds",
    23: "Vegetable combo",
    90: "Other foods eaten together",
}

# 01-02 onward (DR1CCMTX). "Chips w/ additions" added 05-06 as code 14.
COMBO_TYPE = {
    0: "Non-combination food",
    1: "Beverage w/ additions",
    2: "Cereal w/ additions",
    3: "Bread/baked products w/ additions",
    4: "Salad",
    5: "Sandwiches",
    6: "Soup",
    7: "Frozen meals",
    8: "Ice cream/frozen yogurt w/ additions",
    9: "Dried beans and vegetable w/ additions",
    10: "Fruit w/ additions",
    11: "Tortilla products",
    12: "Meat, poultry, fish",
    13: "Lunchables",
    14: "Chips w/ additions",
    90: "Other mixtures",
}

SALT_TYPE_USUAL = {
    1: "Ordinary salt",
    2: "Lite salt",
    3: "Salt substitute",
    4: "Doesn't use salt at the table",
    91: "Other",
    99: "Don't know",
}

SALT_FREQ = {
    1: "Rarely",
    2: "Occasionally",
    3: "Very often",
    7: "Refused",
    9: "Don't know",
}

SALT_PREP = {
    1: "Ordinary salt",
    2: "Lite salt",
    3: "Salt substitute",
    4: "None",
    91: "Other",
    99: "Don't know",
}

SALT_YDAY = {1: "Yes", 2: "No", 7: "Refused", 9: "Don't know"}

SALT_YDAY_TYPE = {
    1: "Ordinary / sea salt",
    2: "Lite salt",
    3: "Salt substitute",
    7: "Refused",
    9: "Don't know",
}

# Tap water source. Early name DR1TWS; later disclosure recode DR1TWSZ.
TAP_WATER = {
    1: "Community supply",
    2: "Well or rain cistern",
    3: "Spring",
    4: "Don't drink tap water",
    91: "Other",
    99: "Don't know",
}




# ---------------------------------------------------------------------------
# File names by cycle (register these as default_table if you want)
# ---------------------------------------------------------------------------

DIET_FILES = {
    # cycle: (day1_iff, day2_iff, day1_tot, day2_tot, food_codes)
    "99-00": ("DRXIFF",   None,       "DRXTOT",   None,       "DRXFMT"),
    "01-02": ("DRXIFF_B", None,       "DRXTOT_B", None,       "DRXFMT_B"),
    "03-04": ("DR1IFF_C", "DR2IFF_C", "DR1TOT_C", "DR2TOT_C", "DRXFCD_C"),
    "05-06": ("DR1IFF_D", "DR2IFF_D", "DR1TOT_D", "DR2TOT_D", "DRXFCD_D"),
    "07-08": ("DR1IFF_E", "DR2IFF_E", "DR1TOT_E", "DR2TOT_E", "DRXFCD_E"),
    "09-10": ("DR1IFF_F", "DR2IFF_F", "DR1TOT_F", "DR2TOT_F", "DRXFCD_F"),
    "11-12": ("DR1IFF_G", "DR2IFF_G", "DR1TOT_G", "DR2TOT_G", "DRXFCD_G"),
    "13-14": ("DR1IFF_H", "DR2IFF_H", "DR1TOT_H", "DR2TOT_H", "DRXFCD_H"),
    "15-16": ("DR1IFF_I", "DR2IFF_I", "DR1TOT_I", "DR2TOT_I", "DRXFCD_I"),
    "17-18": ("DR1IFF_J", "DR2IFF_J", "DR1TOT_J", "DR2TOT_J", "DRXFCD_J"),
    "17-20": ("P_DR1IFF", "P_DR2IFF", "P_DR1TOT", "P_DR2TOT", "P_DRXFCD"),
    "21-23": ("DR1IFF_L", "DR2IFF_L", "DR1TOT_L", "DR2TOT_L", "DRXFCD_L"),
}

TWO_DAY_CYCLES = [c for c in CYCLES if c not in {"99-00", "01-02"}]

# ---------------------------------------------------------------------------
# Nutrient stems
# Individual-foods: DR{day}I{STEM}   totals: DR{day}T{STEM}
# Early (99-02) totals: DRXT{STEM}    early IFF: DRXI{STEM} / DRXIGRMS
# ---------------------------------------------------------------------------

NUTRIENT_STEMS = {
    # stem: (short, label, unit, notes)
    "KCAL": ("energy_kcal", "Energy (kcal)", "kcal", ""),
    "PROT": ("protein", "Protein (gm)", "gm", ""),
    "CARB": ("carbohydrate", "Carbohydrate (gm)", "gm", ""),
    "SUGR": ("sugars", "Total sugars (gm)", "gm", "Not on 99-00 public totals in the original nutrient set."),
    "FIBE": ("fiber", "Dietary fiber (gm)", "gm", ""),
    "TFAT": ("fat_total", "Total fat (gm)", "gm", ""),
    "SFAT": ("fat_sat", "Total saturated fatty acids (gm)", "gm", ""),
    "MFAT": ("fat_mono", "Total monounsaturated fatty acids (gm)", "gm", ""),
    "PFAT": ("fat_poly", "Total polyunsaturated fatty acids (gm)", "gm", ""),
    "CHOL": ("cholesterol", "Cholesterol (mg)", "mg", ""),
    "ATOC": ("vit_e_atoc", "Vitamin E as alpha-tocopherol (mg)", "mg", ""),
    "ATOA": ("vit_e_added", "Added alpha-tocopherol (Vitamin E) (mg)", "mg", ""),
    "RET":  ("retinol", "Retinol (mcg)", "mcg", ""),
    "VARA": ("vit_a_rae", "Vitamin A, RAE (mcg)", "mcg", "99-00 used VAIU / VARE instead of RAE."),
    "ACAR": ("alpha_carotene", "Alpha-carotene (mcg)", "mcg", ""),
    "BCAR": ("beta_carotene", "Beta-carotene (mcg)", "mcg", ""),
    "CRYP": ("cryptoxanthin", "Beta-cryptoxanthin (mcg)", "mcg", ""),
    "LYCO": ("lycopene", "Lycopene (mcg)", "mcg", ""),
    "LZ":   ("lutein_zeaxanthin", "Lutein + zeaxanthin (mcg)", "mcg", ""),
    "VB1":  ("thiamin", "Thiamin (Vitamin B1) (mg)", "mg", ""),
    "VB2":  ("riboflavin", "Riboflavin (Vitamin B2) (mg)", "mg", ""),
    "NIAC": ("niacin", "Niacin (mg)", "mg", ""),
    "VB6":  ("vit_b6", "Vitamin B6 (mg)", "mg", ""),
    "FOLA": ("folate_total", "Total folate (mcg)", "mcg", ""),
    "FA":   ("folic_acid", "Folic acid (mcg)", "mcg", ""),
    "FF":   ("folate_food", "Food folate (mcg)", "mcg", "IFF SAS name is DR1IFF / DR2IFF (collides with file name)."),
    "FDFE": ("folate_dfe", "Folate, DFE (mcg)", "mcg", ""),
    "CHL":  ("choline", "Total choline (mg)", "mg", "Added in later FNDDS cycles."),
    "VB12": ("vit_b12", "Vitamin B12 (mcg)", "mcg", ""),
    "B12A": ("vit_b12_added", "Added vitamin B12 (mcg)", "mcg", ""),
    "VC":   ("vit_c", "Vitamin C (mg)", "mg", ""),
    "VD":   ("vit_d", "Vitamin D (D2 + D3) (mcg)", "mcg", ""),
    "VK":   ("vit_k", "Vitamin K (mcg)", "mcg", ""),
    "CALC": ("calcium", "Calcium (mg)", "mg", ""),
    "PHOS": ("phosphorus", "Phosphorus (mg)", "mg", ""),
    "MAGN": ("magnesium", "Magnesium (mg)", "mg", ""),
    "IRON": ("iron", "Iron (mg)", "mg", ""),
    "ZINC": ("zinc", "Zinc (mg)", "mg", ""),
    "COPP": ("copper", "Copper (mg)", "mg", ""),
    "SODI": ("sodium", "Sodium (mg)", "mg", "99-00/01-02 totals used DRDTSODI (salt-adjusted)."),
    "POTA": ("potassium", "Potassium (mg)", "mg", ""),
    "SELE": ("selenium", "Selenium (mcg)", "mcg", ""),
    "CAFF": ("caffeine", "Caffeine (mg)", "mg", ""),
    "THEO": ("theobromine", "Theobromine (mg)", "mg", ""),
    "ALCO": ("alcohol", "Alcohol (gm)", "gm", ""),
    "MOIS": ("moisture", "Moisture (gm)", "gm", "99-00/01-02 totals used DRXTWATE, not DRXTMOIS."),
}

FATTY_ACID_STEMS = {
    "S040": ("sfa_4_0", "SFA 4:0 butanoic (gm)"),
    "S060": ("sfa_6_0", "SFA 6:0 hexanoic (gm)"),
    "S080": ("sfa_8_0", "SFA 8:0 octanoic (gm)"),
    "S100": ("sfa_10_0", "SFA 10:0 decanoic (gm)"),
    "S120": ("sfa_12_0", "SFA 12:0 dodecanoic (gm)"),
    "S140": ("sfa_14_0", "SFA 14:0 tetradecanoic (gm)"),
    "S160": ("sfa_16_0", "SFA 16:0 hexadecanoic (gm)"),
    "S180": ("sfa_18_0", "SFA 18:0 octadecanoic (gm)"),
    "M161": ("mfa_16_1", "MFA 16:1 hexadecenoic (gm)"),
    "M181": ("mfa_18_1", "MFA 18:1 octadecenoic (gm)"),
    "M201": ("mfa_20_1", "MFA 20:1 eicosenoic (gm)"),
    "M221": ("mfa_22_1", "MFA 22:1 docosenoic (gm)"),
    "P182": ("pfa_18_2", "PFA 18:2 octadecadienoic (gm)"),
    "P183": ("pfa_18_3", "PFA 18:3 octadecatrienoic (gm)"),
    "P184": ("pfa_18_4", "PFA 18:4 octadecatetraenoic (gm)"),
    "P204": ("pfa_20_4", "PFA 20:4 eicosatetraenoic (gm)"),
    "P205": ("pfa_20_5", "PFA 20:5 eicosapentaenoic (gm)"),
    "P225": ("pfa_22_5", "PFA 22:5 docosapentaenoic (gm)"),
    "P226": ("pfa_22_6", "PFA 22:6 docosahexaenoic (gm)"),
}

SHELLFISH_30D = [
    ("A", "clams", "Clams eaten during past 30 days"),
    ("B", "crabs", "Crabs eaten during past 30 days"),
    ("C", "crayfish", "Crayfish eaten during past 30 days"),
    ("D", "lobsters", "Lobsters eaten during past 30 days"),
    ("E", "mussels", "Mussels eaten during past 30 days"),
    ("F", "oysters", "Oysters eaten during past 30 days"),
    ("G", "scallops", "Scallops eaten during past 30 days"),
    ("H", "shrimp", "Shrimp eaten during past 30 days"),
    ("I", "other_shellfish", "Other shellfish eaten past 30 days"),
    ("J", "unknown_shellfish", "Other unknown shellfish eaten past 30 days"),
    ("K", "shellfish_refused", "Refused on shellfish eaten past 30 days"),
]

FISH_30D = [
    ("A", "breaded_fish", "Breaded fish products eaten past 30 days"),
    ("B", "tuna", "Tuna eaten during past 30 days"),
    ("C", "bass", "Bass eaten during past 30 days"),
    ("D", "catfish", "Catfish eaten during past 30 days"),
    ("E", "cod", "Cod eaten during past 30 days"),
    ("F", "flatfish", "Flatfish eaten during past 30 days"),
    ("G", "haddock", "Haddock eaten during past 30 days"),
    ("H", "mackerel", "Mackerel eaten during past 30 days"),
    ("I", "perch", "Perch eaten during past 30 days"),
    ("J", "pike", "Pike eaten during past 30 days"),
    ("K", "pollock", "Pollock eaten during past 30 days"),
    ("L", "porgy", "Porgy eaten during past 30 days"),
    ("M", "salmon", "Salmon eaten during past 30 days"),
    ("N", "sardines", "Sardines eaten during past 30 days"),
    ("O", "sea_bass", "Sea bass eaten during past 30 days"),
    ("P", "shark", "Shark eaten during past 30 days"),
    ("Q", "swordfish", "Swordfish eaten during past 30 days"),
    ("R", "trout", "Trout eaten during past 30 days"),
    ("S", "walleye", "Walleye eaten during past 30 days"),
    ("T", "other_fish", "Other fish eaten during past 30 days"),
    ("U", "unknown_fish", "Other unknown fish eaten in past 30 days"),
    ("V", "fish_refused", "Refused on fish eaten past 30 days"),
]





def _var(
    short,
    sas,
    kind,
    text,
    target,
    codes=None,
    sas_by_cycle=None,
    codes_by_cycle=None,
    label=None,
    notes=None,
    raw_codes=None,
    raw_codes_by_cycle=None,
    target_by_cycle=None,
    definition=None,
    definition_by_cycle=None,
    tables=None,
    day_pair=None,
    aliases=None,
):
    return {
        "short": short,
        "sas": sas,
        "kind": kind,
        "text": text,
        "label": label or text,
        "target": target,
        "codes": None if codes is None else dict(codes),
        "sas_by_cycle": dict(sas_by_cycle or {}),
        "codes_by_cycle": dict(codes_by_cycle or {}),
        "notes": notes or "",
        "raw_codes": None if raw_codes is None else dict(raw_codes),
        "raw_codes_by_cycle": dict(raw_codes_by_cycle or {}),
        "target_by_cycle": dict(target_by_cycle or {}),
        "definition": definition or "",
        "definition_by_cycle": dict(definition_by_cycle or {}),
        "tables": tables or ("tot", "iff"),
        "day_pair": day_pair,
        "aliases": list(aliases or []),
    }


def _early(name_9900, name_0102=None):
    """Cycle aliases for the single-day 1999-2002 files."""
    out = {"99-00": name_9900}
    if name_0102:
        out["01-02"] = name_0102
    elif name_9900:
        out["01-02"] = name_9900
    return out


def _early_tot_name(stem: str) -> str:
    if stem == "SODI":
        return "DRDTSODI"
    if stem == "MOIS":
        return "DRXTWATE"
    return f"DRXT{stem}"


DIET_VARS = {
    "seqn": _var(
        "seqn", "SEQN", "id",
        "Respondent sequence number.",
        T_ALL,
        label="Respondent sequence number",
        definition="Unique respondent identifier. Links diet files to DEMO and all other NHANES tables.",
        tables=("tot", "iff"),
    ),

    # ----- weights --------------------------------------------------------
    "wt_diet_d1": _var(
        "wt_diet_d1", "WTDRD1", "weight",
        "Dietary day one sample weight.",
        T_ALL,
        sas_by_cycle={"17-20": "WTDRD1PP"},
        notes=(
            "Use for any analysis that uses Day 1 recall data (alone or with MEC vars). "
            "Adjusted from the MEC weight for dietary nonresponse and weekday/weekend allocation. "
            "17-20 pre-pandemic public files rename this WTDRD1PP; do not mix with WTDRD1. "
            "On 99-00/01-02 this is the 2-year Day-1 dietary weight."
        ),
        definition="Person-level Day 1 dietary weight. Sums to the same control total as the MEC weight.",
        tables=("tot", "iff"),
    ),
    "wt_diet_d2": _var(
        "wt_diet_d2", "WTDR2D", "weight",
        "Dietary two-day sample weight.",
        T_ALL,
        sas_by_cycle={"17-20": "WTDR2DPP"},
        notes=(
            "Use only when both Day 1 and Day 2 recalls are in the analysis. "
            "Zero when Day 2 was not done/incomplete. "
            "Not on 99-00 or 01-02 (those cycles released one in-person recall). "
            "17-20 uses WTDR2DPP."
        ),
        definition="Person-level two-day dietary weight, further adjusted for Day 2 nonresponse and weekday/weekend pairs.",
        tables=("tot", "iff"),
    ),
    "wt_diet_4yr": _var(
        "wt_diet_4yr", "WTDR4YR", "weight",
        "Dietary day one 4-year sample weight. Used for 1999-2002 data collection years only.",
        T_ALL,
        notes="On 99-00 and 01-02 public diet files only. Use for combined 1999-2002 Day-1 analyses.",
        definition="4-year Day 1 dietary weight for pooled 1999-2002 estimates.",
        tables=("tot", "iff"),
    ),

    # ----- recall quality / coverage -------------------------------------
    "recall_status": _var(
        "recall_status", "DR1DRSTZ", "categorical",
        "Dietary recall status.",
        T_ALL,
        codes=RECALL_STATUS,
        sas_by_cycle={
            "99-00": "DRDDRSTS",
            "01-02": "DRDDRSTZ",
        },
        codes_by_cycle=RECALL_STATUS_BY_CYCLE,
        day_pair="DR2DRSTZ",
        notes=(
            "Filter analytic samples to code 1 for nutrient totals. "
            "IFF files keep only codes 1 and 4 (plus water-only rows in some cycles). "
            "Code 4 = human milk reported; grams and nutrients from human milk are missing, "
            "so daily totals are not computed. "
            "99-00 used a 5-code scheme (DRDDRSTS) that split 'reliable but not minimum' (2) "
            "from 'not reliable' (3). From 01-02 those collapse into code 2; code 3 is unused. "
            "Fasting with a complete AMPM is coded 1."
        ),
        definition=(
            "Quality/completeness of the 24-hour recall. "
            "1 = first 4 AMPM steps complete and foods identified for each occasion. "
            "2 = incomplete / unreliable (no IFF rows; nutrient totals missing). "
            "4 = human milk reported. 5 = recall not done."
        ),
        definition_by_cycle={
            "99-00": (
                "DRDDRSTS: 1=reliable and minimum criteria; 2=reliable but not minimum; "
                "3=not reliable; 4=breast-fed infant or child; 5=not done."
            ),
        },
        tables=("tot", "iff"),
    ),
    "post_recall_status": _var(
        "post_recall_status", "DRASCST2", "categorical",
        "Post dietary recall section status.",
        T_ALL,
        codes=COMPLETE_PARTIAL,
        notes="1999-2002 totals file only.",
        definition="Completeness of the post-recall (water / salt / fish) section.",
        tables=("tot",),
    ),
    "breastfed_either_day": _var(
        "breastfed_either_day", "DRABF", "categorical",
        "Breast-fed infant (either day).",
        T_ALL,
        codes=BREASTFED,
        notes="Added with the two-day files (03-04+). 1 if human milk was reported on either recall day.",
        definition="1 = infant/child consumed human milk on Day 1 and/or Day 2.",
        tables=("tot", "iff"),
    ),
    "intake_days": _var(
        "intake_days", "DRDINT", "categorical",
        "Number of days of intake.",
        T_ALL,
        codes=INTAKE_DAYS,
        notes="03-04 onward. 1 = complete reliable Day 1 only; 2 = complete reliable Day 1 and Day 2.",
        definition="Count of complete intake days available for the participant.",
        tables=("tot", "iff"),
    ),

    # ----- interview metadata --------------------------------------------
    "interviewer_id": _var(
        "interviewer_id", "DR1EXMER", "id",
        "Interviewer ID code.",
        T_ALL,
        sas_by_cycle={"99-00": "DRDEXMER", "01-02": "DRDEXMER"},
        day_pair="DR2EXMER",
        definition="Masked interviewer identifier for the recall.",
        tables=("tot", "iff"),
    ),
    "assigned_interview_mode": _var(
        "assigned_interview_mode", "DRDAINMD", "categorical",
        "Assigned mode of interview.",
        T_ALL,
        codes=INTERVIEW_MODE,
        notes="1999-2002. Distinct from interview_mode (actual mode).",
        definition="Mode the recall was assigned to, not necessarily the completed mode.",
        tables=("tot",),
    ),
    "days_since_hh": _var(
        "days_since_hh", "DR1DBIH", "continuous",
        "Number of days between intake day and the day of family questionnaire administered in the household.",
        T_ALL,
        day_pair="DR2DBIH",
        notes="Negative if the family interview happened after the intake day. Not on 99-02 public files.",
        definition="Signed day count between the 24-hour intake date and the household family interview.",
        tables=("tot", "iff"),
    ),
    "intake_weekday": _var(
        "intake_weekday", "DR1DAY", "categorical",
        "Intake day of the week.",
        T_ALL,
        codes=DAY_OF_WEEK,
        sas_by_cycle={"99-00": "DRDDAY", "01-02": "DRDDAY"},
        day_pair="DR2DAY",
        definition="Weekday of the 24-hour intake (1=Sunday ... 7=Saturday). Needed because WTDRD1 rebalances weekends.",
        tables=("tot", "iff"),
    ),
    "recall_language": _var(
        "recall_language", "DR1LANG", "categorical",
        "Language respondent used mostly.",
        T_ALL,
        codes=DIET_LANG,
        sas_by_cycle={"99-00": "DRALANG", "01-02": "DRALANG"},
        day_pair="DR2LANG",
        definition="Language used for most of the dietary recall.",
        tables=("tot", "iff"),
    ),
    "interview_mode": _var(
        "interview_mode", "DRDINTMD", "categorical",
        "Mode of interview.",
        T_ALL,
        codes=INTERVIEW_MODE,
        notes="Public on 99-00 (and some early docs). Day 1 is MEC in-person through 17-18; 21-23 Day 1 was also telephone.",
        definition="1=in-person; 2=telephone.",
        tables=("tot", "iff"),
    ),
    "main_respondent": _var(
        "main_respondent", "DR1MRESP", "categorical",
        "Who was the main respondent for this interview?",
        T_ALL,
        codes=RESPONDENT_REL,
        sas_by_cycle={
            "99-00": "DRARESP",
            "01-02": "DRDRESP",
            "03-04": "DR1MNRSP",
            "05-06": "DR1MNRSP",
            "07-08": "DR1MNRSP",
            "09-10": "DR1MNRSP",
            "11-12": "DR1MNRSP",
            "13-14": "DR1MNRSP",
        },
        codes_by_cycle={
            "99-00": RESPONDENT_3CAT,
            "01-02": RESPONDENT_3CAT,
        },
        day_pair="DR2MRESP",
        notes=(
            "99-02: 3-cat SP/proxy. 03-14: DR1MNRSP relationship codes. "
            "15-16 renamed to DR1MRESP (same relationship codes). "
            "Day 2 name is DR2MNRSP through 13-14 and DR2MRESP from 15-16."
        ),
        definition="Person who provided most of the recall.",
        tables=("tot",),
    ),
    "helper": _var(
        "helper", "DR1HELP", "categorical",
        "Who helped in responding for this interview?",
        T_ALL,
        codes=RESPONDENT_REL,
        sas_by_cycle={
            "03-04": "DR1HELPD",
            "05-06": "DR1HELPD",
            "07-08": "DR1HELPD",
            "09-10": "DR1HELPD",
            "11-12": "DR1HELPD",
            "13-14": "DR1HELPD",
        },
        day_pair="DR2HELP",
        notes="DR1HELPD through 13-14; DR1HELP from 15-16. Code 13 = no one.",
        definition="Person who assisted the main respondent, if any.",
        tables=("tot",),
    ),
    "amount_vs_usual": _var(
        "amount_vs_usual", "DR1_300", "categorical",
        "Was the amount of food that {you/NAME} ate yesterday much more than usual, usual, or much less than usual?",
        T_ALL,
        codes=AMOUNT_VS_USUAL,
        sas_by_cycle={"99-00": "DRQ300", "01-02": "DRD300"},
        codes_by_cycle={"99-00": AMOUNT_VS_USUAL_9900},
        day_pair="DR2_300",
        notes="99-00 DRQ300 used a different 1/2/3 order (usual / less / more).",
        definition="Self-assessed intake volume relative to a typical day.",
        tables=("tot",),
    ),

    # ----- IFF keys / food row metadata ----------------------------------
    "food_line": _var(
        "food_line", "DR1ILINE", "id",
        "Food/individual component number.",
        T_ALL,
        sas_by_cycle={"99-00": "DRXILINE", "01-02": "DRXILINE"},
        day_pair="DR2ILINE",
        notes="Primary key with SEQN on IFF files. One row per reported food/component.",
        definition="Sequential line number of the food/component within the recall day.",
        tables=("iff",),
    ),
    "food_code": _var(
        "food_code", "DR1IFDCD", "id",
        "USDA food code.",
        T_ALL,
        sas_by_cycle={"99-00": "DRDIFDCD", "01-02": "DRDIFDCD"},
        day_pair="DR2IFDCD",
        notes=(
            "decode_rows=True replaces this code with the FNDDS long description "
            "from Code_Details_Diet_Lookups (cycle-specific, latest fallback). "
            "99-02 format files only have the 60-char short label."
        ),
        definition="8-digit FNDDS/USDA food code identifying the reported item.",
        tables=("iff",),
    ),
    "mod_code": _var(
        "mod_code", "DR1MC", "id",
        "Modification code.",
        T_ALL,
        day_pair="DR2MC",
        notes=(
            "decode_rows=True replaces this code with the modification description "
            "from Code_Details_Diet_Lookups. Not on every cycle's public IFF."
        ),
        definition="FNDDS modification code when the reported food used a modified recipe.",
        tables=("iff",),
    ),
    "combo_number": _var(
        "combo_number", "DR1CCMNM", "categorical",
        "Combination food number (sequential number).",
        T_ALL,
        sas_by_cycle={"99-00": "DRXCCMNM", "01-02": "DRXCCMNM"},
        day_pair="DR2CCMNM",
        definition="Links component rows that were eaten together. 0 = not part of a combination.",
        tables=("iff",),
    ),
    "combo_type": _var(
        "combo_type", "DR1CCMTX", "categorical",
        "Combination food type.",
        T_ALL,
        codes=COMBO_TYPE,
        sas_by_cycle={"99-00": "DRDCCMTY", "01-02": "DRDCCMTZ"},
        codes_by_cycle={"99-00": COMBO_TYPE_9900},
        day_pair="DR2CCMTX",
        notes=(
            "99-00 combination codes are a different scheme (do not pool with later codes). "
            "Code 14 (chips w/ additions) added 05-06."
        ),
        definition="Type of multi-item combination; 0 = standalone food.",
        tables=("iff",),
    ),
    "eaten_at_home": _var(
        "eaten_at_home", "DR1_040Z", "categorical",
        "Did you eat this meal at home?",
        T_ALL,
        codes=YES_NO,
        sas_by_cycle={"99-00": "DRD040", "01-02": "DRD040Z"},
        codes_by_cycle={"99-00": MEAL_PLACE_9900},
        day_pair="DR2_040Z",
        notes=(
            "99-00 DRD040 is a place list (not a yes/no home flag). "
            "Home is code 9. Do not treat those codes as 1/2. "
            "01-02 DRD040Z is the yes/no home flag; 2001 values were derived from place."
        ),
        definition="1=eaten at home; 2=not at home (01-02+). 99-00 = place the meal/food was eaten.",
        tables=("iff",),
    ),
    "eat_time": _var(
        "eat_time", "DR1_020", "continuous",
        "Time of eating occasion (HH:MM).",
        T_ALL,
        sas_by_cycle={"99-00": "DRD020", "01-02": "DRD020"},
        day_pair="DR2_020",
        notes="Released as HH:MM (SAS HHMM). Range typically 00:00-23:59.",
        definition="Clock time the eating occasion began.",
        tables=("iff",),
    ),
    "eat_occasion": _var(
        "eat_occasion", "DR1_030Z", "categorical",
        "Name of eating occasion.",
        T_ALL,
        codes=EAT_OCC,
        sas_by_cycle={"99-00": "DRD030", "01-02": "DRD030Z"},
        codes_by_cycle={"99-00": EAT_OCC_9900},
        day_pair="DR2_030Z",
        notes=(
            "English and Spanish labels are separate codes for the same meal "
            "(e.g. 1 Breakfast / 10 Desayuno). 99-00 used a different numbering (DRD030)."
        ),
        definition="Respondent-chosen name of the eating occasion. Occasions are not defined for the respondent.",
        tables=("iff",),
    ),
    "food_source": _var(
        "food_source", "DR1FS", "categorical",
        "Where did you get (this/most of the ingredients for this) {FOODNAME}?",
        T_ALL,
        codes=FOOD_SOURCE,
        day_pair="DR2FS",
        notes="Added 03-04. Convenience-store split (27/28) and fundraiser (26) appear in later cycles.",
        definition="Where the food or most of its ingredients were obtained.",
        tables=("iff",),
    ),
    "eaten_at_home": _var(
        "eaten_at_home", "DR1_040Z", "categorical",
        "Did you eat this meal at home?",
        T_ALL,
        codes=YES_NO,
        sas_by_cycle={"99-00": "DRD040", "01-02": "DRD040Z"},
        day_pair="DR2_040Z",
        notes="99-00 DRD040 was a place list, not a yes/no home flag. Do not treat those codes as 1/2.",
        definition="1=eaten at home; 2=not at home.",
        tables=("iff",),
    ),
    "food_grams": _var(
        "food_grams", "DR1IGRMS", "continuous",
        "Grams.",
        T_ALL,
        sas_by_cycle={"99-00": "DRXIGRMS", "01-02": "DRXIGRMS"},
        day_pair="DR2IGRMS",
        notes="Missing for unquantified human milk (recall_status=4).",
        definition="Amount of the food/beverage consumed, grams as reported/converted.",
        tables=("iff",),
    ),
    "n_foods": _var(
        "n_foods", "DR1TNUMF", "continuous",
        "Number of foods/beverages reported.",
        T_ALL,
        sas_by_cycle={"99-00": "DRXTNUMF", "01-02": "DRXTNUMF"},
        day_pair="DR2TNUMF",
        definition="Count of food/beverage rows contributing to the day's totals. Missing when recall_status is 2 or 5.",
        tables=("tot",),
    ),
    "total_grams": _var(
        "total_grams", "DR1TGRMS", "continuous",
        "Total grams of food and beverages reported.",
        T_ALL,
        day_pair="DR2TGRMS",
        notes="Present on later TOT files. Not the same as moisture (DR1TMOIS).",
        definition="Sum of food/beverage gram amounts for the recall day.",
        tables=("tot",),
    ),

    # ----- water ----------------------------------------------------------
    "water_plain_g": _var(
        "water_plain_g", "DR1_320Z", "continuous",
        "Total plain water drank yesterday (gm), including tap, fountain, cooler, bottled, and spring water.",
        T_ALL,
        sas_by_cycle={
            "99-00": "DRD320GW",
            "01-02": "DRD320GW",
            "03-04": "DR1_320",
        },
        day_pair="DR2_320Z",
        definition="Total plain (unsweetened) drinking water, grams.",
        tables=("tot",),
    ),
    "water_tap_g": _var(
        "water_tap_g", "DR1_330Z", "continuous",
        "Total tap water drank yesterday (gm), including filtered tap water and drinking-fountain water.",
        T_ALL,
        sas_by_cycle={
            "99-00": "DRD330GW",
            "01-02": "DRD330GW",
            "03-04": "DR1_330",
        },
        day_pair="DR2_330Z",
        definition="Tap-water subset of plain water, grams.",
        tables=("tot",),
    ),
    "water_bottled_g": _var(
        "water_bottled_g", "DR1BWATZ", "continuous",
        "Total bottled water drank yesterday (gm).",
        T_ALL,
        sas_by_cycle={"03-04": "DR1BWATR"},
        day_pair="DR2BWATZ",
        definition="Bottled-water subset of plain water, grams.",
        tables=("tot",),
    ),
    "water_carbonated_g": _var(
        "water_carbonated_g", "DR1CWATR", "continuous",
        "Total carbonated water drank yesterday (gm).",
        T_ALL,
        sas_by_cycle={"99-00": "DRDCWATR", "01-02": "DRDCWATR"},
        day_pair="DR2CWATR",
        notes="Present on early/mid cycles; later water coding dropped a separate carbonated total.",
        definition="Unsweetened carbonated water consumed as a beverage, grams.",
        tables=("tot",),
    ),
    "tap_water_source": _var(
        "tap_water_source", "DR1TWSZ", "categorical",
        "When you drink tap water, what is the main source of the tap water?",
        T_ALL,
        codes=TAP_WATER,
        sas_by_cycle={
            "03-04": "DR1TWS",
            "05-06": "DR1TWS",
            "07-08": "DR1TWS",
            "09-10": "DR1TWS",
            "11-12": "DR1TWS",
            "13-14": "DR1TWS",
        },
        day_pair="DR2TWSZ",
        notes="Older files use DR1TWS / DR2TWS. Later disclosure name is DR1TWSZ.",
        definition="Usual source of tap water.",
        tables=("tot",),
    ),

    # ----- salt / special diet (Day 1 TOT only for most of these) --------
    "salt_adjust_flag": _var(
        "salt_adjust_flag", "DRDTSODF", "categorical",
        "Salt adjustment flag.",
        T_ALL,
        codes=SALT_ADJ,
        notes="1999-2002 indicator that DRDTSODI was adjusted for salt used in food preparation.",
        definition="Whether total sodium was adjusted for reported salt use in preparation.",
        tables=("tot",),
    ),
    "salt_table_type": _var(
        "salt_table_type", "DBQ095Z", "categorical",
        "What type of salt {do you/does SP} usually add to food at the table?",
        T_ALL,
        codes=SALT_TYPE_USUAL,
        sas_by_cycle={"01-02": "DBQ095"},
        notes="Day 1 TOT only. 01-02 name is DBQ095.",
        definition="Usual type of table salt.",
        tables=("tot",),
    ),
    "salt_table_freq": _var(
        "salt_table_freq", "DBD100", "categorical",
        "How often {do you/does SP} add ordinary salt to food at the table?",
        T_ALL,
        codes=SALT_FREQ,
        notes="Day 1 TOT only.",
        definition="Usual frequency of adding salt at the table.",
        tables=("tot",),
    ),
    "salt_in_prep": _var(
        "salt_in_prep", "DRQSPREP", "categorical",
        "Salt used in preparation?",
        T_ALL,
        codes=SALT_PREP,
        notes="Day 1 TOT only.",
        definition="Type of salt usually used in home food preparation.",
        tables=("tot",),
    ),
    "salt_table_yesterday": _var(
        "salt_table_yesterday", "DR1STY", "categorical",
        "Did {you/SP} add any salt to food at the table yesterday?",
        T_ALL,
        codes=SALT_YDAY,
        day_pair="DR2STY",
        definition="Salt added at the table on the recall day.",
        tables=("tot",),
    ),
    "salt_table_yesterday_type": _var(
        "salt_table_yesterday_type", "DR1SKY", "categorical",
        "What type of salt was it?",
        T_ALL,
        codes=SALT_YDAY_TYPE,
        day_pair="DR2SKY",
        definition="Type of salt added at the table on the recall day.",
        tables=("tot",),
    ),
    "special_diet": _var(
        "special_diet", "DRQSDIET", "categorical",
        "On special diet?",
        T_ALL,
        codes=YES_NO,
        notes="Day 1 TOT only. Type flags DRQSDT1-12 and DRQSDT91 can all be 1 on the same person.",
        definition="Currently on a diet to lose weight or for another health-related reason.",
        tables=("tot",),
    ),
    "diet_wt_loss": _var("diet_wt_loss", "DRQSDT1", "categorical", "Weight loss / low calorie diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",)),
    "diet_low_fat": _var("diet_low_fat", "DRQSDT2", "categorical", "Low fat / low cholesterol diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",)),
    "diet_low_salt": _var("diet_low_salt", "DRQSDT3", "categorical", "Low salt / low sodium diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",)),
    "diet_low_sugar": _var("diet_low_sugar", "DRQSDT4", "categorical", "Sugar free / low sugar diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",)),
    "diet_low_fiber": _var("diet_low_fiber", "DRQSDT5", "categorical", "Low fiber diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",)),
    "diet_high_fiber": _var("diet_high_fiber", "DRQSDT6", "categorical", "High fiber diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",)),
    "diet_diabetic": _var("diet_diabetic", "DRQSDT7", "categorical", "Diabetic diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",)),
    "diet_wt_gain": _var("diet_wt_gain", "DRQSDT8", "categorical", "Weight gain / muscle building diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",)),
    "diet_low_carb": _var(
        "diet_low_carb", "DRQSDT9", "categorical",
        "Low carbohydrate diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",),
        notes="Added after the original 8-type list (around 07-08+).",
    ),
    "diet_high_protein": _var(
        "diet_high_protein", "DRQSDT10", "categorical",
        "High protein diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",),
        notes="Added after the original 8-type list.",
    ),
    "diet_gluten_free": _var(
        "diet_gluten_free", "DRQSDT11", "categorical",
        "Gluten-free / celiac diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",),
        notes="Later-cycle addition.",
    ),
    "diet_renal": _var(
        "diet_renal", "DRQSDT12", "categorical",
        "Renal / kidney diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",),
        notes="Later-cycle addition.",
    ),
    "diet_other": _var("diet_other", "DRQSDT91", "categorical", "Other special diet.", T_ALL, codes=YES_NO_ONLY, tables=("tot",)),

    # Early-cycle vitamin measures that are not equivalent to later RAE / ATOC.
    "vit_a_iu": _var(
        "vit_a_iu", "DRXTVAIU", "continuous",
        "Vitamin A (IU).",
        T_ALL,
        notes="1999-2002 only. Do not pool with vit_a_rae.",
        definition="Total vitamin A from foods and beverages, International Units.",
        tables=("tot",),
    ),
    "vit_a_re": _var(
        "vit_a_re", "DRXTVARE", "continuous",
        "Vitamin A (RE).",
        T_ALL,
        notes="1999-2002 only. Retinol equivalents, not RAE.",
        definition="Total vitamin A from foods and beverages, retinol equivalents.",
        tables=("tot",),
    ),
    "carotene_re": _var(
        "carotene_re", "DRXTCARO", "continuous",
        "Carotene (RE).",
        T_ALL,
        notes="1999-2002 combined carotene. Later cycles split ACAR/BCAR/CRYP/LYCO/LZ.",
        definition="Total carotene from foods and beverages, retinol equivalents.",
        tables=("tot",),
    ),
    "vit_e_ate": _var(
        "vit_e_ate", "DRXTVE", "continuous",
        "Vitamin E, alpha-tocopherol equivalents (mg).",
        T_ALL,
        notes="1999-2002 ATE units. Later cycles report vit_e_atoc (alpha-tocopherol mg).",
        definition="Vitamin E from foods and beverages as alpha-tocopherol equivalents.",
        tables=("tot",),
    ),

    # fish/shellfish (Day 1 TOT). Use MEC weights if these are analyzed without other diet vars.
    "ate_shellfish_30d": _var(
        "ate_shellfish_30d", "DRD340", "categorical",
        "During the past 30 days did you eat any types of shellfish listed on this card?",
        T_1_150,
        codes=YES_NO,
        sas_by_cycle={"99-00": "DRQ340", "01-02": "DRQ340"},
        notes="Day 1 TOT only. If no other diet vars are in the model, NCHS says WTMEC2YR / WTMECPRP is appropriate.",
        tables=("tot",),
    ),
    "ate_fish_30d": _var(
        "ate_fish_30d", "DRD360", "categorical",
        "During the past 30 days did you eat any types of fish listed on this card?",
        T_1_150,
        codes=YES_NO,
        sas_by_cycle={"99-00": "DRQ360", "01-02": "DRQ360"},
        notes="Day 1 TOT only. Same weight note as ate_shellfish_30d.",
        tables=("tot",),
    ),
}

DIET_VARS["combo_flag"] = _var(
    "combo_flag", "DRDCFF", "categorical",
    "Combination food flag.",
    T_ALL, codes=COMBO_FLAG, tables=("iff",),
    notes="1999-2000 IFF only. 0=standalone food; 1=part of a combination (use with combo_number).",
    definition="0 = single-component food; 1 = combination food.",
)

DIET_VARS["modified_recipe"] = _var(
    "modified_recipe", "DRDMRUF", "categorical",
    "Flag for modified recipe use.",
    T_ALL, codes=MODIFIED_RECIPE, tables=("iff",),
    notes=(
        "1999-2000 IFF only. 1 = recipe modified or food not in the USDA database. "
        "The 8-digit USDA food code is a reporting label; nutrient values reflect the modification."
    ),
    definition="0 = non-modified recipe; 1 = modified recipe.",
)
DIET_VARS["salt_adjust_food"] = _var(
    "salt_adjust_food", "DRDISODF", "categorical",
    "Salt adjustment flag of individual food.",
    T_ALL, codes=SALT_ADJ_IFF, tables=("iff",),
    notes="1999-2002 IFF counterpart of salt_adjust_flag (DRDTSODF on totals).",
    definition="Whether this food's sodium value was adjusted for reported salt use in preparation.",
)

DIET_VARS["vit_a_iu"] = _var(
    "vit_a_iu", "DRXTVAIU", "continuous",
    "Vitamin A (IU).",
    T_ALL,
    sas_by_cycle={"99-00": "DRXTVAIU"},
    notes=(
        "1999-2000 only. TOT = DRXTVAIU; IFF = DRXIVAIU. "
        "Do not pool with vit_a_rae (RAE starts 01-02)."
    ),
    definition="Vitamin A from foods and beverages, International Units. IFF = this food; TOT = day total.",
    tables=("tot", "iff"),
)
DIET_VARS["vit_a_re"] = _var(
    "vit_a_re", "DRXTVARE", "continuous",
    "Vitamin A (RE).",
    T_ALL,
    sas_by_cycle={"99-00": "DRXTVARE"},
    notes=(
        "1999-2000 only. TOT = DRXTVARE; IFF = DRXIVARE. "
        "Retinol equivalents, not RAE. Do not pool with vit_a_rae."
    ),
    definition="Vitamin A from foods and beverages, retinol equivalents. IFF = this food; TOT = day total.",
    tables=("tot", "iff"),
)
DIET_VARS["carotene_re"] = _var(
    "carotene_re", "DRXTCARO", "continuous",
    "Carotene (RE).",
    T_ALL,
    sas_by_cycle={"99-00": "DRXTCARO"},
    notes=(
        "1999-2000 combined carotene. TOT = DRXTCARO; IFF = DRXICARO. "
        "Later cycles split ACAR/BCAR/CRYP/LYCO/LZ."
    ),
    definition="Total carotene from foods and beverages, retinol equivalents. IFF = this food; TOT = day total.",
    tables=("tot", "iff"),
)
DIET_VARS["vit_e_ate"] = _var(
    "vit_e_ate", "DRXTVE", "continuous",
    "Vitamin E, alpha-tocopherol equivalents (mg).",
    T_ALL,
    sas_by_cycle={"99-00": "DRXTVE"},
    notes=(
        "1999-2000 ATE units. TOT = DRXTVE; IFF = DRXIVE. "
        "Later cycles report vit_e_atoc (alpha-tocopherol mg)."
    ),
    definition="Vitamin E from foods and beverages as alpha-tocopherol equivalents. IFF = this food; TOT = day total.",
    tables=("tot", "iff"),
)

DIET_VARS["food_code_desc_short"] = _var(
    "food_code_desc_short", "DRXFCSD", "text",
    "Short food code description.",
    T_ALL,
    notes="From DRXFCD / cycle equivalent. Join to IFF on DRXFDCD = DR1IFDCD. Early DRXFMT uses VALUE (up to 60 chars).",
    definition="Short USDA/FNDDS food description (up to 60 characters).",
    tables=("fcd",),
)
DIET_VARS["food_code_desc_long"] = _var(
    "food_code_desc_long", "DRXFCLD", "text",
    "Long food code description.",
    T_ALL,
    notes="From DRXFCD (03-04+). Up to 200 characters. Not on 99-00 DRXFMT (that file only has the 60-char VALUE).",
    definition="Complete USDA/FNDDS food description.",
    tables=("fcd",),
)
DIET_VARS["food_code_fcd"] = _var(
    "food_code_fcd", "DRXFDCD", "id",
    "Food code on the Food Code Description file.",
    T_ALL,
    sas_by_cycle={"99-00": "START", "01-02": "START"},
    notes="Join key to IFF food_code (DR1IFDCD / DRDIFDCD). 99-02 format files use START.",
    definition="Numeric USDA food code on the description/format support file.",
    tables=("fcd",),
)
DIET_VARS["mod_code_desc"] = _var(
    "mod_code_desc", "DRXMCD", "text",
    "Modification code description.",
    T_ALL,
    tables=("mcd",),
    notes="Support file DRXMCD. Join to IFF mod_code (DR1MC / DRXMC).",
    definition="Text description of the FNDDS recipe modification.",
)




def _diet_type_flag(short, sas, type_code, label, notes=None):
    extra = notes or ""
    return _var(
        short, sas, "flag",
        label,
        T_ALL,
        codes={
            type_code: label,
            1: label,  # some public files store 1 instead of the type number
        },
        notes=(
            "Special-diet type checkbox on Day 1 TOT (asked only if special_diet=1). "
            f"Selected rows carry {type_code} (or 1 in some cycles); NaN means this type was not reported. "
            "There is no 2=No on the type-number files. Multiple DRQSDT* flags can be set on the same person. "
            + extra
        ).strip(),
        definition=f"1 or {type_code} = currently on a {label.lower()}; missing = not this diet type.",
        tables=("tot",),
    )


DIET_VARS.update({
    "diet_wt_loss": _diet_type_flag("diet_wt_loss", "DRQSDT1", 1, "Weight loss / low calorie diet"),
    "diet_low_fat": _diet_type_flag("diet_low_fat", "DRQSDT2", 2, "Low fat / low cholesterol diet"),
    "diet_low_salt": _diet_type_flag("diet_low_salt", "DRQSDT3", 3, "Low salt / low sodium diet"),
    "diet_low_sugar": _diet_type_flag("diet_low_sugar", "DRQSDT4", 4, "Sugar free / low sugar diet"),
    "diet_low_fiber": _diet_type_flag("diet_low_fiber", "DRQSDT5", 5, "Low fiber diet"),
    "diet_high_fiber": _diet_type_flag("diet_high_fiber", "DRQSDT6", 6, "High fiber diet"),
    "diet_diabetic": _diet_type_flag("diet_diabetic", "DRQSDT7", 7, "Diabetic diet"),
    "diet_wt_gain": _diet_type_flag("diet_wt_gain", "DRQSDT8", 8, "Weight gain / muscle building diet"),
    "diet_low_carb": _diet_type_flag(
        "diet_low_carb", "DRQSDT9", 9, "Low carbohydrate diet",
        notes="Added after the original 8-type list (around 07-08+).",
    ),
    "diet_high_protein": _diet_type_flag(
        "diet_high_protein", "DRQSDT10", 10, "High protein diet",
        notes="Added after the original 8-type list.",
    ),
    "diet_gluten_free": _diet_type_flag(
        "diet_gluten_free", "DRQSDT11", 11, "Gluten-free / celiac diet",
        notes="Later-cycle addition.",
    ),
    "diet_renal": _diet_type_flag(
        "diet_renal", "DRQSDT12", 12, "Renal / kidney diet",
        notes="Later-cycle addition.",
    ),
    "diet_other": _diet_type_flag("diet_other", "DRQSDT91", 91, "Other special diet"),
})

def _add_nutrient_vars(vars_map: dict) -> None:
    """Register nutrient columns. TOT default name is DR1T{stem}; IFF is DR1I{stem}."""
    for stem, (short, label, _unit, extra) in NUTRIENT_STEMS.items():
        early_name = _early_tot_name(stem)
        vars_map[short] = _var(
            short, f"DR1T{stem}", "continuous",
            label, T_ALL,
            sas_by_cycle={"99-00": early_name, "01-02": early_name},
            day_pair=f"DR2T{stem}",
            notes=(
                f"TOT column DR1T{stem} / DR2T{stem}. "
                f"IFF column is DR1I{stem} / DR2I{stem} "
                f"(99-02: DRXI{stem}"
                + (f"; moisture IFF is DRXIWATE on 99-00" if stem == "MOIS" else "")
                + f"). {extra}"
            ).strip(),
            definition=(
                f"{label.lower()} from foods and beverages. "
                "IFF = amount from this food/component; TOT = day total. "
                "Excludes supplements, medications, and plain drinking water."
            ),
            tables=("tot", "iff"),
        )



def _add_fatty_acid_vars(vars_map: dict) -> None:
    for stem, (short, label) in FATTY_ACID_STEMS.items():
        vars_map[short] = _var(
            short, f"DR1T{stem}", "continuous",
            label, T_ALL,
            sas_by_cycle={"99-00": f"DRXT{stem}", "01-02": f"DRXT{stem}"},
            day_pair=f"DR2T{stem}",
            notes=f"TOT column DR1T{stem} / DR2T{stem}. IFF is DR1I{stem}/DRXI{stem}. Early TOT uses DRXT{stem}.",
            definition=f"{label.lower()} from foods and beverages. IFF = this food; TOT = day total.",
            tables=("tot", "iff"),
        )


def _add_seafood_vars(vars_map: dict) -> None:
    for letter, slug, label in SHELLFISH_30D:
        vars_map[f"ate_{slug}_30d"] = _var(
            f"ate_{slug}_30d", f"DRD350{letter}", "categorical",
            label, T_1_150, codes=YES_NO_ONLY, tables=("tot",),
        )
        if letter == "K":
            continue
        vars_map[f"times_{slug}_30d"] = _var(
            f"times_{slug}_30d", f"DRD350{letter}Q", "continuous",
            f"Number of times {slug.replace('_', ' ')} eaten in past 30 days.",
            T_1_150,
            sas_by_cycle={"99-00": f"DRQ350{letter}Q", "01-02": f"DRQ350{letter}Q"},
            tables=("tot",),
        )
    for letter, slug, label in FISH_30D:
        vars_map[f"ate_{slug}_30d"] = _var(
            f"ate_{slug}_30d", f"DRD370{letter}", "categorical",
            label, T_1_150, codes=YES_NO_ONLY, tables=("tot",),
        )
        if letter == "V":
            continue
        vars_map[f"times_{slug}_30d"] = _var(
            f"times_{slug}_30d", f"DRD370{letter}Q", "continuous",
            f"Number of times {slug.replace('_', ' ')} eaten in past 30 days.",
            T_1_150,
            sas_by_cycle={"99-00": f"DRQ370{letter}Q", "01-02": f"DRQ370{letter}Q"},
            tables=("tot",),
        )


_add_nutrient_vars(DIET_VARS)
_add_fatty_acid_vars(DIET_VARS)
_add_seafood_vars(DIET_VARS)

# Day-2 / early-cycle SAS names that are not the current day_pair default.
# describe() and decode() look these up through SAS_TO_SHORT_DIET.
DIET_VARS["main_respondent"]["aliases"] = ["DR2MNRSP"]
DIET_VARS["helper"]["aliases"] = ["DR2HELPD"]
DIET_VARS["water_plain_g"]["aliases"] = ["DR2_320"]
DIET_VARS["water_tap_g"]["aliases"] = ["DR2_330"]
DIET_VARS["water_bottled_g"]["aliases"] = ["DR2BWATR"]
DIET_VARS["tap_water_source"]["aliases"] = ["DR2TWS"]
DIET_VARS["mod_code"]["aliases"] = ["DRXMC"]


# ---------------------------------------------------------------------------
# Dietary supplements, FFQ, and Dietary Screener
# Parsed from the diet_combined codebook PDFs so every public SAS column
# on those files can be described and aligned across cycles.
# ---------------------------------------------------------------------------

SUPP_MATCH = {
    1: "Exact or near exact match",
    2: "Probable match",
    3: "Generic match",
    4: "Reasonable match",
    5: "Default match",
    6: "No match",
    7: "Refused",
    9: "Don't know",
}

SUPP_LOC = {
    1: "Household interview",
    2: "MEC interview",
    3: "Phone interview",
}

SUPP_ANTA = {
    0: "Non-antacid supplement",
    1: "Antacid containing calcium and/or magnesium",
    2: "Antacid reported with antacids",
}

FREQ_UNIT = {
    1: "Day",
    2: "Week",
    3: "Month",
    7: "Refused",
    9: "Don't know",
}

DOSAGE_FORM = {
    1: "Tablets / capsules / pills / caplets / softgels / gelcaps",
    2: "Droppers",
    3: "Drops",
    4: "Chewable / gummies",
    5: "Lozenges / cough drops",
    6: "Liquid",
    7: "Milliliters",
    8: "Packets / packets powder",
    9: "Wafers",
    10: "Powder / granules",
    11: "Tablespoons",
    12: "Teaspoons",
    13: "Wafers",
    14: "Capsules",
    15: "Cans",
    16: "Grams",
    17: "Dots",
    18: "Cups",
    19: "Spray / squirt",
    20: "Scoops",
    21: "Capfuls",
    22: "IUs",
    23: "Milligrams",
    24: "Ounces",
    25: "Packages",
    26: "Bottles",
    91: "Other",
    77: "Refused",
    99: "Don't know",
}

SUPP_REASON_SOURCE = {
    1: "Decided to take it for reasons of my own",
    2: "A doctor or other health provider told me to",
    7: "Refused",
    9: "Don't know",
}

ANTACID_OR_CALCIUM = {
    1: "Antacid",
    2: "Calcium supplement",
    3: "Both",
    4: "Neither",
    7: "Refused",
    9: "Don't know",
}

FFQ_FREQ10 = {
    1: "Never",
    2: "1 time per month or less",
    3: "2-3 times per month",
    4: "1-2 times per week",
    5: "3-4 times per week",
    6: "5-6 times per week",
    7: "1 time per day",
    8: "2-3 times per day",
    9: "4-5 times per day",
    10: "6 or more times per day",
    88: "Blank",
    99: "Error",
}

FFQ_PROP5 = {
    1: "Almost never or never",
    2: "About 1/4 of the time",
    3: "About 1/2 of the time",
    4: "About 3/4 of the time",
    5: "Almost always or always",
    88: "Blank",
    99: "Error",
}

FFQ_YESNO = {
    1: "Yes",
    2: "No",
    88: "Blank",
    99: "Error",
}

DS_NUTRIENT_STEMS = {
    "KCAL": ("energy_kcal", "Energy (kcal)"),
    "PROT": ("protein", "Protein (gm)"),
    "CARB": ("carbohydrate", "Carbohydrate (gm)"),
    "SUGR": ("sugars", "Total sugars (gm)"),
    "FIBE": ("fiber", "Dietary fiber (gm)"),
    "TFAT": ("fat_total", "Total fat (gm)"),
    "SFAT": ("fat_sat", "Total saturated fatty acids (gm)"),
    "MFAT": ("fat_mono", "Total monounsaturated fatty acids (gm)"),
    "PFAT": ("fat_poly", "Total polyunsaturated fatty acids (gm)"),
    "CHOL": ("cholesterol", "Cholesterol (mg)"),
    "LYCO": ("lycopene", "Lycopene (mcg)"),
    "LZ":   ("lutein_zeaxanthin", "Lutein + zeaxanthin (mcg)"),
    "VB1":  ("thiamin", "Thiamin (Vitamin B1) (mg)"),
    "VB2":  ("riboflavin", "Riboflavin (Vitamin B2) (mg)"),
    "NIAC": ("niacin", "Niacin (mg)"),
    "VB6":  ("vit_b6", "Vitamin B6 (mg)"),
    "FA":   ("folic_acid", "Folic acid (mcg)"),
    "FDFE": ("folate_dfe", "Folate, DFE (mcg)"),
    "CHL":  ("choline", "Total choline (mg)"),
    "VB12": ("vit_b12", "Vitamin B12 (mcg)"),
    "VC":   ("vit_c", "Vitamin C (mg)"),
    "VK":   ("vit_k", "Vitamin K (mcg)"),
    "VD":   ("vit_d", "Vitamin D (D2 + D3) (mcg)"),
    "CALC": ("calcium", "Calcium (mg)"),
    "PHOS": ("phosphorus", "Phosphorus (mg)"),
    "MAGN": ("magnesium", "Magnesium (mg)"),
    "IRON": ("iron", "Iron (mg)"),
    "ZINC": ("zinc", "Zinc (mg)"),
    "COPP": ("copper", "Copper (mg)"),
    "SODI": ("sodium", "Sodium (mg)"),
    "POTA": ("potassium", "Potassium (mg)"),
    "SELE": ("selenium", "Selenium (mcg)"),
    "CAFF": ("caffeine", "Caffeine (mg)"),
    "IODI": ("iodine", "Iodine (mcg)"),
}

# Reason-for-use checkboxes on the 30-day individual supplement file.
# Names flip between DSQ128* and DSD128* across cycles; aliases keep them aligned.
SUPP_REASON_FLAGS = [
    ("ds_reason_bowel", "DSQ128A", "For good bowel/colon health"),
    ("ds_reason_prostate", "DSQ128B", "For prostate health"),
    ("ds_reason_mental", "DSQ128C", "For mental health"),
    ("ds_reason_prevent", "DSQ128D", "To prevent health problems"),
    ("ds_reason_overall", "DSQ128E", "To improve my overall health"),
    ("ds_reason_teeth", "DSQ128F", "For teeth, prevent cavities"),
    ("ds_reason_supplement_diet", "DSQ128G", "To supplement my diet, food not enough"),
    ("ds_reason_maintain", "DSQ128H", "To maintain health (to stay healthy)"),
    ("ds_reason_immune", "DSQ128I", "To prevent colds, boost immune system"),
    ("ds_reason_heart", "DSQ128J", "For heart health, cholesterol"),
    ("ds_reason_eye", "DSQ128K", "For eye health"),
    ("ds_reason_joints", "DSQ128L", "For healthy joints, arthritis"),
    ("ds_reason_skin_hair", "DSQ128M", "For healthy skin, hair and nails"),
    ("ds_reason_weight_loss", "DSQ128N", "For weight loss"),
    ("ds_reason_bone", "DSQ128O", "For bone health"),
    ("ds_reason_energy", "DSQ128P", "To get more energy"),
    ("ds_reason_pregnancy", "DSQ128Q", "For pregnancy/breastfeeding"),
    ("ds_reason_anemia", "DSQ128R", "For anemia, such as low iron"),
    ("ds_reason_other", "DSQ128S", "Other specify"),
    ("ds_reason_blood_sugar", "DSD128T", "To maintain blood sugar, diabetes"),
    ("ds_reason_hair_nails", "DSD128U", "For healthy hair and nails"),
    ("ds_reason_kidney", "DSD128V", "For kidney and bladder health"),
    ("ds_reason_respiratory", "DSD128W", "For respiratory health, asthma"),
    ("ds_reason_allergies", "DSD128X", "For allergies"),
    ("ds_reason_breastfeeding", "DSD128Y", "Currently breastfeeding"),
    ("ds_reason_digestion", "DSD128Z", "To improve digestion"),
    ("ds_reason_menopause", "DSD128AA", "For menopause, hot flashes"),
    ("ds_reason_muscle_cramps", "DSD128BB", "For muscle related issues, muscle cramps"),
    ("ds_reason_sleep", "DSD128CC", "To improve sleep"),
    ("ds_reason_stress", "DSD128DD", "For relaxation, decrease stress"),
    ("ds_reason_nervous", "DSD128EE", "For nervous system health"),
    ("ds_reason_liver", "DSD128FF", "For liver health, detoxification"),
    ("ds_reason_antioxidants", "DSD128GG", "For antioxidants"),
    ("ds_reason_word_of_mouth", "DSD128HH", "Word of mouth, advertisement"),
    ("ds_reason_thyroid", "DSD128II", "For thyroid health, gout"),
    ("ds_reason_build_muscle", "DSD128JJ", "To build muscle/weight gain", ("DSQ128NN",)),
    ("ds_reason_low_blood", "DSD128KK", "Low levels in blood"),
    ("ds_reason_after_surgery", "DSD128LL", "For support after surgery"),
    ("ds_reason_headache", "DSD128MM", "Headaches and dizziness"),
    ("ds_reason_inflammation", "DSD128OO", "For inflammation"),
    ("ds_reason_fluid", "DSD128PP", "For fluid/water balance"),
]

SCREENER_FREQ = [
    ("010", "cereal", "How often eat cold or hot cereal?"),
    ("030", "milk", "How often drink milk or on cereal?"),
    ("040", "soda", "How often drink regular soft drinks?"),
    ("050", "juice", "How often drink 100% fruit juice?"),
    ("060", "sweet_coffee_tea", "How often drink sweetened coffee/tea?"),
    ("070", "fruit_sports_drink", "How often drink fruit/sports/energy?"),
    ("080", "fruit", "How often eat fruit?"),
    ("090", "leafy_salad", "How often eat leafy/lettuce salad?"),
    ("100", "fried_potatoes", "How often eat fried potatoes?"),
    ("110", "other_potatoes", "How often eat non-fried potatoes?"),
    ("120", "beans", "How often eat beans?"),
    ("130", "other_vegetables", "How often eat other vegetables?"),
    ("140", "pizza", "How often eat pizza?"),
    ("150", "salsa", "How often eat tomato-based salsa?"),
    ("160", "tomato_sauce", "How often eat tomato sauce?"),
    ("170", "red_meat", "How often eat red meat?"),
    ("180", "processed_meat", "How often eat processed meat?"),
    ("190", "cheese", "How often eat cheese?"),
    ("200", "wg_bread", "How often eat whole grain bread?"),
    ("210", "cooked_wg", "How often eat cooked whole grains?"),
    ("220", "candy", "How often eat chocolate or candy?"),
    ("230", "pastries", "How often eat pastries?"),
    ("240", "cookies_cake", "How often eat cookies/cake?"),
    ("250", "ice_cream", "How often eat ice cream?"),
    ("260", "popcorn", "How often eat popcorn?"),
]

# (sas, label, code_set) for FFQRAW items. code_set in {freq10, prop5, yesno}.
FFQ_ITEMS = [
    ('FFQ0001', 'Q.1 How often drink tomato juice?', 'freq10'),
    ('FFQ0002', 'Q.2 How often drink orange juice?', 'freq10'),
    ('FFQ0003', 'Q.3 How often drink apple juice?', 'freq10'),
    ('FFQ0004', 'Q.4 How often drink grape juice?', 'freq10'),
    ('FFQ0005', 'Q.5 How often drink 100% fruit juice?', 'freq10'),
    ('FFQ0006', 'Q.6 How often drink other fruit drinks?', 'freq10'),
    ('FFQ0006A', 'Q.6A How often drink diet or sugar-free', 'prop5'),
    ('FFQ0007', 'Q.7 How often drink milk as a beverage?', 'freq10'),
    ('FFQ0007A', 'Q.7A What kind of milk did you drink?', 'categorical'),
    ('FFQ0008', 'Q.8 How often drink meal replacement?', 'freq10'),
    ('FFQ0009', 'Q.9 Did you drink soft drinks?', 'yesno'),
    ('FFQ0009A', 'Q.9A How often did you drink in summer?', 'freq10'),
    ('FFQ0009B', 'Q.9B How often drink rest of year?', 'freq10'),
    ('FFQ0009C', 'Q.9C How often drink diet soft drinks?', 'prop5'),
    ('FFQ0009D', 'Q.9D How often drink caffeine-free?', 'prop5'),
    ('FFQ0010', 'Q.10 Did you drink beer?', 'yesno'),
    ('FFQ0010A', 'Q.10A Did you drink beer in summer?', 'freq10'),
    ('FFQ0010B', 'Q.10B Did you drink beer rest of year?', 'freq10'),
    ('FFQ0011', 'Q.11 Did you drink wine?', 'freq10'),
    ('FFQ0012', 'Q.12 Did you drink liquor?', 'freq10'),
    ('FFQ0013', 'Q.13 Did you eat cooked cereal?', 'yesno'),
    ('FFQ0013A', 'Q.13A Did you eat oatmeal in winter?', 'freq10'),
    ('FFQ0013B', 'Q.13B How often eat oatmeal rest of yr?', 'freq10'),
    ('FFQ0013C', 'Q.13C How often was it oatmeal?', 'prop5'),
    ('FFQ0014', 'Q.14 How often eat cold cereal?', 'freq10'),
    ('FFQ0014A', 'Q.14A How often eat whole grain cereal?', 'prop5'),
    ('FFQ0014B', 'Q.14B Was milk added?', 'yesno'),
    ('FFQ0014C', 'Q.14C What kind of milk was added?', 'categorical'),
    ('FFQ0015', 'Q.15 Did you eat applesauce?', 'freq10'),
    ('FFQ0016', 'Q.16 Did you eat apples?', 'freq10'),
    ('FFQ0017', 'Q.17 Did you eat pears?', 'freq10'),
    ('FFQ0018', 'Q.18 Did you eat bananas?', 'freq10'),
    ('FFQ0019', 'Q.19 Did you eat pineapple?', 'freq10'),
    ('FFQ0020', 'Q.20 Did you eat dried fruit?', 'freq10'),
    ('FFQ0021', 'Q.21 Did you eat peaches?', 'yesno'),
    ('FFQ0021A', 'Q.21A Did you eat fresh peaches?', 'freq10'),
    ('FFQ0021B', 'Q.21B Fresh peaches rest of year?', 'freq10'),
    ('FFQ0022', 'Q.22 Did you eat grapes?', 'freq10'),
    ('FFQ0023', 'Q.23 Did you eat melons?', 'yesno'),
    ('FFQ0023A', 'Q.23A Did you eat melons in season?', 'freq10'),
    ('FFQ0023B', 'Q.23B Did you eat melons rest of year?', 'freq10'),
    ('FFQ0024', 'Q.24 Fresh strawberries eaten?', 'yesno'),
    ('FFQ0024A', 'Q.24A Fresh strawberries eaten in season', 'freq10'),
    ('FFQ0024B', 'Q.24B Strawberries eaten other times', 'freq10'),
    ('FFQ0025', 'Q.25 Did you eat oranges?', 'yesno'),
    ('FFQ0025A', 'Q.25A Did you eat fresh oranges?', 'freq10'),
    ('FFQ0025B', 'Q.25B Did you eat oranges rest of year?', 'freq10'),
    ('FFQ0026', 'Q.26 Did you eat grapefruit?', 'yesno'),
    ('FFQ0026A', 'Q.26A Did you eat fresh grapefruit?', 'freq10'),
    ('FFQ0026B', 'Q.26B Did you eat grapefruit rest of yr?', 'freq10'),
    ('FFQ0027', 'Q.27 Did you eat other kinds of fruit?', 'freq10'),
    ('FFQ0028', 'Q.28 Did you eat cooked greens?', 'freq10'),
    ('FFQ0029', 'Q.29 Did you eat raw greens?', 'freq10'),
    ('FFQ0030', 'Q.30 Did you eat coleslaw?', 'freq10'),
    ('FFQ0031', 'Q.31 Did you eat sauerkraut?', 'freq10'),
    ('FFQ0032', 'Q.32 Did you eat carrots?', 'freq10'),
    ('FFQ0033', 'Q.33 Did you eat string beans?', 'freq10'),
    ('FFQ0034', 'Q.34 Did you eat peas?', 'freq10'),
    ('FFQ0035', 'Q.35 Did you eat corn?', 'yesno'),
    ('FFQ0035A', 'Q.35A Did you eat corn in season?', 'freq10'),
    ('FFQ0035B', 'Q.35B Did you eat corn rest of year?', 'freq10'),
    ('FFQ0036', 'Q.36 Did you eat broccoli?', 'freq10'),
    ('FFQ0037', 'Q.37 Did you eat cauliflower?', 'freq10'),
    ('FFQ0038', 'Q.38 Did you eat mixed veggies?', 'freq10'),
    ('FFQ0039', 'Q.39 Did you eat onions?', 'freq10'),
    ('FFQ0040', 'Q.40 Did you eat peppers?', 'freq10'),
    ('FFQ0041', 'Q.41 Did you eat cucumbers?', 'freq10'),
    ('FFQ0042', 'Q.42 Fresh tomatoes eaten?', 'yesno'),
    ('FFQ0042A', 'Q.42A Fresh tomatoes eaten in season?', 'freq10'),
    ('FFQ0042B', 'Q.42B Fresh tomatoes eaten other times?', 'freq10'),
    ('FFQ0043', 'Q.43 Did you eat summer squash?', 'yesno'),
    ('FFQ0043A', 'Q.43A How often eat squash in season?', 'freq10'),
    ('FFQ0043B', 'Q.43B Did you squash rest of year?', 'freq10'),
    ('FFQ0044', 'Q.44 Did you eat lettuce salads?', 'freq10'),
    ('FFQ0044A', 'Q.44A How often eat dark green leaves?', 'prop5'),
    ('FFQ0045', 'Q.45 Did you eat salad dressing?', 'freq10'),
    ('FFQ0046', 'Q.46 Did you eat sweet potatoes?', 'freq10'),
    ('FFQ0047', 'Q.47 Did you eat french fries?', 'freq10'),
    ('FFQ0048', 'Q.48 Did you eat potato salad?', 'freq10'),
    ('FFQ0049', 'Q.49 Did you eat baked potatoes?', 'freq10'),
    ('FFQ0050', 'Q.50 Did you eat salsa?', 'freq10'),
    ('FFQ0051', 'Q.51 Did you eat catsup?', 'freq10'),
    ('FFQ0052', 'Q.52 Did you eat pickles?', 'freq10'),
    ('FFQ0053', 'Q.53 Did you eat stuffing?', 'freq10'),
    ('FFQ0054', 'Q.54 Do you eat chili?', 'freq10'),
    ('FFQ0055', 'Q.55 Do you eat tortillas?', 'freq10'),
    ('FFQ0055A', 'Q.55A How often corn tortillas?', 'prop5'),
    ('FFQ0056', 'Q.56 Did you eat cooked dried beans?', 'freq10'),
    ('FFQ0057', 'Q.57 Did you eat other vegetables?', 'freq10'),
    ('FFQ0058', 'Q.58 Did you eat rice?', 'freq10'),
    ('FFQ0058A', 'Q.58A How often was grain rice?', 'prop5'),
    ('FFQ0059', 'Q.59 Did you eat pancakes?', 'freq10'),
    ('FFQ0059A', 'Q.59A How often syrup added?', 'prop5'),
    ('FFQ0060', 'Q.60 Did you eat lasagna?', 'freq10'),
    ('FFQ0061', 'Q.61 Did you eat macaroni and cheese?', 'freq10'),
    ('FFQ0062', 'Q.62 Did you eat pasta salad?', 'freq10'),
    ('FFQ0063', 'Q.63 Did you eat other pasta?', 'freq10'),
    ('FFQ0063A', 'Q.63A Did you eat spaghetti sauce?', 'prop5'),
    ('FFQ0063B', 'Q.63B Did you eat meatless sauce?', 'prop5'),
    ('FFQ0063C', 'Q.63C Did you eat pasta with margarine?', 'prop5'),
    ('FFQ0064', 'Q.64 Did you eat bagels?', 'freq10'),
    ('FFQ0065', 'Q.65 Did you eat breads as sandwiches?', 'freq10'),
    ('FFQ0065A', 'Q.65A White bread eaten in sandwiches?', 'prop5'),
    ('FFQ0066', 'Q.66 Did you eat bread not sandwiches?', 'freq10'),
    ('FFQ0066A', 'Q.66A Ate other white breads or rolls?', 'prop5'),
    ('FFQ0067', 'Q.67 Did you eat jam?', 'freq10'),
    ('FFQ0068', 'Q.68 Did you eat peanut butter?', 'freq10'),
    ('FFQ0069', 'Q.69 Roast beef sandwiches eaten?', 'freq10'),
    ('FFQ0070', 'Q.70 Did you eat cold cuts?', 'freq10'),
    ('FFQ0071', 'Q.71 Did you eat luncheon ham?', 'freq10'),
    ('FFQ0071A', 'Q.71A Did you eat light ham?', 'prop5'),
    ('FFQ0072', 'Q.72 Did you eat other cold cuts?', 'freq10'),
    ('FFQ0072A', 'Q.72A Did you eat light meats?', 'prop5'),
    ('FFQ0073', 'Q.73 Did you eat canned tuna?', 'freq10'),
    ('FFQ0074', 'Q.74 Did you eat GROUND chicken?', 'freq10'),
    ('FFQ0075', 'Q.75 Did you eat beef hamburgers?', 'freq10'),
    ('FFQ0075A', 'Q.75A Did you eat lean ground beef?', 'prop5'),
    ('FFQ0076', 'Q.76 Ground beef mixtures eaten?', 'freq10'),
    ('FFQ0077', 'Q.77 Did you eat hot dogs?', 'freq10'),
    ('FFQ0077A', 'Q.77A Did you eat light hot dogs?', 'prop5'),
    ('FFQ0078', 'Q.78 Other beef mixtures eaten?', 'freq10'),
    ('FFQ0079', 'Q.79 Roast beef eaten at other times?', 'freq10'),
    ('FFQ0080', 'Q.80 Did you eat steak?', 'freq10'),
    ('FFQ0080A', 'Q.80A Did you eat lean steak?', 'prop5'),
    ('FFQ0081', 'Q.81 Did you eat spareribs?', 'freq10'),
    ('FFQ0082', 'Q.82 Did you eat roast turkey?', 'freq10'),
    ('FFQ0083', 'Q.83 Did you eat chicken in mixtures?', 'freq10'),
    ('FFQ0084', 'Q.84 Did you eat baked chicken?', 'freq10'),
    ('FFQ0084A', 'Q.84A Did you eat fried chicken?', 'prop5'),
    ('FFQ0084B', 'Q.84B Did you eat white meat?', 'prop5'),
    ('FFQ0084C', 'Q.84C Did you eat chicken skin?', 'prop5'),
    ('FFQ0085', 'Q.85 Did you eat baked ham?', 'freq10'),
    ('FFQ0086', 'Q.86 Did you eat pork?', 'freq10'),
    ('FFQ0087', 'Q.87 Did you eat gravy?', 'freq10'),
    ('FFQ0088', 'Q.88 Did you eat liver?', 'freq10'),
    ('FFQ0089', 'Q.89 Did you eat bacon?', 'freq10'),
    ('FFQ0089A', 'Q.89A Did you eat lean bacon?', 'prop5'),
    ('FFQ0090', 'Q.90 Did you eat sausage?', 'freq10'),
    ('FFQ0090A', 'Q.90A Did you eat lean sausage?', 'prop5'),
    ('FFQ0091', 'Q.91 Did you eat smoked fish', 'freq10'),
    ('FFQ0092', 'Q.92 Did you eat sushi', 'freq10'),
    ('FFQ0092A', 'Q.92A Did sushi contain raw fish?', 'prop5'),
    ('FFQ0093', 'Q.93 Did you eat raw oysters?', 'freq10'),
    ('FFQ0094', 'Q.94 Did you eat fried fish?', 'freq10'),
    ('FFQ0095', 'Q.95 Did you eat all other fish?', 'freq10'),
    ('FFQ0096', 'Q.96 Did you eat tofu?', 'freq10'),
    ('FFQ0097', 'Q.97 Did you eat soups?', 'yesno'),
    ('FFQ0097A', 'Q.97A Did you eat soup winter?', 'freq10'),
    ('FFQ0097B', 'Q.97B Did you eat soup rest of year?', 'freq10'),
    ('FFQ0097C', 'Q.99C Did you eat bean soups?', 'prop5'),
    ('FFQ0097D', 'Q.97D Did you eat cream soups?', 'prop5'),
    ('FFQ0097E', 'Q.97E Did you eat tomato soups?', 'prop5'),
    ('FFQ0097F', 'Q.97F Did you eat broth soups?', 'prop5'),
    ('FFQ0098', 'Q.98 Did you eat pizza?', 'freq10'),
    ('FFQ0098A', 'Q.98A Did you eat pizza with meat?', 'prop5'),
    ('FFQ0099', 'Q.99 Did you eat crackers?', 'freq10'),
    ('FFQ0100', 'Q.100 Did you eat corn bread?', 'freq10'),
    ('FFQ0101', 'Q.101 Did you eat biscuits?', 'freq10'),
    ('FFQ0102', 'Q.102 Did you eat potato chips?', 'freq10'),
    ('FFQ0102A', 'Q.102A How often low-fat potato chips?', 'prop5'),
    ('FFQ0103', 'Q.103 Did you eat tortilla chips?', 'freq10'),
    ('FFQ0103A', 'Q.103A How often low-fat tortilla chips?', 'prop5'),
    ('FFQ0104', 'Q.104 Did you eat popcorn?', 'freq10'),
    ('FFQ0105', 'Q.105 Did you eat pretzels?', 'freq10'),
    ('FFQ0106', 'Q.106 Did you eat peanuts?', 'freq10'),
    ('FFQ0107', 'Q.107 Did you eat granola bars?', 'freq10'),
    ('FFQ0108', 'Q.108 Did you eat yogurt?', 'freq10'),
    ('FFQ0109', 'Q.109 Did you eat cottage cheese?', 'freq10'),
    ('FFQ0110', 'Q.110 Did you eat cheese?', 'freq10'),
    ('FFQ0110A', 'Q.110A Did you eat light cheese?', 'prop5'),
    ('FFQ0111', 'Q.111 Did you eat frozen yogurt?', 'freq10'),
    ('FFQ0112', 'Q.112 Did you eat ice cream?', 'freq10'),
    ('FFQ0112A', 'Q.112A Did you eat light ice cream?', 'prop5'),
    ('FFQ0113', 'Q.113 Did you eat pudding?', 'freq10'),
    ('FFQ0114', 'Q.114 Did you eat cake?', 'freq10'),
    ('FFQ0115', 'Q.115 Did you eat cookies?', 'freq10'),
    ('FFQ0116', 'Q.116 Did you eat doughnuts?', 'freq10'),
    ('FFQ0117', 'Q.117 Did you eat sweet muffins?', 'freq10'),
    ('FFQ0118', 'Q.118 Did you eat fruit crisp?', 'freq10'),
    ('FFQ0119', 'Q.119 Did you eat pie?', 'freq10'),
    ('FFQ0119A', 'Q.119A Did you eat fruit pie?', 'prop5'),
    ('FFQ0120', 'Q.120 Did you eat chocolate candy?', 'freq10'),
    ('FFQ0121', 'Q.121 Did you eat other candy?', 'freq10'),
    ('FFQ0122', 'Q.122 Did you eat eggs?', 'freq10'),
    ('FFQ0122A', 'Q.122A Did you eat egg substitutes?', 'prop5'),
    ('FFQ0122B', 'Q.122B Did you eat egg whites?', 'prop5'),
    ('FFQ0122C', 'Q.122C Did you eat whole eggs?', 'prop5'),
    ('FFQ0122D', 'Q.122D Did you eat egg salad?', 'prop5'),
    ('FFQ0123', 'Q.123 Did you drink coffee?', 'freq10'),
    ('FFQ0123A', 'Q.123A Did you drink decaffeinated?', 'prop5'),
    ('FFQ0124', 'Q.124 Did you drink ICED tea?', 'freq10'),
    ('FFQ0124A', 'Q.124A Did you drink iced herbal tea?', 'prop5'),
    ('FFQ0125', 'Q.125 Did you drink Hot tea?', 'freq10'),
    ('FFQ0125A', 'Q.125A Did you drink hot decaffeinated?', 'prop5'),
    ('FFQ0126', 'Q.126 Did you add sugar or honey?', 'freq10'),
    ('FFQ0127', 'Q.127 Did you add artificial sweetener?', 'freq10'),
    ('FFQ0128', 'Q.128 Was non-dairy creamer added?', 'freq10'),
    ('FFQ0128A', 'Q.128A What kind of creamer?', 'categorical'),
    ('FFQ0129', 'Q.129 Was cream or half and half added?', 'freq10'),
    ('FFQ0130', 'Q.130 Was milk added to your coffee?', 'freq10'),
    ('FFQ0130A', 'Q.130A What kind of milk added?', 'categorical'),
    ('FFQ0131', 'Q.131 Was sugar or honey added?', 'freq10'),
    ('FFQ0132', 'Q.132 Did you eat margarine?', 'freq10'),
    ('FFQ0132A', 'Q.132A Was margarine low-fat?', 'prop5'),
    ('FFQ0133', 'Q.133 Did you eat butter on breads?', 'freq10'),
    ('FFQ0133A', 'Q.133A Was butter low-fat?', 'prop5'),
    ('FFQ0134', 'Q.134 Did you eat margarine on potatoes?', 'freq10'),
    ('FFQ0134A', 'Q.134A Was margarine you ate low-fat?', 'prop5'),
    ('FFQ0135', 'Q.135 Did you eat butter on potatoes?', 'freq10'),
    ('FFQ0135A', 'Q.135A Was butter you ate low-fat?', 'prop5'),
    ('FFQ0136', 'Q.136 Did you eat mayonnaise?', 'freq10'),
    ('FFQ0136A', 'Q.136A Was mayonnaise you ate low-fat?', 'prop5'),
    ('FFQ0137', 'Q.137 Did you eat cream cheese?', 'freq10'),
    ('FFQ0137A', 'Q.137A Was cream cheese low-fat?', 'prop5'),
    ('FFQ0138', 'Q.138 Did you eat sour cream?', 'freq10'),
    ('FFQ0138A', 'Q.138A Was sour cream you ate low-fat?', 'prop5'),
    ('FFQ0139', 'Q.139 Did you eat foods with oils?', 'freq10'),
    ('FFQ0139A', 'Q.139A Olive oil eaten?', 'categorical'),
    ('FFQ0139B', 'Q.139B Corn oil eaten?', 'categorical'),
    ('FFQ0139C', 'Q.139C Canola/rapeseed eaten?', 'categorical'),
    ('FFQ0139D', 'Q.139D Other type of oils eaten?', 'categorical'),
]


def _add_supplement_vars(vars_map: dict) -> None:
    t_all = T_ALL
    yes = YES_NO

    def add(short, sas, kind, label, codes=None, day_pair=None, aliases=None, notes="", tables=("dsq",), definition=""):
        vars_map[short] = _var(
            short, sas, kind, label, t_all,
            codes=codes, day_pair=day_pair, aliases=aliases,
            notes=notes, tables=tables,
            definition=definition or label,
        )

    add("ds30_any", "DSD010", "categorical",
        "Any dietary supplements taken (past 30 days)?",
        codes=yes, tables=("dsq", "dsqtot"),
        definition="Whether the SP took any dietary supplement in the past 30 days.")
    add("ds30_count", "DSDCOUNT", "continuous",
        "Total number of dietary supplements taken (past 30 days).",
        tables=("dsq", "dsqtot"))
    add("ds30_any_antacid", "DSD010AN", "categorical",
        "Any antacids taken (past 30 days)?",
        codes=yes, tables=("dsq", "dsqtot"))
    add("ds30_antacid_count", "DSDANCNT", "continuous",
        "Total number of antacids taken (past 30 days).",
        tables=("dsq", "dsqtot"))

    add("ds24_any", "DS1DS", "categorical",
        "Any dietary supplements taken (24-hour recall day)?",
        codes=yes, day_pair="DS2DS", tables=("ds24tot",),
        notes="Person-level 24-hour supplement total files (DS1TOT / DS2TOT).")
    add("ds24_count", "DS1DSCNT", "continuous",
        "Number of dietary supplements reported (24-hour recall day).",
        day_pair="DS2DSCNT", tables=("ds24tot",))
    add("ds24_any_antacid", "DS1AN", "categorical",
        "Any antacids taken (24-hour recall day)?",
        codes=yes, day_pair="DS2AN", tables=("ds24tot",))
    add("ds24_antacid_count", "DS1ANCNT", "continuous",
        "Number of antacids reported (24-hour recall day).",
        day_pair="DS2ANCNT", tables=("ds24tot",))

    add("supp_id", "DSDSUPID", "id",
        "Supplement ID number.",
        aliases=["DSDPID"], tables=("dsqids", "ds24ids"),
        notes=(
            "DSDSUPID on 99-16 files; DSDPID starting 17-18. "
            "decode_rows=True replaces the id with the product name and adds "
            "supp_ingredients from the 1999-2023 supplement database."
        ),
        definition="NCHS dietary supplement product identifier.")
    add("supp_name", "DSDSUPP", "text",
        "Supplement name.",
        tables=("dsqids", "ds24ids"))
    add("supp_container_seen", "DSD070", "categorical",
        "Was container seen?",
        codes=yes, tables=("dsqids",))
    add("supp_match", "DSDMTCH", "categorical",
        "Matching code (reported product vs. database).",
        codes=SUPP_MATCH, tables=("dsqids", "ds24ids"),
        aliases=["DS1MTCH", "DS2MTCH"],
        notes="DS1MTCH / DS2MTCH on 24-hour individual files; DSDMTCH on 30-day files.")

    add("supp_days_taken", "DSD090", "continuous",
        "How long supplement taken (days)?",
        tables=("dsqids",),
        notes="Early (99-00) duration in days. Later cycles use DSD103 = days taken in the past 30 days.")
    add("supp_days_30d", "DSD103", "continuous",
        "Days supplement taken, past 30 days.",
        tables=("dsqids",))
    add("supp_freq_q", "DSD100Q", "continuous",
        "How often taken last month (quantity).",
        tables=("dsqids",),
        notes="99-00/01-02. Later cycles dropped DSD100Q/U in favor of DSD103 + DSD122*.")
    add("supp_freq_u", "DSD100U", "categorical",
        "How often taken last month (unit).",
        codes=FREQ_UNIT, tables=("dsqids",))
    add("supp_amount_q", "DSD120Q", "continuous",
        "Quantity of supplement taken.",
        tables=("dsqids",),
        notes="99-00 amount each time. Later files use DSD122Q (quantity taken daily).")
    add("supp_amount_u", "DSD120U", "categorical",
        "Dosage form / amount unit.",
        codes=DOSAGE_FORM, tables=("dsqids",))
    add("supp_daily_q", "DSD122Q", "continuous",
        "Quantity of supplement taken daily.",
        tables=("dsqids",))
    add("supp_daily_u", "DSD122U", "categorical",
        "Dosage form (daily amount unit).",
        codes=DOSAGE_FORM, tables=("dsqids",))
    add("supp_antacid_flag", "DSDANTA", "categorical",
        "Antacid reported as dietary supplement.",
        codes=SUPP_ANTA, tables=("dsqids", "ds24ids"),
        aliases=["DS1ANTA", "DS2ANTA"])
    add("supp_serving_ratio", "DSDACTSS", "continuous",
        "Reported serving size / label serving size.",
        tables=("dsqids", "ds24ids"),
        aliases=["DS1ACTSS", "DS2ACTSS"])
    add("supp_taken_day1", "DSDDAY1", "categorical",
        "Reported product during Day 1 24-hour recall.",
        codes=yes, tables=("dsqids",))
    add("supp_taken_day2", "DSDDAY2", "categorical",
        "Reported product during Day 2 24-hour recall.",
        codes=yes, tables=("dsqids",))
    add("supp_reason_source", "DSQ124", "categorical",
        "Took product on own or doctor advised.",
        codes=SUPP_REASON_SOURCE, tables=("dsqids",))
    add("supp_antacid_or_calcium", "RXQ215A", "categorical",
        "Antacid, calcium supplement, or both?",
        codes=ANTACID_OR_CALCIUM, tables=("dsqids",))
    add("ds24_location", "DS1LOC", "categorical",
        "Location supplement originally recorded.",
        codes=SUPP_LOC, day_pair="DS2LOC", tables=("ds24ids",))

    for row in SUPP_REASON_FLAGS:
        short, sas, label = row[0], row[1], row[2]
        extra = list(row[3]) if len(row) > 3 else []
        add(short, sas, "categorical", label, codes=YES_NO_ONLY,
            aliases=extra, tables=("dsqids",),
            definition=f"Reason for taking the reported supplement: {label.lower()}.")

    for stem, (slug, label) in DS_NUTRIENT_STEMS.items():
        add(
            f"ds30_item_{slug}", f"DSQI{stem}", "continuous",
            f"{label} from this 30-day supplement.",
            tables=("dsqids",),
            definition=f"{label} contributed by the reported 30-day supplement (serving-adjusted).",
        )
        add(
            f"ds30_tot_{slug}", f"DSQT{stem}", "continuous",
            f"{label} from all 30-day supplements.",
            tables=("dsqtot",),
            definition=f"{label} summed across 30-day supplements for the participant.",
        )
        add(
            f"ds24_item_{slug}", f"DS1I{stem}", "continuous",
            f"{label} from this 24-hour supplement.",
            day_pair=f"DS2I{stem}", tables=("ds24ids",),
            definition=f"{label} contributed by the reported 24-hour supplement.",
        )
        add(
            f"ds24_tot_{slug}", f"DS1T{stem}", "continuous",
            f"{label} from all 24-hour supplements.",
            day_pair=f"DS2T{stem}", tables=("ds24tot",),
            definition=f"{label} summed across 24-hour supplements for the recall day.",
        )


def _add_ffq_vars(vars_map: dict) -> None:
    vars_map["wt_ffq"] = _var(
        "wt_ffq", "WTS_FFQ", "weight",
        "FFQ sample weight.",
        T_ALL, tables=("ffq",),
        definition="Interview weight for the 2003-2006 Food Frequency Questionnaire.",
    )
    vars_map["ffq_n_missing"] = _var(
        "ffq_n_missing", "FFQ_MISS", "continuous",
        "Number of missing raw frequency responses.",
        T_ALL, tables=("ffq",),
    )
    vars_map["ffq_var_id"] = _var(
        "ffq_var_id", "FFQ_VAR", "id",
        "The Variable ID from DietCalc.",
        T_ALL, tables=("ffqdc",),
        notes="Join to VARLOOK (VARLK) for the DietCalc variable label.",
    )
    vars_map["ffq_food_id"] = _var(
        "ffq_food_id", "FFQ_FOOD", "id",
        "The Food ID from DietCalc.",
        T_ALL, tables=("ffqdc",),
        notes="Join to FOODLOOK (FOODLK) for the DietCalc food label.",
    )
    vars_map["ffq_daily_freq"] = _var(
        "ffq_daily_freq", "FFQ_FREQ", "continuous",
        "Daily intake frequency for this food.",
        T_ALL, tables=("ffqdc",),
    )
    vars_map["ffq_impute_code"] = _var(
        "ffq_impute_code", "FFQ_CODE", "id",
        "Daily intake frequency imputation code.",
        T_ALL, tables=("ffqdc",),
        notes="0 = reported; other codes flag DietCalc imputations.",
    )
    code_sets = {"freq10": FFQ_FREQ10, "prop5": FFQ_PROP5, "yesno": FFQ_YESNO}
    for sas, label, kind in FFQ_ITEMS:
        short = sas.lower()
        vars_map[short] = _var(
            short, sas, "categorical", label, T_ALL,
            codes=code_sets.get(kind),
            tables=("ffq",),
            definition=label,
            notes="NHANES 2003-2006 FFQRAW. Frequency is usual intake over the past 12 months.",
        )


def _add_screener_vars(vars_map: dict) -> None:
    vars_map["dsq_n_cereals"] = _var(
        "dsq_n_cereals", "DTDCER", "continuous",
        "Number of cereals reported in the past month.",
        T_ALL, tables=("dtq",),
    )
    vars_map["dsq_cereal_name"] = _var(
        "dsq_cereal_name", "DTQ020", "text",
        "Cereal most often eaten.",
        T_ALL, tables=("dtq",),
        aliases=["DTQ020A", "DTQ020a", "DTQ020B", "DTQ020b"],
        notes="Public files store cereal 1/2 as DTQ020A / DTQ020B (PDF codebook also prints DTQ020).",
    )
    vars_map["dsq_cereal_name_1"] = _var(
        "dsq_cereal_name_1", "DTQ020A", "text",
        "Cereal 1 most often eaten.",
        T_ALL, tables=("dtq",), aliases=["DTQ020a"],
    )
    vars_map["dsq_cereal_name_2"] = _var(
        "dsq_cereal_name_2", "DTQ020B", "text",
        "Cereal 2 most often eaten.",
        T_ALL, tables=("dtq",), aliases=["DTQ020b"],
    )
    vars_map["dsq_cereal_code"] = _var(
        "dsq_cereal_code", "DTD020", "id",
        "FNDDS food code for reported cereal.",
        T_ALL, tables=("dtq",),
        aliases=["DTD020AF", "DTD020BF"],
    )
    vars_map["dsq_cereal_code_1"] = _var(
        "dsq_cereal_code_1", "DTD020AF", "id",
        "FNDDS food code for cereal 1.",
        T_ALL, tables=("dtq",),
    )
    vars_map["dsq_cereal_code_2"] = _var(
        "dsq_cereal_code_2", "DTD020BF", "id",
        "FNDDS food code for cereal 2.",
        T_ALL, tables=("dtq",),
    )
    vars_map["dsq_check_age_skip"] = _var(
        "dsq_check_age_skip", "DTQ305", "id",
        "Screener check item (age 2-11 skip to DTD070Q).",
        T_ALL, tables=("dtq",),
        notes="Instrument routing check, not an analytic response.",
    )
    for num, slug, label in SCREENER_FREQ:
        vars_map[f"dsq_{slug}_q"] = _var(
            f"dsq_{slug}_q", f"DTD{num}Q", "continuous",
            label, T_ALL, tables=("dtq",),
            definition=f"{label} Quantity reported for the past month.",
        )
        vars_map[f"dsq_{slug}_u"] = _var(
            f"dsq_{slug}_u", f"DTQ{num}U", "categorical",
            f"{label} (unit)", T_ALL, codes=FREQ_UNIT, tables=("dtq",),
            definition="Unit for the paired DTD*Q frequency: day, week, or month.",
        )


_add_supplement_vars(DIET_VARS)
_add_ffq_vars(DIET_VARS)
_add_screener_vars(DIET_VARS)


# ---------------------------------------------------------------------------
# Lookups (same contract as the demo catalog)
# ---------------------------------------------------------------------------

def sas_name(spec: dict, cycle: str | None = None, day: int = 1) -> str:
    if cycle and cycle in spec["sas_by_cycle"]:
        name = spec["sas_by_cycle"][cycle]
    else:
        name = spec["sas"]
    if day == 2:
        pair = spec.get("day_pair")
        if pair:
            return pair
    return name


def day_sas_name(spec: dict, day: int = 1, cycle: str | None = None) -> str:
    return sas_name(spec, cycle=cycle, day=day)


def iff_nutrient_sas(stem: str, day: int = 1, cycle: str | None = None) -> str:
    if cycle in {"99-00", "01-02"}:
        return f"DRXI{stem}"
    return f"DR{day}I{stem}"


def tot_nutrient_sas(stem: str, day: int = 1, cycle: str | None = None) -> str:
    if cycle in {"99-00", "01-02"}:
        return _early_tot_name(stem)
    return f"DR{day}T{stem}"


def codes_for(spec: dict, cycle: str | None = None) -> dict | None:
    if cycle and cycle in spec["codes_by_cycle"]:
        return spec["codes_by_cycle"][cycle]
    return spec["codes"]


def raw_codes_for(spec: dict, cycle: str | None = None) -> dict | None:
    raw_by = spec.get("raw_codes_by_cycle") or {}
    if cycle and cycle in raw_by:
        return raw_by[cycle]
    if spec.get("raw_codes"):
        return spec["raw_codes"]
    return codes_for(spec, cycle)


def kind_for(spec: dict, cycle: str | None = None) -> str:
    return spec["kind"]


def target_for(spec: dict, cycle: str | None = None) -> str:
    tgt_by = spec.get("target_by_cycle") or {}
    if cycle and cycle in tgt_by:
        return tgt_by[cycle]
    return spec["target"]


def definition_for(spec: dict, cycle: str | None = None) -> str:
    def_by = spec.get("definition_by_cycle") or {}
    if cycle and cycle in def_by:
        return def_by[cycle]
    return spec.get("definition") or ""


def notes_for(spec: dict) -> str:
    return spec.get("notes") or ""


def diet_table(cycle: str, kind: str = "tot", day: int = 1) -> str | None:
    """kind in {'iff','tot','fcd'}; day is ignored for 99-02."""
    iff, iff2, tot, tot2, fcd = DIET_FILES[cycle]
    if kind == "fcd":
        return fcd
    if kind == "iff":
        return iff if day == 1 else iff2
    return tot if day == 1 else tot2


def _nutrient_sas_names(stem: str) -> list[str]:
    early = _early_tot_name(stem)
    names = [
        f"DR1T{stem}", f"DR2T{stem}",
        f"DR1I{stem}", f"DR2I{stem}",
        early, f"DRXI{stem}",
    ]
    if stem == "MOIS":
        names.extend(["DRXTWATE", "DRXTMOIS", "DRXIWATE", "DRXIMOIS"])
    if stem == "SODI":
        names.extend(["DRDTSODI", "DRDISODI", "DR1ISODI", "DR2ISODI"])
    return names


def _index_sas(index: dict, sas: str | None, short: str) -> None:
    if sas:
        index[str(sas)] = short


SAS_TO_SHORT_DIET = {}
for spec in DIET_VARS.values():
    _index_sas(SAS_TO_SHORT_DIET, spec.get("sas"), spec["short"])
    for alias in (spec.get("sas_by_cycle") or {}).values():
        _index_sas(SAS_TO_SHORT_DIET, alias, spec["short"])
    _index_sas(SAS_TO_SHORT_DIET, spec.get("day_pair"), spec["short"])
    for alias in spec.get("aliases") or []:
        _index_sas(SAS_TO_SHORT_DIET, alias, spec["short"])

for stem in list(NUTRIENT_STEMS) + list(FATTY_ACID_STEMS):
    short = (NUTRIENT_STEMS.get(stem) or FATTY_ACID_STEMS[stem])[0]
    for name in _nutrient_sas_names(stem):
        _index_sas(SAS_TO_SHORT_DIET, name, short)
for sas, short in (
    ("DRXIVAIU", "vit_a_iu"),
    ("DRXIVARE", "vit_a_re"),
    ("DRXICARO", "carotene_re"),
    ("DRXIVE", "vit_e_ate"),
    ("DRXTVAIU", "vit_a_iu"),
    ("DRXTVARE", "vit_a_re"),
    ("DRXTCARO", "carotene_re"),
    ("DRXTVE", "vit_e_ate"),
):
    _index_sas(SAS_TO_SHORT_DIET, sas, short)


def coalesce_sas_aliases(df, sas_to_short: dict | None = None):
    """Fold leftover DRXT* / DR1T* aliases into the short name after a multi-cycle concat."""
    import pandas as pd

    lookup = sas_to_short or SAS_TO_SHORT_DIET
    out = df.copy()
    for col in list(out.columns):
        short = lookup.get(str(col))
        if not short or short == col:
            continue
        if short not in out.columns:
            out.rename(columns={col: short}, inplace=True)
            continue
        out[short] = out[short].where(out[short].notna(), out[col])
        out.drop(columns=[col], inplace=True)
    return out
    

DIET_CATALOG = {
    "name": "dietary",
    "aliases": (
        "diet", "dietary", "dietary interview",
        "dietary supplement", "dietary supplements",
        "food frequency", "ffq", "dietary screener", "dtq",
    ),
    "vars": DIET_VARS,
    "sas_to_short": SAS_TO_SHORT_DIET,
    "grain": "person",
    "tables": {
        "DRXTOT": {"grain": "person", "day": 1},
        "DR1TOT": {"grain": "person", "day": 1},
        "DR2TOT": {"grain": "person", "day": 2},
        "DRXIFF": {"grain": "food", "day": 1},
        "DR1IFF": {"grain": "food", "day": 1},
        "DR2IFF": {"grain": "food", "day": 2},
        "DSQFILE1": {"grain": "person"},
        "DSQ1": {"grain": "person"},
        "DSQTOT": {"grain": "person"},
        "DSQFILE2": {"grain": "food"},
        "DSQ2": {"grain": "food"},
        "DSQIDS": {"grain": "food"},
        "DS1IDS": {"grain": "food", "day": 1},
        "DS2IDS": {"grain": "food", "day": 2},
        "DS1TOT": {"grain": "person", "day": 1},
        "DS2TOT": {"grain": "person", "day": 2},
        "FFQRAW": {"grain": "person"},
        "FFQDC": {"grain": "food"},
        "DTQ": {"grain": "person"},
        "DRXFCD": {"grain": "support"},
        "DRXFMT": {"grain": "support"},
        "DRXMCD": {"grain": "support"},
    },
}