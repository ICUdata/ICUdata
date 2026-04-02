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
- condition_occurrence (niet langer alleen HiX — heeft bronnen van VUMC, AMC, AUMC, OLVG, UMCU en CZE)
- care_site
- procedure_occurrence (alleen HiX)
- visit_detail (alleen HiX)

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

- **Visit occurrence**: Bevat data over IC-opnames.
- **Device- en Procedure-tabellen**: Bevat momenteel weinig concepten, afhankelijk van het EPD en het ziekenhuis, maar kan nuttig zijn voor intubatietijden bij sommige ziekenhuizen. Als specifieke concepten nodig zijn, neem contact op met projectteam@icudata.nl.
- **Measurement-tabel**: Bevat het grootste deel van de data. Sommige procedures en apparaten staan hier als begin- en eindtijden.
- **Observations**: Bevat een zeer klein aantal observaties.
- **Visit detail** (alleen HiX): Bevat data over overplaatsingen naar de operatiekamer en kopieën van visit_occurrences.
- **Death**: Bevat overlijdensregistraties. Het varieert per ziekenhuis of overlijdens buiten de IC of buiten het ziekenhuis worden geregistreerd en tot hoe ver.
- **Condition_occurrence**: Bevat geaggregeerde aangepaste concepten voor Metavision en Epic, en SNOMED-termen gemapt vanuit ICD-10-concepten voor HiX. Bevat nu bronnen van VUMC, AMC, AUMC, OLVG, UMCU en CZE.
- **Drug exposure**: Orale en IV-doseringen zijn omgezet naar mg, maar sommige toedieningsroutes bevatten geen doseerinformatie op ingrediëntniveau.
- **Care site**: Toont alle ziekenhuizen die momenteel data hebben in ICUdata.
- **CDM source**: Bevat versie-informatie over de database, waaronder de CDM-versie en vocabulaireversie.
- **Source to concept map**: Bevat de mappings die gebruikt zijn om bronwaarden te mappen naar standaard OMOP-concepten.

---

## Tips voor het werken met de data

### Datastandardisatie
- **Datakwaliteit**: Data in ICUdata is bewust niet opgeschoond voor extreme waarden, artefacten, afwijkingen of distributieverschillen. Het is aan de onderzoeker om de data zorgvuldig te inspecteren.
- **Conceptmappings**: ICUdata standaardiseert concepten, maar eenheden zijn niet gestandaardiseerd. Controleer altijd de datadistributie van onderliggende `..._source_values` om consistentie over `concept_ids` te waarborgen.
- **Ontbrekende concepten**: De volledigheid van conceptmapping varieert momenteel per tabel. Sommige concepten zijn mogelijk nog niet gemapt. Als je ontbrekende data tegenkomt of je afvraagt of een bepaalde variabele aanwezig is, laat het projectteam@icudata.nl weten zodat we de brondata kunnen controleren.
