# ICUdata 0.3.0

## Nieuwe data

- **NICE APACHE opnamediagnoses toegevoegd voor 7 nieuwe ziekenhuizen**
- **NICE data voor 4 nieuwe ziekenhuizen** (APACHE- en SOFA-items, chronische aandoeningen, IC-uitkomst). Bij NICE-items geeft provider_id de herkomst aan: 0 is aangeleverd door de NICE-registratie (gevalideerd), en `provider_id IS NULL` komt alleen uit de eigen database van het ziekenhuis. 
- **HiX diagnoses toegevoegd**
- **Nieuwe aanlevering Catharina Ziekenhuis Eindhoven** van recente data, aantal patiënten van 4.480 naar 7.304.
- **Lab data Catharina Ziekenhuis 2023 toegevoegd**
- **Operatiekamer registraties voor Epic ziekenhuizen**: heden alleen de meest uitgevoerde, op aanvraag kunnen specifieke OK's gezocht en toegevoegd worden.
- **Nieuwe procedures vanuit Epic**
- **IC en medium care onderscheid**: met nieuwe visit_detail tabel is er nu onderscheid te maken tussen IC en MC. Voor Epic ziekenhuizen zijn ook tussentijdse verplaatsingen naar bijvoorbeeld OK of beeldvorming hierin opgenomen.
- **Gevalideerde en ongevalideerde waarden**: ongevalideerde metingen zijn nu vindbaar door in de measurement tabel te filteren op `provider_id IS NULL`. Alleen Franciscus Gasthuis bevat ongevalideerde IC opname waarden.
- **Bloedtransfusies** in Amsterdam UMC (Epic): erytrocyten, trombocyten en plasma, met de gegeven hoeveelheid.
- VUMC en AMC: waarden van vochtinname en vochtuitscheiding die meetellen voor de vochtbalans, krijgen een aparte vochtbalansregel met '(For total fluid in)' of '(For total fluid out)' in de measurement_source_value.

## Mapping

- **Parameter mapping** in elk ziekenhuis: 3.143 codes toegevoegd, 125 verwijderd en 174 gewijzigd. Een query die een verwijderde of gewijzigde code gebruikt, moet mogelijk worden aangepast.
- **Eenheden** hebben nu mapping naar standaardconcepten via unit_concept_id. Er is niet per parameter gekeken of de originele eenheid klopt.
- **GCS/RASS** hebben nu mapping van de antwoorden naar value_as_concept_id met standaard SNOMED concepten.
- **Toedieningsweg van de meeste medicijnen** (bijvoorbeeld intraveneus, oraal, enteraal) is nu gemapped via route_concept_id.
- **Opname en ontslagafdeling** is nu gemapped via admitted_from_concept_id en discharged_to_concept_id.
- **Herkomst data**: elk gegeven vermeldt nu de bron in *_type_concept_id kolommen, bijvoorbeeld het elektronisch patiëntendossier van het ziekenhuis, het labsysteem of de NICE-registratie. 
- De bron van elke overlijdensregistratie is vastgelegd.

## Bugfixes

