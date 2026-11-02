# ICUdata
Publieke repository van de Dutch ICU Data Warehouse (Stichting ICUdata), een project met als doel het centraliseren en standaardiseren van IC-data in Nederland. Bevat informatie en instructies voor deelnemende ziekenhuizen en databasegebruikers. Meedoen? Zie https://www.icudata.nl/icudata.

## Indeling van de repository

- `instructies/nl/` — Nederlandstalige instructies; begin bij [`aan-de-slag.md`](instructies/nl/aan-de-slag.md), het overzicht in leesvolgorde
  - [`01-toegang.md`](instructies/nl/01-toegang.md) — toegang krijgen: MyDRE-account en onderzoeksaanvraag
  - [`02-starten-en-inloggen.md`](instructies/nl/02-starten-en-inloggen.md) — de Linux VM starten en inloggen
  - [`03-werkomgeving.md`](instructies/nl/03-werkomgeving.md) — werken op de Linux VM: VSCode, Python, R en applicaties
  - [`04-netwerk-en-github.md`](instructies/nl/04-netwerk-en-github.md) — netwerkbeperkingen, GitHub-toegang, applicaties aanvragen
  - [`05-windows-vm-en-ssh.md`](instructies/nl/05-windows-vm-en-ssh.md) — alleen als je de Windows VM nodig hebt
  - [`database-uitleg.md`](instructies/nl/database-uitleg.md) — overzicht van de databasestructuur, tabellen en querytips
  - [`omop-uitleg.md`](instructies/nl/omop-uitleg.md) — uitleg van het OMOP CDM-formaat en alle tabellen
- `instructies/en/` — map met instructies in het Engels
- `releases/` — per release: release notes (`release-notes.md`: wat er nieuw is, in gewone taal), een changelog (`changelog.md`) en de volledige concept-dictionary (`dictionary.csv`, en per tabel in `dictionary/`) van die release, met alle concepten en statistieken (aantal rijen, aantal patiënten, patiëntdekking per ziekenhuis; aantallen onder de 10 patiënten worden niet getoond)
- [`concept_taxonomy.yaml`](releases/v0.3.0-2026-11-02/concept_taxonomy.yaml) — alle concepten van de huidige release (0.3.0), gegroepeerd naar de klinische vraag die ze beantwoorden (categorie, subcategorie, onderwerp), met hun OMOP `concept_id`-waarden; startpunt voor het bevragen van variabelen. Elke releasemap in `releases/` heeft zijn eigen versie; vóór 0.3.0 heette het bestand `common_concepts.yaml`.
- [`concept_taxonomy.md`](releases/v0.3.0-2026-11-02/concept_taxonomy.md) — dezelfde indeling als inklapbare pagina die je op GitHub kunt doorbladeren

---

# ICUdata
Public repository of the Dutch ICU Data Warehouse (Stichting ICUdata), a project aimed at centralizing and standardizing ICU data in the Netherlands. Contains information and instructions for participating hospitals and database users. Want to get involved? See https://www.icudata.nl/icudata.

## Repository layout

- `instructies/en/` — English instructions; start at [`getting-started.md`](instructies/en/getting-started.md), the list of guides in reading order
  - [`01-access.md`](instructies/en/01-access.md) — gaining access: MyDRE account and research request
  - [`02-start-and-log-in.md`](instructies/en/02-start-and-log-in.md) — start the Linux VM and log in
  - [`03-working-environment.md`](instructies/en/03-working-environment.md) — working on the Linux VM: VSCode, Python, R and applications
  - [`04-network-and-github.md`](instructies/en/04-network-and-github.md) — network restrictions, GitHub access, requesting applications
  - [`05-windows-vm-and-ssh.md`](instructies/en/05-windows-vm-and-ssh.md) — only if you need the Windows VM
  - [`database-guide.md`](instructies/en/database-guide.md) — overview of the database structure, tables, and query tips
  - [`omop-explanation.md`](instructies/en/omop-explanation.md) — explanation of the OMOP CDM format and all tables
- `instructies/nl/` — folder with instructions in Dutch
- `releases/` — per release: release notes (`release-notes.md`: what is new, in plain language), a changelog (`changelog.md`) and that release's full concept dictionary (`dictionary.csv`, and per table in `dictionary/`), with all concepts and statistics (row counts, patient counts, patient coverage per hospital; numbers below 10 patients are not shown)
- [`concept_taxonomy.yaml`](releases/v0.3.0-2026-11-02/concept_taxonomy.yaml) — every concept of the current release (0.3.0), grouped by the clinical question it answers (category, subcategory, topic), with its OMOP `concept_id` values; a starting point for querying variables. Each release folder in `releases/` has its own version; before 0.3.0 the file was called `common_concepts.yaml`.
- [`concept_taxonomy.md`](releases/v0.3.0-2026-11-02/concept_taxonomy.md) — the same taxonomy as a collapsible page you can browse on GitHub
