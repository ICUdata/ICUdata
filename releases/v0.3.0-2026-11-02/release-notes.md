# ICUdata 0.3.0: wat is er nieuw sinds 0.2.0

Uitgebracht op 2 november 2026. Dezelfde ziekenhuizen als in 0.2.0.

## Grote wijzigingen

- **Verrichtingen en operaties voor elk ziekenhuis** (eerder alleen Catharina Ziekenhuis en Franciscus): verrichtingen die op de IC zijn vastgelegd, en operaties uit de OK-registratie van ziekenhuizen met Epic en HiX.
- **Opnamediagnoses voor elk ziekenhuis** (eerder: twee ziekenhuizen), gecodeerd met standaard diagnosecodes.
- **NICE-registratiedata in elk ziekenhuis behalve het Catharina Ziekenhuis** (APACHE- en SOFA-items, chronische aandoeningen, IC-uitkomst).
- **Catharina Ziekenhuis Eindhoven**: nieuwe levering met de opnames van 2025; aantal patiënten van 4.480 naar 7.304.

## Middelgrote wijzigingen

- **IC en medium care onderscheiden**: elke ziekenhuisopname is opgesplitst in de verblijven (IC, medium care, operatiekamer, spoedeisende hulp en andere), en elk gegeven is gekoppeld aan het verblijf waar het bij hoort.
- **Medisch specialisme** van elke opname en elk verblijf (bijvoorbeeld neurologie of cardiochirurgie), als het ziekenhuis dat vastlegt.
- **Gecontroleerde en ongecontroleerde waarden** (ziekenhuizen met Epic): waarden die een monitor automatisch heeft vastgelegd en die niemand heeft gecontroleerd, zijn te onderscheiden van gecontroleerde waarden.
- **Eenheden** zijn gekoppeld aan standaardeenheden.
- **Antwoorden die uit een lijst zijn gekozen** (bijvoorbeeld bij scores en beoordelingen) zijn gekoppeld aan standaardcodes.
- **Toedieningsweg van elk medicijn** (bijvoorbeeld intraveneus, oraal, enteraal) is gekoppeld aan standaardcodes.
- **Waar de patiënt vandaan kwam en naartoe ging**, voor en na de opname, is gekoppeld aan standaardcodes.
- **Bloedtransfusies** in Amsterdam UMC (Epic): erytrocyten, trombocyten en plasma, met de gegeven hoeveelheid.
- **Nauwkeuriger medicatieregistratie** (ziekenhuizen met Epic): controles van de snelheid van een lopend infuus tellen niet meer als aparte toedieningen, gemiste en geweigerde toedieningen zijn verwijderd, en infuusperiodes volgen de toedieningsregistratie. Daardoor zijn er minder medicatieregels (Amsterdam UMC Epic: van 18,9 naar 8,7 miljoen).
- **Ontbrekende medicatie toegevoegd** (Franciscus): veel toedieningen ontbraken omdat hun doseringseenheid niet overeenkwam; ze zijn nu opgenomen.
- **Antwoorden uit een lijst tonen de juiste tekst** (ziekenhuizen met Epic), bijvoorbeeld bij GCS, RASS en pijnscores. Eerder toonden sommige alleen een getal of de tekst van een andere vraag.
- **Urineproductie en andere vochtwaarden** met een eenheid ontbraken bij ziekenhuizen met Epic; ze zijn nu opgenomen.
- **Diastolische en gemiddelde bloeddruk** en andere tweede waarden van een registratie van vitale functies ontbraken bij ziekenhuizen met HiX; ze zijn nu opgenomen.
- **Waar elk gegeven vandaan komt**: elk gegeven vermeldt nu de bron, bijvoorbeeld het elektronisch patiëntendossier van het ziekenhuis, het labsysteem of de NICE-registratie. Zo kunnen registratiedata apart worden gehouden van data die aan het bed zijn vastgelegd. De codes hiervoor zijn veranderd sinds 0.2.0 (voor alle medicatie, en voor de meeste metingen en observaties): een query die gegevens selecteert op hun code uit 0.2.0 geeft niets terug en moet worden aangepast.
- **Conceptenlijst hernoemd, compleet en per release**: het bestand dat concepten groepeert naar de klinische vraag die ze beantwoorden, is nu `concept_taxonomy.yaml` (met `concept_taxonomy.md`, een pagina die je op GitHub kunt doorbladeren) in elke releasemap, in plaats van `common_concepts.yaml` in de hoofdmap van de repository. Het bevat elk concept in de database.
- **Standaardcodes bijgewerkt** in elk ziekenhuis: 3.143 codes toegevoegd, 125 verwijderd en 174 gewijzigd. Een query die een verwijderde of gewijzigde code gebruikt, moet mogelijk worden aangepast.