- Antwoorden vanuit bepaalde lijsten zoals GCS/RASS hadden niet de goede waarde; dit is opgelost.
- **Urineproductie en andere vochtwaarden** met een eenheid ontbraken bij ziekenhuizen met Epic; ze zijn nu opgenomen.
- **Diastolische en gemiddelde bloeddruk** en andere tweede waarden van een registratie van vitale functies ontbraken bij ziekenhuizen met HiX; ze zijn nu opgenomen.
- **Ontbrekende medicatie toegevoegd** (Franciscus Gasthuis): veel toedieningen ontbraken omdat de doseringseenheid niet overeenkwam; ze zijn nu opgenomen.
- Opnames zonder ontslagtijd, en lijnen en drains die nog in situ zijn bij ziekenhuizen met Epic, eindigen niet meer op een fictieve datum ver in de toekomst.
- Dubbele gegevens verwijderd: vochtwaarden in Epic die twee keer zijn vastgelegd, en berekende waarden in Epic die gelijk zijn aan de waarde waaruit ze zijn berekend. Waarden uit verschillende bronnen (bijvoorbeeld twee ECG-afleidingen) blijven apart.
- Ziekenhuizen met Metavision: alleen de laatst opgeslagen versie van een formulier wordt bewaard, en een vraag met meerdere aangevinkte antwoorden houdt ze allemaal.
- Ziekenhuizen met Metavision: NICE-antwoorden zijn gekoppeld aan de opname waar ze over gaan, niet aan elk IC-verblijf van de patiënt.
- AMC: tekstantwoorden met een puntkomma nu gescheiden in meerdere regels.
- Ziekenhuizen met Epic: datum en tijd van overlijden staan nu in juiste tijdzone.

## Verbeteringen

- **Nauwkeuriger medicatieregistratie** (ziekenhuizen met Epic): infusieregistraties zijn aan elkaar gekoppeld wanneer dezelfde rate doorgegeven werd (soms leidend tot vermindering totaal aantal rijen).
- Ziekenhuizen met HiX: een labwaarde krijgt het tijdstip van afname, of het tijdstip van de uitslag als dat eerder is.
- Patiënten zonder opname zijn verwijderd.
- Ziekenhuizen met Metavision: een verblijf zonder ontslagbestemming krijgt de bestemming die in de 24 uur daarna is vastgelegd, tot het begin van het volgende verblijf.
- Opnamelogica bijgewerkt voor alle EPD's, wat heeft geleid tot kleine tot grote veranderingen in opnamedatums, afhankelijk van het EPD of ziekenhuis.

## Verplaatsingen

- Sommige verrichtingen die als ja/nee-meting waren vastgelegd, staan nu in procedure_occurrence in plaats van measurement tabel.
- Parameters met als antwoord een datum(-tijd) in de measurement tabel vallen nu vaker in de condition_occurrence, procedure_occurrence of device_exposure tabel wanneer mogelijk.
- Ziekenhuizen met Epic: wonden en decubitus staan bij de diagnoses.

## Bestanden en documentatie

- **Conceptenlijst hernoemd, compleet en per release**: het bestand dat concepten groepeert naar de klinische vraag die ze beantwoorden, is nu `concept_taxonomy.yaml` in elke releasemap, in plaats van `common_concepts.yaml` in de hoofdmap van de repository. Het bevat elk concept in de database met klinische groepering.
- In de gepubliceerde datadictionary worden aantallen onder de 10 patiënten niet getoond, voor deze release en voor 0.2.0: ze staan als "<10", en het percentage van een ziekenhuis dat voor minder dan 10 patiënten staat, is leeg gelaten.
- Het middelste versienummer gaat nu alleen omhoog bij wijzigingen die een bestaande query kunnen breken.

## Binnenkort

- **LUMC en Amphia**: de dataleveringen van het Leids Universitair Medisch Centrum en Amphia zijn ontvangen; hun data komen in een volgende release.

---

# ICUdata 0.3.0

## New data

- **NICE APACHE admission diagnoses added for 7 new hospitals**
- **NICE data for 4 new hospitals** (APACHE and SOFA items, chronic conditions, ICU outcome). For NICE items, provider_id shows where the item comes from: 0 means delivered by the NICE registry (validated), and `provider_id IS NULL` means it comes only from the hospital's own database.
- **HiX diagnoses added**
- **New delivery from Catharina Ziekenhuis Eindhoven** with recent data; patients from 4,480 to 7,304.
- **Catharina Ziekenhuis lab data for 2023 added**
- **Operating room records for hospitals on Epic**: for now only the most frequently performed operations; specific operations can be looked up and added on request.
- **New ICU procedures from Epic**
- **ICU and medium care told apart**: the new visit_detail table separates ICU from medium care. For hospitals on Epic, transfers in between, for example to the operating room or to imaging, are included as well.
- **Validated and unvalidated values**: unvalidated measurements can now be found by filtering the measurement table on `provider_id IS NULL`. Only Franciscus Gasthuis has unvalidated ICU admission values.
- **Blood transfusions** at Amsterdam UMC (Epic): red cells, platelets and plasma, with the amount given.
- VUmc and AMC: fluid intake and output values that count toward the fluid balance get a separate fluid-balance entry with '(For total fluid in)' or '(For total fluid out)' in measurement_source_value.

