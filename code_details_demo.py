from __future__ import annotations


CYCLES = [
    "99-00", "01-02", "03-04", "05-06", "07-08", "09-10",
    "11-12", "13-14", "15-16", "17-18", "17-20", "21-23",
]

SDDSRVYR_TO_CYCLE = {
    1: "99-00",
    2: "01-02",
    3: "03-04",
    4: "05-06",
    5: "07-08",
    6: "09-10",
    7: "11-12",
    8: "13-14",
    9: "15-16",
    10: "17-18",
    66: "17-20", # 11?
    12: "21-23",
}

CYCLE_TO_SDDSRVYR = {cycle: code for code, cycle in SDDSRVYR_TO_CYCLE.items()}

YES_NO = {1: "Yes", 2: "No", 7: "Refused", 9: "Don't know"}
LANG_EN_ES = {1: "English", 2: "Spanish"}
GENDER = {1: "Male", 2: "Female"}

EDUC_ADULT = {
    1: "Less Than 9th Grade",
    2: "9-11th Grade (Includes 12th grade with no diploma)",
    3: "High School Grad/GED or Equivalent",
    4: "Some College or AA degree",
    5: "College Graduate or above",
    7: "Refused",
    9: "Don't Know",
}

EDUC_YOUTH = {
    0: "Never Attended / Kindergarten Only",
    1: "1st Grade",
    2: "2nd Grade",
    3: "3rd Grade",
    4: "4th Grade",
    5: "5th Grade",
    6: "6th Grade",
    7: "7th Grade",
    8: "8th Grade",
    9: "9th Grade",
    10: "10th Grade",
    11: "11th Grade",
    12: "12th Grade, No Diploma",
    13: "High School Graduate",
    14: "GED or Equivalent",
    15: "More than high school",
    55: "Less Than 5th Grade",
    66: "Less Than 9th Grade",
    77: "Refused",
    99: "Don't know",
}

MARITAL_DETAIL = {
    1: "Married",
    2: "Widowed",
    3: "Divorced",
    4: "Separated",
    5: "Never married",
    6: "Living with partner",
    77: "Refused",
    99: "Don't know",
}

MARITAL_COLLAPSED = {
    1: "Married/Living with partner",
    2: "Widowed/Divorced/Separated",
    3: "Never married",
    77: "Refused",
    99: "Don't know",
}

INCOME_V1 = {
    1: "$0 to $4,999",
    2: "$5,000 to $9,999",
    3: "$10,000 to $14,999",
    4: "$15,000 to $19,999",
    5: "$20,000 to $24,999",
    6: "$25,000 to $34,999",
    7: "$35,000 to $44,999",
    8: "$45,000 to $54,999",
    9: "$55,000 to $64,999",
    10: "$65,000 to $74,999",
    11: "$75,000 and Over",
    12: "Over $20,000",
    13: "Under $20,000",
    77: "Refused",
    99: "Don't know",
}

INCOME_V2 = {
    1: "$0 to $4,999",
    2: "$5,000 to $9,999",
    3: "$10,000 to $14,999",
    4: "$15,000 to $19,999",
    5: "$20,000 to $24,999",
    6: "$25,000 to $34,999",
    7: "$35,000 to $44,999",
    8: "$45,000 to $54,999",
    9: "$55,000 to $64,999",
    10: "$65,000 to $74,999",
    12: "Over $20,000",
    13: "Under $20,000",
    14: "$75,000 to $99,999",
    15: "$100,000 and Over",
    77: "Refused",
    99: "Don't know",
}

HHREF_EDUC_COLLAPSED = {
    1: "Less than high school degree",
    2: "High school grad/GED or some college/AA degree",
    3: "College graduate or above",
}

# Discrete stand-in years for DMDHRAGZ bins. Kept numeric so the stacked
# column stays comparable with continuous DMDHRAGE in other cycles.
# Original codebook labels are in HHREF_AGE_BINS.
HHREF_AGE_COLLAPSED = {
    ### fixed ages decided to maintain overall column type identity
    1: 18,  # "<20 years",
    2: 30,  # "20-39 years",
    3: 50,  # "40-59 years",
    4: 65,  # "60+ years",
}
HHREF_AGE_BINS = {
    1: "<20 years",
    2: "20-39 years",
    3: "40-59 years",
    4: "60+ years",
}


YEARS_US_9 = {
    1: "Less than 1 year",
    2: "1 yr., less than 5 yrs.",
    3: "5 yrs., less than 10 yrs.",
    4: "10 yrs., less than 15 yrs.",
    5: "15 yrs., less than 20 yrs.",
    6: "20 yrs., less than 30 yrs.",
    7: "30 yrs., less than 40 yrs.",
    8: "40 yrs., less than 50 yrs.",
    9: "50 years or more",
    77: "Refused",
    88: "Could not determine",
    99: "Don't know",
}

YEARS_US_4 = {
    1: "Less than 5 year",
    2: "5 year or more, but less than 15 years",
    3: "15 year or more, but less than 30 years",
    4: "30 year or more",
    77: "Refused",
    99: "Don't know",
}

YEARS_US_6 = {
    1: "Less than 1 year",
    2: "1 to 4 years",
    3: "5 to 9 years",
    4: "10 to 14 years",
    5: "15 to 19 years",
    6: "20 years or more",
    77: "Refused",
    99: "Don't know",
}

BIRTH_3CAT = {
    1: "Born in 50 US States or Washington, DC",
    2: "Born in Mexico",
    3: "Born Elsewhere",
    7: "Refused",
    9: "Don't Know",
}

BIRTH_2CAT = {
    1: "Born in 50 US states or Washington, DC",
    2: "Others",
    77: "Refused",
    99: "Don't Know",
}

BORN_3CAT = BIRTH_3CAT

BORN_4CAT = {
    1: "Born in 50 US states or Washington, DC",
    2: "Born in Mexico",
    4: "Born in other Spanish-speaking country",
    5: "Born in other non-Spanish-speaking country",
    7: "Refused",
    9: "Don't know",
}

BORN_2CAT = {
    1: "Born in 50 US states or Washington, DC",
    2: "Born outside the US and Washington, DC",
    77: "Refused",
    99: "Don't know",
}


ACASI_3LANG = {1: "English", 2: "Spanish", 3: "Asian languages"}

INCOME_V2_CYCLES = {
    "07-08": INCOME_V2,
    "09-10": INCOME_V2,
    "11-12": INCOME_V2,
    "13-14": INCOME_V2,
    "15-16": INCOME_V2,
    "17-18": INCOME_V2,
}

BIRTH_2CAT_CYCLES = {
    "11-12": BIRTH_2CAT,
    "13-14": BIRTH_2CAT,
    "15-16": BIRTH_2CAT,
    "17-18": BIRTH_2CAT,
    "17-20": BIRTH_2CAT,
    "21-23": BIRTH_2CAT,
}

# DMDBORN2 4-category map is 07-08 and 09-10 only.
# 03-04 and 05-06 still use DMDBORN / BIRTH_3CAT.
BIRTH_4CAT_CYCLES = {
    "07-08": BORN_4CAT,
    "09-10": BORN_4CAT,
}

ACASI_3LANG_CYCLES = {
    "11-12": ACASI_3LANG,
    "13-14": ACASI_3LANG,
    "15-16": ACASI_3LANG,
    "17-18": ACASI_3LANG,
    "17-20": ACASI_3LANG,
}