## Kleine wijzigingen

- Sommige verrichtingen die als ja/nee-meting waren vastgelegd, staan nu bij de verrichtingen.
- Labwaarden hebben het juiste monstertype (bloed, of serum/plasma), bijvoorbeeld natrium en CRP.
- Vragen die met een datum zijn beantwoord, zijn nu vastgelegd als "ja" op die datum.
- Ziekenhuizen met HiX: een labwaarde krijgt het tijdstip van afname, of het tijdstip van de uitslag als dat eerder is.
- De bron van elke overlijdensregistratie is vastgelegd.
- Patiënten zonder opname zijn verwijderd.
- Ziekenhuizen met Metavision: een verblijf zonder ontslagbestemming krijgt de bestemming die in de 24 uur daarna is vastgelegd, tot het begin van het volgende verblijf.
- Opnames zonder ontslagtijd, en lijnen en drains die nog in situ zijn bij ziekenhuizen met Epic, eindigen niet meer op een fictieve datum ver in de toekomst.
- Dubbele gegevens verwijderd: vochtwaarden in Epic die twee keer zijn vastgelegd, en berekende waarden in Epic die gelijk zijn aan de waarde waaruit ze zijn berekend. Waarden uit verschillende bronnen (bijvoorbeeld twee ECG-afleidingen) blijven apart.
- Ziekenhuizen met Metavision: alleen de laatst opgeslagen versie van een formulier wordt bewaard, en een vraag met meerdere aangevinkte antwoorden houdt ze allemaal.
- Ziekenhuizen met Epic: wonden en decubitus staan bij de diagnoses.
- Ziekenhuizen met Metavision: NICE-antwoorden zijn gekoppeld aan de opname waar ze over gaan, niet aan elk IC-verblijf van de patiënt.
- Ziekenhuizen met Metavision: waarden van vochtinname en vochtuitscheiding die meetellen voor de vochtbalans, krijgen een aparte vochtbalansregel.
- Ziekenhuizen met Metavision: aan de oorspronkelijke tekst van een waarde zijn geen labels of opmerkingen meer toegevoegd.
- AMC: tekstantwoorden met een puntkomma behouden hun label en score.
- Ziekenhuizen met Epic: datum en tijd van overlijden staan in UTC.
- Het geslacht zoals het ziekenhuis het heeft vastgelegd, staat naast de standaardcode.
- De database bevat zijn eigen versienummer, lijst met wijzigingen en datadictionary.
- In de gepubliceerde datadictionary worden aantallen onder de 10 patiënten niet getoond, voor deze release en voor 0.2.0: ze staan als "<10", en het percentage van een ziekenhuis dat voor minder dan 10 patiënten staat, is leeg gelaten.
- Het middelste versienummer gaat nu alleen omhoog bij wijzigingen die een bestaande query kunnen breken.

## Binnenkort

- **LUMC en Amphia**: de dataleveringen van het Leids Universitair Medisch Centrum en Amphia zijn ontvangen; hun data komen in een volgende release.

## Bekende problemen

- **Ziekenhuizen met Metavision: infusen zijn vastgelegd als snelheid, niet als hoeveelheid.** Bij een infuus is de opgeslagen waarde de snelheid per minuut en niet de gegeven hoeveelheid. Dit geldt voor `drug_exposure.quantity` in alle ziekenhuizen met Metavision, en voor waarden in `measurement` die uit infusen komen. Bij vochtinname in het AMC en VUmc zijn de meeste waarden snelheden; optellen levert daardoor veel te weinig op. Dit wordt opgelost in de volgende release.

---

# ICUdata 0.3.0: what is new since 0.2.0

Released 2 November 2026. Same hospitals as in 0.2.0.

## Large changes

- **Procedures and operations for every hospital** (before: Catharina Ziekenhuis and Franciscus only): procedures charted on the ICU, and operations from the operating room records of hospitals on Epic and HiX.
- **Admission diagnoses for every hospital** (before: two hospitals), coded with standard diagnosis codes.
- **NICE registry data at every hospital except Catharina Ziekenhuis** (APACHE and SOFA items, chronic conditions, ICU outcome).
- **Catharina Ziekenhuis Eindhoven**: new delivery with the 2025 admissions; patients from 4,480 to 7,304.

## Medium changes

