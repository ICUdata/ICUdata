# ICUdata – Dutch ICU Data Warehouse: metadata

The Dutch ICU Data Warehouse (Stichting ICUdata) centralises and standardises routinely recorded intensive care data
from participating Dutch hospitals.

| | |
|---|---|
| Persistent identifier | TODO: DOI from Zenodo (https://doi.org/10.5281/zenodo.XXXXXXX) |
| Data holder | Stichting ICUdata |
| Contact | projectteam@icudata.nl |
| Website | https://www.icudata.nl/metadata |

## Inclusion criteria
TODO (ICUdata board)

## Exclusion criteria
TODO (ICUdata board)

## Frequency of data collection
TODO (ICUdata board), e.g. how often hospitals deliver data and how often a new release is published.

## Data standard
The data are stored in the OMOP Common Data Model v5.4, using the standard vocabularies SNOMED CT, LOINC, RxNorm and UCUM.
Concepts with a concept_id of 2,000,000,000 or higher are custom ICUdata concepts.

## Codebook
Every release folder in [`releases/`](../releases/) contains the codebook (`dictionary.csv`): all recorded variables,
each with a resolvable identifier (`concept_uri`, `source_uri`). Custom ICUdata concepts are listed in
[`concepts/icudata_concepts.md`](../concepts/icudata_concepts.md).

## Access and terms of use
The data are not openly available. See [ACCESS.md](../ACCESS.md) for the access procedure and conditions,
and [LICENSE](../LICENSE) for the licence of this metadata and codebook.

## Long-term availability of the metadata
This metadata and the codebook are archived in Zenodo under the DOI above, so they remain available
even when the data themselves are no longer available.