## Mapping

- **Parameter mapping** at every hospital: 3,143 codes added, 125 removed and 174 changed. A query that uses a removed or changed code may need updating.
- **Units** are now mapped to standard concepts in unit_concept_id. Whether the original unit is right has not been checked per parameter.
- **GCS/RASS** answers are mapped to standard SNOMED concepts in value_as_concept_id.
- **Route of most medications** (for example intravenous, oral, enteral) is mapped in route_concept_id.
- **Where the patient came from and went to**, before and after the admission, is mapped in admitted_from_concept_id and discharged_to_concept_id.
- **Where each record comes from**: every record now names its source in the *_type_concept_id columns, for example the hospital's electronic health record, the lab system or the NICE registry, so registry data can be kept apart from data recorded at the bedside.
- The source of each death registration is recorded.

## Bug fixes

- Answers from some lists, such as GCS and RASS, did not have the right value; this is fixed.
- **Urine output and other fluid values** with a unit were missing at hospitals on Epic; they are now included.
- **Diastolic and mean blood pressure** and other second values of a vital-sign entry were missing at hospitals on HiX; they are now included.
- **Missing medication added** (Franciscus Gasthuis): many administrations were missing because their dose unit did not match; they are now included.
- Admissions without a discharge time, and lines and drains still in place at hospitals on Epic, no longer end on a placeholder date far in the future.
- Duplicates removed: Epic fluid values recorded twice, and Epic calculated values that equal the value they were calculated from. Values from different sources (for example two ECG leads) stay separate.
- Hospitals on Metavision: only the last saved version of a form is kept, and a question with several ticked answers keeps all of them.
- Hospitals on Metavision: NICE answers are linked to the admission they describe, not to every ICU stay of the patient.
- AMC: text answers that contain a semicolon are now split into separate rows.
- Hospitals on Epic: date and time of death are now in the right time zone.

## Improvements

- **More accurate medication records** (hospitals on Epic): infusion records are joined together when the same rate was passed on, which sometimes lowers the total number of rows.
- Hospitals on HiX: a lab value gets the time the sample was taken, or the result time if that is earlier.
- Patients without an admission are removed.
- Hospitals on Metavision: a stay without a discharge destination gets the destination recorded in the 24 hours after it, up to the start of the next stay.
- Visit logic updated for all EHRs, which has changed visit dates by small to large amounts, depending on the EHR or hospital.

## Moved

- Some procedures that were recorded as yes/no measurements are now in procedure_occurrence instead of the measurement table.
- Parameters answered with a date (and time) in the measurement table now go more often to condition_occurrence, procedure_occurrence or device_exposure where possible.
- Hospitals on Epic: wounds and pressure injuries are listed as diagnoses.

## Files and documentation

- **Concept list renamed, complete and per release**: the file that groups concepts by the clinical question they answer is now `concept_taxonomy.yaml` in each release folder, instead of `common_concepts.yaml` in the repository root. It contains every concept in the database with its clinical grouping.
- In the published data dictionary, numbers of patients below 10 are not shown, for this release and for 0.2.0: they are shown as "<10", and a hospital's percentage that stands for fewer than 10 patients is left blank.
- The middle version number now goes up only for changes that can break an existing query.

## Coming next

- **LUMC and Amphia**: the data deliveries from Leids Universitair Medisch Centrum and Amphia have been received; their data will be in a next release.