- **ICU and medium care told apart**: each hospital admission is split into its stays (ICU, medium care, operating room, emergency department and others), and every record is linked to the stay it belongs to.
- **Medical specialty** of each admission and stay (for example neurology or cardiac surgery), where the hospital records it.
- **Checked and unchecked values** (hospitals on Epic): values that a monitor filed automatically and nobody checked can be told apart from checked values.
- **Units** are linked to standard units.
- **Answers chosen from a list** (for example in scores and assessments) are linked to standard codes.
- **Route of each medication** (for example intravenous, oral, enteral) is linked to standard codes.
- **Where the patient came from and went to**, before and after the admission, is linked to standard codes.
- **Blood transfusions** at Amsterdam UMC (Epic): red cells, platelets and plasma, with the amount given.
- **More accurate medication records** (hospitals on Epic): rate checks of a running infusion are no longer separate doses, missed and refused doses are removed, and infusion periods follow the administration record. This lowers the number of medication records (Amsterdam UMC Epic: from 18.9 to 8.7 million).
- **Missing medication added** (Franciscus): many administrations were left out because their dose unit did not match; they are now included.
- **Answers chosen from a list show the right text** (hospitals on Epic), for example GCS, RASS and pain scores. Before, some showed only a number or the text of another question.
- **Urine output and other fluid values** with a unit were missing at hospitals on Epic; they are now included.
- **Diastolic and mean blood pressure** and other second values of a vital-sign entry were missing at hospitals on HiX; they are now included.
- **Where each record comes from**: every record now says where it comes from, for example the hospital's electronic health record, the lab system or the NICE registry, so registry data can be kept apart from bedside data. The codes for this changed since 0.2.0 (for all medication, and for most measurements and observations): a query that selects records by their 0.2.0 code returns nothing and needs updating.
- **Concept list renamed, complete and per release**: the file that groups concepts by the clinical question they answer is now `concept_taxonomy.yaml` (with `concept_taxonomy.md`, a page you can browse on GitHub) inside each release folder, instead of `common_concepts.yaml` in the repository root. It covers every concept in the database.
- **Standard codes updated** at every hospital: 3,143 codes added, 125 removed and 174 changed. A query that uses a removed or changed code may need updating.

## Small changes

- Some procedures that were recorded as yes/no measurements are now listed as procedures.
- Lab values have the right sample type (blood, or serum/plasma), for example sodium and CRP.
- Questions answered with a date are now recorded as "yes" on that date.
- Hospitals on HiX: a lab value is timed by when the sample was taken, or by the result time if that is earlier.
- The source of each death registration is recorded.
- Patients without any admission are removed.
- Hospitals on Metavision: a stay without a discharge destination takes the destination recorded in the 24 hours after it, up to the start of the next stay.
- Admissions without a discharge time, and lines and drains still in place at hospitals on Epic, no longer end on a placeholder date far in the future.
- Duplicates removed: Epic fluid values recorded twice, and Epic calculated values that equal the value they were calculated from. Values from different sources (for example two ECG leads) stay separate.
- Hospitals on Metavision: only the last saved version of a form is kept, and a question with several ticked answers keeps all of them.
- Hospitals on Epic: wounds and pressure injuries are listed as diagnoses.
- Hospitals on Metavision: NICE answers are linked to the admission they describe, not to every ICU stay of the patient.
- Hospitals on Metavision: fluid intake and output values that count toward the fluid balance get a separate fluid-balance entry.
- Hospitals on Metavision: the original text of a value no longer has tags or comments attached.
- AMC: text answers that contain a semicolon keep their label and score.
- Hospitals on Epic: date and time of death are in UTC.
- The sex as recorded by the hospital is kept next to the standard code.
- The database holds its own version number, list of changes and data dictionary.
- In the published data dictionary, numbers of patients below 10 are hidden, for this release and for 0.2.0: they are shown as "<10", and a hospital's percentage that stands for fewer than 10 patients is left blank.
- The middle version number now goes up only for changes that can break an existing query.

## Coming next

- **LUMC and Amphia**: the data deliveries from Leids Universitair Medisch Centrum and Amphia have been received; their data will be in a next release.

## Known issues

- **Hospitals on Metavision: infusions are recorded as a rate, not an amount.** For an infusion, the stored value is the rate per minute rather than the amount given. This applies to `drug_exposure.quantity` at all hospitals on Metavision, and to values in `measurement` that come from infusions. For fluid intake at AMC and VUmc, most values are rates, so adding them up gives far too little. This will be fixed in the next release.
