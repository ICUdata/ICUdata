# Inhoud database

De database bevat klinische data van de Intensive Care's van negen Nederlandse ziekenhuisbronnen, gestandaardiseerd naar het **OMOP CDM 5.4**-formaat: AMC (`amc`), VUmc (`vumc`), Amsterdam UMC Epic (`aumc`), UMC Utrecht (`umcu`), Catharina Ziekenhuis Eindhoven (`cze`), OLVG (`olvg`), Frisius MC (`mcl`), Radboudumc (`radboud`) en Franciscus (`sfg`). OMOP is een veelgebruikt schema in medisch onderzoek, zodat data van verschillende ziekenhuizen en EPD-systemen samen geanalyseerd kan worden.

Handige links: [OMOP-schema visueel verkennen](https://linkr.interhop.org/en/tools/omop-schema/) — [OMOP-concepten opzoeken en doorzoeken (Athena)](https://athena.ohdsi.org/search-terms/start)

Het centrale concept in OMOP is de **concept ID**: een universeel getal dat een klinisch begrip identificeert — een medicijn, een meettype, een diagnose. Concept ID `8507` betekent overal "mannelijk", ongeacht hoe het bronziekenhuis dit heeft vastgelegd. Elke tabel heeft ook **`_source_value`-kolommen** die de originele tekst uit het ziekenhuissysteem bewaren, zodat je altijd kunt terugzien wat de brondata precies zei.

---

## Patiënt- en opnametabellen

### `person`
Één rij per patiënt. Bevat geslacht (`gender_concept_id`: 8507 = man, 8532 = vrouw), geboortedatum en `person_id`, de sleutel waarmee alles aan elkaar gekoppeld is. Het geboortejaar is correct, maar de dag en maand zijn willekeurig gegenereerd.

### `visit_occurrence`
Één rij per bezoek (visit). Bevat start- en eindtijdstippen, het ziekenhuis (`care_site_id`, zie `care_site`), waar de patiënt vandaan kwam en naartoe ging (`admitted_from_concept_id`, `discharged_to_concept_id`), en het medisch specialisme (`provider_id`). `visit_occurrence_id` is wat alle klinische data in andere tabellen aan terugkoppelt.
Let op: de datums van visits zijn gebaseerd op de ruwe data zoals aangeleverd door de ziekenhuizen; in een klein aantal gevallen kunnen hier kwaliteitsproblemen in zitten. Het wordt aanbevolen om in je cohort te controleren op overlappende, gedupliceerde of gesplitste visits.

### `visit_detail`
De verblijven binnen een visit: verplaatsingen tussen afdelingen, waaronder IC-verblijven. Voorbeelden van `visit_detail_concept_id`: 32037 (Intensive Care), 2001000015 (Medium care unit), 4021813 (Operating room). Een visit kan meerdere visit details hebben, geordend via `preceding_visit_detail_id`. Elke klinische tabel heeft een `visit_detail_id` die een rij koppelt aan het verblijf waarin die valt. Beschikbaar in alle ziekenhuizen.

### `care_site`
De opzoektabel voor ziekenhuizen: `care_site_id` en de naam van het ziekenhuis. Rijen van één ziekenhuis vind je via het schema van dat ziekenhuis, bijvoorbeeld `cze.measurement` (zie [Schema's](#schemas)).

### `provider`
Één rij per medisch specialisme. `provider_id` is de concept-id van het specialisme (`specialty_concept_id`); zie [Specialisme en validatie](#specialisme-en-validatie-provider_id).

### `death`
Één rij per patiënt die in het ziekenhuis is overleden. Als een patiënt hier geen rij heeft, is er geen overlijden geregistreerd. De follow-upperiode voor overlijden verschilt per instelling.

---

## Klinische gegevenstabellen

Al deze tabellen zijn gekoppeld aan `visit_occurrence` via `visit_occurrence_id`, aan het verblijf in `visit_detail` via `visit_detail_id`, en aan de patiënt via `person_id`.

### `measurement`
De grootste tabel. Één rij per geregistreerde klinische waarde — vitale functies, laboratoriumuitslagen, scores. `measurement_source_value` is de originele parameternaam uit het ziekenhuissysteem. `value_as_number` is de waarde. `unit_source_value` is de eenheid, en `unit_concept_id` de eenheid als standaardconcept. Een gecodeerd antwoord staat in `value_as_concept_id`.
Om resultaten van een specifiek klinisch concept te vinden, zoek je het bijbehorende concept_id op in de dictionary en gebruik je dat id om alle gestandaardiseerde measurement_source_values voor dat concept samen te brengen. Let op: sommige procedures en apparaten staan hier ook als begin- en eindtijden.

### `observation`
Dezelfde opbouw als `measurement`, maar voor parameters die niet passen binnen het meetdomein — categorische scores, vlaggen en vergelijkbare data die als getal zijn vastgelegd. Of een concept hier of in measurement staat, is terug te vinden in de dictionary. Bevat relatief weinig rijen in vergelijking met `measurement`.

### `drug_exposure`
Één rij per medicatietoediening. Bevat de medicatienaam (`drug_source_value`), start- en eindtijd, hoeveelheid, toedieningsweg (`route_concept_id`) en doseringseenheid. Orale en IV-doseringen zijn omgezet naar mg, maar sommige toedieningsroutes bevatten geen doseerinformatie op ingrediëntniveau. Er is geen `drug_strength`-tabel; in plaats daarvan staat de totale toegediende hoeveelheid tijdens de exposure in de kolom `quantity`. De toedieningssnelheid wordt als stabiel beschouwd gedurende de exposure — als de snelheid verandert, wordt een nieuwe exposure aangemaakt.
**Bekend probleem in 0.3.0:** in de ziekenhuizen met Metavision bevat `quantity` van een infuus de snelheid per minuut en niet de gegeven hoeveelheid.

### `procedure_occurrence`
Één rij per uitgevoerde procedure, inclusief operaties en procedures die als ja/nee zijn vastgelegd. Bevat start- en eindtijd, wat er is gedaan (`procedure_source_value`) en hoe vaak (`quantity`). Voor operaties zijn hier de incisietijd en eindtijd te vinden. Beschikbaar in alle ziekenhuizen. Als specifieke concepten nodig zijn, neem contact op met projectteam@icudata.nl.

### `condition_occurrence`
Één rij per geregistreerde diagnose of aandoening, in alle ziekenhuizen. Bevat wat de aandoening was (`condition_source_value`, de parameternaam van het ziekenhuis) en wanneer deze actief was. De meeste aandoeningen zijn gekoppeld aan SNOMED `concept_id`-waarden. Opnamediagnoses hebben `condition_status_concept_id` 32890 (Admission diagnosis).

### `device_exposure`
Één rij per apparaatgebruik — beademingsapparaten, katheters, lijnen. Bevat de apparaatnaam (`device_source_value`) en de periode dat het in gebruik was. De einddatum is optioneel (bij sommige apparaten is geen verwijdertijd geregistreerd). `quantity` en `unit_source_value` geven de hoeveelheid, bijvoorbeeld bij bloedtransfusies.
`visit_occurrence_id`s worden gekoppeld op basis van starttijden; daardoor hebben veel device_exposures geen `visit_occurrence_id`, omdat ze voor de IC-opname zijn gestart.

---

## Herkomstcodes

Elke klinische rij vermeldt waar die vandaan komt, in de kolom `*_type_concept_id`:

| Code | Betekenis | Gebruikt in |
|------|-----------|-------------|
| 32817 | EHR | measurement, observation, condition_occurrence, procedure_occurrence, device_exposure, death |
| 32818 | EHR administration record | drug_exposure (alle rijen), device_exposure (bloedtransfusies) |
| 32823 | EHR discharge record | death |
| 32827 | EHR encounter record | visit_occurrence, visit_detail |
| 32833 | EHR order | procedure_occurrence (orders uit Epic) |
| 32856 | Lab | measurement en observation (labuitslagen) |
| 32879 | Registry | de data uit de NICE-registratie |

## Specialisme en validatie (`provider_id`)

- Bij visits en klinische rijen is `provider_id` het medisch specialisme: de concept-id van het specialisme, zoals in de tabel `provider`. 0 betekent dat het specialisme niet bekend is.
- In `measurement` en `observation` laat `provider_id` ook zien of een waarde is gevalideerd: NULL betekent dat niemand de waarde heeft gevalideerd (bijvoorbeeld een waarde die een monitor automatisch heeft vastgelegd); elke andere waarde, ook 0, betekent gevalideerd. Een NICE-item uit de NICE-registratie telt als gevalideerd (0); hetzelfde item uit het eigen systeem van het ziekenhuis heeft NULL.

---

## Tabelrelaties

```
care_site ──── visit_occurrence ──── person ──── death
                 │        │
           visit_detail   provider (provider_id)
                 │
         ┌───────┴────────┐
    measurement      observation
    drug_exposure    procedure_occurrence
    condition_occurrence
    device_exposure
```

Elke klinische rij hoort bij een `visit_occurrence` en, als dat bekend is, bij een verblijf in `visit_detail`; de visit hoort bij een `person` in een `care_site`.

---

## Schema's

Het databasebestand heeft meerdere schema's:

- `omop.*` — de tabellen om te gebruiken: alle ziekenhuizen samen, zonder kolom `hospital`. Daarnaast `source_to_concept_map`, `cdm_source` en `dictionary`.
- `amc.*`, `aumc.*`, `cze.*`, `mcl.*`, `olvg.*`, `radboud.*`, `sfg.*`, `umcu.*`, `vumc.*` — dezelfde tabellen voor één ziekenhuis.
- `icudata.*` — dezelfde tabellen met een kolom `hospital`, plus administratie (geen klinische data):
  - `icudata.version` — de versies van de database en wanneer ze zijn gebouwd
  - `icudata.changelog` — de wijzigingen tussen versies
  - `icudata.mapping_edges` — welke bronparameter aan welk concept is gekoppeld, per ziekenhuis en tabel
- `dictionary.*` — de datadictionary, één tabel per OMOP-tabel; `omop.dictionary` voegt ze samen.

---

## Minder relevante tabellen

Dit zijn standaard OMOP-vocabulairetabellen. Ze zijn zelden nodig voor analyses, maar zijn voor de volledigheid opgenomen.

- `source_to_concept_map` — bevat alle koppelingen van bronwaarden naar `concept_id`-waarden; handig om snel te zien waaraan een bronwaarde is gekoppeld
- `cdm_source` — versie-informatie over de database, waaronder de CDM-versie en vocabulaireversie
- `concept` — grote tabel met alle concepten uit alle vocabulaires; niet praktisch voor het opzoeken van concepten, maar soms nuttig voor joins
- `concept_ancestor` — hiërarchietabel die concepten koppelt aan hun hogere begrippen in vocabulaires die dit ondersteunen; in ICUdata ondersteunt momenteel alleen SNOMED dit. Via `concept_relationship`-koppelingen tussen RxNorm en SNOMED kunnen ook hogere-orde medicijnconcepten worden gevonden.
- `concept_class` — classificeert concepten binnen een vocabulaire (bijv. "Clinical Finding", "Drug")
- `concept_relationship` — gestandaardiseerde koppelingen tussen concepten uit verschillende vocabulaires
- `concept_synonym` — alternatieve namen en synoniemen van concepten
- `domain` — definieert het klinische domein waartoe een concept behoort (bijv. Measurement, Drug, Condition)
- `relationship` — definieert de soorten relaties die worden gebruikt in `concept_relationship`
- `vocabulary` — bevat alle vocabulaires die aanwezig zijn in de database (bijv. SNOMED, LOINC, RxNorm)
