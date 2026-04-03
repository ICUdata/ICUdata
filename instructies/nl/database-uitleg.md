# Database handleiding

Deze handleiding beschrijft de structuur van de ICUdata-database, hoe je queries uitvoert en tips voor het werken met de data.

Voor het opzetten van je omgeving, zie [Aan de slag](getting-started.md).

---

## Overzicht

De database is een DuckDB-database, te vinden in /home/ICUData. Het is een alleen-lezen database om onbedoelde wijzigingen te voorkomen. Om de data te bewerken kun je deze inlezen in scripts en daar aanpassen, opslaan in je eigen map, etc.

De database kan worden gequeryed met standaard SQL, met kleine variaties door DuckDB-syntax. Het omzetten van andere SQL-talen naar DuckDB met behulp van LLMs werkt over het algemeen goed. Tabellen hebben het prefix `icudata`.

---

## Toegang tot de database

### Terminaltoegang
- Gebruik `harlequin /home/ICUData/ICUdata<versie> -readonly` voor een terminaloverzicht dat de databasestructuur duidelijk weergeeft.
- Gebruik `duckdb /home/ICUData/ICUdata<versie> -readonly` voor snellere queries.

### Scripttoegang
- Importeer in Python- of R-scripts de DuckDB-bibliotheek om met de database te werken. DuckDB heeft uitstekende integratie met Pandas DataFrames, waardoor je DataFrames direct kunt bevragen en efficiënt kunt converteren. Zie de [DuckDB-documentatie](https://duckdb.org/docs) voor meer informatie.

---

## Formaat

De database heeft een OMOP-CDM-formaat (zie meer hier: https://ohdsi.github.io/CommonDataModel/cdm54.html).

Datatabellen:
- person
- death
- visit_occurrence
- measurement
- observation
- drug_exposure
- device_exposure
- condition_occurrence
- care_site
- procedure_occurrence (alleen bepaalde ziekenhuizen)
- visit_detail (alleen bepaalde ziekenhuizen)

Standaard-/vocabulairetabellen:
- concept (concept_id boven 2.000.000.000 zijn aangepaste ICUdata-concepten)
- concept_relationship
- concept_ancestor
- concept_class
- concept_synonym
- vocabulary
- domain
- relationship
- cdm_source
- source_to_concept_map

### Hulptabellen

Naast de data- en vocabulairetabellen hierboven, bieden de volgende tabellen metadata over de database zelf:

- `**icudata.version**`: Bevat de laatste versie-informatie.
- `**icudata.changelog**`: Bevat metadata over wijzigingen per versie, waaronder rijaantallen, toegevoegde ziekenhuizen, toegevoegde kolommen en schemawijzigingen.
- `**icudata.dictionary**`: Bevat een woordenboek van alle gebruikte concepten in de database, inclusief patiëntdekking (per ziekenhuis).

---

## Querytips

- Gebruik `SUMMARIZE SELECT * FROM icudata.<TABEL>` voor een overzicht van een tabel. De tabel kan ook worden gespecificeerd met filters in de query.
- Gebruik `DESCRIBE SELECT * FROM icudata.<TABEL>` om het schema te bekijken.
- Om data voor een specifiek ziekenhuis op te vragen, kun je het schemaprefix van het ziekenhuis gebruiken in plaats van `icudata`. Bijvoorbeeld: `SELECT * FROM vumc.measurement` bevraagt alleen VUMC-data. Elk ziekenhuis heeft een eigen schema met dezelfde tabelstructuur.

---

## Tabelspecifieke details

**Disclaimer:** De database wordt continu bijgewerkt, dus onderstaande informatie kan verouderd raken.

- **Person**: Één rij per patiënt.
- **Visit occurrence**: Één rij per IC-opname.
- **Visit detail** (alleen bepaalde ziekenhuizen): IC-verblijven en OK-episodes.
- **Care site**: Lijst van ziekenhuizen.
- **Death**: Overlijdensregistraties in het ziekenhuis.
- **Measurement**: Vitale functies, laboratoriumuitslagen, scores, etc - de grootste tabel.
- **Observation**: Indirecte meetinstrumenten.
- **Drug exposure**: Medicatietoedieningen.
- **Device exposure**: LDA's
- **Condition occurrence**: Diagnoses en aandoeningen.
- **Procedure occurrence** (alleen bepaalde ziekenhuizen): Uitgevoerde procedures.

---

## Tips voor het werken met de data

### Datastandardisatie
- **Datakwaliteit**: Data in ICUdata is bewust niet opgeschoond voor extreme waarden, artefacten, afwijkingen of distributieverschillen. Het is aan de onderzoeker om de data zorgvuldig te inspecteren.
- **Conceptmappings**: ICUdata standaardiseert concepten, maar eenheden zijn niet gestandaardiseerd. Controleer altijd de datadistributie van onderliggende `..._source_values` om consistentie over `concept_ids` te waarborgen.
- **Ontbrekende concepten**: De volledigheid van conceptmapping varieert momenteel per tabel. Sommige concepten zijn mogelijk nog niet gemapt. Als je ontbrekende data tegenkomt of je afvraagt of een bepaalde variabele aanwezig is, laat het projectteam@icudata.nl weten zodat we de brondata kunnen controleren.