# Public-file Target strings that repeat across many columns.
T_ALL = "Both males and females 0 YEARS - 150 YEARS"
T_0_84 = "Both males and females 0 YEARS - 84 YEARS"
T_0_79 = "Both males and females 0 YEARS - 79 YEARS"
T_0_2 = "Both males and females 0 YEARS - 2 YEARS"
T_0_19 = "Both males and females 0 YEARS - 19 YEARS"
T_2_19 = "Both males and females 2 YEARS - 19 YEARS"
T_6_19 = "Both males and females 6 YEARS - 19 YEARS"
T_6_150 = "Both males and females 6 YEARS - 150 YEARS"
T_8_150 = "Both males and females 8 YEARS - 150 YEARS"
T_8_69 = "Both males and females 8 YEARS - 69 YEARS"
T_12_150 = "Both males and females 12 YEARS - 150 YEARS"
T_12_59 = "Both males and females 12 YEARS - 59 YEARS"
T_14_150 = "Both males and females 14 YEARS - 150 YEARS"
T_17_150 = "Both males and females 17 YEARS - 150 YEARS"
T_20_150 = "Both males and females 20 YEARS - 150 YEARS"
T_F_8_59 = "Females only 8 YEARS - 59 YEARS"
T_F_20_44 = "Females only 20 YEARS - 44 YEARS"


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
    }


