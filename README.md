# ICUdata
Publieke repository van de Dutch ICU Data Warehouse (Stichting ICUdata), een project met als doel het centraliseren en standaardiseren van IC-data in Nederland. Bevat informatie en instructies voor deelnemende ziekenhuizen en databasegebruikers. Meedoen? Zie https://www.icudata.nl/icudata.

## Indeling van de repository

- `instructies/nl/` — Nederlandstalige instructies
  - `aan-de-slag.md` — hoe je toegang krijgt en de omgeving instelt
  - `database-uitleg.md` — overzicht van de databasestructuur, tabellen en querytips
  - `omop-uitleg.md` — uitleg van het OMOP CDM-formaat en alle tabellen
- `instructies/en/` — map met instructies in het Engels
- `releases/` — per release: release notes (`release-notes.md`: wat er nieuw is, in gewone taal), een changelog (`changelog.md`) en de volledige concept-dictionary (`dictionary.csv`, en per tabel in `dictionary/`) van die release, met alle concepten en statistieken (aantal rijen, aantal patiënten, patiëntdekking per ziekenhuis; aantallen onder de 10 patiënten worden niet getoond)
- [`concept_taxonomy.yaml`](releases/v0.3.0-2026-11-02/concept_taxonomy.yaml) — alle concepten van de huidige release (0.3.0), gegroepeerd naar de klinische vraag die ze beantwoorden (categorie, subcategorie, onderwerp), met hun OMOP `concept_id`-waarden; startpunt voor het bevragen van variabelen. Elke releasemap in `releases/` heeft zijn eigen versie; vóór 0.3.0 heette het bestand `common_concepts.yaml`.
- [`concept_taxonomy.md`](releases/v0.3.0-2026-11-02/concept_taxonomy.md) — dezelfde indeling als inklapbare pagina die je op GitHub kunt doorbladeren

---

# ICUdata
Public repository of the Dutch ICU Data Warehouse (Stichting ICUdata), a project aimed at centralizing and standardizing ICU data in the Netherlands. Contains information and instructions for participating hospitals and database users. Want to get involved? See https://www.icudata.nl/icudata.

## Repository layout

- `instructies/en/` — English instructions
  - `getting-started.md` — how to set up your environment and open the database
  - `database-guide.md` — overview of the database structure, tables, and query tips
  - `omop-explanation.md` — explanation of the OMOP CDM format and all tables
- `instructies/nl/` — folder with instructions in Dutch
- `releases/` — per release: release notes (`release-notes.md`: what is new, in plain language), a changelog (`changelog.md`) and that release's full concept dictionary (`dictionary.csv`, and per table in `dictionary/`), with all concepts and statistics (row counts, patient counts, patient coverage per hospital; numbers below 10 patients are not shown)
- [`concept_taxonomy.yaml`](releases/v0.3.0-2026-11-02/concept_taxonomy.yaml) — every concept of the current release (0.3.0), grouped by the clinical question it answers (category, subcategory, topic), with its OMOP `concept_id` values; a starting point for querying variables. Each release folder in `releases/` has its own version; before 0.3.0 the file was called `common_concepts.yaml`.
- [`concept_taxonomy.md`](releases/v0.3.0-2026-11-02/concept_taxonomy.md) — the same taxonomy as a collapsible page you can browse on GitHub
