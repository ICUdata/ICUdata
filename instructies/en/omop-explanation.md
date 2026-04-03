# What's in the DuckDB database

The database contains clinical data from Dutch ICU hospitals (AMC, VUMC, AUMC, UMCU, CZE, OLVG), standardized to the **OMOP CDM 5.4** format. OMOP is a common schema used in medical research so that data from different hospitals and EHR systems can be analyzed together.

The core idea in OMOP is the **concept ID**: a universal integer that identifies a clinical concept — a drug, a measurement type, a diagnosis. Concept ID `8507` means "male" everywhere, regardless of what the source hospital called it. Every table also has **`_source_value` columns** that preserve the original text from the hospital system, so you can always see what the raw data actually said.

---

## Patient & visit tables

### `person`
One row per patient. Contains gender (`gender_concept_id`: 8507 = male, 8532 = female), date of birth, and `person_id` which is the key that links everything else together. The year of birth is accurate, but the date has been randomly generated.

### `visit_occurrence`
One row per ICU admission. Contains admission and discharge timestamps, the hospital (`care_site_id`, of which the related hospital can be found in the `care_site` table), and what location the patient was admitted from / discharged to.
`visit_occurrence_id` is what all clinical data links back to in other tables. Note that visit_occurrence dates are generated based on the raw data delivered by the hospitals; as such, these might also contain quality issues in a minor number of cases. It is recommended to check for overlapping/duplicated/split visits in your cohort.

### `visit_detail` (Certain hospitals only)
Sub-stays within an admission — ICU stays (`visit_detail_concept_id` = 32037) and operating room episodes (4021813). A single admission can have multiple visit details, ordered by `preceding_visit_detail_id`.
The ICU stays are duplicates of the visit_occurrence, thus this table is only useful for operating room episodes. The operating specialty has been appended to the name of the surgery in the `visit_source_value`. The timestamps contain information on the entrance and exit of the operating room.

### `care_site`
The hospital lookup table. `care_site_id` maps to: 1 = AMC, 2 = VUMC, 3 = AUMC, 4 = UMCU, 6 = CZE, 8 = OLVG. Through joining the visit_occurrence table on the visit_occurrence_id of a table or on the person_id plus a date, the care_site of all rows can be extracted. Specific rows of one institution can also be found through querying using the "hospital.table" format.

### `death`
One row per patient who died in-hospital. If a patient has no row here, they were not recorded as deceased. The follow-up period for death differs per institution.

---

## Clinical data tables

All of these link to `visit_occurrence` via `visit_occurrence_id`, and to the patient via `person_id`.

### `measurement`
The largest table. One row per recorded clinical value — vitals, lab results, scores. `measurement_source_value` is the original parameter name from the hospital system. `value_as_number` is the value. `unit_source_value` is the unit.
To find results of a specific clinical concept, gather the relevant concept_id from the dictionary, and query using this id to aggregate all standardized measurement_source_values for that concept. Note that some procedures and devices also live here as starting and ending times.

### `observation`
Same structure as `measurement`, but for parameters that don't fit neatly into the measurement domain — categorical scores, flags, and similar data represented as numbers. Whether a concept lives here or in measurement can be found in the dictionary. Contains a relatively small number of records compared to `measurement`.

### `drug_exposure`
One row per medication exposure. Contains the drug name (`drug_source_value`), start and end times, quantity, route, and dose unit. Oral and IV doses have been converted to mg, but some administration routes do not contain ingredient-level dosage information.

### `procedure_occurrence` (Certain hospitals only)
One row per performed procedure. Contains start and end times, what was done (`procedure_source_value`), and how many times (`quantity`). For surgeries, the incision time and end time can be found here. Currently contains few concepts depending on the hospital, but can be useful for intubation timing. If specific concepts are needed, contact projectteam@icudata.nl.

### `condition_occurrence`
One row per recorded diagnosis or condition. Contains what the condition was (`condition_source_value`) and when it was active. Available for HiX hospitals. For some hospitals, conditions have been mapped to SNOMED `concept_id`s. For the Amsterdam UMC hospitals (AMC, VUMC, AUMC), the table contains aggregated custom concepts; these live in the `measurement_source_value` column.

### `device_exposure`
One row per device use — ventilators, catheters, lines. Contains the device name (`device_source_value`) and the period it was in use. End date is optional (some devices have no recorded removal time).
`visit_occurrence_id`s are matched based on starting times; thus, many device_exposures do not have a `visit_occurrence_id`, as they are started pre-ICU admission.

---

## How the tables relate

```
care_site ──────────────── visit_occurrence ─────────── person
                                  │                        │
                                  │                      death
                                  │
                          ┌───────┴────────┐
                     measurement      observation
                     drug_exposure    procedure_occurrence
                     condition_occurrence
                     device_exposure
```

Every clinical row belongs to a `visit_occurrence`, which belongs to a `person` at a `care_site`.

---

## Internal metadata tables

The database also contains tables used for version tracking (not clinical data):

- `icudata.version` — records when the database was last updated and what data was included
- `icudata.changelog` — log of changes between updates (hospitals or tables added/removed, row count changes)
- `icudata.dictionary` — concept ID to parameter name mappings
