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
- condition_occurrence
- care_site
- procedure_occurrence (some hospitals only)
- visit_detail (some hospitals only)

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

- **Person**: One row per patient.
- **Visit occurrence**: One row per ICU admission.
- **Visit detail** (some hospitals only): Sub-stays within an admission — ICU stays and operating room episodes.
- **Care site**: Hospital lookup table.
- **Death**: In-hospital death records.
- **Measurement**: Vitals, labs, scores — the largest table.
- **Observation**: Subjective measurements.
- **Drug exposure**: Medication exposures.
- **Device exposure**: Device use records (LDA's)
- **Condition occurrence**: Diagnoses and conditions.
- **Procedure occurrence** (some hospitals only): Performed procedures.

---

## Tips for Working with the Data

### Data Standardization
- **Data quality**: Data in ICUdata has purposefully not been cleaned for outliers, artifacts, aberrations or distribution differences. It is up to the researcher to inspect the data carefully.
- **Concept Mappings**: ICUdata standardizes concepts, but units are not standardized. Always check the data distribution of underlying `..._source_values` to ensure consistency across `concept_ids`.
- **Missing Concepts**: The completeness of concept mapping currently varies per table. Some concepts may not be mapped yet. If you encounter missing data or are wondering about the presence of a certain variable, let projectteam@icudata.nl know so we can check the source data.
