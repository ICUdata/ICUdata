# ICUdata Roadmap

This document outlines the planned development of the ICUdata database and its
surrounding tooling and documentation. It is a living document and is updated as
priorities shift.

For information about the database itself, see the
[Database Guide](instructies/en/database-guide.md).

> **Note:** Items and their timing are indicative. Nothing here is a firm
> commitment unless stated otherwise. Questions or suggestions?
> Email projectteam@icudata.nl.

_Last updated:_

---

## How to read this roadmap

The roadmap is split into four stages, ordered by how soon work is expected:

| Stage | Meaning |
|-------|---------|
| **In progress** | Actively being worked on right now. |
| **Soon** | Next up; expected to start in the near term. |
| **Later** | Planned, but not scheduled yet. |
| **Not yet planned** | Not scheduled and not yet detailed, but intended to be done in the future. |

Within each stage, items are grouped by the OMOP table they primarily affect.
Work that spans multiple tables — hospital onboarding, vocabulary mapping, or
structural changes — is grouped under descriptive headings instead.

Suggested format for each entry:

```
- Concise, action-oriented description of the change.
  (optional: owner, target version, or related link)
```

---

## In progress

_Work that is currently underway._

### Hospital onboarding & data sources

- Frisius MC parameter mapping
- OLVG parameter mapping
- Radboud UMC parameter mapping

---

## Soon

_Work expected to start in the near term._

### Hospital onboarding & data sources

- Add NICE registry data from the remaining hospitals
- Receive Amphia, LUMC & NWZ delivery  

### Vocabulary & concept mapping

- Unit `concept_id` mapping
- NICE registry concept standardization

### Visit occurrence

- `admitted_from_concept_id` and `discharged_to_concept_id` concept mapping

### Procedure occurrence 

- Add blood transfusion data

### Measurement

- `value_as_concept_id` mapping for common measurements
- Support for multi-select answers in HiX 
---

## Later

_Planned work that is not yet scheduled._

### Condition occurrence

- Include ICD-10 code registrations in `condition_occurrence` from Epic and HiX

### Drug exposure

- Route `concept_id` mapping

### Procedure occurrence

- Add procedures from Metavision
- Reroute boolean procedure registrations from the `measurement` table to `procedure_occurrence`
- Add procedures from Epic

### Measurement

- Overhaul fluid balance concepts
- Add microbiology results from Epic

### Cross-table & structural

- Separate validated and unvalidated data via `provider_id`

---

## Not yet planned

_Intended for the future, but not yet scheduled or detailed._

### Visit occurrence & visit detail

- Add a `provider_id` column to `visit_occurrence` and `visit_detail` to capture medical specialty
  - In OMOP, ICU specialty is best modelled as a provider linked to a visit. It is currently a concept in the `measurement` table; when the specialty changes during a `visit_occurrence`, two `visit_detail` rows are created.
- Add intra-visit transfers as visit details from Epic and Metavision

### Condition occurrence

- Add infection and isolation-status registrations from Epic
- Add daily ICU complication registrations from Metavision (OLVG and UMCU only)

### Drug exposure

- Add the `drug_strength` table
- Add the `dose_era` table
- Add the `drug_era` table
- Add outpatient medication from HiX
- Recover drug administration rate and dose units from Metavision

### Procedure occurrence

- Add surgery data from Epic and HiX 
- Add imaging, pathology, microbiology registration (not results) from HiX and Epic

### Measurement

- Add `range_low` and `range_high` columns to `measurement`
- Link measurements via `measurement_event_id`:
  - Blood pressure measurements
  - Measurements with multiple answers
- Add allergy data from Epic and HiX 

### Death

- Record death registration origin in `death_type_concept_id`

### Observation

- Add medical, surgical, family and social history from Epic
- Add code-status (DNR/CPR) registrations from Epic

---

## Recently completed

_Finished items, most recent first._
