# ICUdata
Publieke repository van de Dutch ICU Data Warehouse (Stichting ICUdata), een project met als doel het centraliseren en standaardiseren van IC-data in Nederland. Bevat informatie en instructies voor deelnemende ziekenhuizen en databasegebruikers. Meedoen? Zie https://www.icudata.nl/icudata.
<<<<<<< HEAD
=======

## Indeling van de repository

- `instructies/nl/` — Nederlandstalige instructies
  - `aan-de-slag.md` — hoe je toegang krijgt en de omgeving instelt
  - `database-uitleg.md` — overzicht van de databasestructuur, tabellen en querytips
  - `omop-uitleg.md` — uitleg van het OMOP CDM-formaat en alle tabellen
- `instructies/en/` — map met instructies in het Engels
- `releases/` — per release: een changelog (`CHANGELOG.md`) en de volledige concept-dictionary (`dictionary.csv`) van die release, met alle concepten en statistieken (aantal rijen, patiëntdekking per ziekenhuis)
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
- `releases/` — per release: a changelog (`CHANGELOG.md`) and that release's full concept dictionary (`dictionary.csv`), with all concepts and statistics (row counts, patient coverage per hospital, value distributions)
- `common_concepts.yaml` — maps clinical concept names to their OMOP `concept_id`s; can be used as a starting point for querying common variables
>>>>>>> 6d730b9dbf59d19ceb0ee7a6aba9026f994de816
