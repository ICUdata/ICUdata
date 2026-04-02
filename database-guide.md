# Database Guide

This guide covers the structure of the ICUdata database, how to query it, and tips for working with the data.

For setting up your environment, see [Getting Started](getting-started.md).

---

## Overview

The database is a DuckDB database, located in /home/ICUData. It is a read-only database to prevent accidental changes. To modify the data, you can read it into scripts and modify it there, save it in your own folder, etc.

The database can be queried using standard SQL, with slight variations due to DuckDB syntax. Converting from other SQL-languages to DuckDB using LLMs usually works well. Tables are prefixed with `icudata`.

---

## Accessing the Database

### Terminal access
- Use `harlequin /home/ICUData/ICUdata<version> -readonly` for a terminal overview that shows the database structure clearly.
- Use `duckdb /home/ICUData/ICUdata<version> -readonly` for faster queries.

### Script access
- In Python or R scripts, import the DuckDB library to interact with the database. DuckDB has excellent synergy with Pandas DataFrames, allowing you to query DataFrames directly and convert them efficiently. Refer to the [DuckDB documentation](https://duckdb.org/docs) for more details.

---

## Format

The database has an OMOP-CDM format (see more here: https://ohdsi.github.io/CommonDataModel/cdm54.html).

Data tables:
- person
- death
- visit_occurrence
- measurement
- observation
- drug_exposure
- device_exposure
- condition_occurrence (no longer HiX only — has sources from VUMC, AMC, AUMC, OLVG, UMCU, and CZE)
- care_site
- procedure_occurrence (HiX only)
- visit_detail (HiX only)

Standard/vocabulary tables:
- concept (concept_id above 2,000,000,000 are custom ICUdata concepts)
- concept_relationship
- concept_ancestor
- concept_class
- concept_synonym
- vocabulary
- domain
- relationship
- cdm_source
- source_to_concept_map

### Utility Tables

In addition to the data and vocabulary tables listed above, the following tables provide metadata about the database itself:

- `**icudata.version**`: Contains the latest version information.
- `**icudata.changelog**`: Provides metadata on changes per version, including row counts, hospitals added, columns added, and schema changes.
- `**icudata.dictionary**`: Contains a dictionary of all used concepts in the database, including patient coverage (per-hospital).

---

## Querying Tips

- Use `SUMMARIZE SELECT * FROM icudata.<TABLE>` to get an overview of a table. The table can be specified with filters in the query too.
- Use `DESCRIBE SELECT * FROM icudata.<TABLE>` to view the schema.
- To query data for a specific hospital, you can use the hospital's schema prefix instead of `icudata`. For example, `SELECT * FROM vumc.measurement` queries only VUMC data. Each hospital has its own schema with the same table structure.

---

## Table-Specific Details

**Disclaimer:** The database is continuously updating, so the information below may become outdated.

- **Visit occurrence**: Contains data on ICU visits.
- **Device and Procedure Tables**: Currently contains few concepts, depending on the EHR and hospital, but can be useful for intubation timing for some hospitals. If specific concepts are needed, contact projectteam@icudata.nl
- **Measurement Table**: Contains most of the data. Some procedures and devices live here as starting and ending times.
- **Observations**: Contains a very small amount of observations.
- **Visit detail** (HiX only): Contains data on transfers to operating room as well as copies of visit_occurrences
- **Death**: Contains death records. It varies per hospital whether deaths outside ICU or outside hospital and up to how far these are recorded.
- **Condition_occurrence**: Contains aggregated custom concepts for Metavision and Epic, and SNOMED terms mapped from ICD-10 concepts for HiX. Now includes sources from VUMC, AMC, AUMC, OLVG, UMCU, and CZE.
- **Drug exposure**: Oral and IV doses have been converted to mg, but some administration routes do not contain ingredient-level dosage information
- **Care site**: Shows all hospitals currently with data in ICUdata.
- **CDM source**: Contains version information about the database, including CDM version and vocabulary version.
- **Source to concept map**: Contains the mappings used to map source values to standard OMOP concepts.

---

## Tips for Working with the Data

### Data Standardization
- **Data quality**: Data in ICUdata has purposefully not been cleaned for outliers, artifacts, aberrations or distribution differences. It is up to the researcher to inspect the data carefully.
- **Concept Mappings**: ICUdata standardizes concepts, but units are not standardized. Always check the data distribution of underlying `..._source_values` to ensure consistency across `concept_ids`.
- **Missing Concepts**: The completeness of concept mapping currently varies per table. Some concepts may not be mapped yet. If you encounter missing data or are wondering about the presence of a certain variable, let projectteam@icudata.nl know so we can check the source data.
