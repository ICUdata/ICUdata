# What's in the DuckDB database

The database contains clinical data from the ICUs of nine Dutch hospital sources, standardized to the **OMOP CDM 5.4** format: AMC (`amc`), VUmc (`vumc`), Amsterdam UMC Epic (`aumc`), UMC Utrecht (`umcu`), Catharina Ziekenhuis Eindhoven (`cze`), OLVG (`olvg`), Frisius MC (`mcl`), Radboudumc (`radboud`) and Franciscus (`sfg`). OMOP is a common schema used in medical research so that data from different hospitals and EHR systems can be analyzed together.

Useful resources: [explore the OMOP schema visually](https://linkr.interhop.org/en/tools/omop-schema/) — [browse and search OMOP concepts (Athena)](https://athena.ohdsi.org/search-terms/start)

The core idea in OMOP is the **concept ID**: a universal integer that identifies a clinical concept — a drug, a measurement type, a diagnosis. Concept ID `8507` means "male" everywhere, regardless of what the source hospital called it. Every table also has **`_source_value` columns** that preserve the original text from the hospital system, so you can always see what the raw data actually said.

---

## Patient & visit tables

### `person`
One row per patient. Contains gender (`gender_concept_id`: 8507 = male, 8532 = female), date of birth, and `person_id` which is the key that links everything else together. The year of birth is accurate, but the date has been randomly generated.

### `visit_occurrence`
One row per visit. Contains start and end timestamps, the hospital (`care_site_id`, see `care_site`), where the patient came from and went to (`admitted_from_concept_id`, `discharged_to_concept_id`), and the medical specialty (`provider_id`). `visit_occurrence_id` is what all clinical data links back to in other tables.
Note that visit dates are generated based on the raw data delivered by the hospitals; as such, these might contain quality issues in a minor number of cases. It is recommended to check for overlapping/duplicated/split visits in your cohort.

### `visit_detail`
The stays within a visit: ward movements, including ICU stays. Examples of `visit_detail_concept_id`: 32037 (Intensive Care), 2001000015 (Medium care unit), 4021813 (Operating room). A visit can have several visit details, ordered by `preceding_visit_detail_id`. Every clinical table has a `visit_detail_id` that links a row to the stay it falls in. Available at all hospitals.

### `care_site`
The hospital lookup table: `care_site_id` and the hospital's name. To get the rows of one hospital, use its schema, for example `cze.measurement` (see [Schemas](#schemas)).

### `provider`
One row per medical specialty. `provider_id` is the specialty's concept id (`specialty_concept_id`); see [Specialty and validation](#specialty-and-validation-provider_id).

### `death`
One row per patient who died in-hospital. If a patient has no row here, they were not recorded as deceased. The follow-up period for death differs per institution.

---

## Clinical data tables

All of these link to `visit_occurrence` via `visit_occurrence_id`, to the stay in `visit_detail` via `visit_detail_id`, and to the patient via `person_id`.

### `measurement`
The largest table. One row per recorded clinical value — vitals, lab results, scores. `measurement_source_value` is the original parameter name from the hospital system. `value_as_number` is the value. `unit_source_value` is the unit, and `unit_concept_id` the unit as a standard concept. A coded answer is in `value_as_concept_id`.
To find results of a specific clinical concept, gather the relevant concept_id from the dictionary, and query using this id to aggregate all standardized measurement_source_values for that concept. Note that some procedures and devices also live here as starting and ending times.

### `observation`
Same structure as `measurement`, but for parameters that don't fit neatly into the measurement domain — categorical scores, flags, and similar data represented as numbers. Whether a concept lives here or in measurement can be found in the dictionary. Contains a relatively small number of records compared to `measurement`.

### `drug_exposure`
One row per medication administration. Contains the drug name (`drug_source_value`), start and end times, quantity, route (`route_concept_id`), and dose unit. Oral and IV doses have been converted to mg, but some administration routes do not contain ingredient-level dosage information. There is no `drug_strength` table; instead, the total quantity administered during the exposure is stored in the `quantity` column. The rate is assumed to be stable throughout the exposure — if the rate changes, a new exposure record is created.
**Known issue in 0.3.0:** at the hospitals on Metavision, `quantity` of an infusion holds the rate per minute, not the amount given.

### `procedure_occurrence`
One row per performed procedure, including operations and procedures recorded as yes/no. Contains start and end times, what was done (`procedure_source_value`), and how many times (`quantity`). For surgeries, the incision time and end time can be found here. Available at all hospitals. If specific concepts are needed, contact projectteam@icudata.nl.

### `condition_occurrence`
One row per recorded diagnosis or condition, at all hospitals. Contains what the condition was (`condition_source_value`, the hospital's parameter name) and when it was active. Most conditions are mapped to SNOMED `concept_id` values. Admission diagnoses have `condition_status_concept_id` 32890 (Admission diagnosis).

### `device_exposure`
One row per device use — ventilators, catheters, lines. Contains the device name (`device_source_value`) and the period it was in use. End date is optional (some devices have no recorded removal time). `quantity` and `unit_source_value` give the amount, for example for blood transfusions.
`visit_occurrence_id`s are matched based on starting times; thus, many device_exposures do not have a `visit_occurrence_id`, as they are started before the ICU admission.

---

## Record-type codes

Each clinical row says where it comes from, in its `*_type_concept_id` column:

| Code | Meaning | Used in |
|------|---------|---------|
| 32817 | EHR | measurement, observation, condition_occurrence, procedure_occurrence, device_exposure, death |
| 32818 | EHR administration record | drug_exposure (all rows), device_exposure (blood transfusions) |
| 32823 | EHR discharge record | death |
| 32827 | EHR encounter record | visit_occurrence, visit_detail |
| 32833 | EHR order | procedure_occurrence (Epic orders) |
| 32856 | Lab | measurement and observation (lab results) |
| 32879 | Registry | the NICE registry data |

## Specialty and validation (`provider_id`)

- On visits and on clinical rows, `provider_id` is the medical specialty: the specialty's concept id, as in the `provider` table. 0 means the specialty is not known.
- In `measurement` and `observation`, `provider_id` also shows whether a value was validated: NULL means nobody validated it (for example a value a monitor filed automatically); any other value, including 0, means validated. A NICE item from the NICE registry counts as validated (0); the same item from the hospital's own system has NULL.

---

## How the tables relate

```
care_site ──── visit_occurrence ──── person ──── death
                 │        │
           visit_detail   provider (provider_id)
                 │
         ┌───────┴────────┐
    measurement      observation
    drug_exposure    procedure_occurrence
    condition_occurrence
    device_exposure
```

Every clinical row belongs to a `visit_occurrence` and, where known, to a stay in `visit_detail`; the visit belongs to a `person` at a `care_site`.

---

## Schemas

The database file has several schemas:

- `omop.*` — the tables to use: all hospitals together, without a `hospital` column. Also `source_to_concept_map`, `cdm_source` and `dictionary`.
- `amc.*`, `aumc.*`, `cze.*`, `mcl.*`, `olvg.*`, `radboud.*`, `sfg.*`, `umcu.*`, `vumc.*` — the same tables for one hospital.
- `icudata.*` — the same tables with a `hospital` column, plus bookkeeping (not clinical data):
  - `icudata.version` — the versions of the database and when they were built
  - `icudata.changelog` — the changes between versions
  - `icudata.mapping_edges` — which source parameter maps to which concept, per hospital and table
- `dictionary.*` — the data dictionary, one table per OMOP table; `omop.dictionary` combines them.

---

## Less relevant tables

These are standard OMOP vocabulary tables. They are rarely needed for analysis but are included for completeness.

- `source_to_concept_map` — contains all mappings from source values to `concept_id` values; useful for quickly checking what a source value is mapped to
- `cdm_source` — version information about the database, including CDM version and vocabulary version
- `concept` — large table containing all concepts across all vocabularies; not practical for looking up concepts, but occasionally useful for joining
- `concept_ancestor` — hierarchy table that links concepts to their higher-level ancestors in vocabularies that support it; in ICUdata, only SNOMED currently supports this. Additionally, through `concept_relationship` mappings between RxNorm and SNOMED, higher-level drug concepts can also be found.
- `concept_class` — classifies concepts within a vocabulary (e.g. "Clinical Finding", "Drug")
- `concept_relationship` — standardized mappings between concepts across vocabularies
- `concept_synonym` — alternative names and synonyms for concepts
- `domain` — defines the clinical domain each concept belongs to (e.g. Measurement, Drug, Condition)
- `relationship` — defines the types of relationships used in `concept_relationship`
- `vocabulary` — lists all vocabularies present in the database (e.g. SNOMED, LOINC, RxNorm)
