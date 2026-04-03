# ICUdata
Publieke repository van de Dutch ICU Data Warehouse (Stichting ICUdata), een project met als doel het centraliseren en standaardiseren van IC-data in Nederland. Bevat informatie en instructies voor deelnemende ziekenhuizen en databasegebruikers. Meedoen? Zie https://www.icudata.nl/icudata.

## Indeling van de repository

- `instructies/nl/` — Nederlandstalige instructies
  - `getting-started.md` — hoe je de omgeving instelt en de database opent
  - `database-guide.md` — overzicht van de databasestructuur, tabellen en querytips
  - `omop-explanation.md` — uitleg van het OMOP CDM-formaat en alle tabellen
- `instructies/en/` — map met instructies in het Engels
- `dictionary.csv` — overzicht van alle concepten in de database, inclusief statistieken (aantal rijen, patiëntdekking per ziekenhuis)
- `common_concepts.yaml` — koppeling van klinische conceptnamen aan hun OMOP `concept_id`s; kan worden gebruikt als startpunt voor het bevragen van veelgebruikte variabelen

---

# ICUdata
Public repository of the Dutch ICU Data Warehouse (Stichting ICUdata), a project aimed at centralizing and standardizing ICU data in the Netherlands. Contains information and instructions for participating hospitals and database users. Want to get involved? See https://www.icudata.nl/icudata.

## Repository layout

- `instructies/en/` — English instructions
  - `getting-started.md` — how to set up your environment and open the database
  - `database-guide.md` — overview of the database structure, tables, and query tips
  - `omop-explanation.md` — explanation of the OMOP CDM format and all tables
- `instructies/nl/` — folder with instructions in Dutch
- `dictionary.csv` — overview of all concepts in the database, including statistics (row counts, patient coverage per hospital, value distributions)
- `common_concepts.yaml` — maps clinical concept names to their OMOP `concept_id`s; can be used as a starting point for querying common variables
