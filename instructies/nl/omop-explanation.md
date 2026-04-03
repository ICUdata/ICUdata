# Inhoud database

De database bevat klinische data van meerdere Intensive Care's van Nederlandse ziekenhuizen (AMC, VUMC, AUMC, UMCU, CZE, OLVG), gestandaardiseerd naar het **OMOP CDM 5.4**-formaat. OMOP is een veelgebruikt schema in medisch onderzoek, zodat data van verschillende ziekenhuizen en EPD-systemen samen geanalyseerd kan worden.

Handige links: [OMOP-schema visueel verkennen](https://linkr.interhop.org/en/tools/omop-schema/) — [OMOP-concepten opzoeken en doorzoeken (Athena)](https://athena.ohdsi.org/search-terms/start)

Het centrale concept in OMOP is de **concept ID**: een universeel getal dat een klinisch begrip identificeert — een medicijn, een meettype, een diagnose. Concept ID `8507` betekent overal "mannelijk", ongeacht hoe het bronziekenhuis dit heeft vastgelegd. Elke tabel heeft ook **`_source_value`-kolommen** die de originele tekst uit het ziekenhuissysteem bewaren, zodat je altijd kunt terugzien wat de brondata precies zei.

---

## Patiënt- en opnametabellen

### `person`
Één rij per patiënt. Bevat geslacht (`gender_concept_id`: 8507 = man, 8532 = vrouw), geboortedatum en `person_id`, de sleutel waarmee alles aan elkaar gekoppeld is. Het geboortejaar is correct, maar de dag en maand zijn willekeurig gegenereerd.

### `visit_occurrence`
Één rij per IC-opname. Bevat opname- en ontslagtijdstippen, het ziekenhuis (`care_site_id`, waarvan het bijbehorende ziekenhuis te vinden is in de `care_site`-tabel), en van/naar welke locatie de patiënt werd overgeplaatst.
`visit_occurrence_id` is wat alle klinische data in andere tabellen aan terugkoppelt. Let op: de datums in visit_occurrence zijn gebaseerd op de ruwe data zoals aangeleverd door de ziekenhuizen; in een klein aantal gevallen kunnen hier kwaliteitsproblemen in zitten. Het wordt aanbevolen om in je cohort te controleren op overlappende, gedupliceerde of gesplitste opnames.

### `visit_detail` (Alleen bepaalde ziekenhuizen)
Deelverblijven binnen een opname — IC-verblijven (`visit_detail_concept_id` = 32037) en OK-episodes (4021813). Een enkele opname kan meerdere visit details hebben, geordend via `preceding_visit_detail_id`.
De IC-verblijven zijn duplicaten van de visit_occurrence en daardoor is deze tabel alleen nuttig voor OK-episodes. Het operatiespecialisme is toegevoegd aan de naam van de ingreep in `visit_source_value`. De tijdstippen geven de in- en uitgang van de operatiekamer weer.

### `care_site`
De opzoektabel voor ziekenhuizen. `care_site_id` verwijst naar: 1 = AMC, 2 = VUMC, 3 = AUMC, 4 = UMCU, 6 = CZE, 8 = OLVG. Door de visit_occurrence-tabel te joinen op het visit_occurrence_id van een tabel, of op person_id plus een datum, kan de care_site van alle rijen worden bepaald. Rijen van één instelling kunnen ook worden opgevraagd via het formaat "ziekenhuis.tabel".

### `death`
Één rij per patiënt die in het ziekenhuis is overleden. Als een patiënt hier geen rij heeft, is er geen overlijden geregistreerd. De follow-upperiode voor overlijden verschilt per instelling.

---

## Klinische gegevenstabellen

Al deze tabellen zijn gekoppeld aan `visit_occurrence` via `visit_occurrence_id`, en aan de patiënt via `person_id`.

### `measurement`
De grootste tabel. Één rij per geregistreerde klinische waarde — vitale functies, laboratoriumuitslagen, scores. `measurement_source_value` is de originele parameternaam uit het ziekenhuissysteem. `value_as_number` is de waarde. `unit_source_value` is de eenheid.
Om resultaten van een specifiek klinisch concept te vinden, zoek je het bijbehorende concept_id op in de dictionary en gebruik je dat id om alle gestandaardiseerde measurement_source_values voor dat concept samen te brengen. Let op: sommige procedures en apparaten staan hier ook als begin- en eindtijden.

### `observation`
Dezelfde opbouw als `measurement`, maar voor parameters die niet passen binnen het meetdomein — categorische scores, vlaggen en vergelijkbare data die als getal zijn vastgelegd. Of een concept hier of in measurement staat, is terug te vinden in de dictionary. Bevat relatief weinig rijen in vergelijking met `measurement`.

### `drug_exposure`
Één rij per medicatietoediening. Bevat de medicatienaam (`drug_source_value`), start- en eindtijd, hoeveelheid, toedieningsweg en doseringseenheid. Orale en IV-doseringen zijn omgezet naar mg, maar sommige toedieningsroutes bevatten geen doseerinformatie op ingrediëntniveau. Er is geen `drug_strength`-tabel; in plaats daarvan staat de totale toegediende hoeveelheid tijdens de exposure in de kolom `quantity`. De toedieningssnelheid wordt als stabiel beschouwd gedurende de exposure — als de snelheid verandert, wordt een nieuwe exposure aangemaakt.

### `procedure_occurrence` (Alleen bepaalde ziekenhuizen)
Één rij per uitgevoerde procedure. Bevat start- en eindtijd, wat er is gedaan (`procedure_source_value`) en hoe vaak (`quantity`). Voor operaties zijn hier de incisietijd en eindtijd te vinden. Bevat momenteel weinig concepten afhankelijk van het ziekenhuis, maar kan nuttig zijn voor intubatietijden. Als specifieke concepten nodig zijn, neem contact op met projectteam@icudata.nl.

### `condition_occurrence`
Één rij per geregistreerde diagnose of aandoening. Bevat wat de aandoening was (`condition_source_value`) en wanneer deze actief was. Beschikbaar voor HiX-ziekenhuizen. Voor sommige ziekenhuizen zijn de aandoeningen gekoppeld aan SNOMED `concept_id`s. Voor de Amsterdam UMC-ziekenhuizen (AMC, VUMC, AUMC) bevat de tabel geaggregeerde aangepaste concepten; deze staan in de kolom `measurement_source_value`.

### `device_exposure`
Één rij per apparaatgebruik — beademingsapparaten, katheters, lijnen. Bevat de apparaatnaam (`device_source_value`) en de periode dat het in gebruik was. De einddatum is optioneel (bij sommige apparaten is geen verwijdertijd geregistreerd).
`visit_occurrence_id`s worden gekoppeld op basis van starttijden; daardoor hebben veel device_exposures geen `visit_occurrence_id`, omdat ze voor de IC-opname zijn gestart.

---

## Tabelrelaties

```
care_site ──────────────── visit_occurrence ─────────── person
                                  │                        │
                                  │                      death
                                  │
                          ┌───────┴────────┐
                     measurement      observation
                     drug_exposure    procedure_occurrence
                     condition_occurrence
                     device_exposure
```

Elke klinische rij hoort bij een `visit_occurrence`, die hoort bij een `person` in een `care_site`.

---

## Interne metadatatablellen

De database bevat ook tabellen voor versiebeheer (geen klinische data):

- `icudata.version` — registreert wanneer de database voor het laatst is bijgewerkt en welke data is opgenomen
- `icudata.changelog` — log van wijzigingen tussen updates (ziekenhuizen of tabellen toegevoegd/verwijderd, wijzigingen in rij-aantallen)
- `icudata.dictionary` — koppeling van concept ID's aan parameternamen

---

## Minder relevante tabellen

Dit zijn standaard OMOP-vocabulairetabellen. Ze zijn zelden nodig voor analyses, maar zijn voor de volledigheid opgenomen.

- `source_to_concept_map` — bevat alle koppelingen van bronwaarden naar `concept_id`s; handig om snel te zien waaraan een bronwaarde is gekoppeld
- `cdm_source` — versie-informatie over de database, waaronder de CDM-versie en vocabulaireversie
- `concept` — grote tabel met alle concepten uit alle vocabulaires; niet praktisch voor het opzoeken van concepten, maar soms nuttig voor joins
- `concept_ancestor` — hiërarchietabel die concepten koppelt aan hun hogere begrippen in vocabulaires die dit ondersteunen; in ICUdata ondersteunt momenteel alleen SNOMED dit. Via `concept_relationship`-koppelingen tussen RxNorm en SNOMED kunnen ook hogere-orde medicijnconcepten worden gevonden.
- `concept_class` — classificeert concepten binnen een vocabulaire (bijv. "Clinical Finding", "Drug")
- `concept_relationship` — gestandaardiseerde koppelingen tussen concepten uit verschillende vocabulaires
- `concept_synonym` — alternatieve namen en synoniemen van concepten
- `domain` — definieert het klinische domein waartoe een concept behoort (bijv. Measurement, Drug, Condition)
- `relationship` — definieert de soorten relaties die worden gebruikt in `concept_relationship`
- `vocabulary` — bevat alle vocabulaires die aanwezig zijn in de database (bijv. SNOMED, LOINC, RxNorm)