DEMO_VARS = {
    "seqn": _var(
        "seqn", "SEQN", "id",
        "Respondent sequence number.",
        T_ALL,
        label="Respondent sequence number",
        definition="Unique respondent identifier assigned to every interviewed sample person.",
    ),
    "release_cycle": _var(
        "release_cycle", "SDDSRVYR", "categorical",
        "Data Release Number.",
        T_ALL,
        label="Data Release Number",
        codes={
            1: "NHANES 1999-2000 Public Release",
            2: "NHANES 2001-2002 Public Release",
            3: "NHANES 2003-2004 Public Release",
            4: "NHANES 2005-2006 Public Release",
            5: "NHANES 2007-2008 Public Release",
            6: "NHANES 2009-2010 Public Release",
            7: "NHANES 2011-2012 Public Release",
            8: "NHANES 2013-2014 Public Release",
            9: "NHANES 2015-2016 Public Release",
            10: "NHANES 2017-2018 public release",
            66: "NHANES 2017-March 2020 pre-pandemic",
            12: "NHANES August 2021-August 2023 public release",
        },
        notes="17-20 pre-pandemic public file uses SDDSRVYR=66, not 11.",
        definition=(
            "Two-year public-release cycle number. 1=1999-2000 ... 10=2017-2018; "
            "66=2017-March 2020 pre-pandemic combined file; 12=August 2021-August 2023."
        ),
    ),
    "interview_exam_status": _var(
        "interview_exam_status", "RIDSTATR", "categorical",
        "Interview and Examination Status of the Sample Person.",
        T_ALL,
        codes={1: "Interviewed Only", 2: "Both Interviewed and MEC examined"},
        definition=(
            "1 = household interview only (no MEC exam). "
            "2 = interviewed and examined in the MEC. "
            "21-23 codebook also allows the household interview to have been by telephone."
        ),
    ),
    "exam_6mo_period": _var(
        "exam_6mo_period", "RIDEXMON", "categorical",
        "Six month time period when the examination was performed - two categories: November 1 through April 30, May 1 through October 31.",
        T_ALL,
        codes={1: "November 1 through April 30", 2: "May 1 through October 31"},
        definition="1 = exam November 1-April 30; 2 = exam May 1-October 31.",
    ),
    "gender": _var(
        "gender", "RIAGENDR", "categorical",
        "Gender of the sample person",
        T_ALL,
        codes=GENDER,
        definition="1 = Male; 2 = Female.",
    ),
    "age_years": _var(
        "age_years", "RIDAGEYR", "continuous",
        "Best age in years of the sample person at time of HH screening. "
        "Topcoded at 85 years in 1999-2006 and at 80 years from 2007-2008 onward. "
        "2021-2023 notes the weighted mean age among those 80+ is 85 years.",
        T_ALL,
        notes=(
            "Public-file topcode changed from 85 (99-06) to 80 (07-08+). "
            "Values are left as released; this catalog does not un-topcode."
        ),
        definition=(
            "Age in years at household screening, usually from date of birth. "
            "If DOB is missing, reported age in years is used."
        ),
        definition_by_cycle={
            "99-00": "Single year of age 0-84; 85 = 85 years or older (weighted mean of 85+ was 88 in 1999-2000).",
            "01-02": "Single year of age 0-84; 85 = 85 years or older.",
            "03-04": "Single year of age 0-84; 85 = 85 years or older.",
            "05-06": "Single year of age 0-84; 85 = 85 years or older.",
            "07-08": "Single year of age 1-79; 80 = 80 years or older.",
            "09-10": "Single year of age 1-79; 80 = 80 years or older.",
            "11-12": "Single year of age 1-79; 80 = 80 years or older.",
            "13-14": "Single year of age 1-79; 80 = 80 years or older.",
            "15-16": "Single year of age 1-79; 80 = 80 years or older.",
            "17-18": "Single year of age 1-79; 80 = 80 years or older (weighted mean of 80+ is 85).",
            "17-20": "Single year of age 1-79; 80 = 80 years or older (weighted mean of 80+ is 85).",
            "21-23": "Single year of age 1-79; 80 = 80 years or older (weighted mean of 80+ is 85).",
        },
    ),
    "age_months_screen": _var(
        "age_months_screen", "RIDAGEMN", "continuous",
        "Age in months at screening. Early files described this for ages under 85; "
        "later public files report it for persons 24 months or younger.",
        T_0_84,
        target_by_cycle={
            "07-08": T_0_79,
            "09-10": T_0_79,
            "11-12": T_0_2,
            "13-14": T_0_2,
            "15-16": T_0_2,
            "17-18": T_0_2,
            "17-20": T_0_2,
            "21-23": T_0_2,
        },
        notes=(
            "Codebook Target: 0-84 (99-06), 0-79 (07-10), 0-2 years / 0-24 months (11-12+). "
            "Later files restrict the public column to infants."
        ),
        definition="Age in months at household screening.",
        definition_by_cycle={
            "99-00": "Best age in months at screening for persons under 85 (RIDAGEYR < 85).",
            "01-02": "Best age in months at screening for persons under 85 (RIDAGEYR < 85).",
            "03-04": "Best age in months at screening for persons under 85 (RIDAGEYR < 85).",
            "05-06": "Best age in months at screening for persons under 85 (RIDAGEYR < 85).",
            "07-08": "Best age in months at screening for persons under 80.",
            "09-10": "Best age in months at screening for persons under 80.",
            "11-12": "Released for persons <25 months at exam (RIDEXAGM < 25). If DOB missing, months are computed from imputed screening age in years.",
            "13-14": "Released for persons <25 months at exam (RIDEXAGM < 25). If DOB missing, months are computed from imputed screening age in years.",
            "15-16": "Released for persons <25 months at exam (RIDEXAGM < 25). If DOB missing, months are computed from imputed screening age in years.",
            "17-18": "Released for persons <25 months at exam (RIDEXAGM < 25). If DOB missing, months are computed from imputed screening age in years.",
            "17-20": "Released for persons aged 24 months or younger at exam (or screening if not examined).",
            "21-23": "Released for persons <25 months at exam (RIDEXAGM < 25). If DOB missing, months are computed from imputed screening age in years.",
        },
    ),
    "age_months_exam": _var(
        "age_months_exam", "RIDAGEEX", "continuous",
        "Age in months at examination. Early files used RIDAGEEX; "
        "from 2011-2012 the public name is RIDEXAGM (typically 0-19 years). "
        "Not on the 2017-2020 pre-pandemic public file (P_DEMO).",
        T_0_84,
        sas_by_cycle={
            "11-12": "RIDEXAGM",
            "13-14": "RIDEXAGM",
            "15-16": "RIDEXAGM",
            "17-18": "RIDEXAGM",
            "21-23": "RIDEXAGM",
        },
        target_by_cycle={
            "07-08": T_0_79,
            "09-10": T_0_79,
            "11-12": T_0_19,
            "13-14": T_0_19,
            "15-16": T_0_19,
            "17-18": T_0_19,
            "21-23": T_0_19,
        },
        notes=(
            "Removed the 17-20 RIDEXAGM alias. P_DEMO does not include "
            "exam age in months. Loader should skip the column that cycle. "
            "Codebook Target: 0-84 (99-06), 0-79 (07-10), 0-19 (11-18 and 21-23)."
        ),
        definition="Age in months at MEC examination.",
        definition_by_cycle={
            "99-00": "RIDAGEEX: months at exam for persons <85 at screening.",
            "01-02": "RIDAGEEX: months at exam for persons <85 at screening.",
            "03-04": "RIDAGEEX: months at exam for persons <85 at screening.",
            "05-06": "RIDAGEEX: months at exam for persons <85 at screening.",
            "07-08": "RIDAGEEX: months at exam for persons <80 at screening.",
            "09-10": "RIDAGEEX: months at exam for persons <80.",
            "11-12": "RIDEXAGM: months at exam for persons <240 months (0-19 years).",
            "13-14": "RIDEXAGM: months at exam for persons <240 months (0-19 years).",
            "15-16": "RIDEXAGM: months at exam for persons <240 months (0-19 years).",
            "17-18": "RIDEXAGM: months at exam for persons <240 months (0-19 years).",
            "21-23": "RIDEXAGM: months at exam for persons <240 months (0-19 years).",
        },
    ),
    "age_years_exam_2_19": _var(
        "age_years_exam_2_19", "RIDEXAGY", "continuous",
        "Age in years of the participant at the time of examination. Reported for persons aged 2-19 years at the time of examination.",
        T_2_19,
        notes="Public DEMO file includes RIDEXAGY in 11-12 only. Absent from other public DEMO files in this stack.",
        definition="Age in years at exam, released for persons aged 2-19 years at screening/exam (11-12 codebook: 2-19 at screening).",
    ),
    "race_ethnicity": _var(
        "race_ethnicity", "RIDRETH1", "categorical",
        "Recode of reported race and ethnicity information.",
        T_ALL,
        codes={
            1: "Mexican American",
            2: "Other Hispanic",
            3: "Non-Hispanic White",
            4: "Non-Hispanic Black",
            5: "Other Race - Including Multi-Racial",
        },
        definition=(
            "Derived from race and Hispanic-origin questions. "
            "Self-identified Mexican American = 1 regardless of other identities. "
            "Other self-identified Hispanic = 2. Remaining non-Hispanic participants: "
            "White=3, Black=4, other including multiracial=5. "
            "From 11-12 onward Non-Hispanic Asians are folded into code 5 so RIDRETH1 "
            "can be pooled with 1999-2010. Codes 6 and 7 are not used."
        ),
    ),
    "race_ethnicity_nh3": _var(
        "race_ethnicity_nh3", "RIDRETH2", "categorical",
        "Linked NH3 Race and Ethnicity Recode.",
        T_ALL,
        codes={
            1: "Non-Hispanic White",
            2: "Non-Hispanic Black",
            3: "Mexican American",
            4: "Other Race - Including Multi-Racial",
            5: "Other Hispanic",
        },
        notes="RIDRETH2 is on 99-00 through 03-04 public files only; dropped starting 05-06.",
        definition="NHANES III-linked race/ethnicity recode. Not derived the same way as RIDRETH1.",
    ),
    "race_ethnicity_asian": _var(
        "race_ethnicity_asian", "RIDRETH3", "categorical",
        "Recode of reported race and Hispanic origin information, with Non-Hispanic Asian Category",
        T_ALL,
        codes={
            1: "Mexican American",
            2: "Other Hispanic",
            3: "Non-Hispanic White",
            4: "Non-Hispanic Black",
            6: "Non-Hispanic Asian",
            7: "Other Race - Including Multi-Racial",
        },
        notes="Added with the Asian oversample starting 2011-2012. Code 5 is unused.",
        definition=(
            "Same derivation as RIDRETH1 except Non-Hispanic Asian is split out as 6 "
            "and other/multiracial is 7. Mexican American=1 regardless of other identities; "
            "other Hispanic=2; NH White=3; NH Black=4. Code 5 is not used."
        ),
    ),
    "military_service": _var(
        "military_service", "DMQMILIT", "categorical",
        "Did {you/SP} ever serve in the Armed Forces of the United States?",
        T_17_150,
        codes=YES_NO,
        sas_by_cycle={
            "11-12": "DMQMILIZ",
            "13-14": "DMQMILIZ",
            "15-16": "DMQMILIZ",
            "17-18": "DMQMILIZ",
            "21-23": "DMQMILIZ",
        },
        notes=(
            "Name is DMQMILIT through 09-10 and DMQMILIZ from 11-12. "
            "Not on 17-20 P_DEMO; that alias was removed."
        ),
        definition="Yes/No/Refused/Don't know veteran or military-service item.",
        definition_by_cycle={
            "99-00": "DMQMILIT: ever served in the U.S. Armed Forces (Army, Navy, Air Force, Marine Corps, Coast Guard).",
            "01-02": "DMQMILIT: ever served in the U.S. Armed Forces.",
            "03-04": "DMQMILIT: ever served in the U.S. Armed Forces.",
            "05-06": "DMQMILIT: ever served in the U.S. Armed Forces.",
            "07-08": "DMQMILIT: ever served in the U.S. Armed Forces.",
            "09-10": "DMQMILIT: ever served in the U.S. Armed Forces.",
            "11-12": "DMQMILIZ: ever served on active duty in the U.S. Armed Forces, Reserves, or National Guard. Active duty excludes training for Reserves/Guard but includes activation for U.S. or foreign military or humanitarian operations. Question wording changed in 2011.",
            "13-14": "DMQMILIZ: active-duty wording introduced in 2011 (see 11-12).",
            "15-16": "DMQMILIZ: active-duty wording introduced in 2011 (see 11-12).",
            "17-18": "DMQMILIZ: active-duty wording introduced in 2011 (see 11-12).",
            "21-23": "DMQMILIZ: active-duty wording introduced in 2011 (see 11-12).",
        },
    ),
    "served_foreign": _var(
        "served_foreign", "DMQADFC", "categorical",
        "Did {you/SP} ever serve in a foreign country during a time of armed conflict or on a humanitarian or peace-keeping mission?",
        T_17_150,
        codes=YES_NO,
        notes="On 11-12 through 17-18 public DEMO files. Not on 17-20 or 21-23.",
        definition=(
            "Asked of persons who reported active duty. Yes if they served in a foreign "
            "country during armed conflict or on a humanitarian/peace-keeping mission "
            "(examples in later codebooks include Bosnia/Kosovo, Sinai, 2004 tsunami, Haiti 2010)."
        ),
    ),
    "country_of_birth": _var(
        "country_of_birth", "DMDBORN", "categorical",
        "In what country {were you/was SP} born?",
        T_ALL,
        codes=BIRTH_3CAT,
        sas_by_cycle={
            "07-08": "DMDBORN2",
            "09-10": "DMDBORN2",
            "11-12": "DMDBORN4",
            "13-14": "DMDBORN4",
            "15-16": "DMDBORN4",
            "17-18": "DMDBORN4",
            "17-20": "DMDBORN4",
            "21-23": "DMDBORN4",
        },
        codes_by_cycle={
            **BIRTH_4CAT_CYCLES,
            **BIRTH_2CAT_CYCLES,
        },
        notes=(
            "99-06: DMDBORN 3-cat. 07-10: DMDBORN2 4-cat. 11+: DMDBORN4 2-cat. "
            "03-04 and 05-06 stay on DMDBORN (they do not have DMDBORN2)."
        ),
        definition="Recode of reported country of birth. Category set is not 1:1 across generations.",
        definition_by_cycle={
            "99-00": "DMDBORN 3-cat: 1=50 US states or DC; 2=Mexico; 3=elsewhere; 7/9 refused/DK.",
            "01-02": "DMDBORN 3-cat: 1=50 US states or DC; 2=Mexico; 3=elsewhere; 7/9 refused/DK.",
            "03-04": "DMDBORN 3-cat: 1=50 US states or DC; 2=Mexico; 3=elsewhere; 7/9 refused/DK.",
            "05-06": "DMDBORN 3-cat: 1=50 US states or DC; 2=Mexico; 3=elsewhere; 7/9 refused/DK.",
            "07-08": (
                "DMDBORN2: 1=50 US states or DC; 2=Mexico; 4=other Spanish-speaking country; "
                "5=other non-Spanish-speaking country; 7/9 refused/DK. Code 3 is unused "
                "(placeholder so 4/5 can be collapsed back to DMDBORN=3 when pooling with 99-06)."
            ),
            "09-10": (
                "DMDBORN2: 1=50 US states or DC; 2=Mexico; 4=other Spanish-speaking country; "
                "5=other non-Spanish-speaking country; 7/9 refused/DK. Code 3 unused placeholder."
            ),
            "11-12": "DMDBORN4 2-cat for disclosure: 1=50 US states or DC; 2=other countries including US territories.",
            "13-14": "DMDBORN4 2-cat for disclosure: 1=50 US states or DC; 2=other countries including US territories.",
            "15-16": "DMDBORN4 2-cat for disclosure: 1=50 US states or DC; 2=other countries including US territories.",
            "17-18": "DMDBORN4 2-cat for disclosure: 1=50 US states or DC; 2=other countries including US territories.",
            "17-20": "DMDBORN4 2-cat for disclosure: 1=50 US states or DC; 2=other countries including US territories.",
            "21-23": "DMDBORN4 2-cat for disclosure: 1=50 US states or DC; 2=other countries including US territories.",
        },
    ),
    "citizenship": _var(
        "citizenship", "DMDCITZN", "categorical",
        "{Are you/Is SP} a citizen of the United States? [Information about citizenship is being collected by the U.S. Public Health Service to perform health related research. Providing this information is voluntary and is collected under the authority of the Public Health Service Act. There will be no effect on pending immigration or citizenship petitions.]",
        T_ALL,
        codes={
            1: "Citizen by birth or naturalization",
            2: "Not a citizen of the US",
            7: "Refused",
            9: "Don't know",
        },
        notes="On 99-00 through 17-18 public DEMO files. Not on 17-20 P_DEMO or 21-23 DEMO_L.",
        definition=(
            "1 = citizen by birth or naturalization; 2 = not a US citizen; 7/9 refused/DK. "
            "Persons born in the US or US territories who acquired citizenship at birth are coded 1."
        ),
    ),
    "years_in_us": _var(
        "years_in_us", "DMDYRSUS", "categorical",
        "Length of time SP has been in the US.",
        T_ALL,
        codes=YEARS_US_9,
        sas_by_cycle={"17-20": "DMDYRUSZ", "21-23": "DMDYRUSR"},
        codes_by_cycle={"17-20": YEARS_US_4, "21-23": YEARS_US_6},
        notes=(
            "9-cat DMDYRSUS through 17-18; 4-cat DMDYRUSZ on 17-20; "
            "6-cat DMDYRUSR on 21-23. These are not 1:1 recodes."
        ),
        definition=(
            "Length of US residence for persons born outside the US, from month/year came "
            "to live in the US (DMQ.160). Missing arrival month is imputed as July (month=7)."
        ),
        definition_by_cycle={
            "99-00": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "01-02": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "03-04": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "05-06": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "07-08": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "09-10": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "11-12": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "13-14": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "15-16": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "17-18": "DMDYRSUS 9-cat from <1 year through 50+ years; 77 refused; 88 could not determine; 99 DK.",
            "17-20": "DMDYRUSZ 4-cat disclosure recode: 1=<5y; 2=5-<15y; 3=15-<30y; 4=30+y. Not a 1:1 map from the 9-cat version.",
            "21-23": "DMDYRUSR 6-cat disclosure recode: 1=<1y; 2=1-4y; 3=5-9y; 4=10-14y; 5=15-19y; 6=20+y. Not a 1:1 map from the 9-cat or 4-cat versions.",
        },
    ),
    "educ_youth": _var(
        "educ_youth", "DMDEDUC3", "categorical",
        "(SP Interview Version) What is the highest grade or level of school {you have/SP has} completed or the highest degree {you have/s/he has} received?",
        T_6_19,
        codes=EDUC_YOUTH,
        notes="On 99-00 through 17-18 public DEMO files. Not on 17-20 P_DEMO or 21-23 DEMO_L.",
        definition=(
            "Highest grade/degree for participants 6-19. Recoded to single grades 1-12, "
            "HS grad, GED, and more than HS. Codes 55 (<5th) and 66 (<9th) flag older "
            "youth with very low education. 0 = never attended / kindergarten only. "
            "77/99 = refused/DK."
        ),
    ),
    "educ_adult": _var(
        "educ_adult", "DMDEDUC2", "categorical",
        "(SP Interview Version) What is the highest grade or level of school {you have/SP has} completed or the highest degree {you have/s/he has} received?",
        T_20_150,
        codes=EDUC_ADULT,
        definition=(
            "Highest grade/degree for adults 20+. 1=<9th; 2=9-11th (includes 12th, no diploma); "
            "3=HS grad/GED; 4=some college or AA; 5=college graduate or above; 7/9 refused/DK."
        ),
    ),
    "educ_3cat": _var(
        "educ_3cat", "DMDEDUC", "categorical",
        "(SP Interview Version) What is the highest grade or level of school {you have/SP has} completed or the highest degree {you have/s/he has} received?",
        T_6_150,
        codes={
            1: "Less Than High School",
            2: "High School Diploma (including GED)",
            3: "More Than High School",
            7: "Refused",
            9: "Don't know",
        },
        notes="Early-cycle combined education recode on 99-00 through 03-04; not on later public files.",
        definition="Collapsed education recode for ages 6+: 1=<HS; 2=HS diploma/GED; 3=>HS.",
    ),
    "in_school": _var(
        "in_school", "DMDSCHOL", "categorical",
        "{Are you/Is SP} now . . .",
        T_6_19,
        codes={
            1: "In school",
            2: "On vacation from school (between grades)",
            3: "Neither in school or on vacation from school (between grades)",
            7: "Refused",
            9: "Don't know",
        },
        notes="On 99-00 through 09-10 public DEMO files. Dropped starting 11-12.",
        definition="Current school attendance for ages 6-19.",
    ),
    "marital": _var(
        "marital", "DMDMARTL", "categorical",
        "Marital Status",
        T_14_150,
        codes=MARITAL_DETAIL,
        sas_by_cycle={"17-20": "DMDMARTZ", "21-23": "DMDMARTZ"},
        codes_by_cycle={"17-20": MARITAL_COLLAPSED, "21-23": MARITAL_COLLAPSED},
        notes=(
            "Question asked of persons 14+ in all cycles. Public Target is 14+ through 05-06 "
            "and 20+ from 07-08 onward (disclosure). 6-cat DMDMARTL through 17-18; "
            "3-cat DMDMARTZ on 17-20 and 21-23. Do not expand 3-cat codes back to 6-cat."
        ),
        target_by_cycle={
            "07-08": T_20_150,
            "09-10": T_20_150,
            "11-12": T_20_150,
            "13-14": T_20_150,
            "15-16": T_20_150,
            "17-18": T_20_150,
            "17-20": T_20_150,
            "21-23": T_20_150,
        },
        definition="Sample-person marital status. Asked 14+; public release age floor changes by cycle.",
        definition_by_cycle={
            "99-00": "6-cat DMDMARTL released for 14+: married, widowed, divorced, separated, never married, living with partner; 77/99 refused/DK. Missing values were sometimes imputed from other questionnaire items.",
            "01-02": "6-cat DMDMARTL released for 14+.",
            "03-04": "6-cat DMDMARTL released for 14+.",
            "05-06": "6-cat DMDMARTL released for 14+.",
            "07-08": "6-cat DMDMARTL still asked of 14+ but released only for 20+.",
            "09-10": "6-cat DMDMARTL asked of 14+, released for 20+.",
            "11-12": "6-cat DMDMARTL asked of 14+, released for 20+.",
            "13-14": "6-cat DMDMARTL asked of 14+, released for 20+.",
            "15-16": "6-cat DMDMARTL asked of 14+, released for 20+.",
            "17-18": "6-cat DMDMARTL asked of 14+, released for 20+.",
            "17-20": "DMDMARTZ 3-cat disclosure recode released for 20+: 1=married/living with partner; 2=widowed/divorced/separated; 3=never married.",
            "21-23": "DMDMARTZ 3-cat disclosure recode released for 20+: 1=married/living with partner; 2=widowed/divorced/separated; 3=never married.",
        },
    ),
    "pregnant_exam": _var(
        "pregnant_exam", "RIDEXPRG", "categorical",
        "Pregnancy status at the time of MEC exam.",
        T_F_8_59,
        codes={
            1: "Yes, positive lab pregnancy test or self-reported pregnant at exam",
            2: "SP not pregnant at exam",
            3: "Cannot ascertain if SP is pregnant at exam",
        },
        target_by_cycle={
            "07-08": T_F_20_44,
            "09-10": T_F_20_44,
            "11-12": T_F_20_44,
            "13-14": T_F_20_44,
            "15-16": T_F_20_44,
            "17-18": T_F_20_44,
            "17-20": T_F_20_44,
            "21-23": T_F_20_44,
        },
        notes=(
            "Ascertained for females 8-59 in all documented cycles. Public Target is 8-59 "
            "through 05-06 and 20-44 from 07-08 onward (disclosure)."
        ),
        definition=(
            "Exam-time pregnancy recode from self-report plus urine pregnancy test. "
            "Self-reported pregnant => 1 even if urine is negative. "
            "Self-report no + negative urine => 2. "
            "Don't-know + negative urine, or interview-only (no exam) => 3. "
            "Don't-know or no + positive urine => 1."
        ),
    ),
    "pregnant_status": _var(
        "pregnant_old", "RIDPREG", "categorical",
        "Pregnancy status variable based on all source data. NOTE: This is the previous pregnancy status recode variable. RIDPREG is a more conservative pregnancy status variable. Please review the file documentation.",
        T_F_8_59,
        codes={
            1: "Yes, based on positive lab pregnancy test, self-reported pregnancy status, screener interview data or menstrual period history",
            2: "SP not pregnant",
            9: "Cannot ascertain if SP is pregnant",
        },
        notes="Early-cycle pregnancy recode on 99-00 and 01-02; later files use RIDEXPRG only.",
        definition=(
            "Broader/conservative pregnancy recode using lab, self-report, screener, and "
            "menstrual-history sources. 1=pregnant; 2=not pregnant; 9=cannot ascertain."
        ),
    ),
    "hh_size": _var(
        "hh_size", "DMDHHSIZ", "continuous",
        "Total number of people in the Household",
        T_ALL,
        notes="Public files top-code household size at 7 (7 or more people).",
        definition="Count of people in the household; 7 = 7 or more.",
    ),
    "family_size": _var(
        "family_size", "DMDFMSIZ", "continuous",
        "Total number of people in the Family",
        T_ALL,
        notes="On 05-06 through 17-18 public DEMO files. Not on 99-04, 17-20 P_DEMO, or 21-23 DEMO_L.",
        definition=(
            "Count of people in the CPS family (two or more related by birth, marriage, or "
            "adoption and living together). 7 = 7 or more."
        ),
    ),
    "hh_kids_0_5": _var(
        "hh_kids_0_5", "DMDHHSZA", "continuous",
        "Number of children aged 5 years or younger in the household",
        T_ALL,
        notes="Added 11-12; on 11-12 through 17-18. Not on 17-20 or 21-23. Top-coded at 3.",
        definition="Count of household children aged 0-5; 3 = 3 or more.",
    ),
    "hh_kids_6_17": _var(
        "hh_kids_6_17", "DMDHHSZB", "continuous",
        "Number of children aged 6-17 years old in the household",
        T_ALL,
        notes="Added 11-12; on 11-12 through 17-18. Not on 17-20 or 21-23. Top-coded at 4.",
        definition="Count of household children aged 6-17; 4 = 4 or more.",
    ),
    "hh_adults_60plus": _var(
        "hh_adults_60plus", "DMDHHSZE", "continuous",
        "Number of adults aged 60 years or older in the household",
        T_ALL,
        notes="Added 11-12; on 11-12 through 17-18. Not on 17-20 or 21-23. Top-coded at 3.",
        definition="Count of household adults aged 60+; 3 = 3 or more.",
    ),
    "hh_income": _var(
        "hh_income", "INDHHINC", "categorical",
        "Total household income (reported as a range value in dollars)",
        T_ALL,
        codes=INCOME_V1,
        sas_by_cycle={
            "07-08": "INDHHIN2",
            "09-10": "INDHHIN2",
            "11-12": "INDHHIN2",
            "13-14": "INDHHIN2",
            "15-16": "INDHHIN2",
            "17-18": "INDHHIN2",
        },
        codes_by_cycle=INCOME_V2_CYCLES,
        notes=(
            "INDHHINC 99-06; INDHHIN2 07-08 through 17-18. Not on 17-20 or "
            "21-23 public files (use family_pir). CDC documents recoding "
            "INDHHIN2 14/15 to INDHHINC=11 when pooling with 99-06."
        ),
        definition=(
            "Total annual household income in dollar ranges. Single-family households use "
            "family income. Multi-family households sum reported family/individual incomes "
            "or use a household-level estimate when some family incomes are missing. "
            "Codes 12/13 (<$20k / >=$20k) are used only when no finer range is given."
        ),
        definition_by_cycle={
            "99-00": "INDHHINC V1 ranges; top detailed bin is 11=$75,000 and over.",
            "01-02": "INDHHINC V1 ranges; top detailed bin is 11=$75,000 and over.",
            "03-04": "INDHHINC V1 ranges; top detailed bin is 11=$75,000 and over.",
            "05-06": "INDHHINC V1 ranges; top detailed bin is 11=$75,000 and over.",
            "07-08": "INDHHIN2 V2 ranges: adds 14=$75,000-$99,999 and 15=$100,000 and over; drops code 11.",
            "09-10": "INDHHIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
            "11-12": "INDHHIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
            "13-14": "INDHHIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
            "15-16": "INDHHIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
            "17-18": "INDHHIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
        },
    ),
    "family_income": _var(
        "family_income", "INDFMINC", "categorical",
        "Total family income (reported as a range value in dollars)",
        T_ALL,
        codes=INCOME_V1,
        sas_by_cycle={
            "07-08": "INDFMIN2",
            "09-10": "INDFMIN2",
            "11-12": "INDFMIN2",
            "13-14": "INDFMIN2",
            "15-16": "INDFMIN2",
            "17-18": "INDFMIN2",
        },
        codes_by_cycle=INCOME_V2_CYCLES,
        notes="Same V1/V2 split as hh_income. Absent 17-20 and 21-23.",
        definition=(
            "Total annual family (or individual, for 1-person / unrelated-adult households) "
            "income in dollar ranges. Exact dollars recoded to ranges; if exact dollars "
            "refused, a <$20k/>=$20k screener plus hand-card range is used and the range "
            "midpoint is stored internally for PIR."
        ),
        definition_by_cycle={
            "99-00": "INDFMINC V1 ranges; top detailed bin is 11=$75,000 and over.",
            "01-02": "INDFMINC V1 ranges; top detailed bin is 11=$75,000 and over.",
            "03-04": "INDFMINC V1 ranges; top detailed bin is 11=$75,000 and over.",
            "05-06": "INDFMINC V1 ranges; top detailed bin is 11=$75,000 and over.",
            "07-08": "INDFMIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
            "09-10": "INDFMIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
            "11-12": "INDFMIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
            "13-14": "INDFMIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
            "15-16": "INDFMIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
            "17-18": "INDFMIN2 V2 ranges: 14=$75k-$99k; 15=$100k+.",
        },
    ),
    "family_pir": _var(
        "family_pir", "INDFMPIR", "continuous",
        "Poverty income ratio (PIR) - a ratio of family income to poverty threshold",
        T_ALL,
        notes="Public files top-code PIR at 5.00.",
        definition=(
            "Family (or individual) income divided by the survey-year HHS poverty guideline "
            "for family size and geography. Not computed if only the <$20k/>=$20k screener "
            "is available or income is missing. Range midpoints are used when income is a "
            "category. Values >=5.00 are coded 5.00."
        ),
    ),
    "sp_lang": _var(
        "sp_lang", "SIALANG", "categorical",
        "Language of the Sample Person Interview Instrument",
        T_ALL,
        codes=LANG_EN_ES,
        notes="On 03-04 through 17-20 public files. Not on 99-02 or 21-23 DEMO_L.",
        definition="1=English, 2=Spanish for the household sample-person interview.",
    ),
    "sp_proxy": _var(
        "sp_proxy", "SIAPROXY", "categorical",
        "Was a Proxy respondent used in conducting the Sample Person (SP) interview?",
        T_ALL,
        codes=YES_NO,
        notes="On 03-04 through 17-20 public files. Not on 99-02 or 21-23 DEMO_L.",
        definition="Whether a proxy answered the sample-person interview.",
    ),
    "sp_interpreter": _var(
        "sp_interpreter", "SIAINTRP", "categorical",
        "Was an interpreter used to conduct the Sample Person (SP) interview?",
        T_ALL,
        codes=YES_NO,
        notes="On 03-04 through 17-20 public files. Not on 99-02 or 21-23 DEMO_L.",
        definition="Whether an interpreter was used for the sample-person interview.",
    ),
    "fam_lang": _var(
        "fam_lang", "FIALANG", "categorical",
        "Language of the Family Interview Instrument",
        T_ALL,
        codes=LANG_EN_ES,
        notes="On 03-04 through 17-20 public files. Not on 99-02 or 21-23 DEMO_L.",
        definition="1=English, 2=Spanish for the family interview.",
    ),
    "fam_proxy": _var(
        "fam_proxy", "FIAPROXY", "categorical",
        "Was a Proxy respondent used in conducting the Family Interview?",
        T_ALL,
        codes=YES_NO,
        notes="On 03-04 through 17-20 public files. Not on 99-02 or 21-23 DEMO_L.",
        definition="Whether a proxy answered the family interview.",
    ),
    "fam_interpreter": _var(
        "fam_interpreter", "FIAINTRP", "categorical",
        "Was an interpreter used to conduct the Family interview?",
        T_ALL,
        codes=YES_NO,
        notes="On 03-04 through 17-20 public files. Not on 99-02 or 21-23 DEMO_L.",
        definition="Whether an interpreter was used for the family interview.",
    ),
    "mec_lang": _var(
        "mec_lang", "MIALANG", "categorical",
        "Language of the MEC CAPI Interview Instrument",
        T_12_150,
        codes=LANG_EN_ES,
        target_by_cycle={
            "05-06": T_ALL,
            "07-08": T_ALL,
            "09-10": T_ALL,
            "11-12": T_ALL,
            "13-14": T_ALL,
            "15-16": T_8_150,
            "17-18": T_8_150,
            "17-20": T_8_150,
        },
        notes=(
            "Language block starts 03-04. Codebook Target: 12+ (03-04), 0-150 (05-14), "
            "8+ (15-20). Not on 99-02 or 21-23."
        ),
        definition="1=English, 2=Spanish for the MEC CAPI interview.",
    ),
    "mec_proxy": _var(
        "mec_proxy", "MIAPROXY", "categorical",
        "Was a Proxy respondent used in conducting the MEC CAPI Interview?",
        T_12_150,
        codes=YES_NO,
        target_by_cycle={
            "05-06": T_ALL,
            "07-08": T_ALL,
            "09-10": T_ALL,
            "11-12": T_ALL,
            "13-14": T_ALL,
            "15-16": T_8_150,
            "17-18": T_8_150,
            "17-20": T_8_150,
        },
        notes="Same Target path as mec_lang. Not on 99-02 or 21-23.",
        definition="Whether a proxy answered the MEC CAPI interview.",
    ),
    "mec_interpreter": _var(
        "mec_interpreter", "MIAINTRP", "categorical",
        "Was an interpreter used to conduct the MEC CAPI interview?",
        T_12_150,
        codes=YES_NO,
        target_by_cycle={
            "05-06": T_ALL,
            "07-08": T_ALL,
            "09-10": T_ALL,
            "11-12": T_ALL,
            "13-14": T_ALL,
            "15-16": T_8_150,
            "17-18": T_8_150,
            "17-20": T_8_150,
        },
        notes="Same Target path as mec_lang. Not on 99-02 or 21-23.",
        definition="Whether an interpreter was used for the MEC CAPI interview.",
    ),
    "acasi_lang": _var(
        "acasi_lang", "AIALANG", "categorical",
        "Language of the MEC ACASI Interview Instrument",
        T_12_59,
        codes=LANG_EN_ES,
        sas_by_cycle={
            "11-12": "AIALANGA",
            "13-14": "AIALANGA",
            "15-16": "AIALANGA",
            "17-18": "AIALANGA",
            "17-20": "AIALANGA",
        },
        codes_by_cycle=ACASI_3LANG_CYCLES,
        target_by_cycle={
            "05-06": T_ALL,
            "07-08": T_ALL,
            "09-10": T_ALL,
            "11-12": T_ALL,
            "13-14": T_ALL,
            "15-16": T_8_69,
            "17-18": T_8_69,
            "17-20": T_8_69,
        },
        notes=(
            "AIALANG 2-cat through 09-10; AIALANGA 3-cat 11-12 through 17-20. "
            "Codebook Target: 12-59 (03-04), 0-150 (05-14), 8-69 (15-20). Not on 21-23."
        ),
        definition="Language of the MEC ACASI instrument.",
        definition_by_cycle={
            "03-04": "AIALANG 2-cat: 1=English; 2=Spanish. Target 12-59.",
            "05-06": "AIALANG 2-cat: 1=English; 2=Spanish.",
            "07-08": "AIALANG 2-cat: 1=English; 2=Spanish.",
            "09-10": "AIALANG 2-cat: 1=English; 2=Spanish.",
            "11-12": "AIALANGA 3-cat after Asian-language ACASI translations: 1=English; 2=Spanish; 3=Asian languages (Chinese traditional/simplified Mandarin, traditional Cantonese, Korean, Vietnamese).",
            "13-14": "AIALANGA 3-cat: 1=English; 2=Spanish; 3=Asian languages.",
            "15-16": "AIALANGA 3-cat: 1=English; 2=Spanish; 3=Asian languages. Target 8-69.",
            "17-18": "AIALANGA 3-cat: 1=English; 2=Spanish; 3=Asian languages. Target 8-69.",
            "17-20": "AIALANGA 3-cat: 1=English; 2=Spanish; 3=Asian languages. Target 8-69.",
        },
    ),
    "hhref_gender": _var(
        "hhref_gender", "DMDHRGND", "categorical",
        "Gender of the household reference person",
        T_ALL,
        codes=GENDER,
        target_by_cycle={
            "21-23": T_0_19,
        },
        notes=(
            "Not on 17-20 P_DEMO. 21-23 codebook restricts the public HH-ref "
            "person block to participants aged 0-19; adult HH-ref data are RDC-only."
        ),
        definition=(
            "Gender of the household reference person (first rostered household member "
            "18+ who owns or rents the residence). 1=Male; 2=Female."
        ),
    ),
    "hhref_age": _var(
        "hhref_age", "DMDHRAGE", "continuous",
        "Age in years of the household reference person at the time of HH screening. "
        "Continuous (topcoded 85, later 80) through 15-16. "
        "17-18 and 21-23 public files use 4-bin DMDHRAGZ; those bins are "
        "decoded to midpoint years 18/30/50/65 so the stacked column stays "
        "numeric and comparable. Not on 17-20 P_DEMO.",
        T_ALL,
        sas_by_cycle={"17-18": "DMDHRAGZ", "21-23": "DMDHRAGZ"},
        codes_by_cycle={"17-18": HHREF_AGE_COLLAPSED, "21-23": HHREF_AGE_COLLAPSED},
        raw_codes_by_cycle={"17-18": HHREF_AGE_BINS, "21-23": HHREF_AGE_BINS},
        target_by_cycle={
            "21-23": T_0_19,
        },
        notes=(
            "DMDHRAGZ codebook bins: 1=<20, 2=20-39, 3=40-59, 4=60+. "
            "HHREF_AGE_COLLAPSED assigns 18/30/50/65. That adds within-bin "
            "bias but keeps a discrete year comparable with DMDHRAGE. "
            "Original labels remain in HHREF_AGE_BINS / raw_codes_by_cycle. "
            "kind_for() still returns categorical for 17-18 and 21-23 so "
            "existing decode/encode behavior is unchanged."
        ),
        definition="Age of the household reference person at screening.",
        definition_by_cycle={
            "99-00": "Continuous DMDHRAGE; 85 = 85+.",
            "01-02": "Continuous DMDHRAGE; 85 = 85+.",
            "03-04": "Continuous DMDHRAGE; 85 = 85+.",
            "05-06": "Continuous DMDHRAGE; 85 = 85+.",
            "07-08": "Continuous DMDHRAGE; 80 = 80+.",
            "09-10": "Continuous DMDHRAGE; 80 = 80+.",
            "11-12": "Continuous DMDHRAGE; 80 = 80+.",
            "13-14": "Continuous DMDHRAGE; 80 = 80+.",
            "15-16": "Continuous DMDHRAGE; 80 = 80+.",
            "17-18": "DMDHRAGZ 4-bin disclosure recode: 1=<20; 2=20-39; 3=40-59; 4=60+. Catalog midpoints 18/30/50/65 are not NCHS values.",
            "21-23": "DMDHRAGZ 4-bin disclosure recode released only for SP aged 0-19: 1=<20; 2=20-39; 3=40-59; 4=60+. Catalog midpoints 18/30/50/65 are not NCHS values.",
        },
    ),
    "hhref_birth_country": _var(
        "hhref_birth_country", "DMDHRBRN", "categorical",
        "HH Ref Person Country of Birth",
        T_ALL,
        codes=BORN_3CAT,
        sas_by_cycle={
            "07-08": "DMDHRBR2",
            "09-10": "DMDHRBR2",
            "11-12": "DMDHRBR4",
            "13-14": "DMDHRBR4",
            "15-16": "DMDHRBR4",
        },
        codes_by_cycle={
            "07-08": BORN_4CAT,
            "09-10": BORN_4CAT,
            "11-12": BORN_2CAT,
            "13-14": BORN_2CAT,
            "15-16": BORN_2CAT,
        },
        notes=(
            "Same 3-cat / 4-cat / 2-cat generations as country_of_birth. "
            "NOT on 17-18 DEMO_J, 17-20 P_DEMO, or 21-23 DEMO_L. "
            "Those aliases were codebook mismatches and were removed."
        ),
        definition="Household reference person's country of birth. Same generation split as DMDBORN/2/4.",
        definition_by_cycle={
            "99-00": "DMDHRBRN 3-cat: 1=50 US states or DC; 2=Mexico; 3=elsewhere.",
            "01-02": "DMDHRBRN 3-cat: 1=50 US states or DC; 2=Mexico; 3=elsewhere.",
            "03-04": "DMDHRBRN 3-cat: 1=50 US states or DC; 2=Mexico; 3=elsewhere.",
            "05-06": "DMDHRBRN 3-cat: 1=50 US states or DC; 2=Mexico; 3=elsewhere.",
            "07-08": "DMDHRBR2 4-cat: 1=50 US states or DC; 2=Mexico; 4=other Spanish-speaking; 5=other non-Spanish-speaking. Code 3 unused placeholder.",
            "09-10": "DMDHRBR2 4-cat: 1=50 US states or DC; 2=Mexico; 4=other Spanish-speaking; 5=other non-Spanish-speaking. Code 3 unused placeholder.",
            "11-12": "DMDHRBR4 2-cat: 1=50 US states or DC; 2=born outside the US and DC.",
            "13-14": "DMDHRBR4 2-cat: 1=50 US states or DC; 2=born outside the US and DC.",
            "15-16": "DMDHRBR4 2-cat: 1=50 US states or DC; 2=born outside the US and DC.",
        },
    ),
    "hhref_educ": _var(
        "hhref_educ", "DMDHREDU", "categorical",
        "What is the highest grade or level of school {you have/NON_SP HEAD has} received?",
        T_ALL,
        codes=EDUC_ADULT,
        sas_by_cycle={"17-18": "DMDHREDZ", "21-23": "DMDHREDZ"},
        codes_by_cycle={"17-18": HHREF_EDUC_COLLAPSED, "21-23": HHREF_EDUC_COLLAPSED},
        target_by_cycle={
            "21-23": T_0_19,
        },
        notes="5-cat DMDHREDU through 15-16; 3-cat DMDHREDZ on 17-18 and 21-23. Not on 17-20.",
        definition="Education of the household reference person.",
        definition_by_cycle={
            "99-00": "DMDHREDU 5-cat adult education (same bins as DMDEDUC2).",
            "01-02": "DMDHREDU 5-cat adult education (same bins as DMDEDUC2).",
            "03-04": "DMDHREDU 5-cat adult education (same bins as DMDEDUC2).",
            "05-06": "DMDHREDU 5-cat adult education (same bins as DMDEDUC2).",
            "07-08": "DMDHREDU 5-cat adult education (same bins as DMDEDUC2).",
            "09-10": "DMDHREDU 5-cat adult education (same bins as DMDEDUC2).",
            "11-12": "DMDHREDU 5-cat adult education (same bins as DMDEDUC2).",
            "13-14": "DMDHREDU 5-cat adult education (same bins as DMDEDUC2).",
            "15-16": "DMDHREDU 5-cat adult education (same bins as DMDEDUC2).",
            "17-18": "DMDHREDZ 3-cat disclosure recode: 1=<HS; 2=HS grad/GED or some college/AA; 3=college graduate or above.",
            "21-23": "DMDHREDZ 3-cat disclosure recode released for SP 0-19: 1=<HS; 2=HS grad/GED or some college/AA; 3=college graduate or above.",
        },
    ),
    "hhref_marital": _var(
        "hhref_marital", "DMDHRMAR", "categorical",
        "Marital Status of household reference person",
        T_ALL,
        codes=MARITAL_DETAIL,
        sas_by_cycle={"17-18": "DMDHRMAZ", "21-23": "DMDHRMAZ"},
        codes_by_cycle={"17-18": MARITAL_COLLAPSED, "21-23": MARITAL_COLLAPSED},
        target_by_cycle={
            "21-23": T_0_19,
        },
        notes="6-cat DMDHRMAR through 15-16; 3-cat DMDHRMAZ on 17-18 and 21-23. Not on 17-20.",
        definition="Marital status of the household reference person.",
        definition_by_cycle={
            "99-00": "DMDHRMAR 6-cat (same bins as DMDMARTL).",
            "01-02": "DMDHRMAR 6-cat (same bins as DMDMARTL).",
            "03-04": "DMDHRMAR 6-cat (same bins as DMDMARTL).",
            "05-06": "DMDHRMAR 6-cat (same bins as DMDMARTL).",
            "07-08": "DMDHRMAR 6-cat (same bins as DMDMARTL).",
            "09-10": "DMDHRMAR 6-cat (same bins as DMDMARTL).",
            "11-12": "DMDHRMAR 6-cat (same bins as DMDMARTL).",
            "13-14": "DMDHRMAR 6-cat (same bins as DMDMARTL).",
            "15-16": "DMDHRMAR 6-cat (same bins as DMDMARTL).",
            "17-18": "DMDHRMAZ 3-cat: 1=married/living with partner; 2=widowed/divorced/separated; 3=never married.",
            "21-23": "DMDHRMAZ 3-cat released for SP 0-19: 1=married/living with partner; 2=widowed/divorced/separated; 3=never married.",
        },
    ),
    "hhref_spouse_educ": _var(
        "hhref_spouse_educ", "DMDHSEDU", "categorical",
        "What is the highest grade or level of school {you have/NON-SP SPOUSE has completed or the highest degree {you have/he/she has} received",
        T_ALL,
        codes=EDUC_ADULT,
        sas_by_cycle={"17-18": "DMDHSEDZ", "21-23": "DMDHSEDZ"},
        codes_by_cycle={"17-18": HHREF_EDUC_COLLAPSED, "21-23": HHREF_EDUC_COLLAPSED},
        target_by_cycle={
            "21-23": T_0_19,
        },
        notes="Same collapse pattern as hhref_educ. Not on 17-20.",
        definition="Education of the household reference person's spouse.",
        definition_by_cycle={
            "99-00": "DMDHSEDU 5-cat adult education (same bins as DMDEDUC2).",
            "01-02": "DMDHSEDU 5-cat adult education (same bins as DMDEDUC2).",
            "03-04": "DMDHSEDU 5-cat adult education (same bins as DMDEDUC2).",
            "05-06": "DMDHSEDU 5-cat adult education (same bins as DMDEDUC2).",
            "07-08": "DMDHSEDU 5-cat adult education (same bins as DMDEDUC2).",
            "09-10": "DMDHSEDU 5-cat adult education (same bins as DMDEDUC2).",
            "11-12": "DMDHSEDU 5-cat adult education (same bins as DMDEDUC2).",
            "13-14": "DMDHSEDU 5-cat adult education (same bins as DMDEDUC2).",
            "15-16": "DMDHSEDU 5-cat adult education (same bins as DMDEDUC2).",
            "17-18": "DMDHSEDZ 3-cat: 1=<HS; 2=HS grad/GED or some college/AA; 3=college graduate or above.",
            "21-23": "DMDHSEDZ 3-cat released for SP 0-19: 1=<HS; 2=HS grad/GED or some college/AA; 3=college graduate or above.",
        },
    ),
    "wt_interview": _var(
        "wt_interview", "WTINT2YR", "weight",
        "Interviewed Sample Persons.",
        T_ALL,
        sas_by_cycle={"17-20": "WTINTPRP"},
        notes="Use WTINTPRP for 17-20 pre-pandemic analyses. Do not mix with WTINT2YR without NCHS guidance.",
        definition="Full-sample interview weight. 17-20 uses the special pre-pandemic weight WTINTPRP.",
    ),
    "wt_exam": _var(
        "wt_exam", "WTMEC2YR", "weight",
        "Both Interviewed and MEC Examined Sample Persons.",
        T_ALL,
        sas_by_cycle={"17-20": "WTMECPRP"},
        notes="Use WTMECPRP for 17-20 pre-pandemic analyses.",
        definition="Full-sample MEC exam weight. 17-20 uses the special pre-pandemic weight WTMECPRP.",
    ),
    "wt_interview_4yr": _var(
        "wt_interview_4yr", "WTINT4YR", "weight",
        "Interviewed Sample Persons. Used for 1999-2002 data collection years only.",
        T_ALL,
        definition="4-year interview weight for combined 1999-2002 analyses only.",
    ),
    "wt_exam_4yr": _var(
        "wt_exam_4yr", "WTMEC4YR", "weight",
        "Both Interviewed and MEC Examined Sample Persons. Used for 1999-2002 data collection years only.",
        T_ALL,
        definition="4-year MEC exam weight for combined 1999-2002 analyses only.",
    ),
    "masked_psu": _var(
        "masked_psu", "SDMVPSU", "id",
        "Masked Variance Unit Pseudo-PSU variable for variance estimation",
        T_ALL,
        definition="Masked variance-unit pseudo-PSU. Use with SDMVSTRA for design-based variance.",
    ),
    "masked_stratum": _var(
        "masked_stratum", "SDMVSTRA", "id",
        "Masked Variance Unit Pseudo-Stratum variable for variance estimation",
        T_ALL,
        definition="Masked variance-unit pseudo-stratum. Use with SDMVPSU for design-based variance.",
    ),
}


def sas_name(spec: dict, cycle: str | None = None) -> str:
    if cycle and cycle in spec["sas_by_cycle"]:
        return spec["sas_by_cycle"][cycle]
    return spec["sas"]


def codes_for(spec: dict, cycle: str | None = None) -> dict | None:
    if cycle and cycle in spec["codes_by_cycle"]:
        return spec["codes_by_cycle"][cycle]
    return spec["codes"]


def raw_codes_for(spec: dict, cycle: str | None = None) -> dict | None:
    """Original codebook labels when codes_for() returns midpoints or recodes."""
    raw_by = spec.get("raw_codes_by_cycle") or {}
    if cycle and cycle in raw_by:
        return raw_by[cycle]
    if spec.get("raw_codes"):
        return spec["raw_codes"]
    return codes_for(spec, cycle)


def kind_for(spec: dict, cycle: str | None = None) -> str:
    if spec["short"] == "hhref_age" and cycle in {"17-18", "21-23"}:
        return "categorical"
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


# SAS_TO_SHORT = {}
# for spec in DEMO_VARS.values():
#     SAS_TO_SHORT[spec["sas"]] = spec["short"]
#     for alias in spec["sas_by_cycle"].values():
#         SAS_TO_SHORT[alias] = spec["short"]


SAS_TO_SHORT_DEMO = {}
for spec in DEMO_VARS.values():
    SAS_TO_SHORT_DEMO[spec["sas"]] = spec["short"]
    for alias in spec.get("sas_by_cycle", {}).values():
        SAS_TO_SHORT_DEMO[alias] = spec["short"]

DEMO_CATALOG = {
    "name": "demographics",
    "aliases": ("demo", "demographics", "demographic"),
    "vars": DEMO_VARS,
    "sas_to_short": SAS_TO_SHORT_DEMO,
    "grain": "person",
}