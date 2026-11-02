For a readable summary, see [release-notes.md](release-notes.md).

# icudata v0.3.0

Released 2026-11-01. Previous version: 0.2.0.
Hospitals: amc, aumc, cze, mcl, olvg, radboud, sfg, umcu, vumc. Tables: 20.

## Breaking Changes

These can make a query written for the previous version fail, or return rows that mean something else.

- Concepts removed: 125
- Concepts remapped: 174
- Columns removed: `condition_occurrence.parameter_name`.
- Column types changed: `concept_relationship.invalid_reason` (integer → text); `relationship.defines_ancestry` (integer → text); `relationship.is_hierarchical` (integer → text).
- Record-type code changed: `drug_exposure.drug_type_concept_id` 38000180 (Inpatient administration) → 32818 (EHR administration record) at all hospitals (57.8 M rows in 0.2.0). A query that selects on the old code returns no rows.
- Record-type code changed: `measurement.measurement_type_concept_id` 0 (No matching concept) → 32817 (EHR) or 32856 (Lab) or 32879 (Registry) at amc, aumc, mcl, olvg, radboud, umcu and vumc (896.9 M rows in 0.2.0). A query that selects on the old code returns no rows.
- Record-type code changed: `observation.observation_type_concept_id` 0 (No matching concept) → 32817 (EHR) or 32879 (Registry) at amc, aumc, mcl, olvg, radboud, umcu and vumc (17.4 M rows in 0.2.0). A query that selects on the old code returns no rows.
- `care_site.care_site_id` is now a 64-bit integer (no effect on queries).
- No hospitals were removed from any table.

## Tables Added

- provider (53 rows)
- visit_detail (197957 rows)

## Schema/Content Changes

- care_site: columns_widened, hospitals_added, rows
- concept: rows
- concept_ancestor: rows
- concept_relationship: columns_type_changed, rows
- concept_synonym: rows
- condition_occurrence: columns_added, columns_removed, hospitals_added, rows
- death: columns_added, rows
- device_exposure: columns_added, rows
- drug_exposure: columns_added, rows
- measurement: columns_added, rows
- observation: columns_added, rows
- person: columns_added, rows
- procedure_occurrence: columns_added, hospitals_added, rows
- relationship: columns_type_changed
- visit_occurrence: columns_added, rows
- vocabulary: rows

## Record-Type Codes Added

- `condition_occurrence.condition_type_concept_id`: 32817 (EHR) at aumc
- `device_exposure.device_type_concept_id`: 32818 (EHR administration record) at aumc, cze, mcl, radboud and sfg
- `measurement.measurement_type_concept_id`: 32856 (Lab) at cze and sfg
- `measurement.measurement_type_concept_id`: 32879 (Registry) at sfg
- `observation.observation_type_concept_id`: 32856 (Lab) at sfg
- `observation.observation_type_concept_id`: 32879 (Registry) at sfg
- `procedure_occurrence.procedure_type_concept_id`: 32879 (Registry) at sfg

## Concept Changes

- 8482 — pH (UCUM) added in measurement
- 8483 — counts per minute (UCUM) added in measurement
- 8483 — counts per minute (UCUM) added in observation
- 8504 — gram (UCUM) added in measurement
- 8505 — hour (UCUM) added in measurement
- 8510 — unit (UCUM) added in measurement
- 8511 — week (UCUM) added in observation
- 8512 — day (UCUM) added in measurement
- 8519 — liter (UCUM) added in measurement
- 8523 — ratio (UCUM) added in measurement
- 8525 — titer (UCUM) added in measurement
- 8541 — per minute (UCUM) added in measurement
- 8554 — percent (UCUM) added in measurement
- 8555 — second (UCUM) added in measurement
- 8576 — milligram (UCUM) added in measurement
- 8576 — milligram (UCUM) added in observation
- 8582 — centimeter (UCUM) added in measurement
- 8582 — centimeter (UCUM) added in observation
- 8583 — femtoliter (UCUM) added in measurement
- 8587 — milliliter (UCUM) added in measurement
- 8588 — millimeter (UCUM) added in measurement
- 8617 — square meter (UCUM) added in measurement
- 8636 — gram per liter (UCUM) added in measurement
- 8645 — unit per liter (UCUM) added in measurement
- 8647 — per microliter (UCUM) added in measurement
- 8698 — liter per minute (UCUM) added in measurement
- 8713 — gram per deciliter (UCUM) added in measurement
- 8720 — microgram per gram (UCUM) added in measurement
- 8723 — milligram per gram (UCUM) added in measurement
- 8725 — nanogram per liter (UCUM) added in measurement
- 8729 — picomole per liter (UCUM) added in measurement
- 8734 — trillion per liter (UCUM) added in measurement
- 8736 — nanomole per liter (UCUM) added in measurement
- 8737 — percent hemoglobin (UCUM) added in measurement
- 8739 — pound (US) (UCUM) added in measurement
- 8748 — microgram per liter (UCUM) added in measurement
- 8749 — micromole per liter (UCUM) added in measurement
- 8751 — milligram per liter (UCUM) added in measurement
- 8752 — millimeter per hour (UCUM) added in measurement
- 8753 — millimole per liter (UCUM) added in measurement
- 8763 — unit per milliliter (UCUM) added in measurement
- 8784 — cells per microliter (UCUM) added in measurement
- 8786 — per high power field (UCUM) added in measurement
- 8795 — milliliter per minute (UCUM) added in measurement
- 8799 — copies per milliliter (UCUM) added in measurement
- 8807 — gram per 24 hours (UCUM) added in measurement
- 8810 — kilounit per liter (UCUM) added in measurement
- 8842 — nanogram per milliliter (UCUM) added in measurement
- 8859 — microgram per milliliter (UCUM) added in measurement
- 8862 — milliosmole per kilogram (UCUM) added in measurement
- 8876 — millimeter mercury column (UCUM) added in measurement
- 8907 — micromole per 24 hours (UCUM) added in measurement
- 8909 — milligram per 24 hours (UCUM) added in measurement
- 8910 — millimole per 24 hours (UCUM) added in measurement
- 8923 — international unit per liter (UCUM) added in measurement
- 8930 — milliliter per 24 hours (UCUM) added in measurement
- 8985 — international unit per milliliter (UCUM) added in measurement
- 9032 — per 100 white blood cells (UCUM) added in measurement
- 9040 — milli-international unit per liter (UCUM) added in measurement
- 9058 — kilo-international unit per liter (UCUM) added in measurement
- 9154 — parts per thousand (UCUM) added in measurement
- 9211 — minute (UCUM) added in measurement
- 9234 — volume percent (UCUM) added in measurement
- 9334 — international unit per gram of hemoglobin (UCUM) added in measurement
- 9384 — point (UCUM) added in measurement
- 9387 — parts per million (UCUM) added in measurement
- 9387 — parts per million (UCUM) added in observation
- 9442 — million per liter (UCUM) added in measurement
- 9444 — billion per liter (UCUM) added in measurement
- 9448 — year (UCUM) added in measurement
- 9454 — standard atmosphere (UCUM) added in measurement
- 9483 — square centimeter (UCUM) added in measurement
- 9484 — degree (UCUM) added in measurement
- 9498 — femtomole (UCUM) added in measurement
- 9508 — gram per 100 gram (UCUM) added in measurement
- 9512 — gram per kilogram (UCUM) added in measurement
- 9514 — gram per milliliter (UCUM) added in measurement
- 9529 — kilogram (UCUM) added in measurement
- 9530 — kilogram per liter (UCUM) added in measurement
- 9531 — kilogram per square meter (UCUM) added in measurement
- 9546 — meter (UCUM) added in measurement
- 9550 — milli-international unit per milliliter (UCUM) added in measurement
- 9557 — milliequivalent per liter (UCUM) added in measurement
- 9569 — milliliter per heart beat (UCUM) added in measurement
- 9570 — milliliter per deciliter (UCUM) added in measurement
- 9571 — milliliter per kilogram (UCUM) added in measurement
- 9573 — millimole (UCUM) added in measurement
- 9574 — millimole per total volume (UCUM) added in measurement
- 9579 — millimole per mole (UCUM) added in measurement
- 9586 — mole per liter (UCUM) added in measurement
- 9593 — millisecond (UCUM) added in measurement
- 9626 — picogram per millimeter (UCUM) added in measurement
- 9667 — micromole (UCUM) added in measurement
- 9674 — micromole per mole (UCUM) added in measurement
- 9677 — volt (UCUM) added in measurement
- 9678 — watt (UCUM) added in measurement
- 9687 — international unit per hour (UCUM) added in measurement
- 22350 — Edema of larynx (SNOMED) added in condition_occurrence
- 22856 — Polyglandular dysfunction (SNOMED) added in condition_occurrence
- 22955 — Perforation of esophagus (SNOMED) added in condition_occurrence
- 23220 — Chronic tonsillitis (SNOMED) added in condition_occurrence
- 23325 — Heartburn (SNOMED) added in condition_occurrence
- 23986 — Disorder of pituitary gland (SNOMED) added in condition_occurrence
- 24609 — Hypoglycemia (SNOMED) added in condition_occurrence
- 24818 — Injury of neck (SNOMED) added in condition_occurrence
- 24974 — Stenosis of larynx (SNOMED) added in condition_occurrence
- 24977 — Mucocele of salivary gland (SNOMED) added in condition_occurrence
- 25189 — Malignant tumor of oral cavity (SNOMED) added in condition_occurrence
- 25297 — Acute pharyngitis (SNOMED) added in condition_occurrence
- 26052 — Primary malignant neoplasm of larynx (SNOMED) added in condition_occurrence
- 26638 — Primary malignant neoplasm of esophagus (SNOMED) added in condition_occurrence
- 26711 — Chronic pharyngitis (SNOMED) added in condition_occurrence
- 26727 — Hematemesis (SNOMED) added in condition_occurrence
- 26935 — Disorder of endocrine testis (SNOMED) added in condition_occurrence
- 26942 — Hemoglobin SS disease with crisis (SNOMED) added in condition_occurrence
- 27674 — Nausea and vomiting (SNOMED) added in condition_occurrence
- 28109 — Carcinoma in situ of esophagus (SNOMED) added in condition_occurrence
- 28457 — Hypertrophy of tonsils (SNOMED) added in condition_occurrence
- 28779 — Bleeding esophageal varices (SNOMED) added in condition_occurrence
- 30133 — Acute laryngitis (SNOMED) added in condition_occurrence
- 30356 — Benign neoplasm of pharynx (SNOMED) added in condition_occurrence
- 30437 — Gastro-esophageal reflux disease with esophagitis (SNOMED) added in condition_occurrence
- 30753 — Esophagitis (SNOMED) added in condition_occurrence
- 31317 — Dysphagia (SNOMED) added in condition_occurrence
- 31610 — Disorder of esophagus (SNOMED) added in condition_occurrence
- 31821 — Disorder of endocrine system (SNOMED) added in condition_occurrence
- 31884 — Acquired diverticulum of esophagus (SNOMED) added in condition_occurrence
- 32037 — Intensive Care (Visit) added in visit_detail
- 32703 — dyne-second per centimeter to the fifth power (UCUM) added in measurement
- 32710 — liter per minute per square meter (UCUM) added in measurement
- 32739 — milliliter per square meter (UCUM) added in measurement
- 32890 — Admission diagnosis (Condition Status) added in condition_occurrence
- 32912 — Generic unit for indivisible thing (UCUM) added in measurement
- 32963 — liter per square meter (UCUM) added in measurement
- 33117 — per nanoliter (UCUM) added in measurement
- 33118 — per picoliter (UCUM) added in measurement
- 72576 — Benign neoplasm of breast (SNOMED) added in condition_occurrence
- 72988 — Pyogenic arthritis of hand (SNOMED) added in condition_occurrence
- 73001 — Myositis (SNOMED) added in condition_occurrence
- 73008 — Enthesopathy (SNOMED) added in condition_occurrence
- 73183 — Myotonic disorder (SNOMED) added in condition_occurrence
- 73300 — Radial styloid tenosynovitis (SNOMED) added in condition_occurrence
- 73349 — Injury of rectum without open wound into abdominal cavity (SNOMED) added in condition_occurrence
- 73571 — Pathological fracture (SNOMED) added in condition_occurrence
- 74125 — Inflammatory polyarthropathy (SNOMED) added in condition_occurrence
- 74188 — Closed fracture of rib (SNOMED) added in condition_occurrence
- 74582 — Primary malignant neoplasm of rectum (SNOMED) added in condition_occurrence
- 74635 — Lumbosacral radiculopathy (SNOMED) added in condition_occurrence
- 74731 — Hypertrophic osteoarthropathy (SNOMED) added in condition_occurrence
- 75036 — Localized, primary osteoarthritis of the hand (SNOMED) added in condition_occurrence
- 75311 — Fibrosclerosis of breast (SNOMED) added in condition_occurrence
- 75344 — Intervertebral disc disorder (SNOMED) added in condition_occurrence
- 75512 — Carcinoma in situ of colon (SNOMED) added in condition_occurrence
- 75860 — Constipation (SNOMED) added in condition_occurrence
- 75865 — Disorder of urinary system (SNOMED) added in condition_occurrence
- 75909 — Disorder of bone (SNOMED) added in condition_occurrence
- 75910 — Osteitis deformans (SNOMED) added in condition_occurrence
- 75911 — Acquired hallux valgus (SNOMED) added in condition_occurrence
- 76196 — Palindromic rheumatism (SNOMED) added in condition_occurrence
- 76482 — Missed miscarriage (SNOMED) added in condition_occurrence
- 76685 — Myasthenia gravis (SNOMED) added in condition_occurrence
- 76725 — Anal fissure (SNOMED) added in condition_occurrence
- 77030 — Disorder of breast (SNOMED) added in condition_occurrence
- 77074 — Pain of joint (SNOMED) added in condition_occurrence
- 77076 — Diastasis of muscle (SNOMED) added in condition_occurrence
- 77079 — Spinal stenosis (SNOMED) added in condition_occurrence
- 77234 — Benign neoplasm of colon (SNOMED) added in condition_occurrence
- 77630 — Disorder of shoulder (SNOMED) added in condition_occurrence
- 77644 — Adhesive capsulitis of shoulder (SNOMED) added in condition_occurrence
- 77670 — Chest pain (SNOMED) added in condition_occurrence
- 77961 — Disseminated idiopathic skeletal hyperostosis (SNOMED) added in condition_occurrence
- 78093 — Primary malignant neoplasm of pleura (SNOMED) added in condition_occurrence
- 78200 — Benign mammary dysplasia (SNOMED) added in condition_occurrence
- 78228 — Joint derangement (SNOMED) added in condition_occurrence
- 78474 — Hypertrophy of breast (SNOMED) added in condition_occurrence
- 78619 — Contusion of knee (SNOMED) added in condition_occurrence
- 78829 — Pyogenic arthritis of the ankle and/or foot (SNOMED) added in condition_occurrence
- 79833 — Ménière's disease (SNOMED) added in condition_occurrence
- 79864 — Hematuria syndrome (SNOMED) added in condition_occurrence
- 79916 — Acquired hallux rigidus (SNOMED) added in condition_occurrence
- 79936 — Polyuria (SNOMED) added in condition_occurrence
- 79938 — Closed fracture of scapula (SNOMED) added in condition_occurrence
- 80045 — Primary malignant neoplasm of anus (SNOMED) added in condition_occurrence
- 80141 — Functional diarrhea (SNOMED) added in condition_occurrence
- 80182 — Dermatomyositis (SNOMED) added in condition_occurrence
- 80482 — Suppurative arthritis (SNOMED) added in condition_occurrence
- 80484 — Crystal arthropathy (SNOMED) added in condition_occurrence
- 80502 — Osteoporosis (SNOMED) added in condition_occurrence
- 80665 — Malignant neoplasm of thorax (SNOMED) added in condition_occurrence
- 80800 — Polymyositis (SNOMED) added in condition_occurrence
- 80809 — Rheumatoid arthritis (SNOMED) added in condition_occurrence
- 81099 — Pyogenic arthritis of shoulder region (SNOMED) added in condition_occurrence
- 81151 — Sprain of ankle (SNOMED) added in condition_occurrence
- 81175 — Contusion of chest (SNOMED) added in condition_occurrence
- 81250 — Carcinoma in situ of breast (SNOMED) added in condition_occurrence
- 81390 — Idiopathic osteoporosis (SNOMED) added in condition_occurrence
- 81611 — Diverticular disease of colon (SNOMED) added in condition_occurrence
- 81878 — Benign paroxysmal positional vertigo (SNOMED) added in condition_occurrence
- 81893 — Ulcerative colitis (SNOMED) added in condition_occurrence
- 81902 — Urinary tract infectious disease (SNOMED) added in condition_occurrence
- 132412 — Post-laminectomy syndrome (SNOMED) added in condition_occurrence
- 132702 — Erythema multiforme (SNOMED) added in condition_occurrence
- 132703 — Lichen planus (SNOMED) added in condition_occurrence
- 132797 — Sepsis (SNOMED) added in condition_occurrence
- 133141 — Tinea pedis (SNOMED) added in condition_occurrence
- 133147 — Primary malignant neoplasm of skin of trunk (SNOMED) added in condition_occurrence
- 133283 — Pyoderma gangrenosum (SNOMED) added in condition_occurrence
- 133424 — Primary malignant neoplasm of thyroid gland (SNOMED) added in condition_occurrence
- 133436 — Thyrotoxic crisis (SNOMED) added in condition_occurrence
- 133566 — Necrotizing fasciitis (SNOMED) added in condition_occurrence
- 133691 — Meningococcemia (SNOMED) added in condition_occurrence
- 133713 — Malignant melanoma of skin of face (SNOMED) added in condition_occurrence
- 133729 — Hyperparathyroidism (SNOMED) added in condition_occurrence
- 134057 — Disorder of cardiovascular system (SNOMED) added in condition_occurrence
- 134159 — Precordial pain (SNOMED) added in condition_occurrence
- 134304 — Benign neoplasm of parathyroid gland (SNOMED) added in condition_occurrence
- 134305 — Acute lymphoid leukemia (SNOMED) added in condition_occurrence
- 134442 — Systemic sclerosis (SNOMED) added in condition_occurrence
- 134603 — Chronic myeloid leukemia (SNOMED) added in condition_occurrence
- 134668 — Chronic maxillary sinusitis (SNOMED) added in condition_occurrence
- 134681 — Diffuse spasm of esophagus (SNOMED) added in condition_occurrence
- 134738 — Acute osteomyelitis of multiple sites (SNOMED) added in condition_occurrence
- 134870 — Pityriasis versicolor (SNOMED) added in condition_occurrence
- 134898 — Non-toxic uninodular goiter (SNOMED) added in condition_occurrence
- 135214 — Polycythemia vera (clinical) (SNOMED) added in condition_occurrence
- 135526 — Spinal cord disease (SNOMED) added in condition_occurrence
- 135618 — Pruritic rash (SNOMED) added in condition_occurrence
- 135777 — Neoplasm of uncertain behavior of skin (SNOMED) added in condition_occurrence
- 135778 — Toxic multinodular goiter (SNOMED) added in condition_occurrence
- 136368 — Non-toxic multinodular goiter (SNOMED) added in condition_occurrence
- 136496 — Cellulitis and abscess of face (SNOMED) added in condition_occurrence
- 136497 — Scar conditions and fibrosis of skin (SNOMED) added in condition_occurrence
- 136580 — Dehiscence of surgical wound (SNOMED) added in condition_occurrence
- 136788 — Spinal stenosis of lumbar region (SNOMED) added in condition_occurrence
- 136917 — Primary malignant neoplasm of skin of face (SNOMED) added in condition_occurrence
- 136934 — Primary hyperparathyroidism (SNOMED) added in condition_occurrence
- 136960 — Vascular myelopathy (SNOMED) added in condition_occurrence
- 137005 — Tracheostomy complication (SNOMED) added in condition_occurrence
- 137053 — Seborrheic dermatitis (SNOMED) added in condition_occurrence
- 137077 — Chronic osteomyelitis of ankle and/or foot (SNOMED) added in condition_occurrence
- 137275 — Disorder of muscle (SNOMED) added in condition_occurrence
- 137548 — Cervical radiculopathy (SNOMED) added in condition_occurrence
- 137682 — Skin sensation disturbance (SNOMED) added in condition_occurrence
- 137813 — Benign neoplasm of mouth region (SNOMED) added in condition_occurrence
- 137900 — Acute sphenoidal sinusitis (SNOMED) added in condition_occurrence
- 138346 — Erysipelas (SNOMED) added in condition_occurrence
- 138379 — Chronic lymphoid leukemia, disease (SNOMED) added in condition_occurrence
- 138387 — Thyrotoxicosis (SNOMED) added in condition_occurrence
- 138388 — Secondary hyperparathyroidism (SNOMED) added in condition_occurrence
- 138455 — Stomatitis (SNOMED) added in condition_occurrence
- 138525 — Pain in limb (SNOMED) added in condition_occurrence
- 138717 — Toxic diffuse goiter (SNOMED) added in condition_occurrence
- 138825 — Actinic keratosis (SNOMED) added in condition_occurrence
- 138994 — Myelodysplastic syndrome (clinical) (SNOMED) added in condition_occurrence
- 139099 — Ingrowing nail (SNOMED) added in condition_occurrence
- 139737 — Pediculosis corporis (SNOMED) added in condition_occurrence
- 139750 — Primary malignant neoplasm of skin (SNOMED) added in condition_occurrence
- 139900 — Urticaria (SNOMED) added in condition_occurrence
- 140352 — Acute myeloid leukemia, disease (SNOMED) added in condition_occurrence
- 140362 — Hypoparathyroidism (SNOMED) added in condition_occurrence
- 140673 — Hypothyroidism (SNOMED) added in condition_occurrence
- 140821 — Spasm (SNOMED) added in condition_occurrence
- 140949 — Infestation by Sarcoptes scabiei var hominis (SNOMED) added in condition_occurrence
- 141004 — Lesion of radial nerve (SNOMED) added in condition_occurrence
- 141095 — Acne (SNOMED) added in condition_occurrence
- 141249 — Benign neoplasm of thyroid gland (SNOMED) added in condition_occurrence
- 141253 — Disorder of thyroid gland (SNOMED) added in condition_occurrence
- 141456 — Chilblains (SNOMED) added in condition_occurrence
- 141663 — Osteomyelitis (SNOMED) added in condition_occurrence
- 141825 — Simple goiter (SNOMED) added in condition_occurrence
- 192273 — Benign neoplasm of adrenal gland (SNOMED) added in condition_occurrence
- 192353 — Disorder of gallbladder (SNOMED) added in condition_occurrence
- 192357 — Paralytic ileus (SNOMED) added in condition_occurrence
- 192359 — Renal failure syndrome (SNOMED) added in condition_occurrence
- 192367 — Dysplasia of cervix (SNOMED) added in condition_occurrence
- 192450 — Retention of urine (SNOMED) added in condition_occurrence
- 192671 — Gastrointestinal hemorrhage (SNOMED) added in condition_occurrence
- 192673 — Vascular insufficiency of intestine (SNOMED) added in condition_occurrence
- 192675 — Biliary cirrhosis (SNOMED) added in condition_occurrence
- 192676 — Cervical intraepithelial neoplasia grade 1 (SNOMED) added in condition_occurrence
- 192680 — Portal hypertension (SNOMED) added in condition_occurrence
- 192683 — Uterovaginal prolapse (SNOMED) added in condition_occurrence
- 192953 — Intestinal adhesions with obstruction (SNOMED) added in condition_occurrence
- 192956 — Cholecystitis (SNOMED) added in condition_occurrence
- 192957 — Perforation of bile duct (SNOMED) added in condition_occurrence
- 192963 — Disorder of pancreas (SNOMED) added in condition_occurrence
- 193165 — Disorder of adrenal gland (SNOMED) added in condition_occurrence
- 193242 — Perforation of intestine (SNOMED) added in condition_occurrence
- 193262 — Inflammatory disorder of penis (SNOMED) added in condition_occurrence
- 193402 — Bacterial enteritis of intestine (SNOMED) added in condition_occurrence
- 193439 — Benign neoplasm of body of uterus (SNOMED) added in condition_occurrence
- 193518 — Intestinal obstruction (SNOMED) added in condition_occurrence
- 193520 — Urinary bladder stone (SNOMED) added in condition_occurrence
- 193666 — Injury of hip region (SNOMED) added in condition_occurrence
- 193688 — Clostridioides difficile infection (SNOMED) added in condition_occurrence
- 193722 — Benign tumor of endocrine pancreas (SNOMED) added in condition_occurrence
- 193871 — Genuine stress incontinence (SNOMED) added in condition_occurrence
- 194071 — Pylorospasm (SNOMED) added in condition_occurrence
- 194081 — Acute cystitis (SNOMED) added in condition_occurrence
- 194406 — Urinary tract obstruction (SNOMED) added in condition_occurrence
- 194408 — Hydroureter (SNOMED) added in condition_occurrence
- 194421 — Endometriosis of intestine (SNOMED) added in condition_occurrence
- 194526 — Injury of trunk (SNOMED) added in condition_occurrence
- 194589 — Primary malignant neoplasm of biliary tract (SNOMED) added in condition_occurrence
- 194683 — Obstructed umbilical hernia (SNOMED) added in condition_occurrence
- 194710 — Placenta previa without hemorrhage (SNOMED) added in condition_occurrence
- 194807 — Injury of inferior vena cava (SNOMED) added in condition_occurrence
- 194984 — Disease of liver (SNOMED) added in condition_occurrence
- 194987 — Hourglass contraction of stomach (SNOMED) added in condition_occurrence
- 194990 — Inflammatory disease of liver (SNOMED) added in condition_occurrence
- 194993 — Intestinal malabsorption (SNOMED) added in condition_occurrence
- 194995 — Disorder of ureter (SNOMED) added in condition_occurrence
- 194997 — Prostatitis (SNOMED) added in condition_occurrence
- 195009 — Leukoplakia of penis (SNOMED) added in condition_occurrence
- 195197 — Primary malignant neoplasm of vulva (SNOMED) added in condition_occurrence
- 195301 — Acute dilatation of stomach (SNOMED) added in condition_occurrence
- 195313 — Urethral abscess (SNOMED) added in condition_occurrence
- 195314 — Nephrotic syndrome (SNOMED) added in condition_occurrence
- 195321 — Postmenopausal bleeding (SNOMED) added in condition_occurrence
- 195363 — Congenital anomaly of the kidney (SNOMED) added in condition_occurrence
- 195401 — Contusion of hip (SNOMED) added in condition_occurrence
- 195480 — Primary malignant neoplasm of renal pelvis (SNOMED) added in condition_occurrence
- 195498 — Benign neoplasm of kidney (SNOMED) added in condition_occurrence
- 195500 — Benign neoplasm of uterus (SNOMED) added in condition_occurrence
- 195559 — Ruptured abdominal aortic aneurysm (SNOMED) added in condition_occurrence
- 195562 — Hemorrhoids (SNOMED) added in condition_occurrence
- 195588 — Cystitis (SNOMED) added in condition_occurrence
- 195590 — Urethral stricture (SNOMED) added in condition_occurrence
- 195596 — Chronic pancreatitis (SNOMED) added in condition_occurrence
- 195603 — Vulval and/or perineal noninflammatory disorders (SNOMED) added in condition_occurrence
- 195770 — Subserous leiomyoma of uterus (SNOMED) added in condition_occurrence
- 195793 — Neoplasm of uncertain behavior of uterus (SNOMED) added in condition_occurrence
- 195856 — Cholangitis (SNOMED) added in condition_occurrence
- 196044 — Primary malignant neoplasm of stomach (SNOMED) added in condition_occurrence
- 196048 — Primary malignant neoplasm of vagina (SNOMED) added in condition_occurrence
- 196151 — Functional disorder of intestine (SNOMED) added in condition_occurrence
- 196152 — Peritonitis (SNOMED) added in condition_occurrence
- 196160 — Fistula of intestine (SNOMED) added in condition_occurrence
- 196168 — Irregular periods (SNOMED) added in condition_occurrence
- 196359 — Primary malignant neoplasm of uterine cervix (SNOMED) added in condition_occurrence
- 196360 — Primary malignant neoplasm of urinary bladder (SNOMED) added in condition_occurrence
- 196431 — Hypersensitivity angiitis (SNOMED) added in condition_occurrence
- 196454 — Colostomy and enterostomy malfunction (SNOMED) added in condition_occurrence
- 196455 — Hepatorenal syndrome (SNOMED) added in condition_occurrence
- 196463 — Alcoholic cirrhosis (SNOMED) added in condition_occurrence
- 196469 — Perforation of gallbladder (SNOMED) added in condition_occurrence
- 196724 — Disorder of diaphragm (SNOMED) added in condition_occurrence
- 196738 — Disorder of male genital organ (SNOMED) added in condition_occurrence
- 196751 — Placenta previa with hemorrhage (SNOMED) added in condition_occurrence
- 197034 — Intussusception of intestine (SNOMED) added in condition_occurrence
- 197037 — Spontaneous rupture of urinary bladder (SNOMED) added in condition_occurrence
- 197044 — Female infertility associated with anovulation (SNOMED) added in condition_occurrence
- 197136 — Injury of small intestine without open wound into abdominal cavity (SNOMED) added in condition_occurrence
- 197151 — Injury of abdominal aorta (SNOMED) added in condition_occurrence
- 197230 — Malignant neoplasm of uterus (SNOMED) added in condition_occurrence
- 197236 — Uterine leiomyoma (SNOMED) added in condition_occurrence
- 197237 — Benign neoplasm of prostate (SNOMED) added in condition_occurrence
- 197253 — Hemolytic uremic syndrome (SNOMED) added in condition_occurrence
- 197304 — Ulcer of lower extremity (SNOMED) added in condition_occurrence
- 197320 — Acute kidney injury (SNOMED) added in condition_occurrence
- 197500 — Primary malignant neoplasm of colon (SNOMED) added in condition_occurrence
- 197593 — Impaction of intestine (SNOMED) added in condition_occurrence
- 197596 — Toxic gastroenteritis (SNOMED) added in condition_occurrence
- 197601 — Spermatocele (SNOMED) added in condition_occurrence
- 197603 — Intestinal volvulus (SNOMED) added in condition_occurrence
- 197605 — Inflammatory disorder of male genital organ (SNOMED) added in condition_occurrence
- 197607 — Excessive and frequent menstruation (SNOMED) added in condition_occurrence
- 197610 — Cyst of ovary (SNOMED) added in condition_occurrence
- 197672 — Urinary incontinence (SNOMED) added in condition_occurrence
- 197675 — Incontinence of feces (SNOMED) added in condition_occurrence
- 197684 — Dysuria (SNOMED) added in condition_occurrence
- 197917 — Disorder of biliary tract (SNOMED) added in condition_occurrence
- 198010 — Injury of stomach without open wound into abdominal cavity (SNOMED) added in condition_occurrence
- 198019 — Iliac blood vessel injury (SNOMED) added in condition_occurrence
- 198177 — Abdominal aortic aneurysm (SNOMED) added in condition_occurrence
- 198199 — Pyelonephritis (SNOMED) added in condition_occurrence
- 198202 — Cystocele (SNOMED) added in condition_occurrence
- 198401 — Neoplasm of uncertain behavior of urinary bladder (SNOMED) added in condition_occurrence
- 198402 — Neoplasm of uncertain behavior of kidney (SNOMED) added in condition_occurrence
- 198446 — Embolism and thrombosis of the abdominal aorta (SNOMED) added in condition_occurrence
- 198464 — Incisional hernia (SNOMED) added in condition_occurrence
- 198465 — Acquired megacolon (SNOMED) added in condition_occurrence
- 198475 — Gallstone ileus (SNOMED) added in condition_occurrence
- 198571 — Cardiogenic shock (SNOMED) added in condition_occurrence
- 198803 — Benign prostatic hyperplasia (SNOMED) added in condition_occurrence
- 198809 — Acute cholecystitis (SNOMED) added in condition_occurrence
- 198892 — Internal injury of abdominal organs without open wound into cavity (SNOMED) added in condition_occurrence
- 198985 — Primary malignant neoplasm of kidney (SNOMED) added in condition_occurrence
- 198988 — Primary malignant neoplasm of pelvis (SNOMED) added in condition_occurrence
- 199064 — Chronic vascular insufficiency of intestine (SNOMED) added in condition_occurrence
- 199074 — Acute pancreatitis (SNOMED) added in condition_occurrence
- 199075 — Neurogenic urinary bladder (SNOMED) added in condition_occurrence
- 199754 — Primary malignant neoplasm of pancreas (SNOMED) added in condition_occurrence
- 199764 — Benign neoplasm of ovary (SNOMED) added in condition_occurrence
- 199837 — Portal vein thrombosis (SNOMED) added in condition_occurrence
- 199860 — Hernia of abdominal cavity (SNOMED) added in condition_occurrence
- 199868 — Incisional hernia with gangrene (SNOMED) added in condition_occurrence
- 200051 — Primary malignant neoplasm of ovary (SNOMED) added in condition_occurrence
- 200052 — Primary malignant neoplasm of uterine adnexa (SNOMED) added in condition_occurrence
- 200054 — Primary malignant neoplasm of ureter (SNOMED) added in condition_occurrence
- 200174 — Disorder of skin and/or subcutaneous tissue (SNOMED) added in condition_occurrence
- 200219 — Abdominal pain (SNOMED) added in condition_occurrence
- 200447 — Gastrointestinal complication (SNOMED) added in condition_occurrence
- 200527 — Splenomegaly (SNOMED) added in condition_occurrence
- 200588 — Injury of abdomen (SNOMED) added in condition_occurrence
- 200675 — Neoplasm of uncertain behavior of ovary (SNOMED) added in condition_occurrence
- 200765 — Chronic cholecystitis (SNOMED) added in condition_occurrence
- 200831 — Congenital anomaly of penis (SNOMED) added in condition_occurrence
- 200962 — Primary malignant neoplasm of prostate (SNOMED) added in condition_occurrence
- 201061 — Diaphragmatic hernia (SNOMED) added in condition_occurrence
- 201066 — Obstruction of bile duct (SNOMED) added in condition_occurrence
- 201254 — Type 1 diabetes mellitus (SNOMED) added in condition_occurrence
- 201265 — Disorder of spleen (SNOMED) added in condition_occurrence
- 201337 — Disorder of urinary bladder (SNOMED) added in condition_occurrence
- 201338 — Urethral fistula (SNOMED) added in condition_occurrence
- 201341 — Incisional hernia with obstruction (SNOMED) added in condition_occurrence
- 201353 — Radiation cystitis (SNOMED) added in condition_occurrence
- 201529 — Neoplasm of uncertain behavior of stomach (SNOMED) added in condition_occurrence
- 201606 — Crohn's disease (SNOMED) added in condition_occurrence
- 201618 — Disorder of intestine (SNOMED) added in condition_occurrence
- 201620 — Kidney stone (SNOMED) added in condition_occurrence
- 201622 — Prostatic congestion or hemorrhage (SNOMED) added in condition_occurrence
- 201690 — Renal colic (SNOMED) added in condition_occurrence
- 201820 — Diabetes mellitus (SNOMED) added in condition_occurrence
- 201824 — Benign neoplasm of urinary bladder (SNOMED) added in condition_occurrence
- 201826 — Type 2 diabetes mellitus (SNOMED) added in condition_occurrence
- 201894 — Acute vascular insufficiency of intestine (SNOMED) added in condition_occurrence
- 201909 — Female infertility (SNOMED) added in condition_occurrence
- 201916 — Ureteric stone (SNOMED) added in condition_occurrence
- 201956 — Congenital anomaly of lower limb (SNOMED) added in condition_occurrence
- 201965 — Shock (SNOMED) added in condition_occurrence
- 252280 — Neoplasm of respiratory tract (SNOMED) added in condition_occurrence
- 253321 — Stridor (SNOMED) added in condition_occurrence
- 253549 — Disorder of connective tissue (SNOMED) added in condition_occurrence
- 253796 — Pneumothorax (SNOMED) added in condition_occurrence
- 254061 — Pleural effusion (SNOMED) added in condition_occurrence
- 254068 — Disorder of upper respiratory system (SNOMED) added in condition_occurrence
- 254443 — Sjögren's syndrome (SNOMED) added in condition_occurrence
- 254761 — Cough (SNOMED) added in condition_occurrence
- 255302 — Spontaneous pneumothorax (SNOMED) added in condition_occurrence
- 255348 — Polymyalgia rheumatica (SNOMED) added in condition_occurrence
- 255573 — Chronic obstructive pulmonary disease (SNOMED) added in condition_occurrence
- 255841 — Chronic bronchitis (SNOMED) added in condition_occurrence
- 255848 — Pneumonia (SNOMED) added in condition_occurrence
- 256449 — Bronchiectasis (SNOMED) added in condition_occurrence
- 256722 — Bronchopneumonia (SNOMED) added in condition_occurrence
- 256723 — Pneumonia and influenza (SNOMED) added in condition_occurrence
- 257007 — Allergic rhinitis (SNOMED) added in condition_occurrence
- 257008 — Parapharyngeal abscess (SNOMED) added in condition_occurrence
- 257011 — Acute upper respiratory infection (SNOMED) added in condition_occurrence
- 257012 — Chronic sinusitis (SNOMED) added in condition_occurrence
- 257293 — Disorder of visual pathways (SNOMED) added in condition_occurrence
- 257315 — Bacterial pneumonia (SNOMED) added in condition_occurrence
- 257628 — Systemic lupus erythematosus (SNOMED) added in condition_occurrence
- 257907 — Disorder of lung (SNOMED) added in condition_occurrence
- 259748 — Primary malignant neoplasm of accessory sinus (SNOMED) added in condition_occurrence
- 259848 — Chronic rhinitis (SNOMED) added in condition_occurrence
- 260131 — Disorder of bronchus (SNOMED) added in condition_occurrence
- 261116 — Acquired deformity of nose (SNOMED) added in condition_occurrence
- 261255 — Benign neoplasm of bronchus and lung (SNOMED) added in condition_occurrence
- 261325 — Pulmonary emphysema (SNOMED) added in condition_occurrence
- 261326 — Viral pneumonia (SNOMED) added in condition_occurrence
- 261687 — Hemoptysis (SNOMED) added in condition_occurrence
- 261880 — Atelectasis (SNOMED) added in condition_occurrence
- 312327 — Acute myocardial infarction (SNOMED) added in condition_occurrence
- 312336 — Arterial aneurysm (SNOMED) added in condition_occurrence
- 312337 — Arterial embolus and thrombosis (SNOMED) added in condition_occurrence
- 312437 — Dyspnea (SNOMED) added in condition_occurrence
- 312902 — Benign intracranial hypertension (SNOMED) added in condition_occurrence
- 312934 — Atherosclerosis of aorta (SNOMED) added in condition_occurrence
- 312938 — Hypertensive encephalopathy (SNOMED) added in condition_occurrence
- 313217 — Atrial fibrillation (SNOMED) added in condition_occurrence
- 313459 — Sleep apnea (SNOMED) added in condition_occurrence
- 314054 — Aortic valve disorder (SNOMED) added in condition_occurrence
- 314059 — Right bundle branch block (SNOMED) added in condition_occurrence
- 314379 — First degree atrioventricular block (SNOMED) added in condition_occurrence
- 314658 — Cardiomegaly (SNOMED) added in condition_occurrence
- 314659 — Arteritis (SNOMED) added in condition_occurrence
- 314963 — Giant cell arteritis (SNOMED) added in condition_occurrence
- 315078 — Palpitations (SNOMED) added in condition_occurrence
- 315116 — Injury of carotid artery (SNOMED) added in condition_occurrence
- 315273 — Mitral valve stenosis (SNOMED) added in condition_occurrence
- 315286 — Chronic ischemic heart disease (SNOMED) added in condition_occurrence
- 315296 — Preinfarction syndrome (SNOMED) added in condition_occurrence
- 315564 — Aortic valve regurgitation (SNOMED) added in condition_occurrence
- 315586 — Priapism (SNOMED) added in condition_occurrence
- 316135 — Atrioventricular block (SNOMED) added in condition_occurrence
- 316139 — Heart failure (SNOMED) added in condition_occurrence
- 316457 — Mallory-Weiss syndrome (SNOMED) added in condition_occurrence
- 316814 — Hyperventilation (SNOMED) added in condition_occurrence
- 316822 — Heart murmur (SNOMED) added in condition_occurrence
- 316866 — Hypertensive disorder (SNOMED) added in condition_occurrence
- 316998 — Left bundle branch block (SNOMED) added in condition_occurrence
- 316999 — Conduction disorder of the heart (SNOMED) added in condition_occurrence
- 317002 — Low blood pressure (SNOMED) added in condition_occurrence
- 317003 — Compression of vein (SNOMED) added in condition_occurrence
- 317009 — Asthma (SNOMED) added in condition_occurrence
- 317109 — Respiratory arrest (SNOMED) added in condition_occurrence
- 317248 — Disorder of hematopoietic structure (SNOMED) added in condition_occurrence
- 317299 — Disorder of vitreous body (SNOMED) added in condition_occurrence
- 317305 — Stricture of artery (SNOMED) added in condition_occurrence
- 317510 — Leukemia (SNOMED) added in condition_occurrence
- 317585 — Aortic aneurysm (SNOMED) added in condition_occurrence
- 317814 — Benign neoplasm of heart (SNOMED) added in condition_occurrence
- 317895 — Renovascular hypertension (SNOMED) added in condition_occurrence
- 318448 — Second degree atrioventricular block (SNOMED) added in condition_occurrence
- 318450 — Cardiac tamponade (SNOMED) added in condition_occurrence
- 318736 — Migraine (SNOMED) added in condition_occurrence
- 318772 — Disorder of pericardium (SNOMED) added in condition_occurrence
- 319034 — Hypertensive heart disease without congestive heart failure (SNOMED) added in condition_occurrence
- 319041 — Orthostatic hypotension (SNOMED) added in condition_occurrence
- 319826 — Secondary hypertension (SNOMED) added in condition_occurrence
- 319835 — Congestive heart failure (SNOMED) added in condition_occurrence
- 319844 — Acute ischemic heart disease (SNOMED) added in condition_occurrence
- 320073 — Neutropenia (SNOMED) added in condition_occurrence
- 320116 — Acute pericarditis (SNOMED) added in condition_occurrence
- 320128 — Essential hypertension (SNOMED) added in condition_occurrence
- 320136 — Disorder of respiratory system (SNOMED) added in condition_occurrence
- 320425 — Heart block (SNOMED) added in condition_occurrence
- 320563 — Injury of heart without open wound into thorax (SNOMED) added in condition_occurrence
- 320739 — Dissection of aorta (SNOMED) added in condition_occurrence
- 320741 — Thrombophlebitis (SNOMED) added in condition_occurrence
- 320744 — Complete atrioventricular block (SNOMED) added in condition_occurrence
- 321042 — Cardiac arrest (SNOMED) added in condition_occurrence
- 321052 — Peripheral vascular disease (SNOMED) added in condition_occurrence
- 321107 — Congenital insufficiency of aortic valve (SNOMED) added in condition_occurrence
- 321314 — Abdominal aortic aneurysm without rupture (SNOMED) added in condition_occurrence
- 321318 — Angina pectoris (SNOMED) added in condition_occurrence
- 321319 — Cardiomyopathy (SNOMED) added in condition_occurrence
- 321588 — Heart disease (SNOMED) added in condition_occurrence
- 321596 — Peripheral venous insufficiency (SNOMED) added in condition_occurrence
- 321710 — Contusion to heart (SNOMED) added in condition_occurrence
- 321822 — Peripheral vascular disorder due to diabetes mellitus (SNOMED) added in condition_occurrence
- 321886 — Rupture of artery (SNOMED) added in condition_occurrence
- 321887 — Disorder of artery (SNOMED) added in condition_occurrence
- 372324 — Eustachian tube disorder (SNOMED) added in condition_occurrence
- 372328 — Otitis media (SNOMED) added in condition_occurrence
- 372604 — Movement disorder (SNOMED) added in condition_occurrence
- 372635 — Corneal degeneration (SNOMED) added in condition_occurrence
- 372652 — Chronic tympanitis (SNOMED) added in condition_occurrence
- 372887 — Disorder of brain (SNOMED) added in condition_occurrence
- 372888 — Sciatic nerve lesion (SNOMED) added in condition_occurrence
- 372900 — Drug-induced dystonia (SNOMED) added in condition_occurrence
- 373175 — Organic hallucinosis (SNOMED) added in condition_occurrence
- 373176 — Organic mood disorder (SNOMED) added in condition_occurrence
- 373182 — Amyotrophic lateral sclerosis (SNOMED) added in condition_occurrence
- 373474 — Diplopia (SNOMED) added in condition_occurrence
- 373503 — Transient cerebral ischemia (SNOMED) added in condition_occurrence
- 373852 — Neuralgia (SNOMED) added in condition_occurrence
- 373995 — Delirium (SNOMED) added in condition_occurrence
- 374009 — Organic mental disorder (SNOMED) added in condition_occurrence
- 374027 — Lesion of ulnar nerve (SNOMED) added in condition_occurrence
- 374034 — Visual disturbance (SNOMED) added in condition_occurrence
- 374044 — Ptosis of eyelid (SNOMED) added in condition_occurrence
- 374221 — Injury of brachial plexus (SNOMED) added in condition_occurrence
- 374313 — Neoplasm of uncertain behavior of soft tissues (SNOMED) added in condition_occurrence
- 374360 — Disorder of optic nerve (SNOMED) added in condition_occurrence
- 374366 — Sensorineural hearing loss (SNOMED) added in condition_occurrence
- 374375 — Impacted cerumen (SNOMED) added in condition_occurrence
- 374377 — Paralytic syndrome (SNOMED) added in condition_occurrence
- 374640 — Serous retinal detachment (SNOMED) added in condition_occurrence
- 374915 — Focal epilepsy (SNOMED) added in condition_occurrence
- 374919 — Multiple sclerosis (SNOMED) added in condition_occurrence
- 374923 — Bell's palsy (SNOMED) added in condition_occurrence
- 375292 — Perforation of tympanic membrane (SNOMED) added in condition_occurrence
- 375415 — Injury of head (SNOMED) added in condition_occurrence
- 375519 — Alcohol withdrawal (SNOMED) added in condition_occurrence
- 375545 — Cataract (SNOMED) added in condition_occurrence
- 375551 — Blepharochalasis (SNOMED) added in condition_occurrence
- 375800 — Dystonia (SNOMED) added in condition_occurrence
- 375801 — Demyelinating disease of central nervous system (SNOMED) added in condition_occurrence
- 376063 — Benign neoplasm of cerebral meninges (SNOMED) added in condition_occurrence
- 376125 — Disorder of eyelid (SNOMED) added in condition_occurrence
- 376208 — Disorder of soft tissue (SNOMED) added in condition_occurrence
- 376337 — Disorder of nervous system (SNOMED) added in condition_occurrence
- 376382 — Tension-type headache (SNOMED) added in condition_occurrence
- 376387 — Spasmodic torticollis (SNOMED) added in condition_occurrence
- 376647 — Primary malignant neoplasm of soft tissues (SNOMED) added in condition_occurrence
- 377263 — Myoneural disorder (SNOMED) added in condition_occurrence
- 377266 — Non-organic disorder of the sleep-wake schedule (SNOMED) added in condition_occurrence
- 377270 — Hereditary retinal dystrophy (SNOMED) added in condition_occurrence
- 377573 — Central perforation of tympanic membrane (SNOMED) added in condition_occurrence
- 377574 — Presbycusis (SNOMED) added in condition_occurrence
- 377830 — Alcohol withdrawal delirium (SNOMED) added in condition_occurrence
- 377845 — Anoxic encephalopathy (SNOMED) added in condition_occurrence
- 377877 — Esotropia (SNOMED) added in condition_occurrence
- 377910 — Deviated nasal septum (SNOMED) added in condition_occurrence
- 378143 — Encephalitis (SNOMED) added in condition_occurrence
- 378253 — Headache (SNOMED) added in condition_occurrence
- 378414 — Retinal detachment (SNOMED) added in condition_occurrence
- 378416 — Retinal disorder (SNOMED) added in condition_occurrence
- 378419 — Alzheimer's disease (SNOMED) added in condition_occurrence
- 378439 — Fourth nerve palsy (SNOMED) added in condition_occurrence
- 378741 — Brachial plexus disorder (SNOMED) added in condition_occurrence
- 378756 — Conjunctival hemorrhage (SNOMED) added in condition_occurrence
- 379782 — Gilles de la Tourette's syndrome (SNOMED) added in condition_occurrence
- 379801 — Trigeminal neuralgia (SNOMED) added in condition_occurrence
- 379832 — Mixed conductive AND sensorineural hearing loss (SNOMED) added in condition_occurrence
- 380055 — Primary malignant neoplasm of brain (SNOMED) added in condition_occurrence
- 380094 — Carpal tunnel syndrome (SNOMED) added in condition_occurrence
- 380102 — Corneal edema (SNOMED) added in condition_occurrence
- 380378 — Epilepsy (SNOMED) added in condition_occurrence
- 380731 — Otitis externa (SNOMED) added in condition_occurrence
- 380834 — Coma (SNOMED) added in condition_occurrence
- 381270 — Parkinson's disease (SNOMED) added in condition_occurrence
- 381295 — Senile cataract (SNOMED) added in condition_occurrence
- 381316 — Cerebrovascular accident (SNOMED) added in condition_occurrence
- 381537 — Organic anxiety disorder (SNOMED) added in condition_occurrence
- 381549 — Migraine with aura (SNOMED) added in condition_occurrence
- 381551 — Polyneuropathy caused by drug (SNOMED) added in condition_occurrence
- 381572 — Abducens nerve palsy (SNOMED) added in condition_occurrence
- 381575 — Disorder of external ear (SNOMED) added in condition_occurrence
- 381581 — Chalazion (SNOMED) added in condition_occurrence
- 381591 — Cerebrovascular disease (SNOMED) added in condition_occurrence
- 381732 — Nerve injury (SNOMED) added in condition_occurrence
- 381854 — Disorder of conjunctiva (SNOMED) added in condition_occurrence
- 381859 — Infective otitis externa (SNOMED) added in condition_occurrence
- 381862 — Paralytic strabismus (SNOMED) added in condition_occurrence
- 432246 — Leptospirosis (SNOMED) added in condition_occurrence
- 432250 — Infectious disease (SNOMED) added in condition_occurrence
- 432257 — Primary malignant neoplasm of transverse colon (SNOMED) added in condition_occurrence
- 432262 — Primary malignant neoplasm of trachea (SNOMED) added in condition_occurrence
- 432307 — Disorder of vagus nerve (SNOMED) added in condition_occurrence
- 432456 — Alcohol intake - finding (SNOMED) added in observation
- 432545 — Bacterial infectious disease (SNOMED) added in condition_occurrence
- 432574 — Diffuse large B-cell lymphoma (SNOMED) added in condition_occurrence
- 432582 — Neoplastic disease of uncertain behavior (SNOMED) added in condition_occurrence
- 432585 — Blood coagulation disorder (SNOMED) added in condition_occurrence
- 432595 — Amyloidosis (SNOMED) added in condition_occurrence
- 432612 — Mild intellectual disability (SNOMED) added in condition_occurrence
- 432620 — Disorder of choroid of eye (SNOMED) added in condition_occurrence
- 432621 — Purulent endophthalmitis (SNOMED) added in condition_occurrence
- 432719 — Panniculitis (SNOMED) added in condition_occurrence
- 432791 — Angioedema (SNOMED) added in condition_occurrence
- 432795 — Traumatic or non-traumatic injury (SNOMED) added in condition_occurrence
- 432796 — Poisoning by anesthetic agent (SNOMED) added in condition_occurrence
- 432833 — Primary malignant neoplasm of oropharynx (SNOMED) added in condition_occurrence
- 432837 — Primary malignant neoplasm of cecum (SNOMED) added in condition_occurrence
- 432838 — Primary malignant neoplasm of cardia of stomach (SNOMED) added in condition_occurrence
- 432843 — Primary malignant neoplasm of tail of pancreas (SNOMED) added in condition_occurrence
- 432851 — Metastatic malignant neoplasm (SNOMED) added in condition_occurrence
- 432870 — Thrombocytopenic disorder (SNOMED) added in condition_occurrence
- 432881 — Pancytopenia (SNOMED) added in condition_occurrence
- 432923 — Subarachnoid hemorrhage (SNOMED) added in condition_occurrence
- 432937 — Rupture of papillary muscle (SNOMED) added in condition_occurrence
- 433316 — Dizziness and giddiness (SNOMED) added in condition_occurrence
- 433329 — Closed fracture of second cervical vertebra (SNOMED) added in condition_occurrence
- 433403 — Viral meningitis (SNOMED) added in condition_occurrence
- 433456 — Acute pain (SNOMED) added in condition_occurrence
- 433486 — Acute inflammation of orbit (SNOMED) added in condition_occurrence
- 433515 — Chronic gastrojejunal ulcer with hemorrhage (SNOMED) added in condition_occurrence
- 433524 — Disorder of appendix (SNOMED) added in condition_occurrence
- 433527 — Endometriosis (clinical) (SNOMED) added in condition_occurrence
- 433577 — Hammer toe (SNOMED) added in condition_occurrence
- 433595 — Edema (SNOMED) added in condition_occurrence
- 433716 — Primary malignant neoplasm of testis (SNOMED) added in condition_occurrence
- 433736 — Obesity (SNOMED) added in condition_occurrence
- 433741 — Familial erythrocytosis (SNOMED) added in condition_occurrence
- 433753 — Harmful pattern of use of alcohol (SNOMED) added in condition_occurrence
- 433811 — Hydronephrosis (SNOMED) added in condition_occurrence
- 433813 — Obstruction of neck of urinary bladder (SNOMED) added in condition_occurrence
- 433991 — Recurrent major depression in remission (SNOMED) added in condition_occurrence
- 434005 — Morbid obesity (SNOMED) added in condition_occurrence
- 434008 — White blood cell disorder (SNOMED) added in condition_occurrence
- 434084 — Abscess of vulva (SNOMED) added in condition_occurrence
- 434311 — Disorder of the urea cycle metabolism (SNOMED) added in condition_occurrence
- 434337 — Retinal vascular disorder (SNOMED) added in condition_occurrence
- 434376 — Acute myocardial infarction of anterior wall (SNOMED) added in condition_occurrence
- 434494 — Closed fracture of upper end of humerus (SNOMED) added in condition_occurrence
- 434500 — Closed fracture of neck of femur (SNOMED) added in condition_occurrence
- 434502 — Closed fracture of phalanx of foot (SNOMED) added in condition_occurrence
- 434559 — Miliary tuberculosis (SNOMED) added in condition_occurrence
- 434592 — B-cell lymphoma (clinical) (SNOMED) added in condition_occurrence
- 434610 — Hyperkalemia (SNOMED) added in condition_occurrence
- 434663 — Acute endocarditis (SNOMED) added in condition_occurrence
- 434819 — Poisoning by benzodiazepine-based tranquilizer (SNOMED) added in condition_occurrence
- 434821 — Systemic inflammatory response syndrome (SNOMED) added in condition_occurrence
- 434822 — Complication of internal prosthetic device (SNOMED) added in condition_occurrence
- 434824 — Injury of cranial nerve (SNOMED) added in condition_occurrence
- 434889 — Dissociative disorder (SNOMED) added in condition_occurrence
- 434926 — Iridocyclitis (SNOMED) added in condition_occurrence
- 435028 — Puerperal pyrexia of unknown origin (SNOMED) added in condition_occurrence
- 435082 — Closed fracture of nasal bones (SNOMED) added in condition_occurrence
- 435220 — Severe recurrent major depression without psychotic features (SNOMED) added in condition_occurrence
- 435243 — Alcohol dependence (SNOMED) added in condition_occurrence
- 435262 — Primary open angle glaucoma (SNOMED) added in condition_occurrence
- 435371 — Hypothermia (SNOMED) added in condition_occurrence
- 435506 — Benign neoplastic disease (SNOMED) added in condition_occurrence
- 435508 — Adrenal cortical hypofunction (SNOMED) added in condition_occurrence
- 435509 — Intracranial abscess (SNOMED) added in condition_occurrence
- 435515 — Hypo-osmolality and or hyponatremia (SNOMED) added in condition_occurrence
- 435524 — Sleep disorder (SNOMED) added in condition_occurrence
- 435565 — Embolism and thrombosis of the vena cava (SNOMED) added in condition_occurrence
- 435613 — Cellulitis (SNOMED) added in condition_occurrence
- 435666 — Closed fracture of upper end of tibia (SNOMED) added in condition_occurrence
- 435752 — Primary malignant neoplasm of duodenum (SNOMED) added in condition_occurrence
- 435783 — Schizophrenia (SNOMED) added in condition_occurrence
- 435785 — Meningitis (SNOMED) added in condition_occurrence
- 435789 — Megaloblastic anemia (SNOMED) added in condition_occurrence
- 435790 — Secondary polycythemia (SNOMED) added in condition_occurrence
- 435796 — Dehydration (SNOMED) added in condition_occurrence
- 435829 — Rheumatic disease of heart valve (SNOMED) added in condition_occurrence
- 435839 — Lymphedema (SNOMED) added in condition_occurrence
- 435875 — Complication of pregnancy, childbirth and/or puerperium (SNOMED) added in condition_occurrence
- 435940 — Closed fracture of shaft of humerus (SNOMED) added in condition_occurrence
- 436062 — Benign neoplasm of duodenum (SNOMED) added in condition_occurrence
- 436070 — Vitamin D deficiency (SNOMED) added in condition_occurrence
- 436091 — Bacterial meningitis (SNOMED) added in condition_occurrence
- 436093 — Disseminated intravascular coagulation (SNOMED) added in condition_occurrence
- 436096 — Chronic pain (SNOMED) added in condition_occurrence
- 436136 — Dissection of thoracic aorta (SNOMED) added in condition_occurrence
- 436145 — Pneumonia caused by respiratory syncytial virus (SNOMED) added in condition_occurrence
- 436251 — Closed fracture of proximal end of ulna (SNOMED) added in condition_occurrence
- 436252 — Closed fracture of shaft of tibia (SNOMED) added in condition_occurrence
- 436389 — Cocaine dependence (SNOMED) added in condition_occurrence
- 436398 — Glaucoma associated with ocular disorder (SNOMED) added in condition_occurrence
- 436585 — Toxic effect of ethyl alcohol (SNOMED) added in condition_occurrence
- 436635 — Primary malignant neoplasm of sigmoid colon (SNOMED) added in condition_occurrence
- 436659 — Iron deficiency anemia (SNOMED) added in condition_occurrence
- 436665 — Bipolar disorder (SNOMED) added in condition_occurrence
- 436670 — Metabolic disease (SNOMED) added in condition_occurrence
- 436676 — Posttraumatic stress disorder (SNOMED) added in condition_occurrence
- 436677 — Adjustment disorder (SNOMED) added in condition_occurrence
- 436682 — Moderate intellectual disability (SNOMED) added in condition_occurrence
- 436700 — Exophthalmos (SNOMED) added in condition_occurrence
- 436785 — Spinal stenosis in cervical region (SNOMED) added in condition_occurrence
- 436839 — Closed fracture of metacarpal bone (SNOMED) added in condition_occurrence
- 436996 — Thoracoabdominal aortic aneurysm (SNOMED) added in condition_occurrence
- 437038 — Blood in urine (SNOMED) added in condition_occurrence
- 437064 — Chondrocalcinosis (SNOMED) added in condition_occurrence
- 437116 — Closed fracture of distal end of radius (SNOMED) added in condition_occurrence
- 437189 — Accidental poisoning by carbon monoxide (SNOMED) added in condition_occurrence
- 437222 — Respiratory syncytial virus infection (SNOMED) added in condition_occurrence
- 437233 — Multiple myeloma (SNOMED) added in condition_occurrence
- 437241 — Qualitative platelet disorder (SNOMED) added in condition_occurrence
- 437262 — Common peroneal nerve lesion (SNOMED) added in condition_occurrence
- 437295 — Abnormal pupillary function (SNOMED) added in condition_occurrence
- 437306 — Transient global amnesia (SNOMED) added in condition_occurrence
- 437461 — Disorder of prosthetic cardiac valve (SNOMED) added in condition_occurrence
- 437496 — Epidemic vertigo (SNOMED) added in condition_occurrence
- 437530 — Disorder of lipid metabolism (SNOMED) added in condition_occurrence
- 437540 — Central retinal artery occlusion (SNOMED) added in condition_occurrence
- 437541 — Glaucoma (SNOMED) added in condition_occurrence
- 437611 — Ectopic pregnancy (SNOMED) added in condition_occurrence
- 437663 — Fever (SNOMED) added in condition_occurrence
- 437671 — Abnormal feces (SNOMED) added in condition_occurrence
- 437744 — Heat exhaustion (SNOMED) added in condition_occurrence
- 437827 — Pure hypercholesterolemia (SNOMED) added in condition_occurrence
- 437828 — Disorder of calcium metabolism (SNOMED) added in condition_occurrence
- 437833 — Hypokalemia (SNOMED) added in condition_occurrence
- 437904 — Laryngeal spasm (SNOMED) added in condition_occurrence
- 437993 — Closed fracture of cervical spine (SNOMED) added in condition_occurrence
- 438028 — Poisoning by drug AND/OR medicinal substance (SNOMED) added in condition_occurrence
- 438105 — Benign neoplasm of mediastinum (SNOMED) added in condition_occurrence
- 438112 — Neoplastic disease (SNOMED) added in condition_occurrence
- 438120 — Opioid dependence (SNOMED) added in condition_occurrence
- 438252 — Spontaneous ecchymosis (SNOMED) added in condition_occurrence
- 438368 — Primary malignant neoplasm of thymus (SNOMED) added in condition_occurrence
- 438406 — Severe major depression, single episode, with psychotic features (SNOMED) added in condition_occurrence
- 438447 — Acute myocardial infarction of inferolateral wall (SNOMED) added in condition_occurrence
- 438608 — Injury of axillary artery (SNOMED) added in condition_occurrence
- 438688 — Sarcoidosis (SNOMED) added in condition_occurrence
- 438693 — Primary malignant neoplasm of mediastinum (SNOMED) added in condition_occurrence
- 438699 — Primary malignant neoplasm of rectosigmoid junction (SNOMED) added in condition_occurrence
- 438720 — Mixed hyperlipidemia (SNOMED) added in condition_occurrence
- 438725 — Disorder of magnesium metabolism (SNOMED) added in condition_occurrence
- 438887 — Closed fracture of shaft of femur (SNOMED) added in condition_occurrence
- 439002 — Eating disorder (SNOMED) added in condition_occurrence
- 439082 — Menopausal syndrome (SNOMED) added in condition_occurrence
- 439254 — Bipolar affective disorder, current episode depression (SNOMED) added in condition_occurrence
- 439297 — Nuclear senile cataract (SNOMED) added in condition_occurrence
- 439393 — Pre-eclampsia (SNOMED) added in condition_occurrence
- 439404 — Primary malignant neoplasm of oral cavity (SNOMED) added in condition_occurrence
- 439407 — Disorder of nasal cavity (SNOMED) added in condition_occurrence
- 439658 — Disorder of pregnancy (SNOMED) added in condition_occurrence
- 439674 — Chronic viral hepatitis B without delta-agent (SNOMED) added in condition_occurrence
- 439708 — Disorders of initiating and maintaining sleep (SNOMED) added in condition_occurrence
- 439727 — Human immunodeficiency virus infection (SNOMED) added in condition_occurrence
- 439776 — Autism spectrum disorder (SNOMED) added in condition_occurrence
- 439777 — Anemia (SNOMED) added in condition_occurrence
- 439846 — Left heart failure (SNOMED) added in condition_occurrence
- 439847 — Intracranial hemorrhage (SNOMED) added in condition_occurrence
- 439907 — Non-traumatic tendon rupture (SNOMED) added in condition_occurrence
- 439928 — Gangrenous disorder (SNOMED) added in condition_occurrence
- 439973 — Nonfatal submersion (SNOMED) added in condition_occurrence
- 440005 — Complication of medical care (SNOMED) added in condition_occurrence
- 440029 — Viral disease (SNOMED) added in condition_occurrence
- 440072 — Hypogammaglobulinemia (SNOMED) added in condition_occurrence
- 440078 — Bipolar affective disorder, current episode manic (SNOMED) added in condition_occurrence
- 440083 — Acute stress disorder (SNOMED) added in condition_occurrence
- 440129 — Hypertrophy of nasal turbinates (SNOMED) added in condition_occurrence
- 440142 — Disorder of mediastinum (SNOMED) added in condition_occurrence
- 440238 — Closed fracture of metatarsal bone (SNOMED) added in condition_occurrence
- 440270 — Poisoning by antidepressant (SNOMED) added in condition_occurrence
- 440276 — Infection AND/OR inflammatory reaction due to internal prosthetic device, implant AND/OR graft (SNOMED) added in condition_occurrence
- 440374 — Obsessive-compulsive disorder (SNOMED) added in condition_occurrence
- 440385 — Obstructive hydrocephalus (SNOMED) added in condition_occurrence
- 440392 — Retinal vascular occlusion (SNOMED) added in condition_occurrence
- 440409 — Disorder of orbit proper (SNOMED) added in condition_occurrence
- 440417 — Pulmonary embolism (SNOMED) added in condition_occurrence
- 440424 — Aphasia (SNOMED) added in condition_occurrence
- 440448 — Appendicitis (SNOMED) added in condition_occurrence
- 440538 — Closed fracture of lower end of radius AND ulna (SNOMED) added in condition_occurrence
- 440548 — Closed fracture of femur, distal end (SNOMED) added in condition_occurrence
- 440603 — Blood transfusion reaction (SNOMED) added in condition_occurrence
- 440615 — Effect of exposure to external cause (SNOMED) added in condition_occurrence
- 440631 — Mycobacteriosis (SNOMED) added in condition_occurrence
- 440649 — Primary malignant neoplasm of head of pancreas (SNOMED) added in condition_occurrence
- 440674 — Gout (SNOMED) added in condition_occurrence
- 440689 — Agranulocytosis (SNOMED) added in condition_occurrence
- 440703 — Trigeminal nerve disorder (SNOMED) added in condition_occurrence
- 440751 — Peritonsillar abscess (SNOMED) added in condition_occurrence
- 440812 — Pathological fracture - lower leg (SNOMED) added in condition_occurrence
- 440921 — Traumatic injury (SNOMED) added in condition_occurrence
- 440971 — Neoplasm of uncertain behavior of testis (SNOMED) added in condition_occurrence
- 440973 — Benign neoplasm of long bones of lower limb (SNOMED) added in condition_occurrence
- 440977 — Megaloblastic anemia due to folate deficiency (SNOMED) added in condition_occurrence
- 441051 — Thoracic aortic aneurysm without rupture (SNOMED) added in condition_occurrence
- 441202 — Anaphylaxis (SNOMED) added in condition_occurrence
- 441225 — Primary malignant neoplasm of ampulla of Vater (SNOMED) added in condition_occurrence
- 441259 — Non-thrombocytopenic purpura (SNOMED) added in condition_occurrence
- 441269 — Autoimmune hemolytic anemia (SNOMED) added in condition_occurrence
- 441364 — Complication of the puerperium (SNOMED) added in condition_occurrence
- 441534 — Severe major depression, single episode, without psychotic features (SNOMED) added in condition_occurrence
- 441553 — Myoclonus (SNOMED) added in condition_occurrence
- 441589 — Endocarditis (SNOMED) added in condition_occurrence
- 441641 — Delivery normal (SNOMED) added in condition_occurrence
- 441761 — Methyl alcohol causing toxic effect (SNOMED) added in condition_occurrence
- 441800 — Primary malignant neoplasm of descending colon (SNOMED) added in condition_occurrence
- 441818 — Hemangioma (SNOMED) added in condition_occurrence
- 441829 — Hyperosmolality and or hypernatremia (SNOMED) added in condition_occurrence
- 441830 — Disorder of fluid AND/OR electrolyte (SNOMED) added in condition_occurrence
- 441838 — Personality disorder (SNOMED) added in condition_occurrence
- 441840 — Clinical finding (SNOMED) added in condition_occurrence
- 441875 — Thoracic aortic aneurysm which has ruptured (SNOMED) added in condition_occurrence
- 441973 — Closed fracture of proximal end of radius (SNOMED) added in condition_occurrence
- 442013 — Burn (SNOMED) added in condition_occurrence
- 442019 — Complication of procedure (SNOMED) added in condition_occurrence
- 442077 — Anxiety disorder (SNOMED) added in condition_occurrence
- 442108 — Benign neoplasm of cecum (SNOMED) added in condition_occurrence
- 442129 — Neoplasm of uncertain behavior of ureter (SNOMED) added in condition_occurrence
- 442263 — Basilar artery stenosis (SNOMED) added in condition_occurrence
- 442553 — Injury of urinary bladder (SNOMED) added in condition_occurrence
- 442562 — Poisoning (SNOMED) added in condition_occurrence
- 442588 — Obstructive sleep apnea syndrome (SNOMED) added in condition_occurrence
- 442615 — Carotid artery stenosis (SNOMED) added in condition_occurrence
- 442639 — Injury of colon without open wound into abdominal cavity (SNOMED) added in condition_occurrence
- 442752 — Muscle pain (SNOMED) added in condition_occurrence
- 442793 — Complication due to diabetes mellitus (SNOMED) added in condition_occurrence
- 443344 — Barrett's esophagus (SNOMED) added in condition_occurrence
- 443388 — Malignant neoplasm of lung (SNOMED) added in condition_occurrence
- 443394 — Addison's disease (SNOMED) added in condition_occurrence
- 443397 — Malignant tumor of small intestine (SNOMED) added in condition_occurrence
- 443454 — Cerebral infarction (SNOMED) added in condition_occurrence
- 443597 — Chronic kidney disease stage 3 (SNOMED) added in condition_occurrence
- 443600 — Localized infection of skin AND/OR subcutaneous tissue (SNOMED) added in condition_occurrence
- 443601 — Chronic kidney disease stage 2 (SNOMED) added in condition_occurrence
- 443605 — Vascular dementia (SNOMED) added in condition_occurrence
- 443611 — Chronic kidney disease stage 5 (SNOMED) added in condition_occurrence
- 443612 — Chronic kidney disease stage 4 (SNOMED) added in condition_occurrence
- 443614 — Chronic kidney disease stage 1 (SNOMED) added in condition_occurrence
- 443617 — Conduct disorder (SNOMED) added in condition_occurrence
- 443622 — Aneurysm of thoracic aorta (SNOMED) added in condition_occurrence
- 443700 — Eclampsia (SNOMED) added in condition_occurrence
- 443727 — Diabetic ketoacidosis (SNOMED) added in condition_occurrence
- 443782 — Tremor (SNOMED) added in condition_occurrence
- 443784 — Vascular disorder (SNOMED) added in condition_occurrence
- 443792 — Calculus of bile duct (SNOMED) added in condition_occurrence
- 443919 — Hypertensive renal failure (SNOMED) added in condition_occurrence
- 443929 — Postpartum hemorrhage (SNOMED) added in condition_occurrence
- 443943 — Herpes zoster (SNOMED) added in condition_occurrence
- 443962 — Mitral valve regurgitation (SNOMED) added in condition_occurrence
- 444044 — Acute tubular necrosis (SNOMED) added in condition_occurrence
- 444070 — Tachycardia (SNOMED) added in condition_occurrence
- 444078 — Inflammation of cervix (SNOMED) added in condition_occurrence
- 444079 — Psychogenic fugue (SNOMED) added in condition_occurrence
- 444084 — Hypersensitivity pneumonitis (SNOMED) added in condition_occurrence
- 444089 — Disorder of abdomen (SNOMED) added in condition_occurrence
- 444095 — Injury of ureter without open wound into abdominal cavity (SNOMED) added in condition_occurrence
- 444100 — Mood disorder (SNOMED) added in condition_occurrence
- 444132 — Injury of knee (SNOMED) added in condition_occurrence
- 444187 — Open wound (SNOMED) added in condition_occurrence
- 444191 — Injury of face (SNOMED) added in condition_occurrence
- 444202 — Abscess (SNOMED) added in condition_occurrence
- 444264 — Thrombosis of iliac artery (SNOMED) added in condition_occurrence
- 444459 — Benign neoplasm of sigmoid colon (SNOMED) added in condition_occurrence
- 586323 — degree Celsius (UCUM) added in measurement
- 586526 — SARS-CoV-2 (COVID-19) RNA [Presence] in Nasopharynx by NAA with probe detection (LOINC) added in measurement
- 600861 — Traumatic spinal cord injury (SNOMED) added in condition_occurrence
- 606761 — Poisoning caused by sedative (SNOMED) added in condition_occurrence
- 606805 — Poisoning caused by opioid receptor agonist (SNOMED) added in condition_occurrence
- 607208 — Acute alcohol intoxication (SNOMED) added in condition_occurrence
- 607808 — Cyanide and/or cyanide compound poisoning (SNOMED) added in condition_occurrence
- 608027 — Poisoning caused by gaseous substance (SNOMED) added in condition_occurrence
- 608324 — Poisoning by hypnotic agent (SNOMED) added in condition_occurrence
- 609083 — Rupture of interventricular septum following acute myocardial infarction (SNOMED) added in condition_occurrence
- 619430 — Lichen sclerosus (SNOMED) added in condition_occurrence
- 702006 — technetium (RxNorm) added in drug_exposure
- 702291 — maribavir (RxNorm) added in drug_exposure
- 706284 — Hematology (LOINC) added in visit_occurrence
- 706367 — Intensive care unit (LOINC) added in visit_occurrence
- 706470 — Emergency department (LOINC) added in visit_detail
- 706470 — Emergency department (LOINC) added in visit_occurrence
- 706520 — Medical Oncology (LOINC) added in visit_occurrence
- 710189 — attomole (UCUM) added in measurement
- 710194 — kilocalorie (UCUM) added in measurement
- 710208 — milliliter per minute per square meter (UCUM) added in measurement
- 710220 — milliampere (UCUM) added in measurement
- 720841 — dyne-second per centimeter to the fifth power per square meter (UCUM) added in measurement
- 720843 — millivolt (UCUM) added in measurement
- 720858 — millibar (UCUM) added in measurement
- 720865 — milliliter per millibar (UCUM) added in measurement
- 720866 — milliliter per centimeter of water (UCUM) added in measurement
- 720867 — millibar per liter (UCUM) added in measurement
- 720868 — fraction (UCUM) added in measurement
- 720870 — milliliter per minute per 1.73 square meter (UCUM) added in measurement
- 720871 — milliliter per square meter per beat (UCUM) added in measurement
- 722044 — Critical Care Pain Observation Tool (CPOT): Facial expression score (OMOP Extension) added in measurement
- 722048 — Critical Care Pain Observation Tool (CPOT): Body movements score (OMOP Extension) added in measurement
- 722056 — Critical Care Pain Observation Tool (CPOT): Compliance with the ventilator score (OMOP Extension) added in measurement
- 735843 — natalizumab (RxNorm) added in drug_exposure
- 739438 — vibegron (RxNorm) added in drug_exposure
- 739471 — relugolix (RxNorm) added in drug_exposure
- 761983 — Outpatient surgery service (SNOMED) added in visit_occurrence
- 763917 — Patient transfer to another hospital (SNOMED) added in visit_occurrence
- 764090 — Defibrillation using automated external cardiac defibrillator (SNOMED) added in procedure_occurrence
- 764865 — Outpatient service (SNOMED) added in visit_occurrence
- 778978 — cytarabine / daunorubicin (RxNorm) added in drug_exposure
- 779055 — casirivimab / imdevimab (RxNorm) added in drug_exposure
- 903277 — Dentistry (Medicare Specialty) added in provider
- 903277 — Dentistry (Medicare Specialty) added in visit_occurrence
- 905078 — trifluridine (RxNorm) added in drug_exposure
- 950183 — lactase (RxNorm) added in drug_exposure
- 977968 — sodium citrate (RxNorm) added in drug_exposure
- 1001651 — Rh antigens and K Ag panel - Blood (LOINC) added in measurement
- 1073322 — Construction of tracheostomy (SNOMED) added in procedure_occurrence
- 1073964 — Cardiac ablation for atrial fibrillation (SNOMED) added in procedure_occurrence
- 1075181 — Plain X-ray of thoracic cage (SNOMED) added in procedure_occurrence
- 1075809 — Lesion of femoral nerve (SNOMED) added in condition_occurrence
- 1076048 — Posterior interbody fusion of joint of lumbar spine (SNOMED) added in procedure_occurrence
- 1091073 — Microscopic observation [Identifier] in Bronchoalveolar lavage by Gram stain (LOINC) added in measurement
- 1091205 — Stomatocytes [Presence] in Blood (LOINC) added in measurement
- 1091242 — Pneumocystis jirovecii DNA [Presence] in Bronchoalveolar lavage by NAA with probe detection (LOINC) added in measurement
- 1091323 — Fungus identified in Catheter tip by Culture (LOINC) added in measurement
- 1091342 — Human coronavirus HKU1 RNA [Presence] in Nasopharynx by NAA with probe detection (LOINC) added in measurement
- 1091352 — Poikilocytosis [Presence] in Blood (LOINC) added in measurement
- 1091393 — Respiratory syncytial virus RNA [Presence] in Sputum by NAA with probe detection (LOINC) added in measurement
- 1091481 — Hyaline casts [Presence] in Urine sediment (LOINC) added in measurement
- 1091714 — HIV 1+2 Ab+HIV1 p24 Ag [Presence] in Serum or Plasma (LOINC) added in measurement
- 1091804 — Beta globulin [Mass/volume] in Serum or Plasma (LOINC) added in measurement
- 1091830 — Polychromasia [Presence] in Blood (LOINC) added in measurement
- 1091854 — Cyclospora cayetanensis DNA [Presence] in Stool (LOINC) added in measurement
- 1091866 — Human coronavirus NL63 RNA [Presence] in Nasopharynx by NAA with probe detection (LOINC) added in measurement
- 1091945 — Legionella pneumophila DNA [Presence] in Nasopharynx by NAA with probe detection (LOINC) added in measurement
- 1091981 — Platelets Large [Presence] in Blood (LOINC) added in measurement
- 1092007 — Epithelial cells.non-squamous [Presence] in Urine (LOINC) added in measurement
- 1092029 — Giardia lamblia DNA [Presence] in Stool (LOINC) added in measurement
- 1092049 — Bacteria identified in Bronchial specimen by Culture (LOINC) added in measurement
- 1092089 — Epithelial cells.squamous [Presence] in Urine (LOINC) added in measurement
- 1092387 — Burr cells [Presence] in Blood (LOINC) added in measurement
- 1092441 — Hematocrit [Pure volume fraction] of Blood by calculation (LOINC) added in measurement
- 1092445 — Erythrocytes [#/area] in Urine sediment (LOINC) added in measurement
- 1175793 — Methicillin resistant Staphylococcus aureus (MRSA) DNA [Presence] in Nose by NAA with probe detection (LOINC) added in measurement
- 1177394 — Nuclear medicine (LOINC) added in visit_occurrence
- 1242722 — Operation on femoral artery (SNOMED) added in procedure_occurrence
- 1243647 — Arterial bypass graft of thoracic artery using arterial graft (SNOMED) added in procedure_occurrence
- 1243926 — Head and neck surgery (SNOMED) added in visit_occurrence
- 1245117 — Vasopressin-related polyuria (SNOMED) added in condition_occurrence
- 1259509 — Body temperature - Groin (LOINC) added in measurement
- 1333357 — busulfan (RxNorm) added in drug_exposure
- 1333379 — arsenic trioxide (RxNorm) added in drug_exposure
- 1335301 — phenoxybenzamine (RxNorm) added in drug_exposure
- 1340204 — History of event (OMOP Extension) added in observation
- 1340217 — History of event within 1 week (OMOP Extension) added in observation
- 1343346 — vinorelbine (RxNorm) added in drug_exposure
- 1350066 — carmustine (RxNorm) added in drug_exposure
- 1367268 — irinotecan (RxNorm) added in drug_exposure
- 1378509 — topotecan (RxNorm) added in drug_exposure
- 1389112 — Echinacea preparation (RxNorm) added in drug_exposure
- 1447756 — Patient controlled intravenous analgesia (SNOMED) added in procedure_occurrence
- 1450471 — Chronic primary bladder pain syndrome (SNOMED) added in condition_occurrence
- 1469496 — Human bocavirus DNA [Presence] in Sputum by NAA with probe detection (LOINC) added in measurement
- 1469649 — Campylobacter sp DNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 1469822 — Escherichia coli shiga-like toxin DNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 1507835 — vasopressin (USP) (RxNorm) added in drug_exposure
- 1523280 — diazoxide (RxNorm) added in drug_exposure
- 1539954 — phenylbutyrate (RxNorm) added in drug_exposure
- 1616439 — Central nervous system [Score] SOFA (LOINC) added in measurement
- 1616794 — Bicarbonate [Moles/volume] in Central venous blood (LOINC) added in measurement
- 1616857 — Abnormal lymphocytes [Presence] in Body fluid by Manual count (LOINC) added in measurement
- 1616907 — Respiration [Score] SOFA (LOINC) added in measurement
- 1616908 — Candida auris DNA [Presence] in Specimen by NAA with probe detection (LOINC) added in measurement
- 1616933 — Salmonella sp DNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 1617043 — Liver [Score] SOFA (LOINC) added in measurement
- 1617673 — Vibrio cholerae DNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 1621272 — Other/unspecified (LOINC) added in provider
- 1621272 — Other/unspecified (LOINC) added in visit_occurrence
- 1718346 — olaratumab (RxNorm) added in drug_exposure
- 1745072 — cidofovir (RxNorm) added in drug_exposure
- 1761466 — Staph aureus and MRSA screening panel - Specimen by Organism specific culture (LOINC) added in measurement
- 1988118 — Temporary pacemaker Ventricular stimulation threshold (LOINC) added in measurement
- 1988411 — Permanent pacemaker panel (LOINC) added in measurement
- 1988914 — Aspergillus sp Ag [Units/volume] in Body fluid by Immunoassay (LOINC) added in measurement
- 1989635 — Pacemaker Atrial wire (LOINC) added in measurement
- 3000494 — Fungus identified in Specimen by Culture (LOINC) added in measurement
- 3000515 — Antithrombin actual/normal in Platelet poor plasma by Chromogenic method (LOINC) added in measurement
- 3001123 — Platelet [Entitic mean volume] in Blood (LOINC) added in measurement
- 3001467 — Alkaline phosphatase.bone [Enzymatic activity/volume] in Serum or Plasma (LOINC) added in measurement
- 3001526 — Acetaminophen [Presence] in Urine (LOINC) added in measurement
- 3001850 — Coagulation factor XI activity actual/normal in Platelet poor plasma by Coagulation assay (LOINC) added in measurement
- 3001873 — Granular casts [Presence] in Urine sediment by Light microscopy (LOINC) added in measurement
- 3001886 — Microscopic observation [Identifier] in Cerebral spinal fluid by Gram stain (LOINC) added in measurement
- 3002888 — Deprecated Erythrocyte distribution width [Entitic volume] (LOINC) added in measurement
- 3002991 — Calcium [Moles/volume] in Dialysis fluid (LOINC) added in measurement
- 3003214 — Platelet morphology finding [Identifier] in Blood (LOINC) added in measurement
- 3003238 — ABO group [Type] in Blood from Donor (LOINC) added in measurement
- 3003745 — Microscopic observation [Identifier] in Urine by Gram stain (LOINC) added in measurement
- 3003867 — Hepatitis E virus IgG Ab [Presence] in Serum (LOINC) added in measurement
- 3004378 — Glucose in CSF/Glucose plas (LOINC) added in measurement
- 3004409 — Coagulation factor X activity actual/normal in Platelet poor plasma by Coagulation assay (LOINC) added in measurement
- 3004490 — Bicarbonate [Moles/volume] standard in Capillary blood (LOINC) added in measurement
- 3004616 — Nuclear Ab [Presence] in Serum (LOINC) added in measurement
- 3004825 — Lactate [Moles/volume] in Body fluid (LOINC) added in measurement
- 3005229 — Alpha 2 globulin [Mass/volume] in Serum or Plasma by Electrophoresis (LOINC) added in measurement
- 3005707 — Macrocytes [Presence] in Blood (LOINC) added in measurement
- 3005757 — Coagulation factor V activity actual/normal in Platelet poor plasma by Coagulation assay (LOINC) added in measurement
- 3006109 — Coagulation factor IX activity actual/normal in Platelet poor plasma by Coagulation assay (LOINC) added in measurement
- 3006585 — Epstein Barr virus capsid IgG Ab [Presence] in Serum (LOINC) added in measurement
- 3006631 — Hepatitis A virus IgG Ab [Presence] in Serum (LOINC) added in measurement
- 3006898 — Lactate dehydrogenase 1/Lactate dehydrogenase.total in Serum or Plasma by Electrophoresis (LOINC) added in measurement
- 3007254 — Physical findings skin pressure injury (LOINC) added in measurement
- 3007424 — Albumin/Protein.total in Serum or Plasma by Electrophoresis (LOINC) added in measurement
- 3007858 — Lactate dehydrogenase 3/Lactate dehydrogenase.total in Serum or Plasma by Electrophoresis (LOINC) added in measurement
- 3008038 — Rheumatoid factor [Titer] in Serum by Latex agglutination (LOINC) added in measurement
- 3008757 — Leukocyte morphology finding [Identifier] in Blood (LOINC) added in measurement
- 3008793 — Fluid output biliary drain (LOINC) added in measurement
- 3008909 — Norovirus RNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 3009628 — Neutrophil cytoplasmic Ab [Presence] in Serum (LOINC) added in measurement
- 3009994 — Fluid intake urinary bladder irrigation Measured (LOINC) added in measurement
- 3010517 — Carboxyhemoglobin/Hemoglobin.total in Venous blood (LOINC) added in measurement
- 3010633 — Mycoplasma sp Ab [Presence] in Serum (LOINC) added in measurement
- 3011547 — Coagulation factor VII activity actual/normal in Platelet poor plasma by Coagulation assay (LOINC) added in measurement
- 3011689 — Deoxyhemoglobin/Hemoglobin.total in Blood (LOINC) added in measurement
- 3011705 — Protein [Mass/volume] in 24 hour Urine (LOINC) added in measurement
- 3012481 — Lactate dehydrogenase 5/Lactate dehydrogenase.total in Serum or Plasma by Electrophoresis (LOINC) added in measurement
- 3013194 — Chloride [Moles/volume] in Body fluid (LOINC) added in measurement
- 3013332 — Cytomegalovirus IgM Ab [Presence] in Serum or Plasma (LOINC) added in measurement
- 3013731 — Hepatitis B virus surface Ab [Units/volume] in Serum or Plasma by Immunoassay (LOINC) added in measurement
- 3014312 — pH of Gastric fluid (LOINC) added in measurement
- 3014401 — Aspergillus sp Ab [Titer] in Serum (LOINC) added in measurement
- 3014502 — Neutrophils/Leukocytes in Body fluid (LOINC) added in measurement
- 3014620 — Thyroxine (T4) [Moles/volume] in Serum or Plasma (LOINC) added in measurement
- 3014891 — Appearance of Pleural fluid (LOINC) added in measurement
- 3015322 — Alpha 1 globulin [Mass/volume] in Serum or Plasma by Electrophoresis (LOINC) added in measurement
- 3015421 — Appearance of Peritoneal fluid (LOINC) added in measurement
- 3015592 — Fungus identified in Body fluid by Culture (LOINC) added in measurement
- 3015711 — Magnesium [Moles/volume] in Body fluid (LOINC) added in measurement
- 3016360 — Urobilinogen [Presence] in Urine (LOINC) added in measurement
- 3016650 — Hepatitis A virus Ab [Presence] in Serum (LOINC) added in measurement
- 3016727 — Bacteria identified in Body fluid by Culture (LOINC) added in measurement
- 3016914 — Bacteria identified in Cerebral spinal fluid by Culture (LOINC) added in measurement
- 3017181 — Myelocytes/Leukocytes in Blood (LOINC) added in measurement
- 3017509 — Phencyclidine [Presence] in Urine (LOINC) added in measurement
- 3017900 — Segmented neutrophils/Leukocytes in Cerebral spinal fluid (LOINC) added in measurement
- 3017918 — Cytomegalovirus IgG Ab [Titer] in Serum or Plasma (LOINC) added in measurement
- 3018013 — Aorta Maximum coarctation pressure gradient by US.doppler (LOINC) added in measurement
- 3018738 — Hemoglobin F/Hemoglobin.total in Blood (LOINC) added in measurement
- 3019154 — Physical findings of Upper arm (LOINC) added in measurement
- 3019284 — Hepatitis B virus surface Ag [Presence] in Serum (LOINC) added in measurement
- 3020192 — Gamma globulin [Mass/volume] in Body fluid by Electrophoresis (LOINC) added in measurement
- 3020682 — Albumin/Creatinine [Ratio] in Urine (LOINC) added in measurement
- 3020784 — Hemoglobin A2/Hemoglobin.total in Blood (LOINC) added in measurement
- 3020951 — Lymphocytes/Leukocytes in Cerebral spinal fluid (LOINC) added in measurement
- 3021440 — Promyelocytes/Leukocytes in Blood (LOINC) added in measurement
- 3021849 — Epstein Barr virus nuclear IgG Ab [Presence] in Serum (LOINC) added in measurement
- 3021879 — Hepatitis B virus core Ab [Presence] in Serum (LOINC) added in measurement
- 3022023 — Deoxyhemoglobin/Hemoglobin.total in Mixed venous blood (LOINC) added in measurement
- 3022036 — Colony count [#/volume] in Urine (LOINC) added in measurement
- 3022130 — Physical findings of Lower extremity (LOINC) added in measurement
- 3022640 — Eosinophils/Leukocytes in Cerebral spinal fluid (LOINC) added in measurement
- 3023368 — Bacteria identified in Blood by Culture (LOINC) added in measurement
- 3023419 — Bacteria identified in Sputum by Culture (LOINC) added in measurement
- 3023919 — Lactate dehydrogenase 2/Lactate dehydrogenase.total in Serum or Plasma by Electrophoresis (LOINC) added in measurement
- 3024340 — Free Hemoglobin [Moles/volume] in Plasma (LOINC) added in measurement
- 3024456 — Kell group Ag [Type] on Red Blood Cells (LOINC) added in measurement
- 3024655 — Bicarbonate [Moles/volume] in Body fluid (LOINC) added in measurement
- 3024830 — Lactate dehydrogenase 4/Lactate dehydrogenase.total in Serum or Plasma by Electrophoresis (LOINC) added in measurement
- 3024958 — Right ventricular Stroke work (LOINC) added in measurement
- 3025135 — Right ventricular Stroke work index (LOINC) added in measurement
- 3025159 — Blasts/Leukocytes in Blood (LOINC) added in measurement
- 3025313 — Albumin [Mass/volume] in Body fluid (LOINC) added in measurement
- 3025317 — Coagulation factor VII activated [Units/volume] in Platelet poor plasma by Coagulation assay (LOINC) added in measurement
- 3025639 — Microcytes [Presence] in Blood (LOINC) added in measurement
- 3025941 — Bacteria identified in Stool by Culture (LOINC) added in measurement
- 3027003 — Microscopic observation [Identifier] in Body fluid by Gram stain (LOINC) added in measurement
- 3027204 — Physical findings of Sense of touch (LOINC) added in measurement
- 3027247 — Bacteria identified in Specimen (LOINC) added in measurement
- 3027480 — Carbon dioxide [Partial pressure] in Body fluid (LOINC) added in measurement
- 3028099 — Epithelial cells.squamous [Presence] in Sputum by Light microscopy (LOINC) added in measurement
- 3028502 — Macrophages/Leukocytes in Cerebral spinal fluid (LOINC) added in measurement
- 3028676 — Leukocytes [Presence] in Sputum by Light microscopy (LOINC) added in measurement
- 3028855 — Bacteria [Presence] in Body fluid by Light microscopy (LOINC) added in measurement
- 3029937 — Albumin [Presence] in Urine by Test strip (LOINC) added in measurement
- 3030872 — Granulocytes [#/volume] in Pleural fluid (LOINC) added in measurement
- 3031020 — Calcium.ionized [Moles/volume] adjusted to pH 7.4 in Body fluid (LOINC) added in measurement
- 3031745 — Lymphocytes Plasmacytoid/Leukocytes in Blood (LOINC) added in measurement
- 3032013 — CT Abdomen (LOINC) added in procedure_occurrence
- 3032072 — Eosinophils [#/volume] in Pleural fluid (LOINC) added in measurement
- 3032566 — Bacteria [Presence] in Pleural fluid by Light microscopy (LOINC) added in measurement
- 3032846 — Bacteria [Presence] in Peritoneal fluid by Light microscopy (LOINC) added in measurement
- 3032893 — Mononuclear cells [#/volume] in Pleural fluid (LOINC) added in measurement
- 3033386 — Bacteria [Presence] in Cerebral spinal fluid by Light microscopy (LOINC) added in measurement
- 3033907 — Neutrophils.vacuolated [Presence] in Blood by Light microscopy (LOINC) added in measurement
- 3033966 — Methicillin resistant Staphylococcus aureus (MRSA) DNA [Presence] in Specimen by NAA with probe detection (LOINC) added in measurement
- 3034118 — Platelets Large [Presence] in Blood by Light microscopy (LOINC) added in measurement
- 3034720 — Initial visit for chief complaint (LOINC) added in measurement
- 3034824 — Hypochromia [Presence] in Blood (LOINC) added in measurement
- 3035206 — Physical mobility Braden scale (LOINC) added in measurement
- 3035320 — C reactive protein [Mass/volume] in Body fluid (LOINC) added in measurement
- 3035400 — Alkaline phosphatase.liver [Enzymatic activity/volume] in Serum or Plasma (LOINC) added in measurement
- 3035519 — Braden scale total score (LOINC) added in measurement
- 3035715 — Granulocytes [#/volume] in Blood (LOINC) added in measurement
- 3035816 — Nutrition intake pattern Braden scale (LOINC) added in measurement
- 3035999 — Lactate [Moles/volume] in Cerebral spinal fluid (LOINC) added in measurement
- 3036426 — Calcium.ionized [Mass/volume] in Blood (LOINC) added in measurement
- 3036468 — Granulocytes/Leukocytes in Pleural fluid by Manual count (LOINC) added in measurement
- 3036884 — Blood group antibody screen.autologous [Interpretation] in Serum or Plasma (LOINC) added in measurement
- 3037022 — Moisture exposure Braden scale (LOINC) added in measurement
- 3037185 — Protein [Presence] in Urine (LOINC) added in measurement
- 3037318 — Physical activity Braden scale (LOINC) added in measurement
- 3037347 — Friction and shear Braden scale (LOINC) added in measurement
- 3037429 — Mononuclear cells/Leukocytes in Pleural fluid by Manual count (LOINC) added in measurement
- 3037836 — Fluid output pericardial drain (LOINC) added in measurement
- 3038058 — Lymphocytes/Leukocytes in Blood by Manual count (LOINC) added in measurement
- 3038224 — Microscopic observation [Identifier] in Urine sediment by Light microscopy (LOINC) added in measurement
- 3039608 — Clotting time.intrinsic coagulation system activated.heparin insensitive of Blood by Rotational TEG (LOINC) added in measurement
- 3040808 — Maximum clot firmness [Length] in Blood by Thromboelastography (LOINC) added in measurement
- 3040852 — Aspergillus fumigatus Ab [Presence] in Body fluid (LOINC) added in measurement
- 3041078 — Clot formation [Time] in Blood by Thromboelastography (LOINC) added in measurement
- 3041292 — Length of Wound (LOINC) added in measurement
- 3041671 — Calcium.ionized [Moles/volume] adjusted to pH 7.4 in Venous blood (LOINC) added in measurement
- 3041706 — Calcium.ionized [Moles/volume] adjusted to pH 7.4 in Arterial blood (LOINC) added in measurement
- 3041899 — Schistocytes [Presence] in Blood by Automated count (LOINC) added in measurement
- 3042075 — Hepatitis A virus IgM Ab [Presence] in Body fluid (LOINC) added in measurement
- 3042736 — Bacteria [Presence] in Specimen (LOINC) added in measurement
- 3042817 — Minumum expired volume setting Ventilator alarm (LOINC) added in measurement
- 3043748 — Appearance of Bronchial specimen (LOINC) added in measurement
- 3044587 — Neutrophils.hypersegmented [Presence] in Blood by Automated count (LOINC) added in measurement
- 3044599 — Bilirubin.conjugated/Bilirubin.total in Serum or Plasma (LOINC) added in measurement
- 3044629 — Leukocytes [Presence] in Body fluid (LOINC) added in measurement
- 3044637 — Erythrocytes [Presence] in Body fluid (LOINC) added in measurement
- 3045452 — LMW Heparin [Units/volume] in Platelet poor plasma (LOINC) added in measurement
- 3047117 — Bordetella pertussis DNA [Presence] in Nasopharynx by NAA with probe detection (LOINC) added in measurement
- 3048816 — Calcium.ionized [Moles/volume] adjusted to pH 7.4 in Blood (LOINC) added in measurement
- 3051232 — Leukocytes [#/volume] in Dialysis fluid (LOINC) added in measurement
- 3051269 — Microscopic observation [Identifier] in Bronchial specimen by Rhodamine-auramine fluorochrome stain (LOINC) added in measurement
- 3053156 — Parathyrin [Moles/volume] in Serum or Plasma --baseline (LOINC) added in measurement
- 3654996 — Peripheral arterial disease (SNOMED) added in condition_occurrence
- 3655118 — Respiratory condition caused by chemical fumes (SNOMED) added in condition_occurrence
- 3655437 — Cardiotoxicity (SNOMED) added in condition_occurrence
- 3655901 — Assisted ventilation in prone position (SNOMED) added in procedure_occurrence
- 3655950 — Heated and humidified high flow oxygen therapy (SNOMED) added in procedure_occurrence
- 3663197 — Glaucoma suspect (SNOMED) added in condition_occurrence
- 3964452 — Trauma Surgery (LOINC) added in visit_occurrence
- 3965358 — Campylobacter coli DNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 3966032 — Colony count [#/volume] in Specimen by Culture Standard Plate Count (LOINC) added in measurement
- 3966289 — Campylobacter jejuni DNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 4000518 — Biopsy of mediastinum (SNOMED) added in procedure_occurrence
- 4000609 — Disorder of upper gastrointestinal tract (SNOMED) added in condition_occurrence
- 4000610 — Disorder of gastrointestinal tract (SNOMED) added in condition_occurrence
- 4000889 — Heart closure (SNOMED) added in procedure_occurrence
- 4000895 — Aorta reconstruction (SNOMED) added in procedure_occurrence
- 4000968 — Biceps tendinitis (SNOMED) added in condition_occurrence
- 4001336 — Concussion injury of brain (SNOMED) added in condition_occurrence
- 4001664 — Intrahepatic bile duct carcinoma (SNOMED) added in condition_occurrence
- 4001666 — Mesothelioma of peritoneum (SNOMED) added in condition_occurrence
- 4001670 — Ductal carcinoma in situ of breast (SNOMED) added in condition_occurrence
- 4002497 — Acute promyelocytic leukemia, FAB M3 (SNOMED) added in condition_occurrence
- 4003037 — Creation of cerebrospinal fluid shunt (SNOMED) added in procedure_occurrence
- 4005686 — Impaired insight (SNOMED) added in observation
- 4005907 — Injury of brachial artery (SNOMED) added in condition_occurrence
- 4006860 — Intra-articular (SNOMED) added in drug_exposure
- 4006971 — Tricuspid valve regurgitation (SNOMED) added in condition_occurrence
- 4009610 — Closed fracture proximal femur, subtrochanteric (SNOMED) added in condition_occurrence
- 4009619 — Bursitis of knee (SNOMED) added in condition_occurrence
- 4010017 — Atypical chest pain (SNOMED) added in condition_occurrence
- 4010333 — Postmenopausal osteoporosis (SNOMED) added in condition_occurrence
- 4012185 — Cardiovascular surgical procedure (SNOMED) added in procedure_occurrence
- 4012314 — Suture of large intestine (SNOMED) added in procedure_occurrence
- 4012500 — Nausea present (SNOMED) added in observation
- 4012907 — Operation on musculoskeletal system (SNOMED) added in procedure_occurrence
- 4012933 — Arteriectomy with graft replacement of thoracoabdominal aorta (SNOMED) added in procedure_occurrence
- 4012936 — Femoral-popliteal artery bypass graft (SNOMED) added in procedure_occurrence
- 4013354 — Insertion of endotracheal tube (SNOMED) added in procedure_occurrence
- 4013596 — Closed fracture thoracic vertebra (SNOMED) added in condition_occurrence
- 4013604 — Closed fracture lumbar vertebra (SNOMED) added in condition_occurrence
- 4013613 — Fracture of lumbar spine and/or pelvis (SNOMED) added in condition_occurrence
- 4013643 — Pulmonary arterial hypertension (SNOMED) added in condition_occurrence
- 4014781 — Closed traumatic subdural hemorrhage (SNOMED) added in condition_occurrence
- 4015701 — Cesarean section (SNOMED) added in procedure_occurrence
- 4016042 — Diabetic on oral treatment (SNOMED) added in observation
- 4016548 — Closed injury of pleura (SNOMED) added in condition_occurrence
- 4016891 — Isolation of infection carrier (SNOMED) added in procedure_occurrence
- 4018012 — Emergency appendectomy (SNOMED) added in procedure_occurrence
- 4019128 — Fluoroscopy guided percutaneous transluminal angioplasty of subclavian artery with contrast (SNOMED) added in procedure_occurrence
- 4019424 — Open embolectomy of renal artery (SNOMED) added in procedure_occurrence
- 4019540 — Evacuation of intracerebral hematoma (SNOMED) added in procedure_occurrence
- 4019824 — Transesophageal echocardiography (SNOMED) added in procedure_occurrence
- 4020216 — Revision of bypass for coronary artery (SNOMED) added in procedure_occurrence
- 4020329 — Pancreaticoduodenectomy (SNOMED) added in procedure_occurrence
- 4021015 — Alternating the patient's position (SNOMED) added in procedure_occurrence
- 4021363 — Salpingo-oophorectomy (SNOMED) added in procedure_occurrence
- 4021519 — Changing endotracheal tube tapes (SNOMED) added in procedure_occurrence
- 4021529 — Abdominal hysterectomy (SNOMED) added in procedure_occurrence
- 4021813 — Operating room (SNOMED) added in visit_detail
- 4022029 — Reconstruction of renal artery (SNOMED) added in procedure_occurrence
- 4022093 — Electrolyte imbalance (SNOMED) added in condition_occurrence
- 4022318 — Revision of reconstruction of artery (SNOMED) added in procedure_occurrence
- 4022478 — Open excision of renal lesion (SNOMED) added in procedure_occurrence
- 4022804 — Kidney operation (SNOMED) added in procedure_occurrence
- 4022807 — Nephroureterectomy (SNOMED) added in procedure_occurrence
- 4023156 — Otic (SNOMED) added in drug_exposure
- 4023288 — Perineal urethrostomy (SNOMED) added in procedure_occurrence
- 4023415 — Bronchial sleeve resection with pulmonary resection (SNOMED) added in procedure_occurrence
- 4024117 — Pulmonary insufficiency following surgery (SNOMED) added in condition_occurrence
- 4024561 — Pain in lower limb (SNOMED) added in condition_occurrence
- 4025129 — Antibody screen (SNOMED) added in measurement
- 4026032 — Acute hepatic failure (SNOMED) added in condition_occurrence
- 4027426 — Kidney excision (SNOMED) added in procedure_occurrence
- 4027460 — Closed pertrochanteric fracture (SNOMED) added in condition_occurrence
- 4027663 — Peptic ulcer (SNOMED) added in condition_occurrence
- 4028070 — Infectious disease of central nervous system (SNOMED) added in condition_occurrence
- 4028244 — Chronic disease of cardiovascular system (SNOMED) added in condition_occurrence
- 4028623 — Transplantation of bone marrow (SNOMED) added in procedure_occurrence
- 4029205 — Procedure by method (SNOMED) added in procedure_occurrence
- 4029329 — Hemifacial spasm (SNOMED) added in condition_occurrence
- 4029357 — Surgical removal of foreign body (SNOMED) added in procedure_occurrence
- 4029488 — Hepatic encephalopathy (SNOMED) added in condition_occurrence
- 4029498 — Seizure disorder (SNOMED) added in condition_occurrence
- 4029499 — Infectious disease of brain (SNOMED) added in condition_occurrence
- 4029571 — Excision of urinary bladder (SNOMED) added in procedure_occurrence
- 4029966 — Intracranial aneurysm (SNOMED) added in condition_occurrence
- 4030065 — Hyposplenism (SNOMED) added in condition_occurrence
- 4030087 — Nasal septoplasty (SNOMED) added in procedure_occurrence
- 4030107 — Thyroidectomy (SNOMED) added in procedure_occurrence
- 4030153 — Operative procedure on hematopoietic system (SNOMED) added in procedure_occurrence
- 4030239 — Arthrotomy for removal of prosthesis of knee (SNOMED) added in procedure_occurrence
- 4030312 — Decompression of spinal cord (SNOMED) added in procedure_occurrence
- 4030387 — Laparoscopic-assisted sigmoid colectomy (SNOMED) added in procedure_occurrence
- 4030412 — Pelvic lymphadenectomy (SNOMED) added in procedure_occurrence
- 4030555 — Measles (SNOMED) added in condition_occurrence
- 4030654 — Operative procedure on digestive system (SNOMED) added in procedure_occurrence
- 4030657 — Operative procedure on small intestine (SNOMED) added in procedure_occurrence
- 4030715 — Operation on mandible (SNOMED) added in procedure_occurrence
- 4030825 — Debulking of pelvic tumor (SNOMED) added in procedure_occurrence
- 4030835 — Limited thoracotomy (SNOMED) added in procedure_occurrence
- 4030840 — Electroconvulsive therapy (SNOMED) added in procedure_occurrence
- 4031019 — Allergic contact dermatitis (SNOMED) added in condition_occurrence
- 4031321 — Operation on face (SNOMED) added in procedure_occurrence
- 4031454 — Open pleural procedure (SNOMED) added in procedure_occurrence
- 4031970 — Repair of incisional hernia (SNOMED) added in procedure_occurrence
- 4032334 — Hyperbilirubinemia (SNOMED) added in condition_occurrence
- 4032404 — Bronchoscopy (SNOMED) added in procedure_occurrence
- 4032735 — Laparoscopic radical hysterectomy (SNOMED) added in procedure_occurrence
- 4032774 — Thoracoscopy (SNOMED) added in procedure_occurrence
- 4032878 — Hair follicle disorder (SNOMED) added in condition_occurrence
- 4033319 — Lipoma of skin and subcutaneous tissue of trunk (SNOMED) added in condition_occurrence
- 4033396 — Laparoscopic repair of inguinal hernia (SNOMED) added in procedure_occurrence
- 4033525 — Arthroplasty of patella with prosthesis (SNOMED) added in procedure_occurrence
- 4033837 — Melanocytic nevus of trunk (SNOMED) added in condition_occurrence
- 4034680 — Operation for spinal trauma (SNOMED) added in procedure_occurrence
- 4035415 — Tear of meniscus of knee (SNOMED) added in condition_occurrence
- 4035436 — Secondary gout (SNOMED) added in condition_occurrence
- 4035611 — Seropositive rheumatoid arthritis (SNOMED) added in condition_occurrence
- 4035764 — Forefoot amputation (SNOMED) added in procedure_occurrence
- 4037761 — Report of transfusion reaction (SNOMED) added in observation
- 4038030 — Hearing difficulty (SNOMED) added in observation
- 4038835 — Hodgkin's disease (clinical) (SNOMED) added in condition_occurrence
- 4038838 — Non-Hodgkin's lymphoma (clinical) (SNOMED) added in condition_occurrence
- 4038839 — Hodgkin lymphoma, nodular lymphocyte predominance (clinical) (SNOMED) added in condition_occurrence
- 4039691 — Necrotizing vasculitis (SNOMED) added in condition_occurrence
- 4040299 — Operation on stomach (SNOMED) added in procedure_occurrence
- 4040392 — Procedure on genitourinary system (SNOMED) added in procedure_occurrence
- 4040820 — Rheumatic disease of mitral AND aortic valves (SNOMED) added in condition_occurrence
- 4041980 — Gastrointestinal tract repair (SNOMED) added in procedure_occurrence
- 4042673 — Procedure on heart (SNOMED) added in procedure_occurrence
- 4042677 — Procedure on artery (SNOMED) added in procedure_occurrence
- 4042907 — Hartmann operation, rectal resection (SNOMED) added in procedure_occurrence
- 4043019 — Procedure on nervous system (SNOMED) added in procedure_occurrence
- 4043191 — Procedure on urinary bladder (SNOMED) added in procedure_occurrence
- 4043371 — Inflammatory disorder of digestive tract (SNOMED) added in condition_occurrence
- 4043382 — Inguinal hernia with gangrene (SNOMED) added in condition_occurrence
- 4043731 — Infarction - precerebral (SNOMED) added in condition_occurrence
- 4043738 — Hydrocephalus (SNOMED) added in condition_occurrence
- 4044404 — Lumbosacral plexus neuropathy (SNOMED) added in condition_occurrence
- 4044526 — Amputation - action (SNOMED) added in observation
- 4045461 — External drainage procedure from ventricle of brain (SNOMED) added in procedure_occurrence
- 4045733 — Cerebrovascular and spinal vascular disorders (SNOMED) added in condition_occurrence
- 4045859 — Biopsy of brain tissue (SNOMED) added in procedure_occurrence
- 4046205 — Discitis (SNOMED) added in condition_occurrence
- 4046287 — Fixation and immobilization (SNOMED) added in procedure_occurrence
- 4046448 — Cerebrospinal fluid leak (SNOMED) added in condition_occurrence
- 4046500 — Acute peptic ulcer with hemorrhage (SNOMED) added in condition_occurrence
- 4046828 — Operation on pharynx (SNOMED) added in procedure_occurrence
- 4046917 — Repair of cranial cerebrospinal fluid fistula (SNOMED) added in procedure_occurrence
- 4047007 — Surgical procedure on intracranial aneurysm (SNOMED) added in procedure_occurrence
- 4047082 — Implantation of insertable loop recorder (SNOMED) added in procedure_occurrence
- 4047392 — Postpartum care (SNOMED) added in visit_occurrence
- 4048304 — Shunt of portal vein to vena cava (SNOMED) added in procedure_occurrence
- 4048317 — Operation on internal nose (SNOMED) added in procedure_occurrence
- 4048684 — Lumbosacral spondylosis (SNOMED) added in condition_occurrence
- 4049417 — Vesicular eczema (SNOMED) added in condition_occurrence
- 4049659 — Subcortical hemorrhage (SNOMED) added in condition_occurrence
- 4049677 — Axillobifemoral bypass graft (SNOMED) added in procedure_occurrence
- 4049812 — Portosystemic shunt operation (SNOMED) added in procedure_occurrence
- 4049832 — Insertion of peripheral venous cannula into peripheral vein (SNOMED) added in procedure_occurrence
- 4049965 — Fungal pneumonia (SNOMED) added in condition_occurrence
- 4050089 — Open wound of front wall of thorax (SNOMED) added in condition_occurrence
- 4050415 — Banding of arteriovenous fistula (SNOMED) added in procedure_occurrence
- 4050572 — Implantation of automatic cardiac defibrillator (SNOMED) added in procedure_occurrence
- 4050884 — Pleural plaque (SNOMED) added in condition_occurrence
- 4050977 — Wernicke's disease (SNOMED) added in condition_occurrence
- 4051005 — Open wound of nose (SNOMED) added in condition_occurrence
- 4051140 — Open wound of anterior abdominal wall (SNOMED) added in condition_occurrence
- 4051330 — Continuous venovenous hemofiltration (SNOMED) added in procedure_occurrence
- 4051619 — Repair of external nose (SNOMED) added in procedure_occurrence
- 4051764 — Contusion, throat (SNOMED) added in condition_occurrence
- 4051938 — Cardiac pacemaker procedure (SNOMED) added in procedure_occurrence
- 4052213 — Injury to blood vessels of lower limb (SNOMED) added in condition_occurrence
- 4052390 — Transjugular intrahepatic portosystemic shunt (SNOMED) added in procedure_occurrence
- 4052413 — Central venous cannula insertion (SNOMED) added in procedure_occurrence
- 4053272 — Injury of spleen (SNOMED) added in condition_occurrence
- 4053584 — Superficial injury (SNOMED) added in condition_occurrence
- 4053597 — Open wound of neck (SNOMED) added in condition_occurrence
- 4053604 — Open wound of lower leg (SNOMED) added in condition_occurrence
- 4053837 — Open wound of toe (SNOMED) added in condition_occurrence
- 4054047 — Lobectomy (SNOMED) added in procedure_occurrence
- 4054671 — Corrosion of esophagus (SNOMED) added in condition_occurrence
- 4054884 — Multiple open wounds of hip and/or thigh (SNOMED) added in condition_occurrence
- 4055224 — Toxic liver disease (SNOMED) added in condition_occurrence
- 4055341 — Calculus of bile duct with cholangitis (SNOMED) added in condition_occurrence
- 4056770 — Breast signs and symptoms (SNOMED) added in condition_occurrence
- 4057420 — Catheter ablation of tissue of heart (SNOMED) added in procedure_occurrence
- 4057765 — Vaginal (SNOMED) added in drug_exposure
- 4057953 — Acute gastric ulcer with perforation (SNOMED) added in condition_occurrence
- 4058494 — Superficial injuries involving multiple body regions (SNOMED) added in condition_occurrence
- 4058634 — Vascular bypass of renal artery with graft (SNOMED) added in procedure_occurrence
- 4058841 — Nephrotic syndrome, diffuse membranous glomerulonephritis (SNOMED) added in condition_occurrence
- 4059290 — Steatotic liver disease (SNOMED) added in condition_occurrence
- 4059379 — Mitochondrial myopathy (SNOMED) added in condition_occurrence
- 4059416 — Myxedema coma (SNOMED) added in condition_occurrence
- 4060036 — Obstructed labor due to breech presentation (SNOMED) added in condition_occurrence
- 4060043 — Excision of lesion of atrium (SNOMED) added in procedure_occurrence
- 4060257 — Insertion of intra-aortic balloon counterpulsation (SNOMED) added in procedure_occurrence
- 4060364 — Fasting (SNOMED) added in observation
- 4061074 — Periodic paralysis (SNOMED) added in condition_occurrence
- 4062791 — Endocrine, nutritional and metabolic disease complicating pregnancy, childbirth and puerperium (SNOMED) added in condition_occurrence
- 4062876 — Stereotactic biopsy of brain (SNOMED) added in procedure_occurrence
- 4063237 — Aortocoronary artery bypass graft with vein graft (SNOMED) added in procedure_occurrence
- 4063759 — Evacuation of intracranial extradural hematoma (SNOMED) added in procedure_occurrence
- 4064036 — Generalized skin eruption caused by drug and medicament (SNOMED) added in condition_occurrence
- 4064161 — Cirrhosis of liver (SNOMED) added in condition_occurrence
- 4064645 — Stereotactic ablation of brain tissue (SNOMED) added in procedure_occurrence
- 4065313 — Transsphenoidal hypophysectomy (SNOMED) added in procedure_occurrence
- 4065661 — Cerebrospinal fluid appearance (SNOMED) added in measurement
- 4066036 — Gastroduodenal fistula (SNOMED) added in condition_occurrence
- 4066995 — Fracture of vertebral column with spinal cord injury (SNOMED) added in condition_occurrence
- 4067028 — Removal of foreign body from cornea (SNOMED) added in procedure_occurrence
- 4067311 — Lumbar discitis (SNOMED) added in condition_occurrence
- 4067367 — Uncinectomy (SNOMED) added in procedure_occurrence
- 4067670 — Localized perfusion of liver (SNOMED) added in procedure_occurrence
- 4067713 — Bilobectomy of lung (SNOMED) added in procedure_occurrence
- 4068155 — Atrial arrhythmia (SNOMED) added in condition_occurrence
- 4068507 — Examination of rectum under anesthesia (SNOMED) added in procedure_occurrence
- 4070581 — Open pleurectomy (SNOMED) added in procedure_occurrence
- 4070719 — Tonsillectomy (SNOMED) added in procedure_occurrence
- 4070879 — Lobectomy of lung (SNOMED) added in procedure_occurrence
- 4070880 — Excision of segment of lung (SNOMED) added in procedure_occurrence
- 4070882 — Open excision of lesion of lung (SNOMED) added in procedure_occurrence
- 4070989 — Wedge resection of lip (SNOMED) added in procedure_occurrence
- 4071247 — Plantar fasciectomy (SNOMED) added in procedure_occurrence
- 4072147 — Supraomohyoid lymph nodes neck dissection (SNOMED) added in procedure_occurrence
- 4072633 — Weaning from mechanically assisted ventilation (SNOMED) added in procedure_occurrence
- 4073393 — Opening of chest (SNOMED) added in procedure_occurrence
- 4073990 — Removal of ureteral stent (SNOMED) added in procedure_occurrence
- 4074571 — Endoscopic freeing of adhesions of ovary (SNOMED) added in procedure_occurrence
- 4074689 — Open drainage of pleural cavity (SNOMED) added in procedure_occurrence
- 4074815 — Inflammatory bowel disease (SNOMED) added in condition_occurrence
- 4074848 — Endoscopic resection of lesion of peritoneum (SNOMED) added in procedure_occurrence
- 4075182 — Elective cesarean section (SNOMED) added in procedure_occurrence
- 4075360 — Surgical debridement of wound (SNOMED) added in procedure_occurrence
- 4075431 — Exploratory burrhole of cranium (SNOMED) added in procedure_occurrence
- 4076599 — Arthroscopic removal of loose body from knee joint (SNOMED) added in procedure_occurrence
- 4076787 — Stoma assessment (SNOMED) added in observation
- 4076862 — Transplantation of liver (SNOMED) added in procedure_occurrence
- 4077017 — Sedated (SNOMED) added in observation
- 4077078 — Uncemented prosthetic hemiarthroplasty of hip joint (SNOMED) added in procedure_occurrence
- 4077081 — Superficial mycosis (SNOMED) added in condition_occurrence
- 4077577 — Moderate recurrent major depression (SNOMED) added in condition_occurrence
- 4078043 — Open reduction of fracture of zygomatic bone (SNOMED) added in procedure_occurrence
- 4078199 — Epidural anesthesia (SNOMED) added in procedure_occurrence
- 4078220 — Incision of mediastinum (SNOMED) added in procedure_occurrence
- 4078224 — Change of dressing (SNOMED) added in procedure_occurrence
- 4078260 — Puncture of joint (SNOMED) added in procedure_occurrence
- 4078308 — Repair of ileostomy (SNOMED) added in procedure_occurrence
- 4078747 — Application of mallet splint (SNOMED) added in procedure_occurrence
- 4078793 — Direct current cardioversion (SNOMED) added in procedure_occurrence
- 4079133 — Cormack and Lehane grade (SNOMED) added in observation
- 4079402 — Uncemented prosthetic total arthroplasty of shoulder joint (SNOMED) added in procedure_occurrence
- 4079713 — Excision of colon (SNOMED) added in procedure_occurrence
- 4079730 — Pleurectomy (SNOMED) added in procedure_occurrence
- 4079749 — Osteoarthritis of hip (SNOMED) added in condition_occurrence
- 4079750 — Osteoarthritis of knee (SNOMED) added in condition_occurrence
- 4079978 — Overlap syndrome (SNOMED) added in condition_occurrence
- 4080064 — Day hospital care (SNOMED) added in visit_occurrence
- 4080762 — Psychoactive substance dependence (SNOMED) added in condition_occurrence
- 4080965 — Extracorporeal circulation procedure (SNOMED) added in procedure_occurrence
- 4081119 — Nil by mouth (SNOMED) added in procedure_occurrence
- 4081709 — Endarterectomy of subclavian artery (SNOMED) added in procedure_occurrence
- 4081730 — Fleur de Lys abdominoplasty (SNOMED) added in procedure_occurrence
- 4081731 — Biopsy of skin (SNOMED) added in procedure_occurrence
- 4082463 — Monoclonal gammopathy of uncertain significance (SNOMED) added in condition_occurrence
- 4082555 — Antithromboembolic stockings (SNOMED) added in device_exposure
- 4082850 — Induction of general anesthesia (SNOMED) added in procedure_occurrence
- 4083100 — Fasciitis with eosinophilia syndrome (SNOMED) added in condition_occurrence
- 4083391 — Excision of lumbar intervertebral disc (SNOMED) added in procedure_occurrence
- 4083784 — Complement deficiency disease (SNOMED) added in condition_occurrence
- 4084229 — Primary gout (SNOMED) added in condition_occurrence
- 4085220 — Arthroscopy of shoulder (SNOMED) added in procedure_occurrence
- 4085259 — Respiratory muscular pressure (SNOMED) added in observation
- 4085444 — Intravascular ultrasound angiography of blood vessel (SNOMED) added in procedure_occurrence
- 4085901 — Gynecologic examination under general anesthesia (SNOMED) added in procedure_occurrence
- 4086024 — Removal of external fixation (SNOMED) added in procedure_occurrence
- 4086195 — Superficial injury of head (SNOMED) added in condition_occurrence
- 4086243 — Pulmonary sarcoidosis (SNOMED) added in condition_occurrence
- 4086433 — Active cooling of patient (SNOMED) added in procedure_occurrence
- 4086522 — Weight change (SNOMED) added in measurement
- 4086760 — Percutaneous balloon valvuloplasty of heart (SNOMED) added in procedure_occurrence
- 4086802 — Patient temporarily left (SNOMED) added in visit_detail
- 4086802 — Patient temporarily left (SNOMED) added in visit_occurrence
- 4087619 — Color of extremity (SNOMED) added in observation
- 4087760 — Bypass gastroenterostomy (SNOMED) added in procedure_occurrence
- 4088051 — Closed fracture of phalanx of finger (SNOMED) added in condition_occurrence
- 4089462 — Ventricular premature complex (SNOMED) added in condition_occurrence
- 4089843 — Energy expenditure (SNOMED) added in observation
- 4090926 — Revision of hip arthroplasty (SNOMED) added in procedure_occurrence
- 4091512 — Congenital cerebral arteriovenous aneurysm (SNOMED) added in condition_occurrence
- 4092632 — Rupture of urinary bladder (SNOMED) added in condition_occurrence
- 4092686 — Human immunodeficiency virus infection with secondary clinical infectious disease (SNOMED) added in condition_occurrence
- 4093228 — Disorder of soft tissue of lower limb (SNOMED) added in condition_occurrence
- 4093960 — Carcinoma in situ of bronchus and lung (SNOMED) added in condition_occurrence
- 4094240 — Open heart surgery (SNOMED) added in procedure_occurrence
- 4094283 — Lower limb joint arthritis (SNOMED) added in condition_occurrence
- 4094438 — Anti factor Xa measurement (SNOMED) added in measurement
- 4094683 — Chest injury (SNOMED) added in condition_occurrence
- 4094822 — Foreign body in respiratory tract (SNOMED) added in condition_occurrence
- 4095407 — Replacement of aortic valve (SNOMED) added in procedure_occurrence
- 4095470 — Irregular blood group antibody (SNOMED) added in observation
- 4095850 — Spinal injury (SNOMED) added in condition_occurrence
- 4096152 — Exploratory thoracotomy (SNOMED) added in procedure_occurrence
- 4096313 — Multiple injuries (SNOMED) added in condition_occurrence
- 4096479 — Traumatic amputation (SNOMED) added in condition_occurrence
- 4096616 — Diffuse brain injury (SNOMED) added in condition_occurrence
- 4096682 — Bleeding from nose (SNOMED) added in condition_occurrence
- 4096947 — Disorder of acid-base balance (SNOMED) added in condition_occurrence
- 4097064 — Operation on bronchus (SNOMED) added in procedure_occurrence
- 4097550 — Legionella infection (SNOMED) added in condition_occurrence
- 4097962 — Open wound of lower limb (SNOMED) added in condition_occurrence
- 4098039 — Cardiac electrophysiology (SNOMED) added in procedure_occurrence
- 4098191 — Replacement of tricuspid valve (SNOMED) added in procedure_occurrence
- 4098597 — Waldenström macroglobulinemia (SNOMED) added in condition_occurrence
- 4099402 — Insertion of intracardiac pacemaker (SNOMED) added in procedure_occurrence
- 4099792 — Drug-induced adrenocortical insufficiency (SNOMED) added in condition_occurrence
- 4100184 — Pustular psoriasis of palms and soles (SNOMED) added in condition_occurrence
- 4100857 — Extreme obesity with alveolar hypoventilation (SNOMED) added in condition_occurrence
- 4101149 — Non-organic psychosis (SNOMED) added in condition_occurrence
- 4101256 — Cocaine intoxication (SNOMED) added in condition_occurrence
- 4101626 — Craniotomy (SNOMED) added in procedure_occurrence
- 4102177 — Iris and ciliary body vascular disorder (SNOMED) added in condition_occurrence
- 4102631 — Acute tubulointerstitial nephritis (SNOMED) added in condition_occurrence
- 4102985 — Nonorganic insomnia (SNOMED) added in condition_occurrence
- 4103295 — Ventricular tachycardia (SNOMED) added in condition_occurrence
- 4103399 — Emotionally unstable personality disorder (SNOMED) added in condition_occurrence
- 4103532 — Immune thrombocytopenia (SNOMED) added in condition_occurrence
- 4103615 — Platelet product (SNOMED) added in device_exposure
- 4103650 — Disorder of Bartholin's gland (SNOMED) added in condition_occurrence
- 4103703 — Melena (SNOMED) added in condition_occurrence
- 4103791 — Plasma product (SNOMED) added in device_exposure
- 4105773 — Acute epiglottitis (SNOMED) added in condition_occurrence
- 4106678 — Superficial injury of ear region (SNOMED) added in condition_occurrence
- 4107893 — Blood culture (SNOMED) added in measurement
- 4108002 — Post-tetanic count (SNOMED) added in measurement
- 4108235 — Combined disorders of mitral, aortic and tricuspid valves (SNOMED) added in condition_occurrence
- 4108637 — Superficial injury of nose (SNOMED) added in condition_occurrence
- 4108814 — Pericardial effusion - noninflammatory (SNOMED) added in condition_occurrence
- 4108838 — Insertion of chronic ambulatory peritoneal dialysis catheter (SNOMED) added in procedure_occurrence
- 4110180 — Pneumonitis caused by inhalation of vomitus (SNOMED) added in condition_occurrence
- 4110815 — Sensorineural hearing loss of bilateral ears (SNOMED) added in condition_occurrence
- 4110961 — Generalized ischemic myocardial dysfunction (SNOMED) added in condition_occurrence
- 4111700 — Ventricular fibrillation and flutter (SNOMED) added in condition_occurrence
- 4111917 — Malignant mesothelioma of pleura (SNOMED) added in condition_occurrence
- 4112026 — Sequelae of cerebral infarction (SNOMED) added in condition_occurrence
- 4112340 — Dilation of esophagus (SNOMED) added in procedure_occurrence
- 4112813 — Drug-induced interstitial lung disorder (SNOMED) added in condition_occurrence
- 4113129 — Benign tumor of soft tissue of head, face and neck (SNOMED) added in condition_occurrence
- 4114638 — Uterine packing (SNOMED) added in procedure_occurrence
- 4115173 — Atrial premature complex (SNOMED) added in condition_occurrence
- 4115282 — Trichilemmal cyst (SNOMED) added in condition_occurrence
- 4116092 — Intracranial tumor (SNOMED) added in condition_occurrence
- 4116209 — Acute inflammation of lacrimal passages (SNOMED) added in condition_occurrence
- 4116629 — Embolectomy of axillary artery (SNOMED) added in procedure_occurrence
- 4117553 — Recurrent dislocation of the patellofemoral joint (SNOMED) added in condition_occurrence
- 4118634 — Grafting to skin (SNOMED) added in procedure_occurrence
- 4118910 — Maternal hypertension (SNOMED) added in condition_occurrence
- 4118958 — Lobectomy of thyroid gland (SNOMED) added in procedure_occurrence
- 4118992 — Intracranial meningioma (SNOMED) added in condition_occurrence
- 4118993 — Pheochromocytoma (SNOMED) added in condition_occurrence
- 4119130 — Malignant lymphoma - small lymphocytic (SNOMED) added in condition_occurrence
- 4119250 — Lung tumor excision (SNOMED) added in procedure_occurrence
- 4119438 — Acute mediastinitis (SNOMED) added in condition_occurrence
- 4119460 — Infective endocarditis (SNOMED) added in condition_occurrence
- 4119786 — Interstitial lung disease (SNOMED) added in condition_occurrence
- 4119939 — Bronchopleural fistula (SNOMED) added in condition_occurrence
- 4119942 — Stable angina (SNOMED) added in condition_occurrence
- 4120088 — Cardiac arrest with successful resuscitation (SNOMED) added in condition_occurrence
- 4120275 — Drug-induced hypotension (SNOMED) added in condition_occurrence
- 4120425 — Excision of group of lymph nodes (SNOMED) added in procedure_occurrence
- 4120657 — Interventional debulking surgery (SNOMED) added in procedure_occurrence
- 4121463 — Postoperative cardiac complication (SNOMED) added in condition_occurrence
- 4121697 — Surgery (SNOMED) added in visit_occurrence
- 4121803 — Cerebral arteriovenous malformation (SNOMED) added in condition_occurrence
- 4122234 — Percutaneous endoscopic gastrostomy (SNOMED) added in procedure_occurrence
- 4122784 — Excision of pelvic lymph node (SNOMED) added in procedure_occurrence
- 4124310 — Subtotal pancreatectomy (SNOMED) added in procedure_occurrence
- 4124693 — Hypertrophic cardiomyopathy (SNOMED) added in condition_occurrence
- 4125465 — Block dissection of pelvic lymph nodes (SNOMED) added in procedure_occurrence
- 4125482 — Splenectomy (SNOMED) added in procedure_occurrence
- 4125650 — Thrombophilia (SNOMED) added in condition_occurrence
- 4126119 — Toxic nephropathy (SNOMED) added in condition_occurrence
- 4127117 — Varicose ulcer of lower extremity (SNOMED) added in condition_occurrence
- 4127137 — Local transposition flap (SNOMED) added in procedure_occurrence
- 4127726 — Functional disorder of penis (SNOMED) added in condition_occurrence
- 4127886 — Hysterectomy (SNOMED) added in procedure_occurrence
- 4128302 — Mediastinoscopy (SNOMED) added in procedure_occurrence
- 4129391 — Female genital tract infection (SNOMED) added in condition_occurrence
- 4129407 — Open wound of knee (SNOMED) added in condition_occurrence
- 4129595 — Autologous blood product (SNOMED) added in device_exposure
- 4129747 — Operation on female genital organs (SNOMED) added in procedure_occurrence
- 4129922 — Unknown (SNOMED) added in visit_occurrence
- 4130040 — Neoplasm of spinal cord (SNOMED) added in condition_occurrence
- 4130390 — Refashioning urinary stoma (SNOMED) added in procedure_occurrence
- 4130675 — Neoplasm of adrenal gland (SNOMED) added in condition_occurrence
- 4130851 — Injury of upper extremity (SNOMED) added in condition_occurrence
- 4130852 — Injury of lower limb (SNOMED) added in condition_occurrence
- 4131102 — Cerebellopontine angle tumor (SNOMED) added in condition_occurrence
- 4131770 — Neoplasm of central nervous system (SNOMED) added in condition_occurrence
- 4131791 — Hydrocele of testis (SNOMED) added in condition_occurrence
- 4131909 — Neoplasm of thyroid gland (SNOMED) added in condition_occurrence
- 4132161 — Oral (SNOMED) added in drug_exposure
- 4132254 — Gastrostomy (SNOMED) added in drug_exposure
- 4132546 — Traumatic brain injury (SNOMED) added in condition_occurrence
- 4133004 — Deep venous thrombosis (SNOMED) added in condition_occurrence
- 4133177 — Jejunostomy (SNOMED) added in drug_exposure
- 4133224 — Lobar pneumonia (SNOMED) added in condition_occurrence
- 4133599 — Chronic myelomonocytic leukemia (SNOMED) added in condition_occurrence
- 4134121 — Lumbar radiculopathy (SNOMED) added in condition_occurrence
- 4134162 — Subarachnoid hemorrhage due to traumatic injury (SNOMED) added in condition_occurrence
- 4134423 — Removal of device (SNOMED) added in procedure_occurrence
- 4134439 — Injury of central nervous system (SNOMED) added in condition_occurrence
- 4134455 — Mononeuropathy (SNOMED) added in condition_occurrence
- 4134552 — Hereditary motor and sensory neuropathy (SNOMED) added in condition_occurrence
- 4134577 — Complex regional pain syndrome (SNOMED) added in condition_occurrence
- 4134603 — Vascular disorder of intestine (SNOMED) added in condition_occurrence
- 4134867 — Mixed collagen vascular disease (SNOMED) added in condition_occurrence
- 4134891 — Removal of therapeutic shunt device (SNOMED) added in procedure_occurrence
- 4134928 — Perforation of urinary bladder (SNOMED) added in condition_occurrence
- 4135096 — Fracture dislocation of spine (SNOMED) added in condition_occurrence
- 4135466 — Hemothorax (SNOMED) added in condition_occurrence
- 4135822 — Primary biliary cholangitis (SNOMED) added in condition_occurrence
- 4136335 — Thrombosis of arteries of upper extremity (SNOMED) added in condition_occurrence
- 4137127 — Transplantation of heart (SNOMED) added in procedure_occurrence
- 4137275 — Vasculitis (SNOMED) added in condition_occurrence
- 4137462 — Adrenalectomy (SNOMED) added in procedure_occurrence
- 4137468 — Abscess of skin and/or subcutaneous tissue (SNOMED) added in condition_occurrence
- 4137916 — Admission to anesthetic department (SNOMED) added in visit_occurrence
- 4138149 — Dislocation of acromioclavicular joint (SNOMED) added in condition_occurrence
- 4138676 — Arteriectomy with graft replacement of thoracic aorta (SNOMED) added in procedure_occurrence
- 4138738 — Vaginal hysterectomy (SNOMED) added in procedure_occurrence
- 4138763 — Acceptable pain level status (SNOMED) added in observation
- 4138816 — Cranioplasty (SNOMED) added in procedure_occurrence
- 4138837 — Pericarditis (SNOMED) added in condition_occurrence
- 4138959 — Heart-lung transplant with recipient cardiectomy-pneumonectomy (SNOMED) added in procedure_occurrence
- 4138962 — Acute duodenal ulcer without hemorrhage AND without perforation (SNOMED) added in condition_occurrence
- 4139147 — Drain (SNOMED) added in device_exposure
- 4139214 — Open implantation of cardiac ventricular assist device (SNOMED) added in procedure_occurrence
- 4139367 — Ethylene glycol poisoning (SNOMED) added in condition_occurrence
- 4139931 — Operation on aorta (SNOMED) added in procedure_occurrence
- 4140007 — Creation of graft fistula for dialysis (SNOMED) added in procedure_occurrence
- 4140266 — Operation on burnt skin (SNOMED) added in procedure_occurrence
- 4141028 — Cervical disc disorder (SNOMED) added in condition_occurrence
- 4141360 — Chronic atrial fibrillation (SNOMED) added in condition_occurrence
- 4141456 — Pancreatectomy (SNOMED) added in procedure_occurrence
- 4141919 — Insertion of pleural tube drain (SNOMED) added in procedure_occurrence
- 4142048 — Subcutaneous (SNOMED) added in drug_exposure
- 4142194 — Renal abscess (SNOMED) added in condition_occurrence
- 4142332 — Alveolar dead space (SNOMED) added in measurement
- 4142628 — Pericardiectomy (SNOMED) added in procedure_occurrence
- 4142645 — Angiography of coronary artery (SNOMED) added in procedure_occurrence
- 4142959 — Fasciotomy thigh (SNOMED) added in procedure_occurrence
- 4143247 — Respiratory assist, manual, using bag-valve-mask (SNOMED) added in procedure_occurrence
- 4143443 — Discharge to nursing home (SNOMED) added in visit_occurrence
- 4143445 — Discharge to tertiary referral hospital (SNOMED) added in visit_occurrence
- 4143480 — Hyperkeratosis follicularis in cutem penetrans (SNOMED) added in condition_occurrence
- 4143508 — Ureteroscopic removal of ureteric calculus (SNOMED) added in procedure_occurrence
- 4143658 — Split thickness graft of skin to skin (SNOMED) added in procedure_occurrence
- 4143700 — Smoke inhalation injury (SNOMED) added in condition_occurrence
- 4143852 — Laparoscopic sleeve gastrectomy (SNOMED) added in procedure_occurrence
- 4144111 — Gastroesophageal reflux disease without esophagitis (SNOMED) added in condition_occurrence
- 4144800 — Laparoscopic gastroenterostomy (SNOMED) added in procedure_occurrence
- 4144835 — Crushing injury of chest (SNOMED) added in condition_occurrence
- 4144861 — Drainage of pericardium (SNOMED) added in procedure_occurrence
- 4144868 — Transluminal operations on renal artery (SNOMED) added in procedure_occurrence
- 4144895 — Flaccid neurogenic urinary bladder (SNOMED) added in condition_occurrence
- 4145042 — Thrombolytic therapy (SNOMED) added in procedure_occurrence
- 4145119 — Heart valve replacement (SNOMED) added in procedure_occurrence
- 4145308 — 12 lead ECG (SNOMED) added in procedure_occurrence
- 4145497 — Intrinsic asthma (SNOMED) added in condition_occurrence
- 4145658 — Physiotherapy/remedial therapy (SNOMED) added in procedure_occurrence
- 4145825 — Anorectal disorder (SNOMED) added in condition_occurrence
- 4145834 — Open thrombectomy of renal vein (SNOMED) added in procedure_occurrence
- 4145909 — Pericardial fluid (SNOMED) added in observation
- 4146116 — Nystagmus and other irregular eye movements (SNOMED) added in condition_occurrence
- 4146142 — Repair of traumatic injury of heart (SNOMED) added in procedure_occurrence
- 4146154 — Biopsy of tendon (SNOMED) added in procedure_occurrence
- 4146256 — Transplant nephrectomy (SNOMED) added in procedure_occurrence
- 4146331 — Diathermy of skin lesion (SNOMED) added in procedure_occurrence
- 4146781 — Endarterectomy of iliac artery (SNOMED) added in procedure_occurrence
- 4147164 — Malignant tumor of lymphoid hemopoietic and related tissue (SNOMED) added in condition_occurrence
- 4147223 — Rupture of ventricle due to acute myocardial infarction (SNOMED) added in condition_occurrence
- 4147411 — Follicular lymphoma (SNOMED) added in condition_occurrence
- 4147498 — Encephalitis, myelitis and encephalomyelitis (SNOMED) added in condition_occurrence
- 4147787 — Supravalvar aortic stenosis (SNOMED) added in condition_occurrence
- 4147837 — Generalized metabolic disorder (SNOMED) added in condition_occurrence
- 4148369 — Angiocardiography (SNOMED) added in procedure_occurrence
- 4148645 — Endoscopy service (SNOMED) added in visit_detail
- 4148645 — Endoscopy service (SNOMED) added in visit_occurrence
- 4148882 — Hemorrhagic shock (SNOMED) added in condition_occurrence
- 4148906 — Spontaneous subarachnoid hemorrhage (SNOMED) added in condition_occurrence
- 4148948 — Vascular surgery procedure (SNOMED) added in procedure_occurrence
- 4148972 — Extubation of trachea (SNOMED) added in procedure_occurrence
- 4149322 — Primary malignant neoplasm of unknown site (SNOMED) added in condition_occurrence
- 4149851 — Malignant melanoma of upper limb (SNOMED) added in condition_occurrence
- 4149930 — Pericardiocentesis (SNOMED) added in procedure_occurrence
- 4150301 — Stenosis and insufficiency of lacrimal passages (SNOMED) added in condition_occurrence
- 4150663 — Operation on pleural cavity (SNOMED) added in procedure_occurrence
- 4150799 — Dissociative motor disorder (SNOMED) added in condition_occurrence
- 4150851 — Cognitive functions (SNOMED) added in observation
- 4150864 — Rehabilitation service (SNOMED) added in visit_occurrence
- 4151109 — Partial thickness burn of wrist and hand (SNOMED) added in condition_occurrence
- 4151134 — Cyst of pancreas (SNOMED) added in condition_occurrence
- 4151250 — Malignant neoplasm of upper lobe, bronchus or lung (SNOMED) added in condition_occurrence
- 4151263 — Malignant melanoma of lower limb (SNOMED) added in condition_occurrence
- 4151314 — Removal of Kirschner wire internal bone fixator (SNOMED) added in procedure_occurrence
- 4151385 — Manual removal of retained placenta (SNOMED) added in procedure_occurrence
- 4151597 — Patient discharge, deceased, autopsy (SNOMED) added in visit_occurrence
- 4151768 — Pack years (SNOMED) added in measurement
- 4152054 — Functional endoscopic sinus surgery, total (SNOMED) added in procedure_occurrence
- 4152376 — Intentional self poisoning (SNOMED) added in condition_occurrence
- 4152592 — Spinal stenosis of lumbosacral region (SNOMED) added in condition_occurrence
- 4152745 — Excision of neoplasm (SNOMED) added in procedure_occurrence
- 4153292 — Schizoaffective disorder, manic type (SNOMED) added in condition_occurrence
- 4153359 — Arthritis of spine (SNOMED) added in condition_occurrence
- 4153380 — Disorder of carotid artery (SNOMED) added in condition_occurrence
- 4153739 — Open wound of larynx and trachea (SNOMED) added in condition_occurrence
- 4153877 — Post-traumatic wound infection (SNOMED) added in condition_occurrence
- 4154168 — Pelvic injury (SNOMED) added in condition_occurrence
- 4154290 — Paroxysmal atrial fibrillation (SNOMED) added in condition_occurrence
- 4155151 — Oxygen administration by nasal cannula (SNOMED) added in procedure_occurrence
- 4155910 — Generalized edema (SNOMED) added in condition_occurrence
- 4155911 — Petechiae (SNOMED) added in condition_occurrence
- 4155966 — Patient deceased during stay (discharge status = dead) (SNOMED) added in observation
- 4156705 — Intracardiac (SNOMED) added in drug_exposure
- 4156706 — Intradermal (SNOMED) added in drug_exposure
- 4156707 — Intrapleural (SNOMED) added in drug_exposure
- 4157408 — Medical Research Council questionnaire (SNOMED) added in measurement
- 4157453 — Disorder of joint of spine (SNOMED) added in condition_occurrence
- 4157758 — Intralesional (SNOMED) added in drug_exposure
- 4157759 — Intralymphatic (SNOMED) added in drug_exposure
- 4157760 — Intraocular (SNOMED) added in drug_exposure
- 4157761 — Perineural (SNOMED) added in drug_exposure
- 4158349 — Deficient urine secretion (SNOMED) added in condition_occurrence
- 4158481 — Disorder of intrauterine contraceptive device (SNOMED) added in condition_occurrence
- 4158978 — Somnolence syndrome (SNOMED) added in condition_occurrence
- 4159411 — American Society of Anesthesiologists physical status classification (SNOMED) added in measurement
- 4159691 — Poisoning by anti-psychotic agent (SNOMED) added in condition_occurrence
- 4159766 — Amputation of toe (SNOMED) added in procedure_occurrence
- 4159949 — Surgical procedure on soft tissue (SNOMED) added in procedure_occurrence
- 4159959 — Vascular surgery procedure on abdominal region (SNOMED) added in procedure_occurrence
- 4160159 — Log roll (SNOMED) added in procedure_occurrence
- 4160163 — Construction of cecostomy (SNOMED) added in procedure_occurrence
- 4160328 — Tinea cruris (SNOMED) added in condition_occurrence
- 4161701 — Pericardial effusion (SNOMED) added in condition_occurrence
- 4162246 — Insertion of inferior vena caval filter (SNOMED) added in procedure_occurrence
- 4162253 — Primary malignant neoplasm of breast (SNOMED) added in condition_occurrence
- 4163765 — Dental (SNOMED) added in drug_exposure
- 4163768 — Intrabursal (SNOMED) added in drug_exposure
- 4163770 — Subconjunctival (SNOMED) added in drug_exposure
- 4163872 — Plain X-ray of chest (SNOMED) added in procedure_occurrence
- 4163971 — Laparoscopic cholecystectomy (SNOMED) added in procedure_occurrence
- 4164649 — Non-cardiac chest pain (SNOMED) added in condition_occurrence
- 4164770 — Guillain-Barré syndrome (SNOMED) added in condition_occurrence
- 4164898 — Diverticulosis of large intestine without diverticulitis (SNOMED) added in condition_occurrence
- 4165145 — Hospital anxiety and depression scale (SNOMED) added in measurement
- 4165549 — Operative procedure on large intestine (SNOMED) added in procedure_occurrence
- 4165998 — Generalized enlarged lymph nodes (SNOMED) added in condition_occurrence
- 4166673 — Replacement of prosthesis of lower extremity (SNOMED) added in procedure_occurrence
- 4166844 — Intraventricular conduction defect (SNOMED) added in condition_occurrence
- 4167031 — Pulmonary medicine (SNOMED) added in visit_occurrence
- 4167074 — Osteotomy for hallux valgus (SNOMED) added in procedure_occurrence
- 4167183 — Cordectomy of vocal cord (SNOMED) added in procedure_occurrence
- 4167420 — Reduction of dislocation of ankle (SNOMED) added in procedure_occurrence
- 4167540 — Enteral (SNOMED) added in drug_exposure
- 4167984 — Bacterial arthritis (SNOMED) added in condition_occurrence
- 4168047 — Colostomy (SNOMED) added in drug_exposure
- 4168082 — Bone nailing (SNOMED) added in procedure_occurrence
- 4168133 — Incision of trachea (SNOMED) added in procedure_occurrence
- 4168213 — Chest pain on breathing (SNOMED) added in condition_occurrence
- 4168335 — Wound (SNOMED) added in condition_occurrence
- 4168656 — Intratympanic (SNOMED) added in drug_exposure
- 4168665 — Gastro-intestinal stoma (SNOMED) added in drug_exposure
- 4168700 — Localized enlarged lymph nodes (SNOMED) added in condition_occurrence
- 4168831 — Minimally invasive direct coronary artery bypass (SNOMED) added in procedure_occurrence
- 4169095 — Bradycardia (SNOMED) added in condition_occurrence
- 4169171 — Medical Research Council motor power scale (SNOMED) added in measurement
- 4169270 — Intrapulmonary (SNOMED) added in drug_exposure
- 4169287 — Itching of skin (SNOMED) added in condition_occurrence
- 4169306 — Internal medicine (SNOMED) added in visit_occurrence
- 4169333 — Respiratory index (SNOMED) added in measurement
- 4169456 — Otolaryngology (SNOMED) added in visit_occurrence
- 4169634 — Submucosal (SNOMED) added in drug_exposure
- 4169822 — Syme through ankle amputation (SNOMED) added in procedure_occurrence
- 4169954 — Genitourinary tract hemorrhage (SNOMED) added in condition_occurrence
- 4170058 — Operation on esophagus (SNOMED) added in procedure_occurrence
- 4170137 — Non-suppurative otitis media (SNOMED) added in condition_occurrence
- 4170143 — Respiratory tract infection (SNOMED) added in condition_occurrence
- 4170554 — Pain of hip region (SNOMED) added in condition_occurrence
- 4170620 — Aortic thromboembolism (SNOMED) added in condition_occurrence
- 4170675 — Aspirin overdose (SNOMED) added in condition_occurrence
- 4171047 — Intravenous (SNOMED) added in drug_exposure
- 4171243 — Mucous fistula (SNOMED) added in drug_exposure
- 4171379 — Disorder of the genitourinary system (SNOMED) added in condition_occurrence
- 4171917 — Localized edema (SNOMED) added in condition_occurrence
- 4172438 — Total pneumonectomy (SNOMED) added in procedure_occurrence
- 4172515 — Therapeutic procedure (SNOMED) added in procedure_occurrence
- 4172820 — Elevation of head of bed (SNOMED) added in procedure_occurrence
- 4173491 — Internal fixation of fracture of spine (SNOMED) added in procedure_occurrence
- 4173525 — Acetaminophen overdose (SNOMED) added in condition_occurrence
- 4173746 — Hallucinogen intoxication (SNOMED) added in condition_occurrence
- 4173824 — B-cell chronic lymphocytic leukemia variant (SNOMED) added in condition_occurrence
- 4174035 — Subtotal gastrectomy (SNOMED) added in procedure_occurrence
- 4174262 — Polyneuropathy (SNOMED) added in condition_occurrence
- 4174389 — Operation on biliary tract (SNOMED) added in procedure_occurrence
- 4174487 — Tetracyclic antidepressant drug overdose (SNOMED) added in condition_occurrence
- 4175154 — Disorder of the peripheral nervous system (SNOMED) added in condition_occurrence
- 4175848 — Monoarthritis of hip joint (SNOMED) added in condition_occurrence
- 4176148 — Extradural intracranial hematoma (SNOMED) added in condition_occurrence
- 4176725 — Retroperitoneal fibrosis (SNOMED) added in condition_occurrence
- 4177112 — Malignant tumor of trachea (SNOMED) added in condition_occurrence
- 4177206 — Tubulointerstitial nephritis (SNOMED) added in condition_occurrence
- 4177224 — Non-invasive ventilation (SNOMED) added in procedure_occurrence
- 4177376 — Laparoscopic adrenalectomy (SNOMED) added in procedure_occurrence
- 4177387 — Chronic gastrojejunal ulcer without hemorrhage AND without perforation (SNOMED) added in condition_occurrence
- 4178411 — Overdose of tricyclic antidepressant (SNOMED) added in condition_occurrence
- 4178431 — Cartilage disorder (SNOMED) added in condition_occurrence
- 4178736 — Pelvic exenteration (SNOMED) added in procedure_occurrence
- 4179720 — Primary malignant neoplasm of gastrointestinal tract (SNOMED) added in condition_occurrence
- 4180007 — Decompressive fasciotomy (SNOMED) added in procedure_occurrence
- 4181064 — Inflammatory disorder of extremity (SNOMED) added in condition_occurrence
- 4181152 — Endovascular repair of thoracic aortic aneurysm using endovascular stent graft (SNOMED) added in procedure_occurrence
- 4181187 — Inflammatory disorder of head (SNOMED) added in condition_occurrence
- 4181209 — Peripheral vascular complication of procedure (SNOMED) added in condition_occurrence
- 4181404 — Heat stroke (SNOMED) added in condition_occurrence
- 4181450 — Insertion of stent into ureter (SNOMED) added in procedure_occurrence
- 4181705 — Varicose veins of lower limb without ulcer and without inflammation (SNOMED) added in condition_occurrence
- 4181897 — Buccal (SNOMED) added in drug_exposure
- 4182210 — Dementia (SNOMED) added in condition_occurrence
- 4182562 — Lower abdominal pain (SNOMED) added in condition_occurrence
- 4182596 — Myxedema (SNOMED) added in condition_occurrence
- 4182711 — Vasculitis of the skin (SNOMED) added in condition_occurrence
- 4183308 — Endarterectomy of upper limb artery (SNOMED) added in procedure_occurrence
- 4183430 — Aneurysmectomy of ventricle of heart (SNOMED) added in procedure_occurrence
- 4184746 — Left ventricular hypertrophy (SNOMED) added in condition_occurrence
- 4184976 — Angioimmunoblastic T-cell lymphoma (SNOMED) added in condition_occurrence
- 4185284 — Removal of thrombus (SNOMED) added in procedure_occurrence
- 4185572 — Ventricular arrhythmia (SNOMED) added in condition_occurrence
- 4186832 — Endotracheopulmonary (SNOMED) added in drug_exposure
- 4186834 — Gastroenteral (SNOMED) added in drug_exposure
- 4186836 — Intracoronary (SNOMED) added in drug_exposure
- 4186837 — Intrasternal (SNOMED) added in drug_exposure
- 4186838 — Intravesical (SNOMED) added in drug_exposure
- 4186839 — Oromucosal (SNOMED) added in drug_exposure
- 4187067 — Disorder of coronary artery (SNOMED) added in condition_occurrence
- 4187501 — Angiectomy with anastomosis (SNOMED) added in procedure_occurrence
- 4188155 — Hernia of anterior abdominal wall (SNOMED) added in condition_occurrence
- 4189194 — Vascular subclavian-subclavian bypass (SNOMED) added in procedure_occurrence
- 4189235 — Third cranial nerve weakness (SNOMED) added in condition_occurrence
- 4189293 — Vascular disorder of lower extremity (SNOMED) added in condition_occurrence
- 4189343 — Aortic valve stenosis (SNOMED) added in condition_occurrence
- 4190430 — Ophthalmology (SNOMED) added in visit_occurrence
- 4190526 — Laparoscopic total abdominal hysterectomy and bilateral salpingo-oophorectomy (SNOMED) added in procedure_occurrence
- 4190569 — Other category (SNOMED) added in visit_occurrence
- 4190647 — Pneumocystosis pneumonia (SNOMED) added in condition_occurrence
- 4191479 — Allergic asthma (SNOMED) added in condition_occurrence
- 4191597 — Disorder of refraction (SNOMED) added in condition_occurrence
- 4191948 — Implantation of internal cardiac defibrillator (SNOMED) added in procedure_occurrence
- 4192174 — Illness (SNOMED) added in condition_occurrence
- 4192640 — Pancreatitis (SNOMED) added in condition_occurrence
- 4192647 — Hypovolemic shock (SNOMED) added in condition_occurrence
- 4192658 — Neurology (SNOMED) added in provider
- 4192658 — Neurology (SNOMED) added in visit_occurrence
- 4193506 — Disease of presumed infectious origin (SNOMED) added in condition_occurrence
- 4193868 — Sedative, hypnotic AND/OR anxiolytic-related disorder (SNOMED) added in condition_occurrence
- 4194238 — Endarterectomy (SNOMED) added in procedure_occurrence
- 4194377 — Patient discharge, deceased, no autopsy (SNOMED) added in visit_occurrence
- 4194666 — Posterior tibial artery bypass graft with vein (SNOMED) added in procedure_occurrence
- 4194676 — General treatment (SNOMED) added in procedure_occurrence
- 4194894 — Muscle and tendon injury (SNOMED) added in condition_occurrence
- 4194964 — Operation on endocrine system (SNOMED) added in procedure_occurrence
- 4195136 — Amputation above-knee (SNOMED) added in procedure_occurrence
- 4195255 — Excision of excessive skin and subcutaneous tissue of buttock (SNOMED) added in procedure_occurrence
- 4195694 — Acute respiratory distress syndrome (SNOMED) added in condition_occurrence
- 4195847 — Acute peritonitis (SNOMED) added in condition_occurrence
- 4196232 — Hemodynamic measurements (SNOMED) added in procedure_occurrence
- 4196678 — Hernia repair (SNOMED) added in procedure_occurrence
- 4197480 — Percutaneous insertion of nephrostomy tube (SNOMED) added in procedure_occurrence
- 4197485 — Epileptic seizure (SNOMED) added in condition_occurrence
- 4197894 — Insertion of implantable venous access port (SNOMED) added in procedure_occurrence
- 4198190 — Appendectomy (SNOMED) added in procedure_occurrence
- 4198492 — Shoulder joint unstable (SNOMED) added in condition_occurrence
- 4198854 — Total ureterectomy (SNOMED) added in procedure_occurrence
- 4199899 — Closure of ventricular septal defect (SNOMED) added in procedure_occurrence
- 4199961 — Acute lung injury (SNOMED) added in condition_occurrence
- 4200113 — Non-Q wave myocardial infarction (SNOMED) added in condition_occurrence
- 4200418 — Parathyroidectomy (SNOMED) added in procedure_occurrence
- 4200520 — Neck swelling (SNOMED) added in condition_occurrence
- 4200997 — Administration of analgesic (SNOMED) added in procedure_occurrence
- 4201174 — Injury of lung (SNOMED) added in condition_occurrence
- 4201387 — Tracheostomy present (SNOMED) added in condition_occurrence
- 4201745 — Disorder of digestive system (SNOMED) added in condition_occurrence
- 4202064 — Gastrointestinal perforation (SNOMED) added in condition_occurrence
- 4203153 — Replacement of mitral valve (SNOMED) added in procedure_occurrence
- 4203625 — Chronic constrictive pericarditis (SNOMED) added in condition_occurrence
- 4203771 — Total replacement of hip (SNOMED) added in procedure_occurrence
- 4204677 — Gastrostomy (SNOMED) added in procedure_occurrence
- 4205229 — Arthroscopy of knee (SNOMED) added in procedure_occurrence
- 4205990 — Implantation of simple one wire intravenous cardiac pacemaker (SNOMED) added in procedure_occurrence
- 4205991 — Implantation of complex two wire intravenous cardiac pacemaker (SNOMED) added in procedure_occurrence
- 4206116 — Patient warming therapy (SNOMED) added in procedure_occurrence
- 4206148 — Syncope and collapse (SNOMED) added in condition_occurrence
- 4206400 — Laparoscopic partial nephrectomy (SNOMED) added in procedure_occurrence
- 4207050 — Cosmetic surgery (SNOMED) added in procedure_occurrence
- 4207539 — Syndrome of inappropriate vasopressin secretion (SNOMED) added in condition_occurrence
- 4208085 — Working diagnosis (SNOMED) added in observation
- 4208113 — Spinal arthrodesis (SNOMED) added in procedure_occurrence
- 4208524 — Arthroscopically aided anterior cruciate ligament repair (SNOMED) added in procedure_occurrence
- 4208719 — Pharyngeal hemorrhage (SNOMED) added in condition_occurrence
- 4208748 — Open reduction of trimalleolar fracture of ankle with internal fixation (SNOMED) added in procedure_occurrence
- 4208798 — Replacement of ascending aorta (SNOMED) added in procedure_occurrence
- 4208815 — Abscess of nervous system (SNOMED) added in condition_occurrence
- 4209088 — Varicose vein of lower limb with phlebitis (SNOMED) added in condition_occurrence
- 4209746 — Duodenal ulcer without hemorrhage AND without perforation (SNOMED) added in condition_occurrence
- 4209859 — Empyema (SNOMED) added in condition_occurrence
- 4211657 — Closed fracture of lower leg (SNOMED) added in condition_occurrence
- 4211987 — Open reduction of fracture of femur with internal fixation (SNOMED) added in procedure_occurrence
- 4212044 — Supine plain X-ray of abdomen (SNOMED) added in procedure_occurrence
- 4212887 — Disorder of rotator cuff (SNOMED) added in condition_occurrence
- 4213041 — Operation on skin (SNOMED) added in procedure_occurrence
- 4213045 — Lumpectomy of breast (SNOMED) added in procedure_occurrence
- 4213258 — Hospital re-admission (SNOMED) added in visit_occurrence
- 4213373 — Dislocation of shoulder joint (SNOMED) added in condition_occurrence
- 4213507 — Dislocation of joint of digit (SNOMED) added in condition_occurrence
- 4214034 — Duodenoscopy (SNOMED) added in procedure_occurrence
- 4214194 — Tracheal intubation technique (SNOMED) added in observation
- 4214376 — Hyperglycemia (SNOMED) added in condition_occurrence
- 4214521 — Strabismus surgery (SNOMED) added in procedure_occurrence
- 4214566 — Dermatology (SNOMED) added in visit_occurrence
- 4214567 — Gastroenterology (SNOMED) added in visit_occurrence
- 4214569 — Medical oncology (SNOMED) added in visit_occurrence
- 4214702 — Rheumatology (SNOMED) added in visit_occurrence
- 4215120 — Cardiology (SNOMED) added in visit_occurrence
- 4215122 — Obstetrics and gynecology (SNOMED) added in visit_occurrence
- 4215124 — Psychiatry (SNOMED) added in visit_occurrence
- 4215125 — Nephrology (SNOMED) added in visit_occurrence
- 4215132 — Cardiothoracic surgery (SNOMED) added in visit_occurrence
- 4215133 — Neurosurgery (SNOMED) added in visit_occurrence
- 4215134 — Urology (SNOMED) added in visit_occurrence
- 4216185 — Open wound of upper limb (SNOMED) added in condition_occurrence
- 4216188 — Nummular eczema (SNOMED) added in condition_occurrence
- 4216397 — Nerve root disorder (SNOMED) added in condition_occurrence
- 4216493 — Cocaine withdrawal (SNOMED) added in condition_occurrence
- 4216752 — Drug therapy (SNOMED) added in procedure_occurrence
- 4216972 — Bursitis of hip (SNOMED) added in condition_occurrence
- 4217075 — Infectious pericarditis (SNOMED) added in condition_occurrence
- 4217202 — Intrathecal (SNOMED) added in drug_exposure
- 4217615 — Plication of diaphragm (SNOMED) added in procedure_occurrence
- 4217665 — Repair of diaphragmatic hernia by thoracic approach (SNOMED) added in procedure_occurrence
- 4218999 — Ileostomy bag (SNOMED) added in device_exposure
- 4219400 — Cormack and Lehane grade 1 (SNOMED) added in condition_occurrence
- 4219502 — Sedation (SNOMED) added in procedure_occurrence
- 4220238 — Multiple congenital cysts of kidney (SNOMED) added in condition_occurrence
- 4220631 — Injury of kidney (SNOMED) added in condition_occurrence
- 4221694 — Operation on colon (SNOMED) added in procedure_occurrence
- 4221760 — Cormack and Lehane grade 2 (SNOMED) added in condition_occurrence
- 4221821 — Thrombophlebitis of deep veins of lower extremity (SNOMED) added in condition_occurrence
- 4221874 — Hysteroscopy with removal of submucous leiomyomata (SNOMED) added in procedure_occurrence
- 4222936 — Pleurodesis (SNOMED) added in procedure_occurrence
- 4223020 — Cardiac catheterization (SNOMED) added in visit_detail
- 4223020 — Cardiac catheterization (SNOMED) added in visit_occurrence
- 4223965 — Intrabiliary (SNOMED) added in drug_exposure
- 4224004 — Hiatal hernia (SNOMED) added in condition_occurrence
- 4224012 — Major reconstruction of chest wall (SNOMED) added in procedure_occurrence
- 4224926 — Obstruction of esophagus (SNOMED) added in condition_occurrence
- 4224968 — Tinea corporis (SNOMED) added in condition_occurrence
- 4225555 — Epidural (SNOMED) added in drug_exposure
- 4226144 — Endobronchial tube incorrectly positioned (SNOMED) added in observation
- 4226983 — Resection of rectum (SNOMED) added in procedure_occurrence
- 4227086 — Hemorrhage of blood vessel (SNOMED) added in condition_occurrence
- 4228313 — Tracheal intubation event (SNOMED) added in observation
- 4228361 — Asteatosis cutis (SNOMED) added in condition_occurrence
- 4228759 — Ophthalmic surgery (SNOMED) added in visit_detail
- 4228759 — Ophthalmic surgery (SNOMED) added in visit_occurrence
- 4229543 — Intratracheal (SNOMED) added in drug_exposure
- 4229828 — Measurement of blood flow rate in vascular access (SNOMED) added in procedure_occurrence
- 4230238 — Enterectomy with anastomosis (SNOMED) added in procedure_occurrence
- 4230911 — Echocardiography (SNOMED) added in procedure_occurrence
- 4231009 — Cardiac pacemaker electrode (SNOMED) added in device_exposure
- 4231681 — Aorto-femoral arterial bypass with prosthesis (SNOMED) added in procedure_occurrence
- 4231838 — Inadvertent tracheal extubation (SNOMED) added in observation
- 4232181 — Chronic duodenal ulcer with hemorrhage (SNOMED) added in condition_occurrence
- 4232320 — Cardiopulmonary resuscitation (SNOMED) added in procedure_occurrence
- 4232337 — Valvular endocarditis (SNOMED) added in condition_occurrence
- 4232697 — Persistent atrial fibrillation (SNOMED) added in condition_occurrence
- 4232742 — Vacuum assisted skin closure (SNOMED) added in procedure_occurrence
- 4233244 — Paralysis of larynx (SNOMED) added in condition_occurrence
- 4233974 — Urethral (SNOMED) added in drug_exposure
- 4234083 — Traumatic pneumothorax (SNOMED) added in condition_occurrence
- 4234536 — Transurethral prostatectomy (SNOMED) added in procedure_occurrence
- 4235267 — Neonatology (SNOMED) added in visit_occurrence
- 4235388 — Vascular surgery (SNOMED) added in visit_occurrence
- 4235389 — Oral and maxillofacial surgery (SNOMED) added in visit_occurrence
- 4235391 — Obstetrics (SNOMED) added in visit_occurrence
- 4235863 — Spinal cord injury (SNOMED) added in condition_occurrence
- 4236169 — Ventricular aneurysm (SNOMED) added in condition_occurrence
- 4236711 — Aorto-iliac bypass with prosthesis (SNOMED) added in procedure_occurrence
- 4236905 — Thrombosis of arteries of lower extremity (SNOMED) added in condition_occurrence
- 4237062 — Mural thrombus of heart (SNOMED) added in condition_occurrence
- 4237458 — Fracture of clavicle (SNOMED) added in condition_occurrence
- 4237748 — Surgical removal of residual tooth roots (SNOMED) added in procedure_occurrence
- 4238559 — Central pontine myelinolysis (SNOMED) added in condition_occurrence
- 4238648 — Angiodysplasia of small intestine (SNOMED) added in condition_occurrence
- 4238808 — Empyema of pleura (SNOMED) added in condition_occurrence
- 4239130 — Oxygen therapy (SNOMED) added in procedure_occurrence
- 4239190 — Autopsy review, consultation and report (SNOMED) added in measurement
- 4239191 — Tracheobronchial suctioning (SNOMED) added in procedure_occurrence
- 4240701 — Lysis of adhesions of intestines (SNOMED) added in procedure_occurrence
- 4240824 — Intra-arterial (SNOMED) added in drug_exposure
- 4241033 — Acute abdomen (SNOMED) added in condition_occurrence
- 4241530 — Asymptomatic human immunodeficiency virus infection (SNOMED) added in condition_occurrence
- 4241777 — Carcinoma in situ of endometrium (SNOMED) added in condition_occurrence
- 4241849 — Sitting a patient up in a chair (SNOMED) added in procedure_occurrence
- 4242348 — Benign neoplasm of intrathoracic organs (SNOMED) added in condition_occurrence
- 4242520 — Suture of stomach (SNOMED) added in procedure_occurrence
- 4242574 — Intertrigo (SNOMED) added in condition_occurrence
- 4242814 — Benign neoplasm of parotid gland (SNOMED) added in condition_occurrence
- 4242816 — Benign neoplasm of pituitary gland (SNOMED) added in condition_occurrence
- 4242877 — Evacuation of subdural hematoma (SNOMED) added in procedure_occurrence
- 4242997 — Cholecystectomy (SNOMED) added in procedure_occurrence
- 4243022 — Intraperitoneal (SNOMED) added in drug_exposure
- 4243161 — Open wound of head (SNOMED) added in condition_occurrence
- 4243445 — Benign neoplasm of pancreas (SNOMED) added in condition_occurrence
- 4243973 — Laparoscopic appendectomy (SNOMED) added in procedure_occurrence
- 4244662 — Disorder of musculoskeletal system (SNOMED) added in condition_occurrence
- 4244809 — Esophageal hiatus hernia repair (SNOMED) added in procedure_occurrence
- 4245646 — Congenital septal defect of heart (SNOMED) added in condition_occurrence
- 4245842 — Umbilical hernia (SNOMED) added in condition_occurrence
- 4245975 — Hepatic failure (SNOMED) added in condition_occurrence
- 4246371 — Arterial embolectomy (SNOMED) added in procedure_occurrence
- 4247238 — Primary malignant neoplasm of endometrium (SNOMED) added in condition_occurrence
- 4247350 — Primary malignant neoplasm of skin of ear (SNOMED) added in condition_occurrence
- 4247719 — Primary malignant neoplasm of ascending colon (SNOMED) added in condition_occurrence
- 4247802 — Muscular dystrophy (SNOMED) added in condition_occurrence
- 4247842 — Primary malignant neoplasm of myometrium (SNOMED) added in condition_occurrence
- 4248028 — Supraventricular arrhythmia (SNOMED) added in condition_occurrence
- 4248429 — Gastric ulcer without hemorrhage AND without perforation (SNOMED) added in condition_occurrence
- 4249161 — Operation on heart valve (SNOMED) added in procedure_occurrence
- 4249605 — Spasm of cerebral arteries (SNOMED) added in condition_occurrence
- 4249893 — Colonoscopy (SNOMED) added in procedure_occurrence
- 4251304 — Intervertebral disc prolapse (SNOMED) added in condition_occurrence
- 4251314 — Laparoscopy (SNOMED) added in procedure_occurrence
- 4251336 — Radical resection of thoracic structures (SNOMED) added in procedure_occurrence
- 4252365 — Thoracic surgery (SNOMED) added in provider
- 4252365 — Thoracic surgery (SNOMED) added in visit_occurrence
- 4253207 — Repair of urinary bladder (SNOMED) added in procedure_occurrence
- 4253523 — Exploratory laparotomy (SNOMED) added in procedure_occurrence
- 4253894 — Maxillary sinusotomy by Caldwell-Luc approach (SNOMED) added in procedure_occurrence
- 4254906 — Tracheostomy care assessment (SNOMED) added in procedure_occurrence
- 4255407 — Cardiac surgery (SNOMED) added in visit_occurrence
- 4256228 — Respiratory failure (SNOMED) added in condition_occurrence
- 4256889 — Dissection of abdominal aorta (SNOMED) added in condition_occurrence
- 4256899 — Device observable (SNOMED) added in observation
- 4257906 — Injury due to suicide attempt (SNOMED) added in condition_occurrence
- 4258502 — Tube care: endotracheal (SNOMED) added in procedure_occurrence
- 4258554 — Incision and drainage of hip joint (SNOMED) added in procedure_occurrence
- 4259121 — Femoral-femoral artery vascular bypass (SNOMED) added in procedure_occurrence
- 4261842 — Sick sinus syndrome (SNOMED) added in condition_occurrence
- 4262099 — Transdermal (SNOMED) added in drug_exposure
- 4262914 — Nasal (SNOMED) added in drug_exposure
- 4263360 — Fracture of pubis (SNOMED) added in condition_occurrence
- 4263480 — Suprapubic prostatectomy (SNOMED) added in procedure_occurrence
- 4263689 — Topical (SNOMED) added in drug_exposure
- 4264285 — Percutaneous transluminal coronary angioplasty by rotablation using imaging guidance with contrast (SNOMED) added in procedure_occurrence
- 4264332 — Breast reconstruction with free flap (SNOMED) added in procedure_occurrence
- 4265293 — Percutaneous transluminal coronary angioplasty by rotablation, single vessel using imaging guidance with contrast (SNOMED) added in procedure_occurrence
- 4265433 — Visual impairment (SNOMED) added in condition_occurrence
- 4265479 — Acute duodenal ulcer with perforation (SNOMED) added in condition_occurrence
- 4265605 — Dialysis catheter (SNOMED) added in device_exposure
- 4265608 — Detorsion of ovary (SNOMED) added in procedure_occurrence
- 4266062 — Revision of total hip replacement (SNOMED) added in procedure_occurrence
- 4266202 — Amputation of limb (SNOMED) added in procedure_occurrence
- 4266238 — Nasopharyngeal airway device (SNOMED) added in device_exposure
- 4266367 — Influenza (SNOMED) added in condition_occurrence
- 4266809 — Diverticular disease (SNOMED) added in condition_occurrence
- 4266931 — Restrictive lung disease (SNOMED) added in condition_occurrence
- 4267417 — Hepatic fibrosis (SNOMED) added in condition_occurrence
- 4269222 — Repair of nasal septal perforation (SNOMED) added in procedure_occurrence
- 4269517 — Inorganic arsenic poisoning (SNOMED) added in condition_occurrence
- 4269621 — Intrauterine (SNOMED) added in drug_exposure
- 4270024 — Acute non-ST segment elevation myocardial infarction (SNOMED) added in condition_occurrence
- 4270363 — Removal of cardiac pacemaker (SNOMED) added in procedure_occurrence
- 4271013 — Melanocytic nevus (SNOMED) added in condition_occurrence
- 4271016 — Disorder of skin of trunk (SNOMED) added in condition_occurrence
- 4271587 — Ventriculostomy (SNOMED) added in procedure_occurrence
- 4274025 — Disease (SNOMED) added in condition_occurrence
- 4274575 — Idiopathic generalized epilepsy (SNOMED) added in condition_occurrence
- 4274789 — Transection of cranial nerve (SNOMED) added in procedure_occurrence
- 4275133 — Construction of mucous fistula (SNOMED) added in procedure_occurrence
- 4275142 — Implantation of heart assist system (SNOMED) added in procedure_occurrence
- 4275423 — Supraventricular tachycardia (SNOMED) added in condition_occurrence
- 4275564 — Operation on heart (SNOMED) added in procedure_occurrence
- 4276282 — Serology: organism - finding (SNOMED) added in measurement
- 4276360 — Undernutrition (SNOMED) added in condition_occurrence
- 4276418 — Feces quantity finding (SNOMED) added in measurement
- 4278217 — Arterial thrombosis (SNOMED) added in condition_occurrence
- 4280680 — Closed manipulation of dislocation of hip (SNOMED) added in procedure_occurrence
- 4280942 — Acute gastrojejunal ulcer with perforation (SNOMED) added in condition_occurrence
- 4282316 — Recurrent major depression (SNOMED) added in condition_occurrence
- 4283095 — Carotid endarterectomy (SNOMED) added in procedure_occurrence
- 4283229 — Excision of lesion of spleen (SNOMED) added in procedure_occurrence
- 4283942 — Bronchopulmonary dysplasia of newborn (SNOMED) added in condition_occurrence
- 4284492 — Guttate psoriasis (SNOMED) added in condition_occurrence
- 4285725 — Percutaneous valvuloplasty (SNOMED) added in procedure_occurrence
- 4285898 — Polyp of colon (SNOMED) added in condition_occurrence
- 4286507 — Upper respiratory tract obstruction (SNOMED) added in condition_occurrence
- 4286887 — Radical orchiectomy (SNOMED) added in procedure_occurrence
- 4287115 — Intra-atrial pacing (SNOMED) added in procedure_occurrence
- 4287321 — Thrombectomy of vein (SNOMED) added in procedure_occurrence
- 4287786 — Osteonecrosis (SNOMED) added in condition_occurrence
- 4287790 — Posterior repair of vagina (SNOMED) added in procedure_occurrence
- 4287923 — Patient controlled epidural analgesia (SNOMED) added in procedure_occurrence
- 4288168 — Open reduction of separation of epiphysis of fibula (SNOMED) added in procedure_occurrence
- 4288544 — Inguinal hernia (SNOMED) added in condition_occurrence
- 4290759 — Rectal (SNOMED) added in drug_exposure
- 4291025 — Arthritis (SNOMED) added in condition_occurrence
- 4291649 — Upper gastrointestinal bleeding (SNOMED) added in condition_occurrence
- 4292110 — Sublingual (SNOMED) added in drug_exposure
- 4292410 — Intraluminal (SNOMED) added in drug_exposure
- 4292673 — Artefactual skin disease (SNOMED) added in condition_occurrence
- 4293619 — Repair of tricuspid valve (SNOMED) added in procedure_occurrence
- 4293859 — Width of wound (SNOMED) added in observation
- 4295069 — Tracheostomy care (SNOMED) added in observation
- 4295278 — Peripheral arterial bypass (SNOMED) added in procedure_occurrence
- 4295336 — Left anterior fascicular block (SNOMED) added in condition_occurrence
- 4296529 — Anesthesia management (SNOMED) added in procedure_occurrence
- 4296653 — Acute ST segment elevation myocardial infarction (SNOMED) added in condition_occurrence
- 4296728 — Polyneuritis (SNOMED) added in condition_occurrence
- 4297235 — Repair of mitral valve (SNOMED) added in procedure_occurrence
- 4297236 — Mitral valvuloplasty (SNOMED) added in procedure_occurrence
- 4297321 — Amputation of finger, except thumb (SNOMED) added in procedure_occurrence
- 4297400 — Mild neurocognitive disorder (SNOMED) added in condition_occurrence
- 4297894 — Greater trochanteric pain syndrome (SNOMED) added in condition_occurrence
- 4298166 — Removal of calculus of renal pelvis through percutaneous nephrostomy (SNOMED) added in procedure_occurrence
- 4298484 — Operation on oral cavity (SNOMED) added in procedure_occurrence
- 4298562 — Operation on spinal cord (SNOMED) added in procedure_occurrence
- 4298809 — Nephritic syndrome (SNOMED) added in condition_occurrence
- 4299094 — Opioid intoxication (SNOMED) added in condition_occurrence
- 4299440 — Vascular disorder of pelvis (SNOMED) added in condition_occurrence
- 4299447 — Surgical procedure on chest wall (SNOMED) added in procedure_occurrence
- 4299449 — Hematoma (SNOMED) added in condition_occurrence
- 4299523 — Angiography (SNOMED) added in procedure_occurrence
- 4299602 — Operation on gastrointestinal tract (SNOMED) added in procedure_occurrence
- 4299720 — Repair of pulmonary valve (SNOMED) added in procedure_occurrence
- 4300064 — Dorsolumbar spinal fusion with Harrington rod (SNOMED) added in procedure_occurrence
- 4300185 — Transplantation to recipient (SNOMED) added in procedure_occurrence
- 4300243 — Postoperative complication (SNOMED) added in condition_occurrence
- 4300244 — Surgical procedure on thorax (SNOMED) added in procedure_occurrence
- 4300372 — Operation on larynx (SNOMED) added in procedure_occurrence
- 4300757 — Computed tomography (SNOMED) added in procedure_occurrence
- 4300828 — Wound care management (SNOMED) added in procedure_occurrence
- 4301351 — Surgical procedure (SNOMED) added in procedure_occurrence
- 4301458 — Hospice care (SNOMED) added in visit_occurrence
- 4301600 — Direct laryngoscopy (SNOMED) added in procedure_occurrence
- 4301602 — Thrombotic thrombocytopenic purpura (SNOMED) added in condition_occurrence
- 4301606 — Pulmonary hemorrhage (SNOMED) added in condition_occurrence
- 4302354 — Intraduodenal (SNOMED) added in drug_exposure
- 4302381 — Physical restraint (SNOMED) added in procedure_occurrence
- 4302537 — Digestive system finding (SNOMED) added in condition_occurrence
- 4302612 — Intramuscular (SNOMED) added in drug_exposure
- 4302745 — Irrigation of urinary bladder (SNOMED) added in procedure_occurrence
- 4302754 — Neurocutaneous syndrome (SNOMED) added in condition_occurrence
- 4302785 — Intravitreal (SNOMED) added in drug_exposure
- 4303087 — Delirious (SNOMED) added in observation
- 4303233 — Gastric polyp (SNOMED) added in condition_occurrence
- 4303277 — Oropharyngeal (SNOMED) added in drug_exposure
- 4303673 — Retrobulbar (SNOMED) added in drug_exposure
- 4304008 — Memory impairment (SNOMED) added in condition_occurrence
- 4304277 — Fistula (SNOMED) added in drug_exposure
- 4304412 — Surgical drain (SNOMED) added in drug_exposure
- 4304484 — Chronic myeloproliferative disorder (clinical) (SNOMED) added in condition_occurrence
- 4304571 — Ureteral (SNOMED) added in drug_exposure
- 4304688 — Double valve replacement (SNOMED) added in procedure_occurrence
- 4304746 — Surgical oncology (SNOMED) added in visit_occurrence
- 4304943 — Endoscopic retrograde cholangiopancreatography (SNOMED) added in procedure_occurrence
- 4305074 — Ureterorenoscopy (SNOMED) added in procedure_occurrence
- 4305077 — Transurethral excision of neoplasm of urinary bladder (SNOMED) added in procedure_occurrence
- 4305080 — Abnormal breathing (SNOMED) added in condition_occurrence
- 4305679 — Ileostomy (SNOMED) added in drug_exposure
- 4305852 — Off-pump coronary artery bypass (SNOMED) added in procedure_occurrence
- 4306060 — Construction of end colostomy (SNOMED) added in procedure_occurrence
- 4306073 — Operation on respiratory tract (SNOMED) added in procedure_occurrence
- 4306084 — Dislocation of hip joint (SNOMED) added in condition_occurrence
- 4306192 — Cardiotochogram (SNOMED) added in procedure_occurrence
- 4306203 — Peritoneal lavage (SNOMED) added in procedure_occurrence
- 4306206 — Laminectomy (SNOMED) added in procedure_occurrence
- 4306292 — Upper abdominal pain (SNOMED) added in condition_occurrence
- 4306575 — Anoxic-ischemic encephalopathy (SNOMED) added in condition_occurrence
- 4307036 — Percutaneous coil embolization of cerebral artery aneurysm (SNOMED) added in procedure_occurrence
- 4307240 — Uvulopalatopharyngoplasty (SNOMED) added in procedure_occurrence
- 4307254 — Closed fracture (SNOMED) added in condition_occurrence
- 4307532 — Ligation of lymphatic vessel (SNOMED) added in procedure_occurrence
- 4307820 — Unplanned pregnancy (SNOMED) added in condition_occurrence
- 4307925 — Psoriasis vulgaris (SNOMED) added in condition_occurrence
- 4308074 — Pyogenic granuloma (SNOMED) added in condition_occurrence
- 4308093 — Dupuytren's disease of palm (SNOMED) added in condition_occurrence
- 4308446 — Ureteroneocystostomy with urinary bladder flap (SNOMED) added in procedure_occurrence
- 4308570 — Phototoxic drug eruption (SNOMED) added in condition_occurrence
- 4308807 — Myocardial biopsy (SNOMED) added in procedure_occurrence
- 4309106 — Aspiration pneumonia (SNOMED) added in condition_occurrence
- 4309425 — Dilation and curettage of uterus after delivery (SNOMED) added in procedure_occurrence
- 4310313 — Multifactorial encephalopathy (SNOMED) added in condition_occurrence
- 4310400 — Acute appendicitis (SNOMED) added in condition_occurrence
- 4310737 — Cystourethroscopy with resection of neck of urinary bladder (SNOMED) added in procedure_occurrence
- 4310821 — Bipolar disorder in remission (SNOMED) added in condition_occurrence
- 4311036 — Drainage of peritonsillar abscess (SNOMED) added in procedure_occurrence
- 4311038 — Operative procedure on spinal structure (SNOMED) added in procedure_occurrence
- 4311043 — Arterial cannula insertion (SNOMED) added in procedure_occurrence
- 4311112 — Decompression of cranial nerve (SNOMED) added in procedure_occurrence
- 4311115 — Intracranial mass (SNOMED) added in condition_occurrence
- 4311499 — Primary malignant neoplasm of respiratory tract (SNOMED) added in condition_occurrence
- 4312194 — Repair of heart valve (SNOMED) added in procedure_occurrence
- 4312685 — Primary malignant neoplasm of skin of lower limb (SNOMED) added in condition_occurrence
- 4313365 — Neoplasm of uncertain behavior of brain (SNOMED) added in condition_occurrence
- 4313592 — Extracorporeal bench surgery of kidney (SNOMED) added in procedure_occurrence
- 4314436 — Enterostomy (SNOMED) added in procedure_occurrence
- 4316068 — Total pancreatectomy (SNOMED) added in procedure_occurrence
- 4316366 — Hemorrhage of kidney (SNOMED) added in condition_occurrence
- 4316995 — Neoplasm of uncertain behavior of renal pelvis (SNOMED) added in condition_occurrence
- 4317284 — Respiratory tract hemorrhage (SNOMED) added in condition_occurrence
- 4317285 — Non-cardiogenic pulmonary edema (SNOMED) added in condition_occurrence
- 4317526 — Injection of drug or medicament into nerve (SNOMED) added in procedure_occurrence
- 4317685 — Neoplasm of uncertain behavior of respiratory tract (SNOMED) added in condition_occurrence
- 4317816 — Neoplasm of uncertain behavior of small intestine (SNOMED) added in condition_occurrence
- 4318408 — Subdural intracranial hematoma (SNOMED) added in condition_occurrence
- 4318539 — Retroperitoneal hemorrhage (SNOMED) added in condition_occurrence
- 4318699 — Disorder of lacrimal gland (SNOMED) added in condition_occurrence
- 4319447 — Urolithiasis (SNOMED) added in condition_occurrence
- 4319450 — Ruptured cyst of ovary (SNOMED) added in condition_occurrence
- 4320030 — Soft tissue infection (SNOMED) added in condition_occurrence
- 4322169 — Subcutaneous mastectomy (SNOMED) added in procedure_occurrence
- 4322306 — Poisoning caused by acetaminophen (SNOMED) added in condition_occurrence
- 4322471 — Transplant of kidney (SNOMED) added in procedure_occurrence
- 4322818 — Partial hepatectomy (SNOMED) added in procedure_occurrence
- 4323201 — Replacement of aortic root (SNOMED) added in procedure_occurrence
- 4323283 — Operation on brain (SNOMED) added in procedure_occurrence
- 4323902 — Lung volume reduction surgery (SNOMED) added in procedure_occurrence
- 4324058 — Correction of congenital deformity of heart (SNOMED) added in procedure_occurrence
- 4324634 — Transportation request (SNOMED) added in observation
- 4325283 — Closure of enterostomy (SNOMED) added in procedure_occurrence
- 4326255 — Abdominal abscess (SNOMED) added in condition_occurrence
- 4326683 — Bariatric operative procedure (SNOMED) added in procedure_occurrence
- 4327115 — Operative procedure on hip (SNOMED) added in procedure_occurrence
- 4327195 — Mobilization (SNOMED) added in procedure_occurrence
- 4327488 — Repair of aneurysm (SNOMED) added in procedure_occurrence
- 4328240 — Thoracoscopic lobectomy of lung (SNOMED) added in procedure_occurrence
- 4329041 — Pain (SNOMED) added in condition_occurrence
- 4329847 — Myocardial infarction (SNOMED) added in condition_occurrence
- 4331311 — Changing tracheostomy tube (SNOMED) added in procedure_occurrence
- 4331725 — Operative procedure on artery of extremity (SNOMED) added in procedure_occurrence
- 4332304 — Status epilepticus (SNOMED) added in condition_occurrence
- 4332593 — Spinal anesthesia (SNOMED) added in procedure_occurrence
- 4334245 — Retinal artery occlusion (SNOMED) added in condition_occurrence
- 4334485 — At increased risk for delirium (SNOMED) added in observation
- 4335169 — Acute transient psychotic disorder (SNOMED) added in condition_occurrence
- 4335479 — Bilateral sequential single lung transplant (SNOMED) added in procedure_occurrence
- 4335825 — Transthoracic echocardiography (SNOMED) added in procedure_occurrence
- 4335872 — Injury of globe of eye (SNOMED) added in condition_occurrence
- 4336080 — Packed red blood cells (SNOMED) added in device_exposure
- 4336157 — Acute non-infective otitis externa (SNOMED) added in condition_occurrence
- 4336459 — Nasopharyngeal suction (SNOMED) added in procedure_occurrence
- 4336464 — Coronary artery bypass graft (SNOMED) added in procedure_occurrence
- 4336544 — Operation on trachea (SNOMED) added in procedure_occurrence
- 4336593 — Replacement of implanted mitral valve (SNOMED) added in procedure_occurrence
- 4337034 — Wedge excision of lung (SNOMED) added in procedure_occurrence
- 4337190 — Aortic valve resuspension and replacement of ascending aorta (SNOMED) added in procedure_occurrence
- 4337271 — Excision of intracardiac tumor with cardiopulmonary bypass (SNOMED) added in procedure_occurrence
- 4337608 — Pneumonectomy with tracheobronchoplasty (SNOMED) added in procedure_occurrence
- 4337610 — Excision of bulla of lung (SNOMED) added in procedure_occurrence
- 4338120 — Altered bowel function (SNOMED) added in condition_occurrence
- 4338315 — Tricuspid valve operation (SNOMED) added in procedure_occurrence
- 4338523 — Amaurosis fugax (SNOMED) added in condition_occurrence
- 4338544 — Lower gastrointestinal hemorrhage (SNOMED) added in condition_occurrence
- 4338616 — Ventricular operation (SNOMED) added in procedure_occurrence
- 4338843 — Disorder of pleura (SNOMED) added in condition_occurrence
- 4339184 — Replacement of pulmonary valve (SNOMED) added in procedure_occurrence
- 4339214 — Secondary pulmonary hypertension (SNOMED) added in condition_occurrence
- 4339608 — Open biopsy of lung (SNOMED) added in procedure_occurrence
- 4339741 — Replacement of implanted aortic valve (SNOMED) added in procedure_occurrence
- 4339742 — Composite aortic root operation (SNOMED) added in procedure_occurrence
- 4339829 — Pulmonary valve operation (SNOMED) added in procedure_occurrence
- 4340361 — Rupture of intestine (SNOMED) added in condition_occurrence
- 4340383 — Alcoholic hepatitis (SNOMED) added in condition_occurrence
- 4340493 — Alcohol-induced acute pancreatitis (SNOMED) added in condition_occurrence
- 4341387 — Cystoscopy and destruction of lesion of urinary bladder (SNOMED) added in procedure_occurrence
- 4342896 — Parastomal hernia (SNOMED) added in condition_occurrence
- 4343792 — Fixation of fracture using screws (SNOMED) added in procedure_occurrence
- 4343794 — Internal fixation of fracture (SNOMED) added in procedure_occurrence
- 4343935 — Giant cell arteritis with polymyalgia rheumatica (SNOMED) added in condition_occurrence
- 4344166 — Adult onset Still's disease (SNOMED) added in condition_occurrence
- 4344258 — Bursitis of shoulder (SNOMED) added in condition_occurrence
- 4344264 — Triggering of digit (SNOMED) added in condition_occurrence
- 4345578 — Rhabdomyolysis (SNOMED) added in condition_occurrence
- 4345680 — Disorder of amputation stump (SNOMED) added in condition_occurrence
- 4347287 — Drug-induced myopathy (SNOMED) added in condition_occurrence
- 4353621 — Minute volume (SNOMED) added in measurement
- 4353741 — Cardioversion (SNOMED) added in procedure_occurrence
- 19002829 — tolazoline (RxNorm) added in drug_exposure
- 19011437 — icodextrin (RxNorm) added in drug_exposure
- 19012585 — asparaginase (RxNorm) added in drug_exposure
- 19017810 — amsacrine (RxNorm) added in drug_exposure
- 19024728 — decitabine (RxNorm) added in drug_exposure
- 19028947 — dimethindene (RxNorm) added in drug_exposure
- 19037624 — acetylcholine (RxNorm) added in drug_exposure
- 19040060 — dydrogesterone (RxNorm) added in drug_exposure
- 19045317 — digoxin antibodies Fab fragments (RxNorm) added in drug_exposure
- 19049410 — chloroprocaine (RxNorm) added in drug_exposure
- 19058572 — calcium citrate (RxNorm) added in drug_exposure
- 19066865 — silicon dioxide (RxNorm) added in drug_exposure
- 19069076 — hydroxyethyl cellulose (RxNorm) added in drug_exposure
- 19092377 — lysine (RxNorm) added in drug_exposure
- 19095275 — potassium iodate (RxNorm) added in drug_exposure
- 19105879 — ajmaline (RxNorm) added in drug_exposure
- 19126774 — mucins (RxNorm) added in drug_exposure
- 19136716 — taurine (RxNorm) added in drug_exposure
- 19137385 — thiotepa (RxNorm) added in drug_exposure
- 21490519 — Carbon dioxide [VFr/PPres] in Gas delivery system (LOINC) added in measurement
- 21490525 — Isoflurane [VFr/PPres] Airway adaptor --during inspiration (LOINC) added in measurement
- 21490627 — Desflurane [VFr/PPres] Airway adaptor --at end expiration (LOINC) added in measurement
- 21490631 — Isoflurane [VFr/PPres] Airway adaptor --at end expiration (LOINC) added in measurement
- 21490632 — Nitrous oxide [VFr/PPres] Airway adaptor --at end expiration (LOINC) added in measurement
- 21490642 — Carbon dioxide [VFr/PPres] in Airway adaptor --during inspiration (LOINC) added in measurement
- 21490680 — Right atrial pressure (LOINC) added in measurement
- 21491103 — Multiple drug resistant gram negative organism [Identifier] in Specimen by Culture (LOINC) added in measurement
- 21492392 — Abnormal lymphocytes [Presence] in Blood by Manual count (LOINC) added in measurement
- 21492393 — Bacteria identified in Implanted device by Culture (LOINC) added in measurement
- 21493147 — Human coronavirus 229E RNA [Presence] in Nasopharynx by NAA with non-probe detection (LOINC) added in measurement
- 21493148 — Human coronavirus OC43 RNA [Presence] in Nasopharynx by NAA with non-probe detection (LOINC) added in measurement
- 21493149 — Human metapneumovirus RNA [Presence] in Nasopharynx by NAA with non-probe detection (LOINC) added in measurement
- 21494961 — Bowel sounds by Auscultation (LOINC) added in measurement
- 21494966 — Physical findings of Abdomen by Palpation (LOINC) added in measurement
- 21498471 — Cardiac Catheterization Lab (LOINC) added in visit_detail
- 21498471 — Cardiac Catheterization Lab (LOINC) added in visit_occurrence
- 21498612 — Discharged/Transferred to another type of healthcare institution not defined elsewhare in this code list (LOINC) added in visit_occurrence
- 21499255 — Radiotherapy (LOINC) added in visit_occurrence
- 21499433 — Geriatrics (LOINC) added in visit_occurrence
- 35606087 — zinc sulfide (RxNorm) added in drug_exposure
- 35608078 — Epilesional (SNOMED) added in drug_exposure
- 35609490 — Alcohol units consumed per day (SNOMED) added in observation
- 35609491 — Alcohol units consumed per week (SNOMED) added in observation
- 35622931 — Doppler ultrasound (SNOMED) added in procedure_occurrence
- 35624178 — Extracorporeal hemodialysis (SNOMED) added in drug_exposure
- 35624213 — Secondary cataract (SNOMED) added in condition_occurrence
- 35624320 — Acute adrenal insufficiency (SNOMED) added in condition_occurrence
- 35624825 — Obstructed bilateral inguinal hernia (SNOMED) added in condition_occurrence
- 35624826 — Laparoscopic adenomyomectomy (SNOMED) added in procedure_occurrence
- 35626024 — Vaso-occlusive pain episode in sickle cell disease (SNOMED) added in condition_occurrence
- 36027924 — magnesium sulfate / potassium sulfate / sodium sulfate (RxNorm) added in drug_exposure
- 36028193 — ferrous fumarate / polysaccharide iron complex (RxNorm) added in drug_exposure
- 36028646 — chondroitin sulfates / glucosamine (RxNorm) added in drug_exposure
- 36028719 — lidocaine / norepinephrine (RxNorm) added in drug_exposure
- 36028773 — magnesium chloride / potassium chloride / sodium acetate / sodium chloride / sodium gluconate (RxNorm) added in drug_exposure
- 36029616 — allantoin / zinc oxide (RxNorm) added in drug_exposure
- 36029651 — atenolol / chlorthalidone (RxNorm) added in drug_exposure
- 36029920 — calcium carbonate / magnesium carbonate (RxNorm) added in drug_exposure
- 36029974 — enalapril / hydrochlorothiazide (RxNorm) added in drug_exposure
- 36029999 — hydrochlorothiazide / irbesartan (RxNorm) added in drug_exposure
- 36030000 — hydrochlorothiazide / lisinopril (RxNorm) added in drug_exposure
- 36030057 — glucose / potassium chloride (RxNorm) added in drug_exposure
- 36030099 — fosinopril / hydrochlorothiazide (RxNorm) added in drug_exposure
- 36030108 — articaine / epinephrine (RxNorm) added in drug_exposure
- 36030109 — atovaquone / proguanil (RxNorm) added in drug_exposure
- 36030121 — iodine / potassium iodide (RxNorm) added in drug_exposure
- 36030126 — buprenorphine / naloxone (RxNorm) added in drug_exposure
- 36030184 — carbidopa / entacapone / levodopa (RxNorm) added in drug_exposure
- 36030600 — betamethasone / calcipotriene (RxNorm) added in drug_exposure
- 36031122 — esomeprazole / naproxen (RxNorm) added in drug_exposure
- 36031412 — Erythrocytes [#/volume] in Lower respiratory specimen by Manual count (LOINC) added in measurement
- 36086759 — Antithymocyte immunoglobulin (equine) (RxNorm Extension) added in drug_exposure
- 36203320 — Influenza virus A and B and Respiratory syncytial virus RNA panel - Upper respiratory specimen by NAA with probe detection (LOINC) added in measurement
- 36303326 — Yeast [Presence] in Urine (LOINC) added in measurement
- 36303637 — Inspiratory pause time Ventilator (LOINC) added in measurement
- 36303911 — Respiratory pathogens panel - Bronchoalveolar lavage by Immunofluorescence (LOINC) added in measurement
- 36304133 — Respiratory syncytial virus B RNA [Presence] in Lower respiratory specimen by NAA with probe detection (LOINC) added in measurement
- 36304330 — Human coronavirus 229E RNA [Presence] in Lower respiratory specimen by NAA with probe detection (LOINC) added in measurement
- 36304370 — Diastolic blood pressure goal (LOINC) added in measurement
- 36304419 — Bacteria [Presence] in Urine (LOINC) added in measurement
- 36304745 — Adenovirus DNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 36304965 — Erythrocytes [Presence] in Cerebral spinal fluid by Gram stain (LOINC) added in measurement
- 36304988 — Human coronavirus RNA [Presence] in Upper respiratory specimen by NAA with probe detection (LOINC) added in measurement
- 36305349 — Human coronavirus HKU1 RNA [Presence] in Lower respiratory specimen by NAA with probe detection (LOINC) added in measurement
- 36305771 — Cryptosporidium sp DNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 36306099 — Low pressure hold time setting Ventilator (LOINC) added in measurement
- 36307912 — Hospital ward (LOINC) added in visit_occurrence
- 36308041 — Other surgery (LOINC) added in visit_occurrence
- 36309887 — Hospital (General) (LOINC) added in visit_occurrence
- 36659740 — Bacteria [Presence] in Bronchoalveolar lavage by Light microscopy (LOINC) added in measurement
- 36660329 — Human coronavirus NL63 RNA [Presence] in Lower respiratory specimen by NAA with non-probe detection (LOINC) added in measurement
- 36675277 — Open repair of umbilical hernia using synthetic mesh (SNOMED) added in procedure_occurrence
- 36675314 — Laparoscopic repair of umbilical hernia (SNOMED) added in procedure_occurrence
- 36675325 — Open repair of epigastric hernia using sutures (SNOMED) added in procedure_occurrence
- 36683564 — Allergic disorder (SNOMED) added in condition_occurrence
- 36685526 — Insufflation using warm humidified carbon dioxide (SNOMED) added in procedure_occurrence
- 36712702 — Preterm labor with preterm delivery (SNOMED) added in condition_occurrence
- 36712821 — Postprocedural infection (SNOMED) added in condition_occurrence
- 36712846 — Persistent proteinuria (SNOMED) added in condition_occurrence
- 36713107 — Lumbar spondylolisthesis (SNOMED) added in condition_occurrence
- 36714927 — Sequelae of infectious disease (SNOMED) added in condition_occurrence
- 36715430 — Sepsis due to urinary tract infection (SNOMED) added in condition_occurrence
- 36715792 — Acquired absence of breast (SNOMED) added in condition_occurrence
- 36716163 — Excessive skin and subcutaneous tissue (SNOMED) added in condition_occurrence
- 36716270 — Cyst of kidney (SNOMED) added in condition_occurrence
- 36716700 — Perforation and abscess of large intestine co-occurrent and due to diverticulitis (SNOMED) added in condition_occurrence
- 36716712 — Calculus of gallbladder without cholecystitis or cholangitis (SNOMED) added in condition_occurrence
- 36717471 — Injury of thoracic spinal cord (SNOMED) added in condition_occurrence
- 36717743 — Transplantation of kidney and pancreas (SNOMED) added in procedure_occurrence
- 36717881 — Sweep gas flow rate (OMOP Extension) added in measurement
- 36717922 — High frequency ventilation amplitude (OMOP Extension) added in observation
- 36848804 — PRITELIVIR (RxNorm Extension) added in drug_exposure
- 36849272 — O-(2-FLUOROETHYL)-L-TYROSINE F-18 (RxNorm Extension) added in drug_exposure
- 36855381 — SENNOSIDES A AND B ACIDS (RxNorm Extension) added in drug_exposure
- 36861098 — PYRIDOXINE PHOSPHATE (RxNorm Extension) added in drug_exposure
- 36863154 — METAZOCINE (RxNorm Extension) added in drug_exposure
- 36879073 — Iron isomaltoside 1000 (RxNorm Extension) added in drug_exposure
- 36879148 — Factor XI (RxNorm Extension) added in drug_exposure
- 37016130 — Lesion of oral mucosa (SNOMED) added in condition_occurrence
- 37016342 — Hypothyroidism caused by drug (SNOMED) added in condition_occurrence
- 37016897 — Open reduction of intussusception of intestine (SNOMED) added in procedure_occurrence
- 37016994 — Laparoscopic total colectomy with ileo-rectal anastomosis (SNOMED) added in procedure_occurrence
- 37017263 — Lymphadenopathy co-occurrent with human immunodeficiency virus infection (SNOMED) added in condition_occurrence
- 37017357 — Fluoroscopy guided percutaneous transluminal revascularization of chronic total occlusion of coronary artery with contrast (SNOMED) added in procedure_occurrence
- 37017409 — CHA2DS2-VASc score (SNOMED) added in measurement
- 37018288 — Extracorporeal (SNOMED) added in drug_exposure
- 37018292 — Continuous renal replacement therapy (SNOMED) added in procedure_occurrence
- 37019613 — Parainfluenza virus 2 RNA [Presence] in Respiratory system specimen by NAA with probe detection (LOINC) added in measurement
- 37020058 — Rotavirus A RNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 37020335 — Parainfluenza virus 4 RNA [Presence] in Respiratory system specimen by NAA with probe detection (LOINC) added in measurement
- 37020445 — Astrovirus RNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 37020792 — Rhinovirus+Enterovirus RNA [Presence] in Lower respiratory specimen by NAA with non-probe detection (LOINC) added in measurement
- 37020902 — Legionella pneumophila DNA [Presence] in Respiratory system specimen by NAA with probe detection (LOINC) added in measurement
- 37020957 — Sapovirus genogroups I+II+IV+V RNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 37021202 — Vibrio cholerae+parahaemolyticus+vulnificus DNA [Presence] in Stool by NAA with probe detection (LOINC) added in measurement
- 37021229 — Gastrointestinal viral pathogens panel - Stool by NAA with probe detection (LOINC) added in measurement
- 37079538 — Immunology (LOINC) added in provider
- 37079538 — Immunology (LOINC) added in visit_occurrence
- 37109423 — Venography of left upper extremity (SNOMED) added in procedure_occurrence
- 37109843 — Absence of lower limb (SNOMED) added in condition_occurrence
- 37109944 — Bodily distress disorder (SNOMED) added in condition_occurrence
- 37110282 — Venous complication of pregnancy (SNOMED) added in condition_occurrence
- 37110393 — Sudden idiopathic hearing loss (SNOMED) added in condition_occurrence
- 37110437 — Psychotic disorder caused by cocaine (SNOMED) added in condition_occurrence
- 37116783 — Therapeutic fecal matter collection container, non-sterile (SNOMED) added in device_exposure
- 37118664 — Injury of femoral artery (SNOMED) added in condition_occurrence
- 37119138 — Iron deficiency anemia due to blood loss (SNOMED) added in condition_occurrence
- 37153653 — Moving subject to sitting on edge of bed from lying down (SNOMED) added in procedure_occurrence
- 37157537 — Positioning subject in sitting position (SNOMED) added in procedure_occurrence
- 37157745 — Carotid artery to axillary artery bypass (SNOMED) added in procedure_occurrence
- 37157813 — Implantation of cardiac resynchronization defibrillator system (SNOMED) added in procedure_occurrence
- 37158404 — Invasive mechanical ventilation (SNOMED) added in procedure_occurrence
- 37159532 — Pressure injury (SNOMED) added in condition_occurrence
- 37160124 — Has mental capacity to make decision (Mental Capacity Act 2005) (SNOMED) added in observation
- 37160591 — Lithium and/or lithium compound overdose (SNOMED) added in condition_occurrence
- 37160775 — Multiple traumatic injuries (SNOMED) added in condition_occurrence
- 37162280 — Disorder caused by psychoactive substance (SNOMED) added in condition_occurrence
- 37162916 — Hyperthermia (SNOMED) added in condition_occurrence
- 37163760 — Open jejunectomy (SNOMED) added in procedure_occurrence
- 37163764 — Laparoscopic ileectomy (SNOMED) added in procedure_occurrence
- 37164445 — Pigmented purpuric dermatosis (SNOMED) added in condition_occurrence
- 37164749 — Excision of breast (SNOMED) added in procedure_occurrence
- 37164773 — Psychosis caused by ethanol (SNOMED) added in condition_occurrence
- 37164793 — Organic mental disorder caused by ethanol (SNOMED) added in condition_occurrence
- 37165425 — Substance withdrawal (SNOMED) added in condition_occurrence
- 37165984 — Transanal total mesorectal excision (SNOMED) added in procedure_occurrence
- 37167847 — Injury of blood vessel of abdomen (SNOMED) added in condition_occurrence
- 37169699 — Postpartum hemolysis-elevated liver enzymes-low platelet count syndrome (SNOMED) added in condition_occurrence
- 37173029 — CK-MB (creatine kinase muscle brain) isoenzyme/creatine kinase ratio in serum (SNOMED) added in measurement
- 37174549 — Intracorporus cavernosum (SNOMED) added in drug_exposure
- 37203984 — Anal fistula (SNOMED) added in condition_occurrence
- 37204026 — Laparoscopic restorative proctocolectomy with ileal pouch anal anastomosis (SNOMED) added in procedure_occurrence
- 37206832 — Mechanical insufflation exsufflation (SNOMED) added in procedure_occurrence
- 37208354 — Royal College of Physicians NEWS2 (National Early Warning Score 2) (SNOMED) added in measurement
- 37208374 — Royal College of Physicians NEWS2 (National Early Warning Score 2) - respiration rate score (SNOMED) added in measurement
- 37208375 — Royal College of Physicians NEWS2 (National Early Warning Score 2) - oxygen saturation scale 1 score (SNOMED) added in measurement
- 37208377 — Royal College of Physicians NEWS2 (National Early Warning Score 2) - air or oxygen score (SNOMED) added in measurement
- 37208378 — Royal College of Physicians NEWS2 (National Early Warning Score 2) - systolic blood pressure score (SNOMED) added in measurement
- 37208379 — Royal College of Physicians NEWS2 (National Early Warning Score 2) - pulse score (SNOMED) added in measurement
- 37208381 — Royal College of Physicians NEWS2 (National Early Warning Score 2) - temperature score (SNOMED) added in measurement
- 37311061 — COVID-19 (SNOMED) added in condition_occurrence
- 37311319 — Hypovolemia (SNOMED) added in condition_occurrence
- 37311320 — Extracellular fluid volume depletion (SNOMED) added in condition_occurrence
- 37311900 — Osteoarthritis of hip due to and following trauma (SNOMED) added in condition_occurrence
- 37396146 — Gastrointestinal infection (SNOMED) added in condition_occurrence
- 37397638 — Infiltration (SNOMED) added in drug_exposure
- 37498202 — silver nitrite (RxNorm) added in drug_exposure
- 38003680 — Oral and Maxillofacial Surgery (Dentist) (NUCC) added in provider
- 38003680 — Oral and Maxillofacial Surgery (Dentist) (NUCC) added in visit_occurrence
- 38003826 — Oral & Maxillofacial Surgery (D.M.D.) (NUCC) added in provider
- 38003826 — Oral & Maxillofacial Surgery (D.M.D.) (NUCC) added in visit_occurrence
- 38003876 — Hepatology Physician (NUCC) added in provider
- 38003876 — Hepatology Physician (NUCC) added in visit_occurrence
- 38004016 — Trauma Surgery Physician (NUCC) added in provider
- 38004016 — Trauma Surgery Physician (NUCC) added in visit_occurrence
- 38004447 — General Surgery (Medicare Specialty) added in condition_occurrence
- 38004447 — General Surgery (Medicare Specialty) added in procedure_occurrence
- 38004447 — General Surgery (Medicare Specialty) added in provider
- 38004447 — General Surgery (Medicare Specialty) added in visit_occurrence
- 38004448 — Allergy / Immunology (Medicare Specialty) added in provider
- 38004448 — Allergy / Immunology (Medicare Specialty) added in visit_occurrence
- 38004449 — Otolaryngology (Medicare Specialty) added in condition_occurrence
- 38004449 — Otolaryngology (Medicare Specialty) added in procedure_occurrence
- 38004449 — Otolaryngology (Medicare Specialty) added in provider
- 38004449 — Otolaryngology (Medicare Specialty) added in visit_occurrence
- 38004450 — Anesthesiology (Medicare Specialty) added in condition_occurrence
- 38004450 — Anesthesiology (Medicare Specialty) added in procedure_occurrence
- 38004450 — Anesthesiology (Medicare Specialty) added in provider
- 38004450 — Anesthesiology (Medicare Specialty) added in visit_occurrence
- 38004451 — Cardiology (Medicare Specialty) added in condition_occurrence
- 38004451 — Cardiology (Medicare Specialty) added in procedure_occurrence
- 38004451 — Cardiology (Medicare Specialty) added in provider
- 38004451 — Cardiology (Medicare Specialty) added in visit_occurrence
- 38004452 — Dermatology (Medicare Specialty) added in condition_occurrence
- 38004452 — Dermatology (Medicare Specialty) added in provider
- 38004452 — Dermatology (Medicare Specialty) added in visit_occurrence
- 38004455 — Gastroenterology (Medicare Specialty) added in condition_occurrence
- 38004455 — Gastroenterology (Medicare Specialty) added in procedure_occurrence
- 38004455 — Gastroenterology (Medicare Specialty) added in provider
- 38004455 — Gastroenterology (Medicare Specialty) added in visit_occurrence
- 38004456 — Internal Medicine (Medicare Specialty) added in condition_occurrence
- 38004456 — Internal Medicine (Medicare Specialty) added in provider
- 38004456 — Internal Medicine (Medicare Specialty) added in visit_occurrence
- 38004458 — Neurology (Medicare Specialty) added in condition_occurrence
- 38004458 — Neurology (Medicare Specialty) added in provider
- 38004458 — Neurology (Medicare Specialty) added in visit_occurrence
- 38004459 — Neurosurgery (Medicare Specialty) added in condition_occurrence
- 38004459 — Neurosurgery (Medicare Specialty) added in procedure_occurrence
- 38004459 — Neurosurgery (Medicare Specialty) added in provider
- 38004459 — Neurosurgery (Medicare Specialty) added in visit_occurrence
- 38004461 — Obstetrics / Gynecology (Medicare Specialty) added in condition_occurrence
- 38004461 — Obstetrics / Gynecology (Medicare Specialty) added in procedure_occurrence
- 38004461 — Obstetrics / Gynecology (Medicare Specialty) added in provider
- 38004461 — Obstetrics / Gynecology (Medicare Specialty) added in visit_occurrence
- 38004462 — Hospice And Palliative Care (Medicare Specialty) added in provider
- 38004462 — Hospice And Palliative Care (Medicare Specialty) added in visit_occurrence
- 38004463 — Ophthalmology (Medicare Specialty) added in condition_occurrence
- 38004463 — Ophthalmology (Medicare Specialty) added in procedure_occurrence
- 38004463 — Ophthalmology (Medicare Specialty) added in provider
- 38004463 — Ophthalmology (Medicare Specialty) added in visit_occurrence
- 38004465 — Orthopedic Surgery (Medicare Specialty) added in condition_occurrence
- 38004465 — Orthopedic Surgery (Medicare Specialty) added in procedure_occurrence
- 38004465 — Orthopedic Surgery (Medicare Specialty) added in provider
- 38004465 — Orthopedic Surgery (Medicare Specialty) added in visit_occurrence
- 38004467 — Plastic And Reconstructive Surgery (Medicare Specialty) added in condition_occurrence
- 38004467 — Plastic And Reconstructive Surgery (Medicare Specialty) added in procedure_occurrence
- 38004467 — Plastic And Reconstructive Surgery (Medicare Specialty) added in provider
- 38004467 — Plastic And Reconstructive Surgery (Medicare Specialty) added in visit_occurrence
- 38004468 — Physical Medicine And Rehabilitation (Medicare Specialty) added in condition_occurrence
- 38004468 — Physical Medicine And Rehabilitation (Medicare Specialty) added in provider
- 38004468 — Physical Medicine And Rehabilitation (Medicare Specialty) added in visit_occurrence
- 38004469 — Psychiatry (Medicare Specialty) added in condition_occurrence
- 38004469 — Psychiatry (Medicare Specialty) added in provider
- 38004469 — Psychiatry (Medicare Specialty) added in visit_occurrence
- 38004472 — Pulmonary Disease (Medicare Specialty) added in condition_occurrence
- 38004472 — Pulmonary Disease (Medicare Specialty) added in procedure_occurrence
- 38004472 — Pulmonary Disease (Medicare Specialty) added in provider
- 38004472 — Pulmonary Disease (Medicare Specialty) added in visit_occurrence
- 38004473 — Thoracic Surgery (Medicare Specialty) added in condition_occurrence
- 38004473 — Thoracic Surgery (Medicare Specialty) added in procedure_occurrence
- 38004473 — Thoracic Surgery (Medicare Specialty) added in provider
- 38004473 — Thoracic Surgery (Medicare Specialty) added in visit_occurrence
- 38004474 — Urology (Medicare Specialty) added in condition_occurrence
- 38004474 — Urology (Medicare Specialty) added in procedure_occurrence
- 38004474 — Urology (Medicare Specialty) added in provider
- 38004474 — Urology (Medicare Specialty) added in visit_occurrence
- 38004476 — Nuclear Medicine (Medicare Specialty) added in provider
- 38004476 — Nuclear Medicine (Medicare Specialty) added in visit_occurrence
- 38004477 — Pediatric Medicine (Medicare Specialty) added in condition_occurrence
- 38004477 — Pediatric Medicine (Medicare Specialty) added in provider
- 38004477 — Pediatric Medicine (Medicare Specialty) added in visit_occurrence
- 38004478 — Geriatric Medicine (Medicare Specialty) added in condition_occurrence
- 38004478 — Geriatric Medicine (Medicare Specialty) added in provider
- 38004478 — Geriatric Medicine (Medicare Specialty) added in visit_occurrence
- 38004479 — Nephrology (Medicare Specialty) added in provider
- 38004479 — Nephrology (Medicare Specialty) added in visit_occurrence
- 38004484 — Infectious Disease (Medicare Specialty) added in provider
- 38004484 — Infectious Disease (Medicare Specialty) added in visit_occurrence
- 38004485 — Endocrinology (Medicare Specialty) added in provider
- 38004485 — Endocrinology (Medicare Specialty) added in visit_occurrence
- 38004488 — Psychology (Medicare Specialty) added in procedure_occurrence
- 38004488 — Psychology (Medicare Specialty) added in provider
- 38004491 — Rheumatology (Medicare Specialty) added in condition_occurrence
- 38004491 — Rheumatology (Medicare Specialty) added in provider
- 38004491 — Rheumatology (Medicare Specialty) added in visit_occurrence
- 38004494 — Pain Management (Medicare Specialty) added in condition_occurrence
- 38004494 — Pain Management (Medicare Specialty) added in provider
- 38004494 — Pain Management (Medicare Specialty) added in visit_occurrence
- 38004496 — Vascular Surgery (Medicare Specialty) added in provider
- 38004496 — Vascular Surgery (Medicare Specialty) added in visit_occurrence
- 38004500 — Critical care (intensivist) (Medicare Specialty) added in procedure_occurrence
- 38004500 — Critical care (intensivist) (Medicare Specialty) added in provider
- 38004500 — Critical care (intensivist) (Medicare Specialty) added in visit_occurrence
- 38004501 — Hematology (Medicare Specialty) added in provider
- 38004501 — Hematology (Medicare Specialty) added in visit_occurrence
- 38004504 — Maxillofacial Surgery (Medicare Specialty) added in procedure_occurrence
- 38004504 — Maxillofacial Surgery (Medicare Specialty) added in provider
- 38004504 — Maxillofacial Surgery (Medicare Specialty) added in visit_occurrence
- 38004507 — Medical Oncology (Medicare Specialty) added in provider
- 38004507 — Medical Oncology (Medicare Specialty) added in visit_occurrence
- 38004508 — Surgical Oncology (Medicare Specialty) added in provider
- 38004508 — Surgical Oncology (Medicare Specialty) added in visit_occurrence
- 38004509 — Radiation Oncology (Medicare Specialty) added in condition_occurrence
- 38004509 — Radiation Oncology (Medicare Specialty) added in provider
- 38004509 — Radiation Oncology (Medicare Specialty) added in visit_occurrence
- 38004510 — Emergency Medicine (Medicare Specialty) added in provider
- 38004510 — Emergency Medicine (Medicare Specialty) added in visit_occurrence
- 38004511 — Interventional Radiology (Medicare Specialty) added in provider
- 38004511 — Interventional Radiology (Medicare Specialty) added in visit_occurrence
- 38004513 — Gynecology / Oncology (Medicare Specialty) added in provider
- 38004513 — Gynecology / Oncology (Medicare Specialty) added in visit_occurrence
- 38004675 — Physician / Diagnostic Radiology (Medicare Specialty) added in procedure_occurrence
- 38004675 — Physician / Diagnostic Radiology (Medicare Specialty) added in provider
- 38004675 — Physician / Diagnostic Radiology (Medicare Specialty) added in visit_occurrence
- 40166954 — calcium chloride / lactate / potassium chloride / sodium chloride Irrigation Solution (RxNorm) added in drug_exposure
- 40219540 — Hospital anxiety and depression scale: anxiety subscale (OMOP Extension) added in measurement
- 40238188 — ipilimumab (RxNorm) added in drug_exposure
- 40299999 — Cystoscopy (SNOMED) added in procedure_occurrence
- 40326053 — Dysphonia (SNOMED) added in condition_occurrence
- 40405599 — Fibromyalgia (SNOMED) added in condition_occurrence
- 40479688 — Reamputation of lower leg through tibia and fibula (SNOMED) added in procedure_occurrence
- 40479758 — Pseudoaneurysm (SNOMED) added in condition_occurrence
- 40480196 — Endovascular repair of abdominal aortic aneurysm (SNOMED) added in procedure_occurrence
- 40480427 — Revisional fusion of joint of spine (SNOMED) added in procedure_occurrence
- 40480556 — Excision of part of pericardium (SNOMED) added in procedure_occurrence
- 40480915 — Revision of reverse polarity total prosthetic replacement of shoulder joint not using cement (SNOMED) added in procedure_occurrence
- 40481901 — Mantle cell lymphoma (SNOMED) added in condition_occurrence
- 40481912 — Excision of sentinel lymph node (SNOMED) added in procedure_occurrence
- 40481919 — Coronary atherosclerosis (SNOMED) added in condition_occurrence
- 40482021 — Left against medical advice (SNOMED) added in visit_occurrence
- 40482507 — Incipient senile cataract (SNOMED) added in condition_occurrence
- 40482662 — Disorder of joint of ankle and/or foot (SNOMED) added in condition_occurrence
- 40482893 — Extranodal marginal zone B-cell lymphoma of mucosa-associated lymphoid tissue (MALT-lymphoma) (SNOMED) added in condition_occurrence
- 40483172 — Stimulant dependence (SNOMED) added in condition_occurrence
- 40483287 — Disorder of kidney and/or ureter (SNOMED) added in condition_occurrence
- 40483383 — Canadian Study of Health and Aging clinical frailty scale (SNOMED) added in measurement
- 40483531 — Revision of ventriculoperitoneal shunt (SNOMED) added in procedure_occurrence
- 40483561 — Procedure on wound (SNOMED) added in procedure_occurrence
- 40483613 — Inflammatory disease of female genital structure (SNOMED) added in condition_occurrence
- 40483641 — Hemorrhage into peritoneal cavity (SNOMED) added in condition_occurrence
- 40484137 — Excision of infected vascular graft (SNOMED) added in procedure_occurrence
- 40484160 — Excision of foreign body of subcutaneous tissue (SNOMED) added in procedure_occurrence
- 40484571 — Disorder of joint of shoulder region (SNOMED) added in condition_occurrence
- 40485074 — Injury of collateral ligament of knee (SNOMED) added in condition_occurrence
- 40485457 — Multiple system atrophy, Parkinson's variant (SNOMED) added in condition_occurrence
- 40486024 — Cyst of abdomen (SNOMED) added in condition_occurrence
- 40486116 — Removal of total hip prosthesis (SNOMED) added in procedure_occurrence
- 40486150 — Video assisted thoracoscopy (SNOMED) added in procedure_occurrence
- 40486896 — Primary malignant neoplasm of extrahepatic bile duct (SNOMED) added in condition_occurrence
- 40487059 — Sepsis caused by Staphylococcus (SNOMED) added in condition_occurrence
- 40487348 — Excision of scar (SNOMED) added in procedure_occurrence
- 40487349 — Laparoscopic total nephrectomy (SNOMED) added in procedure_occurrence
- 40487616 — Sepsis caused by Streptococcus pyogenes (SNOMED) added in condition_occurrence
- 40487945 — Percutaneous transluminal ablation of conducting system of heart (SNOMED) added in procedure_occurrence
- 40488368 — Laparoscopic partial cystectomy (SNOMED) added in procedure_occurrence
- 40489793 — Exploration using laparoscope (SNOMED) added in procedure_occurrence
- 40489907 — Sepsis caused by Staphylococcus aureus (SNOMED) added in condition_occurrence
- 40489908 — Sepsis caused by Streptococcus (SNOMED) added in condition_occurrence
- 40489989 — Intrajejunal (SNOMED) added in drug_exposure
- 40490507 — Cutaneous (SNOMED) added in drug_exposure
- 40490888 — Herniation of rectum into vagina (SNOMED) added in condition_occurrence
- 40490927 — Craniotomy and excision of neoplasm of brain (SNOMED) added in procedure_occurrence
- 40491321 — Intramammary (SNOMED) added in drug_exposure
- 40491916 — One stage extracapsular extraction of lens and insertion of prosthetic intraocular lens (SNOMED) added in procedure_occurrence
- 40492287 — Intravascular (SNOMED) added in drug_exposure
- 40492305 — Intrapericardial (SNOMED) added in drug_exposure
- 40492392 — Closed fracture of fibula (SNOMED) added in condition_occurrence
- 40492458 — Neoplasm of uncertain behavior of digestive organ (SNOMED) added in condition_occurrence
- 40492969 — Intraparenchymal hemorrhage of brain (SNOMED) added in condition_occurrence
- 40493038 — Sepsis caused by Gram negative bacteria (SNOMED) added in condition_occurrence
- 40549429 — Ocular (SNOMED) added in drug_exposure
- 40568467 — Seborrheic keratosis (SNOMED) added in condition_occurrence
- 40758433 — Fungus [Presence] in Sputum by KOH preparation (LOINC) added in measurement
- 40758438 — Yeast.pseudohyphae [Presence] in Sputum by KOH preparation (LOINC) added in measurement
- 40759746 — Procollagen type III [Mass/volume] in Serum (LOINC) added in measurement
- 40761537 — Casts [Type] in Urine sediment by Light microscopy (LOINC) added in measurement
- 40762052 — BIPAP AndOr CPAP setting Ventilator (LOINC) added in measurement
- 40762243 — Vancomycin resistant enterococcus [Presence] in Anal by Organism specific culture (LOINC) added in measurement
- 40765038 — 1,25-Dihydroxyvitamin D [Mass/volume] in Serum or Plasma (LOINC) added in measurement
- 40766929 — How many cigarettes do you smoke per day now [PhenX] (LOINC) added in observation
- 40769146 — Heparin unfractionated [Units/volume] in Platelet poor plasma (LOINC) added in measurement
- 40769405 — Clot Lysis [Length fraction] in Blood by Thromboelastography --30 minutes post maximum clot amplitude (LOINC) added in measurement
- 40798873 — Herbal extract (RxNorm Extension) added in drug_exposure
- 42527085 — Burst count Cerebral cortex Electroencephalogram (EEG) (LOINC) added in measurement
- 42527815 — HIV 1 and 2 Ab and HIV 1 p24 Ag panel - Serum or Plasma by Immunoassay (LOINC) added in measurement
- 42528502 — Mode setting Nebulizer (LOINC) added in measurement
- 42535090 — Need for personal care assistance (SNOMED) added in observation
- 42535424 — Spontaneous hemorrhage of cortical intracerebral hemisphere (SNOMED) added in condition_occurrence
- 42535425 — Spontaneous hemorrhage of cerebral hemisphere (SNOMED) added in condition_occurrence
- 42536233 — Complex regional pain syndrome type I (SNOMED) added in condition_occurrence
- 42536383 — Anaphylactic shock (SNOMED) added in condition_occurrence
- 42536547 — Ischemia of kidney (SNOMED) added in condition_occurrence
- 42536603 — Hyperosmolar hyperglycemic coma due to diabetes mellitus without ketoacidosis (SNOMED) added in condition_occurrence
- 42536886 — Ischemia of muscle due to traumatic injury (SNOMED) added in condition_occurrence
- 42537054 — Post anesthesia care management (SNOMED) added in procedure_occurrence
- 42537585 — Open repair of incisional hernia (SNOMED) added in procedure_occurrence
- 42537727 — Degeneration of posterior pole of eye (SNOMED) added in condition_occurrence
- 42537748 — Acquired absence of organ (SNOMED) added in condition_occurrence
- 42538967 — Retroperitoneal lymph node dissection (SNOMED) added in procedure_occurrence
- 42539146 — Psychotic disorder caused by stimulant (SNOMED) added in condition_occurrence
- 42801287 — pertuzumab (RxNorm) added in drug_exposure
- 42868487 — Positive airway pressure device Leak (LOINC) added in measurement
- 42868608 — Yeast.hyphae [Presence] in Specimen by KOH preparation (LOINC) added in measurement
- 42869515 — Rotavirus identified in Stool by Sequencing (LOINC) added in measurement
- 42872434 — Intracranial hematoma (SNOMED) added in condition_occurrence
- 42872509 — Laparoscopic cholecystostomy (SNOMED) added in procedure_occurrence
- 42872569 — Laparoscopic removal of ovarian cyst (SNOMED) added in procedure_occurrence
- 42872572 — Laparoscopic excision of ectopic ovarian pregnancy (SNOMED) added in procedure_occurrence
- 42872749 — National Institutes of Health stroke scale (SNOMED) added in measurement
- 42873638 — carfilzomib (RxNorm) added in drug_exposure
- 42904275 — cranberry juice (RxNorm) added in drug_exposure
- 43054905 — Erythrocytes [Presence] in Specimen by Gram stain (LOINC) added in measurement
- 43054906 — Leukocytes [Presence] in Specimen by Gram stain (LOINC) added in measurement
- 43055120 — Cytomegalovirus DNA [Units/volume] (viral load) in Serum or Plasma by NAA with probe detection (LOINC) added in measurement
- 43055255 — Appearance of Exudate from wound (LOINC) added in measurement
- 43530674 — Spontaneous cerebellar hemorrhage (SNOMED) added in condition_occurrence
- 43530714 — Sensory disorder of smell and/or taste (SNOMED) added in condition_occurrence
- 43530727 — Spontaneous cerebral hemorrhage (SNOMED) added in condition_occurrence
- 43531085 — Open reduction of fracture of scapula with internal fixation (SNOMED) added in procedure_occurrence
- 43531086 — Open reduction of dislocation of acromioclavicular joint (SNOMED) added in procedure_occurrence
- 43531100 — Open repair of inguinal hernia (SNOMED) added in procedure_occurrence
- 43531101 — Open repair of obstructed femoral hernia (SNOMED) added in procedure_occurrence
- 43531648 — Total knee replacement (SNOMED) added in procedure_occurrence
- 44777549 — per square meter (UCUM) added in measurement
- 44777556 — per 24 hours (UCUM) added in observation
- 44777560 — per year (UCUM) added in measurement
- 44777578 — milliunit per liter (UCUM) added in measurement
- 44777590 — centimeter watercolumn (UCUM) added in measurement
- 44777590 — centimeter watercolumn (UCUM) added in observation
- 44777602 — kilopascal (UCUM) added in measurement
- 44777604 — liter per liter (UCUM) added in measurement
- 44777612 — milligram per millimole (UCUM) added in measurement
- 44777613 — milliliter per hour (UCUM) added in measurement
- 44777619 — millimole per millimole of creatinine (UCUM) added in measurement
- 44777656 — micromole per millimole (UCUM) added in measurement
- 44782560 — Idiopathic pulmonary arterial hypertension (SNOMED) added in condition_occurrence
- 44783078 — Arthroscopic repair of rotator cuff (SNOMED) added in procedure_occurrence
- 44783205 — Post traumatic osteoarthritis (SNOMED) added in condition_occurrence
- 44783222 — Aortic arch replacement (SNOMED) added in procedure_occurrence
- 44783371 — Arthrotomy of joint of shoulder girdle (SNOMED) added in procedure_occurrence
- 44783604 — Laparoscopic construction of cutaneous ureteroileostomy (SNOMED) added in procedure_occurrence
- 44783696 — Vaginal hysterectomy with repair of cystocele and rectocele (SNOMED) added in procedure_occurrence
- 44783698 — Injection of neurolytic substance to intercostal nerve (SNOMED) added in procedure_occurrence
- 44784217 — Cardiac arrhythmia (SNOMED) added in condition_occurrence
- 44784339 — Monoarthritis of wrist (SNOMED) added in condition_occurrence
- 44784581 — Patient clinical record lost (SNOMED) added in visit_occurrence
- 44790388 — Nebuliser ventilation (SNOMED) added in procedure_occurrence
- 44791025 — Referral to pulmonary rehabilitation (SNOMED) added in visit_occurrence
- 44791135 — Ventilatory support (SNOMED) added in procedure_occurrence
- 44792363 — Passive warming of patient (SNOMED) added in procedure_occurrence
- 44800078 — Physical fitness state (SNOMED) added in observation
- 44803815 — Gynaecology (SNOMED) added in visit_occurrence
- 44804203 — Plastic surgery (SNOMED) added in visit_occurrence
- 44805913 — Primary closure of atrial septal defect (SNOMED) added in procedure_occurrence
- 44806024 — Hyperthermic intraoperative peritoneal chemotherapy (SNOMED) added in procedure_occurrence
- 44806251 — Biliary acute pancreatitis (SNOMED) added in condition_occurrence
- 44808151 — Psychiatric intensive care (SNOMED) added in visit_occurrence
- 44808672 — Placing in supine position (SNOMED) added in procedure_occurrence
- 44808681 — Suspected sepsis (SNOMED) added in observation
- 44809207 — Target body temperature (SNOMED) added in measurement
- 44812002 — Neuromuscular disorder (SNOMED) added in condition_occurrence
- 45757291 — Closed fracture of orbital floor (SNOMED) added in condition_occurrence
- 45757610 — Pulmonary rehabilitation service (SNOMED) added in visit_occurrence
- 45758151 — Pericardium drainage catheter (SNOMED) added in device_exposure
- 45758297 — Negative-pressure wound therapy system, line-powered (SNOMED) added in device_exposure
- 45758721 — Mediastinal drain (SNOMED) added in device_exposure
- 45762340 — Drainage biliary catheter (SNOMED) added in device_exposure
- 45762688 — Intravascular heating/cooling system catheter (SNOMED) added in device_exposure
- 45765790 — Aerosol therapy (SNOMED) added in procedure_occurrence
- 45766075 — Acute anterior ST segment elevation myocardial infarction (SNOMED) added in condition_occurrence
- 45766116 — Acute ST segment elevation myocardial infarction of inferior wall (SNOMED) added in condition_occurrence
- 45766714 — Inflammatory dermatosis (SNOMED) added in condition_occurrence
- 45767544 — Anchoring of endotracheal tube (SNOMED) added in procedure_occurrence
- 45767889 — Rectal catheter (SNOMED) added in device_exposure
- 45768119 — External cardiac pacemaker (SNOMED) added in device_exposure
- 45768449 — Hypertensive crisis (SNOMED) added in condition_occurrence
- 45769227 — Percutaneous transluminal ablation of pulmonary vein to left atrium conducting system (SNOMED) added in procedure_occurrence
- 45769428 — Illicit drug overdose (SNOMED) added in condition_occurrence
- 45770892 — Primary malignant neoplasm of uterus (SNOMED) added in condition_occurrence
- 45770904 — Perichondritis of external ear (SNOMED) added in condition_occurrence
- 45772085 — Anal abscess (SNOMED) added in condition_occurrence
- 45772120 — Gastroduodenal disorder (SNOMED) added in condition_occurrence
- 45772707 — Closed fracture of phalanx of thumb (SNOMED) added in condition_occurrence
- 45773181 — Phantom limb syndrome with pain (SNOMED) added in condition_occurrence
- 45774639 — vedolizumab (RxNorm) added in drug_exposure
- 45775636 — meningococcal group B vaccine (RxNorm) added in drug_exposure
- 45876502 — Orthopedics (LOINC) added in visit_occurrence
- 45876918 — Outpatient (LOINC) added in visit_occurrence
- 45877533 — Home environment (LOINC) added in visit_occurrence
- 45878057 — Same Day/Ambulatory Surgery (LOINC) added in visit_detail
- 45878057 — Same Day/Ambulatory Surgery (LOINC) added in visit_occurrence
- 45878574 — Operating room (LOINC) added in visit_detail
- 45878574 — Operating room (LOINC) added in visit_occurrence
- 45878834 — Pediatrics (LOINC) added in visit_occurrence
- 45878837 — Recovery room (LOINC) added in visit_occurrence
- 45879036 — In other facility (LOINC) added in visit_occurrence
- 45879104 — Short Stay Unit (LOINC) added in visit_occurrence
- 45879108 — Pre-Op Holding (LOINC) added in visit_detail
- 45879108 — Pre-Op Holding (LOINC) added in visit_occurrence
- 45879637 — Psychiatric hospital (LOINC) added in visit_occurrence
- 45880582 — Post Anesthesia Care Unit (LOINC) added in visit_occurrence
- 45881321 — Otolaryngology/ENT (LOINC) added in visit_occurrence
- 45882979 — Endoscopy (LOINC) added in visit_detail
- 45882979 — Endoscopy (LOINC) added in visit_occurrence
- 45883311 — Morgue/mortuary (LOINC) added in visit_occurrence
- 45883627 — Other (not listed) (LOINC) added in provider
- 45883627 — Other (not listed) (LOINC) added in visit_occurrence
- 45883663 — Nursing Home (LOINC) added in visit_occurrence
- 45883682 — Rehabilitation facility (LOINC) added in visit_occurrence
- 45884382 — Dialysis (LOINC) added in visit_occurrence
- 45885033 — Deceased (LOINC) added in visit_occurrence
- 45885090 — Adult Coronary Critical Care Unit (LOINC) added in visit_occurrence
- 45885291 — Adult Medical Unit (LOINC) added in visit_occurrence
- 45891013 — milliliter per liter (UCUM) added in measurement
- 45892531 — blinatumomab (RxNorm) added in drug_exposure
- 45892628 — nivolumab (RxNorm) added in drug_exposure
- 46234983 — Respiratory syncytial virus B RNA [Presence] in Nasopharynx by NAA with probe detection (LOINC) added in measurement
- 46236049 — Colony count [#/volume] in Implanted device by Culture (LOINC) added in measurement
- 46236950 — Fasting glucose [Moles/volume] in Serum, Plasma or Blood (LOINC) added in measurement
- 46237787 — Hospital-Other (LOINC) added in visit_occurrence
- 46270383 — Headache caused by drug (SNOMED) added in condition_occurrence
- 46270879 — Fluoroscopy guided percutaneous transluminal angioplasty of lower limb artery with contrast (SNOMED) added in procedure_occurrence
- 46270974 — Laparoscopic bypass of stomach (SNOMED) added in procedure_occurrence
- 46270977 — Laparoscopic total gastrectomy (SNOMED) added in procedure_occurrence
- 46271022 — Chronic kidney disease (SNOMED) added in condition_occurrence
- 46271049 — Fluoroscopy guided percutaneous transluminal angioplasty of peripheral blood vessel with contrast (SNOMED) added in procedure_occurrence
- 46272242 — Intestinal obstruction co-occurrent and due to decreased peristalsis (SNOMED) added in condition_occurrence
- 46272514 — Methicillin resistant Staphylococcus (SNOMED) added in observation
- 46272911 — Intraneural (SNOMED) added in drug_exposure
- 46273178 — Osteoarthritis of hip due to dysplasia (SNOMED) added in condition_occurrence
- 46273463 — Upper respiratory tract infection caused by Influenza virus (SNOMED) added in condition_occurrence
- 46284419 — Surgical wound (SNOMED) added in condition_occurrence
- 46287148 — Acute stimulant intoxication (SNOMED) added in condition_occurrence
- 2000000024 — Post filter ionised calcium (ICUdata) added in measurement
- 2000000031 — CRRT dialysate solution (ICUdata) added in drug_exposure
- 2000000074 — NICE admission diagnosis (ICUdata) added in observation
- 2000000086 — Fluid intake parenteral feeding (ICUdata) added in measurement
- 2000000100 — ECMO venous flow (ICUdata) added in measurement
- 2000000164 — Extracorporeal membrane oxygenation line location (ICUdata) added in measurement
- 2000000205 — Oxygen/Gas Total [Percentage] Inhaled Gas (ICUdata) added in measurement
- 2000000218 — Inspiratory rise time placeholder (ICUdata) added in measurement
- 2000000234 — Chest wall compliance (ICUdata) added in measurement
- 2000000235 — Vent mechanics compliance respiratory (ICUdata) added in measurement
- 2000000239 — Vent mechanis paw total peep (ICUdata) added in measurement
- 2000000240 — Vent mechanics pes exp dyn (ICUdata) added in measurement
- 2000000241 — Vent mechanics pes exp occl (ICUdata) added in measurement
- 2000000242 — Vent mechanics pes insp dyn (ICUdata) added in measurement
- 2000000243 — Vent mechanics pes insp occl (ICUdata) added in measurement
- 2000000244 — Vent mechanics ptranspulm exp (ICUdata) added in measurement
- 2000000245 — Vent mechanics ptranspulm insp (ICUdata) added in measurement
- 2000000246 — Vent mechanics volume end inspiration (ICUdata) added in measurement
- 2000000252 — Volume trigger (ICUdata) added in measurement
- 2000000269 — Delirium observation screening - question 6 (ICUdata) added in measurement
- 2000000278 — Delirium observation screening - question 7 (ICUdata) added in measurement
- 2000000287 — Delirium observation screening - question 10 (ICUdata) added in measurement
- 2000000297 — Delirium observation screening - question 4 (ICUdata) added in measurement
- 2000000298 — Delirium observation screening - question 11 (ICUdata) added in measurement
- 2000000299 — Delirium observation screening - question 12 (ICUdata) added in measurement
- 2000000301 — Delirium observation screening - question 5 (ICUdata) added in measurement
- 2000000302 — Delirium observation screening - question 3 (ICUdata) added in measurement
- 2000000309 — decubitus score - rear of head (ICUdata) added in measurement
- 2000000310 — decubitus score - toes left (ICUdata) added in measurement
- 2000000314 — decubitus score - elbow right (ICUdata) added in measurement
- 2000000315 — decubitus score - shoulder left (ICUdata) added in measurement
- 2000000319 — decubitus score - knee right (ICUdata) added in measurement
- 2000000322 — decubitus score - fingers left (ICUdata) added in measurement
- 2000000324 — decubitus score - hip right (ICUdata) added in measurement
- 2000000325 — decubitus score - heel left (ICUdata) added in measurement
- 2000000326 — decubitus score - hip left (ICUdata) added in measurement
- 2000000328 — decubitus score - heel right (ICUdata) added in measurement
- 2000000332 — Reason for ICU discharge (ICUdata) added in observation
- 2000000352 — fluid output - bladder flush drain (ICUdata) added in measurement
- 2000000353 — fluid output - wound flush drain (ICUdata) added in measurement
- 2000000371 — fluid output - spinal cord drain (ICUdata) added in measurement
- 2000000377 — fluid output - jejunostoma (ICUdata) added in measurement
- 2000000379 — fluid output - fistula drain (ICUdata) added in measurement
- 2000000392 — ICARUS - fluid status (ICUdata) added in measurement
- 2000000400 — ecmo venous temperature (ICUdata) added in measurement
- 2000000404 — ICARUS - suspected cardiac tamponade (ICUdata) added in measurement
- 2000000405 — ICARUS - PLAPS left (ICUdata) added in measurement
- 2000000406 — ICARUS - right ventricle (ICUdata) added in measurement
- 2000000415 — ICARUS - Blue profile (ICUdata) added in measurement
- 2000000418 — ICARUS - right ventricular function (ICUdata) added in measurement
- 2000000423 — ICARUS - lung sliding left (ICUdata) added in measurement
- 2000000435 — ICARUS - left ventricle (ICUdata) added in measurement
- 2000000482 — Arterial sheath (ICUdata) added in device_exposure
- 2000000490 — Venous sheath (ICUdata) added in device_exposure
- 2000000492 — Sideport (ICUdata) added in device_exposure
- 2000000517 — central venous line placement (ICUdata) added in procedure_occurrence
- 2000000530 — Extubation order (ICUdata) added in procedure_occurrence
- 2000000539 — Jejunostomy (ICUdata) added in device_exposure
- 2000000550 — Shunt (ICUdata) added in procedure_occurrence
- 2000000563 — Intubation Complication (ICUdata) added in measurement
- 2000000568 — decubitus score - elbow left (ICUdata) added in measurement
- 2000000622 — renal replacement therapy - duration (ICUdata) added in measurement
- 2000000901 — NICE admission: origin (ICUdata) added in observation
- 2000000906 — Weaning time duration (ICUdata) added in measurement
- 2000000919 — Arterial catheter insertion site (ICUdata) added in observation
- 2000000920 — Oxygen saturation in Arterial blood by Pulse oximetry given as range (ICUdata) added in measurement
- 2000000926 — Finding of pulse by palpation (ICUdata) added in observation
- 2000000927 — History of chronic dialysis (ICUdata) added in measurement
- 2000000929 — Vasoactive medication 24 hours after admission (ICUdata) added in measurement
- 2000000937 — NEWS2 Consciousness points (ICUdata) added in measurement
- 2000000938 — Carbon dioxide arterial to end-tidal gradient (ICUdata) added in measurement
- 2000000939 — ECMO VA line pressure (ICUdata) added in measurement
- 2000000943 — External ventricular drain level compared to Monro (ICUdata) added in measurement
- 2000000947 — Inspiratory oxygen - expiratory oxgen [Percentage Difference] Airway adaptor (ICUdata) added in measurement
- 2000000953 — Quick SOFA respiratory rate score (ICUdata) added in measurement
- 2000000954 — Blood pressure cuff placement (ICUdata) added in observation
- 2000000957 — Quick SOFA systolic pressure score (ICUdata) added in measurement
- 2000000958 — Blood volume Unspecified body region CVVH (ICUdata) added in measurement
- 2000000959 — Manual bag ventilation (ICUdata) added in procedure_occurrence
- 2000000960 — Quick SOFA GCS (ICUdata) added in measurement
- 2000000963 — Tube depth in comparison to (ICUdata) added in measurement
- 2000000967 — Airway status (ICUdata) added in measurement
- 2000000968 — Not eligible for donation of organs (reason) (ICUdata) added in measurement
- 2000000971 — Intraosseous access location (ICUdata) added in measurement
- 2000000972 — Tidal volume.spontaneous+mechanical/Ideal Body weight [Volume/mass] --on ventilator (ICUdata) added in measurement
- 2000000973 — Type of emergency department presentation (ICUdata) added in observation
- 2000000977 — Urine culture collection (ICUdata) added in procedure_occurrence
- 2000000978 — Blood culture collection (ICUdata) added in procedure_occurrence
- 2000000985 — Oxygen consumption (VO2)/Body weight [Volume Rate/Area] (ICUdata) added in measurement
- 2000000989 — Type of external ventrical drain (ICUdata) added in observation
- 2000000991 — Venous catheter width (ICUdata) added in measurement
- 2000000992 — Atrial pacing frequency (ICUdata) added in measurement
- 2000000994 — Neuromuscular blockade blocked nerve (ICUdata) added in observation
- 2000000995 — Sputum culture collection (ICUdata) added in procedure_occurrence
- 2000000996 — Type of venous access (ICUdata) added in observation
- 2000000997 — Thermoregulation type (ICUdata) added in observation
- 2000000999 — Pacemaker ventricular frequency setting (ICUdata) added in measurement
- 2000001000 — CPAX Supine to Sitting (ICUdata) added in observation
- 2000001001 — CPAX Cough (ICUdata) added in observation
- 2000001002 — CPAX Sit to stand (ICUdata) added in observation
- 2000001003 — NICE admission diagnosis: burns (ICUdata) added in observation
- 2000001004 — NICE GCS: highest motor score, first 24h (ICUdata) added in measurement
- 2000001005 — NICE GCS: lowest verbal score, first 24h (ICUdata) added in measurement
- 2000001006 — NICE admission diagnosis: delirium (ICUdata) added in observation
- 2000001007 — CPAX Standing balance (ICUdata) added in observation
- 2000001009 — Bladder pressure (ICUdata) added in measurement
- 2000001011 — History of drug use (ICUdata) added in observation
- 2000001012 — Restrictive policy order - invasive mechanical ventilation (ICUdata) added in measurement
- 2000001020 — decubitus score - toe(s) (ICUdata) added in measurement
- 2000001024 — CAM-ICU step 4a disorganized thinking score (ICUdata) added in measurement
- 2000001025 — CAM-ICU step 2 inattention test (ICUdata) added in measurement
- 2000001029 — Short nutritional assessment questionnaire score (ICUdata) added in measurement
- 2000001030 — CAM-ICU not perfomed because (ICUdata) added in measurement
- 2000001034 — NICE APACHE IV: predicted length of stay (ICUdata) added in measurement
- 2000001036 — CPAX Respiratory function (ICUdata) added in measurement
- 2000001038 — CPAX Bed to Chair (ICUdata) added in measurement
- 2000001039 — CPAX Stepping (ICUdata) added in measurement
- 2000001040 — fluid output liquor (ICUdata) added in measurement
- 2000001056 — CAM-ICU step 3 consciousness level (ICUdata) added in measurement
- 2000001064 — Spontaneous Breathing Trial Anxiety (ICUdata) added in measurement
- 2000001066 — Restrictive policy order - anti-arrhythmic treatment (ICUdata) added in measurement
- 2000001067 — Restrictive policy order - antibiotics (ICUdata) added in measurement
- 2000001068 — Restrictive policy order - multiple transfusions (ICUdata) added in measurement
- 2000001069 — Restrictive policy order - surgery (ICUdata) added in measurement
- 2000001070 — Restrictive policy order - intubation (ICUdata) added in measurement
- 2000001071 — Restrictive policy order - ICU admission (ICUdata) added in measurement
- 2000001072 — Restrictive policy order - blood product transfusion (ICUdata) added in measurement
- 2000001073 — Restrictive policy order - cardiopulmonary resuscitation (ICUdata) added in measurement
- 2000001078 — Reticulocytes/1000 erythrocytes in Blood (ICUdata) added in measurement
- 2000001082 — EuroSCORE: total logistic (ICUdata) added in measurement
- 2000001091 — Respiratory system elasticity (ICUdata) added in measurement
- 2000001099 — Consciousness at CPR (ICUdata) added in measurement
- 2000001110 — RASS goal (ICUdata) added in measurement
- 2000001111 — Autodetubation - reason (ICUdata) added in measurement
- 2000001114 — Restrictive policy order - sedation and muscle relaxation (ICUdata) added in measurement
- 2000001118 — Left side body position (ICUdata) added in procedure_occurrence
- 2000001119 — Right side body position (ICUdata) added in procedure_occurrence
- 2000001124 — beclometason / formoterol (ICUdata) added in drug_exposure
- 2000001126 — Restrictive policy order - tracheostomy (ICUdata) added in measurement
- 2000001127 — Restrictive policy order - non-invasive ventilation (ICUdata) added in measurement
- 2000001128 — Restrictive policy order - oxygen therapy (ICUdata) added in measurement
- 2000001129 — Tracheobronchial toilet frequency 1 hour (ICUdata) added in measurement
- 2000001131 — NICE admission: type (ICUdata) added in observation
- 2000001132 — decubitus score - surgery (ICUdata) added in measurement
- 2000001134 — ECMO circuit temperature (ICUdata) added in measurement
- 2000001135 — NICE SOFA daily: lowest GCS verbal score (ICUdata) added in measurement
- 2000001136 — NICE SOFA daily: highest dopamine rate (ICUdata) added in measurement
- 2000001137 — NICE SOFA daily: phosphodiesterase inhibitor administered (ICUdata) added in measurement
- 2000001138 — NICE SOFA daily: highest adrenaline rate (ICUdata) added in measurement
- 2000001139 — NICE SOFA daily: dobutamine administered (ICUdata) added in measurement
- 2000001140 — NICE SOFA daily: diuresis (ICUdata) added in measurement
- 2000001141 — NICE SOFA daily: cardiac assist device (ICUdata) added in measurement
- 2000001142 — NICE SOFA daily: artificial liver support (ICUdata) added in measurement
- 2000001145 — Chest tube fluid aspect (ICUdata) added in observation
- 2000001146 — NICE chronic diagnosis: metastasized neoplasm (ICUdata) added in observation
- 2000001147 — NICE chronic diagnosis: cirrhosis (ICUdata) added in observation
- 2000001148 — NICE chronic diagnosis: immunological insufficiency (ICUdata) added in observation
- 2000001149 — NICE admission diagnosis: CPR (ICUdata) added in observation
- 2000001150 — NICE chronic diagnosis: respiratory insufficiency (ICUdata) added in observation
- 2000001151 — NICE chronic diagnosis: renal insufficiency (ICUdata) added in observation
- 2000001152 — NICE admission diagnosis: myocardial infarction (ICUdata) added in observation
- 2000001153 — NICE 24h diagnosis: acute renal failure (ICUdata) added in observation
- 2000001154 — NICE 24h diagnosis: proven infection (ICUdata) added in observation
- 2000001155 — NICE 24h diagnosis: mechanical ventilation (ICUdata) added in observation
- 2000001156 — NICE admission diagnosis: mechanical ventilation (ICUdata) added in observation
- 2000001157 — NICE SOFA daily: highest adrenaline rate (ICUdata) added in measurement
- 2000001158 — NICE SOFA daily: highest dobutamine rate (ICUdata) added in measurement
- 2000001159 — NICE SOFA daily: lowest GCS motor score (ICUdata) added in measurement
- 2000001160 — NICE SOFA daily: lowest GCS eye score (ICUdata) added in measurement
- 2000001162 — NICE SOFA daily: highest noradrenaline rate (ICUdata) added in measurement
- 2000001165 — NICE SOFA daily: lowest mean arterial blood pressure (ICUdata) added in measurement
- 2000001167 — NICE complication: gastrointestinal bleed (deprecated) (ICUdata) added in observation
- 2000001180 — NICE admission diagnosis: cerebrovascular accident (deprecated) (ICUdata) added in observation
- 2000001181 — NICE complication: delirium (per shift) (ICUdata) added in observation
- 2000001183 — Nursing Activities Score mobilisation and positioning (ICUdata) added in measurement
- 2000001184 — Nursing Activities Score item 2: laboratory investigation (ICUdata) added in measurement
- 2000001185 — Nursing Activities Score Administrative and Management tasks (ICUdata) added in measurement
- 2000001186 — Nursing Activities Score item 1: monitoring (ICUdata) added in measurement
- 2000001187 — Nursing Activities Score support for family members (ICUdata) added in measurement
- 2000001188 — Nursing Activities Score hygiene procedures (ICUdata) added in measurement
- 2000001189 — Nursing Activities Score item 3: medication (ICUdata) added in measurement
- 2000001195 — Aspect of liquor (ICUdata) added in observation
- 2000001196 — Nursing Activities Score respiratory support (ICUdata) added in measurement
- 2000001197 — Nursing Activities Score care for artificial airway (ICUdata) added in measurement
- 2000001201 — Nursing Activities Score treatment of metabolic aci-/alkalosis (ICUdata) added in measurement
- 2000001209 — Tracheobronchial toilet response (ICUdata) added in measurement
- 2000001211 — midazolam / morphine (ICUdata) added in drug_exposure
- 2000001213 — Nursing Activities Score vasoactive medication (ICUdata) added in measurement
- 2000001214 — NICE discharge: died in ICU (ICUdata) added in observation
- 2000001215 — Selective digestive decontamination culture result (ICUdata) added in measurement
- 2000001216 — Extubation reason (ICUdata) added in measurement
- 2000001218 — CPAX Grip Strength (ICUdata) added in measurement
- 2000001219 — CPAX Dynamic sitting (ICUdata) added in measurement
- 2000001220 — NICE admission: readmission (ICUdata) added in observation
- 2000001222 — CPAX Moving within the bed (ICUdata) added in measurement
- 2000001223 — NICE GCS: lowest motor score, first 24h (ICUdata) added in measurement
- 2000001224 — NICE GCS: highest verbal score, first 24h (ICUdata) added in measurement
- 2000001225 — Enema fluid (ICUdata) added in drug_exposure
- 2000001226 — Total parenteral nutrition ingredients (ICUdata) added in drug_exposure
- 2000001230 — Clot Lysis [Length fraction] in Blood by Thromboelastography --60 minutes post maximum clot amplitude (ICUdata) added in measurement
- 2000001231 — NICE APACHE II: post-operative reason for admission (ICUdata) added in observation
- 2000001232 — NICE admission: planned admission (ICUdata) added in observation
- 2000001233 — NICE: height (ICUdata) added in measurement
- 2000001234 — NICE admission: referring specialty (ICUdata) added in observation
- 2000001235 — NICE: weight (ICUdata) added in measurement
- 2000001236 — Rethoracotomy (ICUdata) added in procedure_occurrence
- 2000001237 — Pain context (ICUdata) added in observation
- 2000001238 — Thrombolysis catheter (ICUdata) added in device_exposure
- 2000001239 — Nursing Activities Score 17 measuring urine output (ICUdata) added in measurement
- 2000001240 — EuroSCORE II: acute endocarditis (ICUdata) added in measurement
- 2000001241 — EuroSCORE II: gender (ICUdata) added in measurement
- 2000001242 — Nursing Activities Score 14 Left Atrium monitoring (ICUdata) added in measurement
- 2000001243 — Nursing Activities Score 22 Specific interventions inside ICU (ICUdata) added in measurement
- 2000001244 — Erythroblasts/100 leukocytes in Blood (ICUdata) added in measurement
- 2000001245 — NICE score: SAPS II (ICUdata) added in measurement
- 2000001246 — ICARUS - left ventricular function (ICUdata) added in measurement
- 2000001247 — Nurse Activities Score 5 care of drains (ICUdata) added in measurement
- 2000001248 — Nursing Activities Score 16 Hemofiltration/dialysis (ICUdata) added in measurement
- 2000001253 — centimeter watercolumn per milimeter mercury column (ICUdata) added in measurement
- 2000001286 — Intra aortic baloon pump augmentation ratio (ICUdata) added in measurement
- 2000001290 — NICE admission diagnosis: dysrhythmia (deprecated) (ICUdata) added in observation
- 2000001292 — NICE SOFA daily: lowest P/F ratio (ICUdata) added in measurement
- 2000001293 — NICE admission diagnosis thrombolytic therapy after MI (ICUdata) added in observation
- 2000001296 — NICE admission diagnosis: intracranial mass (ICUdata) added in observation
- 2000001298 — NICE GCS: lowest eye score, first 24h (ICUdata) added in measurement
- 2000001300 — NICE GCS: eye score at 24h (deprecated) (ICUdata) added in measurement
- 2000001301 — NICE GCS: verbal score at 24h (deprecated) (ICUdata) added in measurement
- 2000001302 — Erytrhocytes [Presence] in Pleural fluid (ICUdata) added in measurement
- 2000001303 — NICE chronic diagnosis: cardiovascular insufficiency (ICUdata) added in observation
- 2000001304 — Adenovirus 40+42 DNA [Presence] in Stool (ICUdata) added in measurement
- 2000001305 — Leukocytes [Presence] in Pleural fluid (ICUdata) added in measurement
- 2000001306 — Epithelial cells [Presence] in Sputum (ICUdata) added in measurement
- 2000001307 — Maximum clot firmness [Length] in Blood by Thromboelastography --at 10 minutes (ICUdata) added in measurement
- 2000001308 — Human bocavirus DNA [Presence] in Stool (ICUdata) added in measurement
- 2000001309 — Meticillin resistant staphylococcus aureus DNA [Presence] in Perineum (ICUdata) added in measurement
- 2000001310 — Epithelial cells [Identifier] in Urine (ICUdata) added in measurement
- 2000001311 — Maximum clot firmness [Length] in Blood by Thromboelastography -- at 5 minutes (ICUdata) added in measurement
- 2000001320 — EuroSCORE II: kidney failure (ICUdata) added in measurement
- 2000001321 — calcium chloride / magnesium chloride / malic acid / potassium chloride / sodium acetate / sodium chloride [Sterofundin/Tetraspan] (ICUdata) added in drug_exposure
- 2000001322 — Subcutaneous catheter port (ICUdata) added in device_exposure
- 2000001323 — Type of cerebral spinal fluid drain (ICUdata) added in observation
- 2000001324 — Vascular closure device (ICUdata) added in device_exposure
- 2000001325 — Paravertabral catheter (ICUdata) added in device_exposure
- 2000001335 — Autodetubation with direct reintubation (ICUdata) added in condition_occurrence
- 2000001336 — NICE admission diagnosis: gastrointestinal bleed (ICUdata) added in observation
- 2000001339 — Free hemoglobin [Moles/volume] in Cerebral spinal fluid (ICUdata) added in measurement
- 2000001340 — Leukocytes [Presence] in Cerebral Spinal Fluid (ICUdata) added in measurement
- 2000001345 — NICE chronic diagnosis: diabetes (ICUdata) added in observation
- 2000001346 — NICE chronic diagnosis: COPD (ICUdata) added in observation
- 2000001348 — NICE chronic diagnosis: AIDS (ICUdata) added in observation
- 2000001350 — NICE chronic diagnosis: hematologic malignancy (ICUdata) added in observation
- 2000001351 — History of event within 1 day (ICUdata) added in measurement
- 2000001352 — CAM-ICU step 1 acute change or fluctuation mental status (ICUdata) added in measurement
- 2000001353 — History of event 72 hours pre-admission (ICUdata) added in measurement
- 2000001354 — NICE chronic diagnosis: chronic dialysis (ICUdata) added in observation
- 2000001355 — Intubation urgency (ICUdata) added in observation
- 2000001356 — NICE calculated: apache II score (ICUdata) added in measurement
- 2000001357 — NICE calculated: apache IV score (ICUdata) added in measurement
- 2000001358 — NICE delivered: apache II score (ICUdata) added in measurement
- 2000001359 — NICE delivered: apache IV score (ICUdata) added in measurement
- 2000001361 — NICE SOFA daily: PaO2 at lowest P/F ratio (ICUdata) added in measurement
- 2000001362 — NICE SOFA daily: pH at PaO2 measurement (ICUdata) added in measurement
- 2000001363 — NICE SOFA daily: PaCO2 (ICUdata) added in measurement
- 2000001368 — Tracheobronchial toilet frequency 24 hours (ICUdata) added in measurement
- 2000001369 — Tracheobronchial toilet technique (ICUdata) added in observation
- 2000001370 — Tracheobronchial toilet sputum aspect (ICUdata) added in observation
- 2000001371 — Sputum derived from (ICUdata) added in observation
- 2000001373 — NICE admission: (cardiothoracic) surgical patient (deprecated) (ICUdata) added in observation
- 2000001374 — NICE GCS: eye score at admission (deprecated) (ICUdata) added in measurement
- 2000001375 — NICE GCS: motor score at 24h (deprecated) (ICUdata) added in measurement
- 2000001376 — NICE GCS: verbal score at admission (deprecated) (ICUdata) added in measurement
- 2000001377 — NICE GCS: motor score at admission (deprecated) (ICUdata) added in measurement
- 2000001378 — NICE SOFA daily: special ventilation methods (ICUdata) added in observation
- 2000001379 — NICE SOFA daily: respiratory support during lowest P/F ratio (ICUdata) added in observation
- 2000001380 — NICE delivered: apache III score (ICUdata) added in measurement
- 2000001381 — Nursing Activities Score total (ICUdata) added in measurement
- 2000001382 — Inspiratory pressure above PEEP set --on pressure support (ICUdata) added in measurement
- 2000001383 — Inspiratory pressure including PEEP set --on pressure support (ICUdata) added in measurement
- 2000001385 — Inspiratory pressure above PEEP set --on pressure control (ICUdata) added in measurement
- 2000001386 — Inspiratory pressure including PEEP set --on pressure control (ICUdata) added in measurement
- 2000001388 — Inspiratory pressure including PEEP (ICUdata) added in measurement
- 2000001389 — Inspiratory pressure including PEEP set (ICUdata) added in measurement
- 2000001391 — CAM-ICU step 4b command (ICUdata) added in measurement
- 2000001399 — Phase angle [Angle] Body by Bioelectrical impedance analysis (ICUdata) added in measurement
- 2000001406 — Clot amplitude.extrinsic coagulation system activated [Length] in Blood by Rotational TEG --10 minutes post clotting time (ICUdata) added in measurement
- 2000001407 — Clot amplitude.extrinsic coagulation system activated [Length] in Blood by Rotational TEG --5 minutes post clotting time (ICUdata) added in measurement
- 2000001408 — Clot amplitude.extrinsic coagulation system activated.platelets inhibited [Length] in Blood by Rotational TEG --10 minutes post clotting time (ICUdata) added in measurement
- 2000001409 — Clot amplitude.extrinsic coagulation system activated.platelets inhibited [Length] in Blood by Rotational TEG --5 minutes post clotting time (ICUdata) added in measurement
- 2000001410 — Clot amplitude.intrinsic coagulation system activated [Length] in Blood by Rotational TEG --10 minutes post clotting time (ICUdata) added in measurement
- 2000001411 — Clot amplitude.intrinsic coagulation system activated [Length] in Blood by Rotational TEG --5 minutes post clotting time (ICUdata) added in measurement
- 2000001412 — Clot amplitude.intrinsic coagulation system activated.heparin insensitive [Length] in Blood by Rotational TEG --10 minutes post clotting time (ICUdata) added in measurement
- 2000001413 — Clot amplitude.intrinsic coagulation system activated.heparin insensitive [Length] in Blood by Rotational TEG --5 minutes post clotting time (ICUdata) added in measurement
- 2000001415 — Macrocytes/Erythrocytes in Blood by Automated count (ICUdata) added in measurement
- 2000001417 — Blood pressure --1 minute after standing (ICUdata) added in measurement
- 2000001443 — Vascular catheter complication (ICUdata) added in measurement
- 2000001459 — Filter running time CVVH (ICUdata) added in measurement
- 2000001461 — Postdilution fraction set CVVH (ICUdata) added in measurement
- 2000001462 — Predilution fraction set CVVH (ICUdata) added in measurement
- 2000001468 — External ventricular drain open/closed status (ICUdata) added in measurement
- 2000001474 — Gram negative bacilli [Presence] in Sputum by Gram stain (ICUdata) added in measurement
- 2000001475 — Gram negative cocci [Presence] in Sputum by Gram stain (ICUdata) added in measurement
- 2000001476 — Gram positive bacilli [Presence] in Sputum by Gram stain (ICUdata) added in measurement
- 2000001477 — Gram positive cocci [Presence] in Bronchial specimen by Gram stain (ICUdata) added in measurement
- 2000001479 — Gram positive cocci [Presence] in Sputum by Gram stain (ICUdata) added in measurement
- 2000001481 — Nontuberculous mycobacteria DNA [Presence] in Bronchoalveolar lavage by NAA with probe detection (ICUdata) added in measurement
- 2000001489 — Air stacking (ICUdata) added in procedure_occurrence
- 2000001512 — Trigger timeout setting Ventilator (ICUdata) added in measurement
- 2000001515 — One-lung ventilation (ICUdata) added in procedure_occurrence
- 2000001520 — End-expiratory gas flow Respiratory system airway --on ventilator (ICUdata) added in measurement
- 2000001521 — SIMV cycle time setting Ventilator (ICUdata) added in measurement
- 2000001526 — EuroSCORE II: pulmonary hypertension (ICUdata) added in measurement
- 2000001530 — Aldrete score circulation (ICUdata) added in measurement
- 2000001531 — Aldrete score colour (ICUdata) added in measurement
- 2000001532 — Aldrete score consciousness (ICUdata) added in measurement
- 2000001539 — Nursing Activities Score 13 intravenous replacement of large fluid losses (ICUdata) added in measurement
- 2000001542 — Nursing Activities Score 23 specific interventions outside ICU (ICUdata) added in measurement
- 2000001549 — Gram negative bacilli [Presence] in Urine by Gram stain (ICUdata) added in measurement
- 2000001550 — Gram positive bacilli [Presence] in Urine by Gram stain (ICUdata) added in measurement
- 2000001551 — Gram positive cocci [Presence] in Urine by Gram stain (ICUdata) added in measurement
- 2000001553 — Maximum lysis.extrinsic coagulation system activated.platelets inhibited [Length fraction] in Blood by Rotational TEG (ICUdata) added in measurement
- 2000001555 — Expiratory positive airway pressure setting (ICUdata) added in measurement
- 2001000001 — Own living environment (ICUdata) added in visit_occurrence
- 2001000002 — Standard hospital (ICUdata) added in visit_occurrence
- 2001000003 — Foreign hospital (ICUdata) added in visit_occurrence
- 2001000004 — Independent treatment centre (ICUdata) added in visit_occurrence
- 2001000005 — Specialty hospital (ICUdata) added in visit_occurrence
- 2001000006 — Tertiary hospital (ICUdata) added in visit_occurrence
- 2001000007 — Outpatient/emergency department (ICUdata) added in visit_occurrence
- 2001000008 — Military, emergency or penitentiary hospital (ICUdata) added in visit_occurrence
- 2001000009 — Other hospital (ICUdata) added in visit_occurrence
- 2001000010 — Other establishment (ICUdata) added in visit_occurrence
- 2001000011 — Neurology and neurosurgery (ICUdata) added in visit_occurrence
- 2001000012 — Otorhinolargyngial oncology (ICUdata) added in visit_occurrence
- 2001000014 — Neurology and Dermatology (ICUdata) added in visit_occurrence
- 2001000015 — Medium care unit (ICUdata) added in visit_detail
- 2001000015 — Medium care unit (ICUdata) added in visit_occurrence
- 2001000016 — Surgery and Gastroenterology (ICUdata) added in visit_occurrence
- 2001000017 — Orthopedics and Sports medicine (ICUdata) added in visit_occurrence
- 2001000018 — Gynaecology and Internal Medicine (ICUdata) added in visit_occurrence
- 2001000019 — Psychiatry medium care (ICUdata) added in visit_occurrence
- 2001000020 — Coronary care unit and cardiac emergency department (ICUdata) added in visit_occurrence
- 2001000021 — Vascular surgery and oro and maxillofacial surgery (ICUdata) added in visit_occurrence
- 2001000022 — Medical-psychiatric unit (ICUdata) added in visit_occurrence
- 2001000023 — Same Day Oncology treatment unit (ICUdata) added in visit_occurrence
- 2001000024 — Same Day treatment unit (ICUdata) added in visit_detail
- 2001000024 — Same Day treatment unit (ICUdata) added in visit_occurrence
- 2001000025 — Pulmonary medicine treatment room (ICUdata) added in visit_occurrence
- 2001000026 — Hemapharesis room (ICUdata) added in visit_detail
- 2001000026 — Hemapharesis room (ICUdata) added in visit_occurrence
- 2001000027 — Pulmonary medicine and lung surgery (ICUdata) added in visit_occurrence
- 2001000028 — Nephrology, rheumatology and dermatology (ICUdata) added in visit_occurrence
- 2001000029 — Orthopedics, Sports medicine and Plastic surgery (ICUdata) added in visit_occurrence
- 2001000030 — Mobile Intensive Care Unit (ICUdata) added in visit_occurrence
- 2001000032 — Urology and Gynaecology (ICUdata) added in visit_occurrence
- 2001000033 — Pulmonary medicine oncology (ICUdata) added in visit_occurrence
- 2001000034 — Neurosurgery and Plastic surgery (ICUdata) added in visit_occurrence
- 1 — Domain (Domain) removed in person
- 2 — Gender (Domain) removed in person
- 713196 — interferon beta-1b (RxNorm) removed in drug_exposure
- 742185 — atomoxetine (RxNorm) removed in drug_exposure
- 778873 — Streptococcus pneumoniae serotype 1 capsular antigen diphtheria CRM197 protein conjugate vaccine / Streptococcus pneumoniae serotype 14 capsular antigen diphtheria CRM197 protein conjugate vaccine / Streptococcus pneumoniae serotype 18C capsular antige... (RxNorm) removed in drug_exposure
- 792777 — varicella zoster virus glycoprotein E (RxNorm) removed in drug_exposure
- 908523 — mineral oil (RxNorm) removed in drug_exposure
- 979096 — zinc acetate (RxNorm) removed in drug_exposure
- 984232 — isotretinoin (RxNorm) removed in drug_exposure
- 994341 — meclizine (RxNorm) removed in drug_exposure
- 996625 — fluorescein (RxNorm) removed in drug_exposure
- 1073572 — Rotational thromboelastometry technique (SNOMED) removed in observation
- 1156378 — flurbiprofen (RxNorm) removed in drug_exposure
- 1195334 — choline (RxNorm) removed in drug_exposure
- 1398039 — St. John's wort extract (RxNorm) removed in drug_exposure
- 1501309 — thyroid (USP) (RxNorm) removed in drug_exposure
- 1503184 — mestranol (RxNorm) removed in drug_exposure
- 1520218 — betaine (RxNorm) removed in drug_exposure
- 1586640 — nitisinone (RxNorm) removed in drug_exposure
- 1593331 — etelcalcetide (RxNorm) removed in drug_exposure
- 1616989 — Carbon dioxide [Partial pressure] in Central venous blood (LOINC) removed in measurement
- 1792429 — proguanil (RxNorm) removed in drug_exposure
- 3002088 — cefTAZidime [Mass/volume] in Serum or Plasma (LOINC) removed in measurement
- 3004501 — Glucose [Mass/volume] in Serum or Plasma (LOINC) removed in measurement
- 3006025 — Fluid output wound drain 8 hour (LOINC) removed in measurement
- 3007637 — Fluid output chest tube 1 hour (LOINC) removed in measurement
- 3008828 — Urine output 8 hour (LOINC) removed in measurement
- 3009041 — Cardiolipin IgG Ab [Units/volume] in Serum by Immunoassay (LOINC) removed in measurement
- 3009420 — Ganciclovir [Mass/volume] in Serum or Plasma (LOINC) removed in measurement
- 3010488 — Prolactin [Mass/volume] in Serum or Plasma --1st specimen post XXX challenge (LOINC) removed in measurement
- 3010657 — Triiodothyronine (T3) Free [Mass/volume] in Serum or Plasma by Dialysis (LOINC) removed in measurement
- 3011550 — Carboxyhemoglobin [Mass/volume] in Blood (LOINC) removed in measurement
- 3011961 — Ferritin [Mass/volume] in Blood (LOINC) removed in measurement
- 3012796 — Blood product type (LOINC) removed in measurement
- 3013707 — Erythrocyte sedimentation rate [Velocity] in Red Blood Cells by Westergren method (LOINC) removed in measurement
- 3013826 — Glucose [Moles/volume] in Serum or Plasma (LOINC) removed in measurement
- 3014300 — Beta 2 glycoprotein 1 IgM Ab [Units/volume] in Serum (LOINC) removed in measurement
- 3014576 — Chloride [Moles/volume] in Serum or Plasma (LOINC) removed in measurement
- 3014835 — Urine output 1 hour (LOINC) removed in measurement
- 3015182 — Deprecated Erythrocyte distribution width [Entitic volume] by Automated count (LOINC) removed in measurement
- 3015511 — Apache III score (LOINC) removed in measurement
- 3016267 — Urine output by in and out urethral catheter (LOINC) removed in measurement
- 3016293 — Bicarbonate [Moles/volume] in Serum or Plasma (LOINC) removed in measurement
- 3016431 — Calcium.ionized [Moles/volume] adjusted to pH 7.4 in Serum or Plasma (LOINC) removed in measurement
- 3018658 — Beta 2 glycoprotein 1 IgG Ab [Units/volume] in Serum (LOINC) removed in measurement
- 3018677 — aPTT in Platelet poor plasma by Coagulation assay (LOINC) removed in measurement
- 3018913 — Phosphate [Moles/volume] in Blood (LOINC) removed in measurement
- 3019550 — Sodium [Moles/volume] in Serum or Plasma (LOINC) removed in measurement
- 3020460 — C reactive protein [Mass/volume] in Serum or Plasma (LOINC) removed in measurement
- 3024128 — Bilirubin.total [Mass/volume] in Serum or Plasma (LOINC) removed in measurement
- 3024929 — Platelets [#/volume] in Blood by Automated count (LOINC) removed in measurement
- 3025643 — Ethanol [Mass/volume] in Blood (LOINC) removed in measurement
- 3030884 — Deprecated Polymorphonuclear cells [#/volume] in Cerebral spinal fluid (LOINC) removed in measurement
- 3030905 — Deprecated Polymorphonuclear cells [#/volume] in Blood (LOINC) removed in measurement
- 3032948 — Heparin induced platelet Ab [Presence] in Serum (LOINC) removed in measurement
- 3033836 — Magnesium [Moles/volume] in Blood (LOINC) removed in measurement
- 3043995 — Bilirubin.conjugated+indirect [Moles/volume] in Serum or Plasma (LOINC) removed in measurement
- 4083588 — Patient sex (SNOMED) removed in observation
- 19005147 — methotrimeprazine (RxNorm) removed in drug_exposure
- 19008867 — cromoglycate (RxNorm) removed in drug_exposure
- 19016670 — docosahexaenoate (RxNorm) removed in drug_exposure
- 19026739 — pantothenic acid (RxNorm) removed in drug_exposure
- 19031397 — dipyrone (RxNorm) removed in drug_exposure
- 19039298 — sevoflurane (RxNorm) removed in drug_exposure
- 19043395 — phosphorus (RxNorm) removed in drug_exposure
- 19048699 — corticotropin-releasing hormone (RxNorm) removed in drug_exposure
- 19050104 — carnitine (RxNorm) removed in drug_exposure
- 19066274 — selenite (RxNorm) removed in drug_exposure
- 19072030 — curcumin (RxNorm) removed in drug_exposure
- 19080406 — anti-inhibitor coagulant complex (RxNorm) removed in drug_exposure
- 19080512 — articaine (RxNorm) removed in drug_exposure
- 19092061 — zinc citrate (RxNorm) removed in drug_exposure
- 19136048 — sodium (RxNorm) removed in drug_exposure
- 19136207 — lymphocyte immune globulin, anti-thymocyte globulin (RxNorm) removed in drug_exposure
- 21490855 — PEEP Respiratory system --on ventilator (LOINC) removed in measurement
- 35198180 — acetated ringer's solution(with glucose) (RxNorm Extension) removed in drug_exposure
- 35884360 — Heparin Sodium (RxNorm Extension) removed in drug_exposure
- 36027520 — glucosamine hydrochloride / glucosamine sulfate (RxNorm) removed in drug_exposure
- 36030139 — ethinyl estradiol / norethindrone (RxNorm) removed in drug_exposure
- 36030575 — acetic acid / salicylic acid (RxNorm) removed in drug_exposure
- 36659961 — Intensive care unit (ICU) admission date (LOINC) removed in observation
- 36849343 — COAGULATION FACTOR VIIA HUMAN (RxNorm Extension) removed in drug_exposure
- 36852771 — LANDIOLOL (RxNorm Extension) removed in drug_exposure
- 36855301 — VERAPAMIL, (-)- (RxNorm Extension) removed in drug_exposure
- 36861661 — HUMAN PLASMA (RxNorm Extension) removed in drug_exposure
- 36878602 — Taurolidine (RxNorm Extension) removed in drug_exposure
- 36879118 — human platelets (RxNorm Extension) removed in drug_exposure
- 37493796 — Epithiazide (RxNorm Extension) removed in drug_exposure
- 40762387 — Lacosamide [Mass/volume] in Blood (LOINC) removed in measurement
- 40763164 — OLANZapine [Mass/volume] in Blood (LOINC) removed in measurement
- 42709324 — vitamin D3 (RxNorm) removed in drug_exposure
- 42868692 — Triglyceride [Moles/volume] in Blood (LOINC) removed in measurement
- 42870551 — Thromboelastography after addtion of heparinase panel - Blood (LOINC) removed in measurement
- 42898711 — chlorine (RxNorm) removed in drug_exposure
- 42898837 — crospovidone (RxNorm) removed in drug_exposure
- 43013090 — isoprene (RxNorm) removed in drug_exposure
- 43013156 — sodium chlorate (RxNorm) removed in drug_exposure
- 46274210 — ceftaroline fosamil (RxNorm) removed in drug_exposure
- 2000000031 — CRRT dialysate solution (ICUdata) removed in measurement
- 2000000079 removed in measurement
- 2000000144 removed in measurement
- 2000000212 removed in measurement
- 2000000213 removed in measurement
- 2000000359 removed in measurement
- 2000000372 removed in measurement
- 2000000378 removed in measurement
- 2000000574 removed in drug_exposure
- 2000000583 removed in drug_exposure
- 2000000591 removed in drug_exposure
- 2000000628 removed in measurement
- 2000000635 removed in measurement
- 2000000663 removed in observation
- 2000000664 removed in observation
- 2000000665 removed in observation
- 2000000666 removed in observation
- 2000000667 removed in observation
- 2000000668 removed in observation
- 2000000669 removed in observation
- 2000000671 removed in observation
- 2000000901 — NICE admission: origin (ICUdata) removed in measurement
- 2000000911 removed in measurement
- 2000000950 removed in measurement
- 2000000951 removed in measurement
- 2000000952 removed in measurement
- 2000000956 removed in measurement

## Parameter Remappings

### 732893 — bupivacaine — 1/26 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| BUPIVACAINE/ADRENALINE INJVLST 5MG/5UG/ML FL 20ML | 36029293 |

### 789578 — levodopa — 8/13 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| LEVODOPA/BENSERAZIDE DISPERTABLET 100/25MG | 36030306 |
| LEVODOPA/CARBIDOPA GEL GASTRO-ENT 20/5MG/ML 100ML | 36029225 |
| LEVODOPA/CARBIDOPA TABLET   50/12,5MG | 36029225 |
| LEVODOPA/CARBIDOPA TABLET  250/25MG | 36029225 |
| LEVODOPA/CARBIDOPA TABLET MGA 100/25MG | 36029225 |
| LEVODOPA/CARBIDOPA/ENTACAPON TABLET  75/18,7/200MG | 36030184 |
| LEVODOPA/CARBIDOPA/ENTACAPON TABLET 100/25/200MG | 36030184 |
| LEVODOPA/CARBIDOPA/ENTACAPON TABLET 150/37,5/200MG | 36030184 |

### 902427 — timolol — 10/32 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| TIMOLOL/BIMATOPROST OOGDR 5/0,3MG/ML FL 3ML+B(OUD) | 21060563 |
| TIMOLOL/BIMATOPROST OOGDR 5/0,3MG/ML FL 3ML+BENZAL | 21060563 |
| TIMOLOL/BRIMONIDINE OOGDR 5/2MG/ML FL 5ML BENZ | 36030258 |
| TIMOLOL/DORZOLAM OOGDR 5/20MG/ML M 0,2ML Z CON OUD | 36030344 |
| TIMOLOL/DORZOLAMID OOGDR 5/20MG/ML FL 5ML BENZ | 36030344 |
| TIMOLOL/DORZOLAMIDE OOGDR 5/20MG/ML FL 10ML Z BENZ | 36030344 |
| TIMOLOL/DORZOLAMIDE OOGDR 5/20MG/ML M 0,2ML Z BENZ | 36030344 |
| TIMOLOL/DORZOLAMIDE OOGDRUPPELS 5/20MG/ML FL  5ML | 36030344 |
| TIMOLOL/LATANOPROST OOGDR 5MG/50UG/ML 2,5ML BENZAL | 36030140 |
| TIMOLOL/LATANOPROST OOGDR 5MG/50UG/ML 2,5ML Z CONS | 36030140 |

### 903963 — triamcinolone — 1/15 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| AZIJNZUUR/TRIAMCINOLONACETONIDE OORDR 7,2/1MG/G | 929549 |

### 907879 — miconazole — 1/13 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| MICONAZOL 2% ZINKOXIDESMEERSEL | 36027059 |

### 908921 — calcipotriene — 1/5 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| BETAMETHASON/CALCIPOTRIOL ZALF 0,5MG/50UG/G | 36030600 |

### 938044 — brinzolamide — 2/5 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| BRINZOLAMIDE/BRIMONIDI OOGDR 10/2MG/ML FL 5ML BENZ | 778917 |
| BRINZOLAMIDE/BRIMONIDINE OOGDR 10/2MG/ML FL 5ML | 778917 |

### 948487 — polyethylene glycol 300 — 1/5 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| MACROGOL/ZOUTEN PDR V DRANK (KLEAN PREP) | 948515 |

### 974166 — hydrochlorothiazide — 1/13 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| AMILORIDE/HYDROCHLOORTHIAZIDE TABLET 5/50MG | 36029883 |

### 989878 — lidocaine — 5/60 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| LIDOCAINE/ADRENALINE INJVL 10MG/ 5UG/ML FL 20ML | 36028719, 36029291 |
| LIDOCAINE/ADRENALINE INJVL 10MG/ 5UG/ML FL 20MLOUD | 36028719 |
| LIDOCAINE/ADRENALINE INJVL 20MG/ 5UG/ML FL 20ML | 36028719 |
| LIDOCAINE/ADRENALINE INJVL 20MG/ 5UG/ML FL 20MLOUD | 36028719 |
| LIDOCAINE/ADRENALINE INJVL 20MG/12,5UG/ML PATR 1,8 | 36028719 |

### 1073572 — Rotational thromboelastometry technique — 4/4 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| A5 extem | 2000001407 |
| A5 fibtem | 2000001409 |
| A5 heptem | 2000001413 |
| A5 intem | 2000001411 |

### 1133201 — buprenorphine — 2/19 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| BUPRENORFINE/NALOXON TABLET SUBLINGU  2/0,5MG | 36030126 |
| BUPRENORFINE/NALOXON TABLET SUBLINGU  8/2MG | 36030126 |

### 1149380 — fluticasone — 1/23 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| AZELASTINE/FLUTICASON NEUSSPRAY 137/50UG/DO 120 DO | 778911 |

### 1308216 — lisinopril — 1/12 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| LISINOPRIL/HYDROCHLOORTHIAZIDE TABLET 20/12,5MG | 36030000 |

### 1308842 — valsartan — 1/10 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| VALSARTAN/HYDROCHLOORTHIAZIDE TAB OMH 160/12,5MG | 36030008 |

### 1314002 — atenolol — 1/8 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| ATENOLOL/CHLOORTALIDON TABLET  50/12,5MG | 36029651 |

### 1317640 — telmisartan — 2/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| TELMISARTAN/HYDROCHLOORTHIAZIDE TABLET 40/12,5MG | 36030113 |
| TELMISARTAN/HYDROCHLOORTHIAZIDE TABLET 80/12,5MG | 36030113 |

### 1341927 — enalapril — 1/11 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| ENALAPRIL/HYDROCHLOORTHIAZIDE TABLET 20/12,5MG | 36029974 |

### 1347384 — irbesartan — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| IRBESARTAN/HYDROCHLOORTHIAZIDE TABLET 150/12,5MG | 36029999 |

### 1351557 — candesartan — 1/9 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| CANDESARTAN/HYDROCHLOORTHIAZIDE TABLET 16/12,5MG | 36030110 |

### 1363749 — fosinopril — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| FOSINOPRIL/HYDROCHLOORTHIAZIDE TABLET 20/12,5MG | 36030099 |

### 1367500 — losartan — 2/10 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| LOSARTAN/HYDROCHLOORTHIAZIDE TAB OMHULD  50/12,5MG | 36030001 |
| LOSARTAN/HYDROCHLOORTHIAZIDE TABLET 100/12,5MG | 36030001 |

### 1373225 — perindopril — 1/16 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| PERINDOPRIL/INDAPAMIDE TABLET  4/1,25MG (ERBUMINE) | 36030141 |

### 1447532 — Richmond Agitation Sedation Scale — 1/15 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Aandacht (RASS = 0);R RUMC CAM ICU VERSIE 2 SAVEAHAART RASS = 0 STAP 4 | 2000001025 |

### 1518254 — dexamethasone — 4/74 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| DEXAMETHASON/FRAMYCETINE/GRAMICIDINE OOGDR FL 8OUD | 2000000580 |
| DEXAMETHASON/FRAMYCETINE/GRAMICIDINE OORDR | 2000000580 |
| DEXAMETHASON/GENTAMICINE OOGZALF 0,3/3MG/G TUBE 3G | 2000000581 |
| DEXAMETHASON/TOBRAMYCINE OOGZALF 1/3MG/G TUBE 3,5G | 36031113 |

### 1616373 — Oxygen saturation in Central venous blood — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| SvO2 Vigilance | 3018465 |

### 1616989 — Carbon dioxide [Partial pressure] in Central venous blood — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| PCO2 veneus | 3021447 |

### 1713332 — amoxicillin — 4/46 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| AMOXICILLINE/CLAVULAANZUUR (1000/200MG) KORTLOPEND INFUUS | 36029811 |
| AMOXICILLINE/CLAVULAANZUUR 50/5 MG/ML INJECTIE | 36029811 |
| AMOXICILLINE/CLAVULAANZUUR INJPDR  500/50MG FL | 36029811 |
| AMOXICILLINE/CLAVULAANZUUR TABLET 875/125MG | 36029811 |

### 1718517 — acetylsalicylsalicylic acid — 7/17 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| ACETYLSALICYLZUUR 100MG/ML INJECTIE | 1112807 |
| Acetylsalicylzuur | 1112807 |
| Acetylsalicylzuur (Aspirine / Aspro / Alka seltzer / Aspirine protect) | 1112807 |
| Acetylsalicylzuur IV (Aspegic) | 1112807 |
| ZZZ ACETYLSALICYLZUUR INJECTIE | 1112807 |
| acetylsalicylzuur | 1112807 |
| acetylsalicylzuur pdr v injvlst 500mg | 1112807 |

### 1746114 — piperacillin — 1/6 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| PIPERACILLINE/TAZOBACTAM 200/25 MG/ML INJECTIE | 36030773 |

### 1776684 — ceftazidime — 1/21 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| CEFTAZIDIM/AVIBACTAM INFUSIEPOEDER 2000/500MG FL | 36029713 |

### 1792429 — proguanil — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| ATOVAQUON/PROGUANIL TABLET FO 250/100MG | 36030109 |

### 1988717 — Continuous renal replacement therapy mode Renal replacement therapy circuit — 1/11 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Niervervangende therapie | 2000000333 |

### 3000333 — Central venous pressure (CVP) Mean — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| CVP;R UMCA CVD/CVP | 21490675 |

### 3000461 — Pressure support setting Ventilator — 1/3 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Psupport above PEEP;R UMCA ICU VENTILATOR PRESSURE SUPP S | 2000001382 |

### 3001308 — Cholesterol in LDL [Moles/volume] in Serum or Plasma — 1/6 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Chemie (s) non-HDL cholesterol | 42868678 |

### 3002088 — cefTAZidime [Mass/volume] in Serum or Plasma — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| CEF-KAOL.T (bloed) | 3013466 |

### 3004501 — Glucose [Mass/volume] in Serum or Plasma — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| GLUCOSE (PLASMA) (Onbekend) | 46236948 |
| GLUCOSE, NIET NUCHTER | 46236948 |

### 3004921 — Ventilation mode Ventilator — 1/27 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Mode (Bipap Vision) | 2000000250 |

### 3005445 — Coagulation factor X activated [Units/volume] in Platelet poor plasma by Coagulation assay — 1/3 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Anti FXa (bloed) | 21493512 |

### 3005629 — Inhaled oxygen flow rate — 2/20 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Flow PLS | 2000000099 |
| HFO-Amplitude | 36717922 |

### 3005772 — Bilirubin.conjugated [Moles/volume] in Serum or Plasma — 2/10 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Bilirubine (bloed) | 3006140 |
| Gecon.Bili (bloed) | 3044599 |

### 3006552 — Fluid intake oral Estimated — 766/1632 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| input - Per Os ( Carezzo) | 2000001123 |
| input - Per Os ( Water) | 2000001123 |
| input - Per Os ( shake) | 2000001123 |
| input - Per Os (-) | 2000001123 |
| input - Per Os (0.5 banaan) | 2000001123 |
| input - Per Os (0.5 warme maaltijd) | 2000001123 |
| input - Per Os (00 - 07) | 2000001123 |
| input - Per Os (08 - 23) | 2000001123 |
| input - Per Os (08- 14:30) | 2000001123 |
| input - Per Os (08-23) | 2000001123 |
| input - Per Os (1 boterham kaas) | 2000001123 |
| input - Per Os (1 boterham met kaas ) | 2000001123 |
| input - Per Os (1 boterham) | 2000001123 |
| input - Per Os (1 gr Mg in Nacl) | 2000001123 |
| input - Per Os (1 krenten boterham) | 2000001123 |
| input - Per Os (1 warme maaltijd) | 2000001123 |
| input - Per Os (1 witte boterham jam) | 2000001123 |
| input - Per Os (1 witte boterham met 2boter en oude kaas, 1 krentenbotterham) | 2000001123 |
| input - Per Os (1 xboterham + smeerkaas en kaas) | 2000001123 |
| input - Per Os (1/2 waterijsje) | 2000001123 |
| input - Per Os (1/3 avondmaaltijd) | 2000001123 |
| input - Per Os (1/4 fles water) | 2000001123 |
| input - Per Os (100cc sv) | 2000001123 |
| input - Per Os (1075) | 2000001123 |
| input - Per Os (11/1 vanaf 14 uur) | 2000001123 |
| input - Per Os (12-21.30) | 2000001123 |
| input - Per Os (15.00-24.00 per os) | 2000001123 |
| input - Per Os (1500) | 2000001123 |
| input - Per Os (1525) | 2000001123 |
| input - Per Os (1560) | 2000001123 |
| input - Per Os (15gr fresubin) | 2000001123 |
| input - Per Os (15gr proteine) | 2000001123 |
| input - Per Os (1x beschuit me kaas) | 2000001123 |
| input - Per Os (1x boterham kaas) | 2000001123 |
| input - Per Os (1x boterham met jam) | 2000001123 |
| input - Per Os (1x boterham met kaas) | 2000001123 |
| input - Per Os (1x boterham) | 2000001123 |
| input - Per Os (1x brood met jam) | 2000001123 |
| input - Per Os (1x krenteboterham) | 2000001123 |
| input - Per Os (1x krntebrood met kaas) | 2000001123 |
| input - Per Os (2 appels geschild) | 2000001123 |
| input - Per Os (2 appels) | 2000001123 |
| input - Per Os (2 beschuit met suiker en boter) | 2000001123 |
| input - Per Os (2 boterham bruin met jam een hagelslag) | 2000001123 |
| input - Per Os (2 boterhammen ham+ kaas) | 2000001123 |
| input - Per Os (2 boterhammen met appelstroop en pindakaas) | 2000001123 |
| input - Per Os (2 boterhammen met kaas en jam) | 2000001123 |
| input - Per Os (2 boterhammen met kaas en worst) | 2000001123 |
| input - Per Os (2 boterhammen met kaas) | 2000001123 |
| input - Per Os (2 boterhammen met rookvlees) | 2000001123 |
| input - Per Os (2 boterhammen met smeerkaas) | 2000001123 |
| input - Per Os (2 boterhammen met smeerworst) | 2000001123 |
| input - Per Os (2 botterhamen met hartig beleg) | 2000001123 |
| input - Per Os (2 botterhamen met kaas) | 2000001123 |
| input - Per Os (2 br boterhammen met kaas /worst) | 2000001123 |
| input - Per Os (2 brood) | 2000001123 |
| input - Per Os (2 bruine boterham + kaas + boter) | 2000001123 |
| input - Per Os (2 bruine boterhammen met kaas en kipfilet) | 2000001123 |
| input - Per Os (2 bruine boterhammen met kaas) | 2000001123 |
| input - Per Os (2 plakken kaas) | 2000001123 |
| input - Per Os (2 witte boterhammen met smeerkaas en smeerworst.) | 2000001123 |
| input - Per Os (2x beschuit jam) | 2000001123 |
| input - Per Os (2x beschuit met kipfilet) | 2000001123 |
| input - Per Os (2x boterham met kaas) | 2000001123 |
| input - Per Os (2x boterham met smeerworst) | 2000001123 |
| input - Per Os (2x boterham smeerworst) | 2000001123 |
| input - Per Os (2x boterham wit kipfilet) | 2000001123 |
| input - Per Os (2x boterham) | 2000001123 |
| input - Per Os (2x boterham, 2x creaker, 2x kaas, 2x kipfilet, 2x jam) | 2000001123 |
| input - Per Os (2x boterhammen kaas) | 2000001123 |
| input - Per Os (2x boterhammen wit kipfilet) | 2000001123 |
| input - Per Os (2x boterhammen) | 2000001123 |
| input - Per Os (2x brood met kaas) | 2000001123 |
| input - Per Os (2x brood, kipfilet, hagelslag.) | 2000001123 |
| input - Per Os (2x bruin brood met kaas) | 2000001123 |
| input - Per Os (2x bruin brood met kaas, ontbijtkoek) | 2000001123 |
| input - Per Os (2x cracker, hagelslag, boter, ei) | 2000001123 |
| input - Per Os (2x pistolet met vleeswaren) | 2000001123 |
| input - Per Os (2x warme maaltijd) | 2000001123 |
| input - Per Os (2x wit brood kaas) | 2000001123 |
| input - Per Os (2x witte boterhammen met kaas) | 2000001123 |
| input - Per Os (3 Liter NACL correctie SEH) | 2000001123 |
| input - Per Os (3 botterhamen met hartig beleg) | 2000001123 |
| input - Per Os (3) | 2000001123 |
| input - Per Os (3/4 boterham met jam) | 2000001123 |
| input - Per Os (300) | 2000001123 |
| input - Per Os (350) | 2000001123 |
| input - Per Os (3x bruine boterhammen) | 2000001123 |
| input - Per Os (4 boterhammen) | 2000001123 |
| input - Per Os (440) | 2000001123 |
| input - Per Os (4x boterham+ boter + kaas) | 2000001123 |
| input - Per Os (4x mandarijn) | 2000001123 |
| input - Per Os (5 glazen water) | 2000001123 |
| input - Per Os (550 ml) | 2000001123 |
| input - Per Os (655) | 2000001123 |
| input - Per Os (750 ml) | 2000001123 |
| input - Per Os (955) | 2000001123 |
| input - Per Os (970) | 2000001123 |
| input - Per Os (AA drank ) | 2000001123 |
| input - Per Os (AA) | 2000001123 |
| input - Per Os (Aantal happen van gemalen warme maaltijd) | 2000001123 |
| input - Per Os (Aanvullende eiwitrijke dieetvoeding in poedervorm) | 2000001123 |
| input - Per Os (Aardappelpuree) | 2000001123 |
| input - Per Os (Aardbeien vla) | 2000001123 |
| input - Per Os (Aardbeien) | 2000001123 |
| input - Per Os (Actieve kool) | 2000001123 |
| input - Per Os (Alpro toetje) | 2000001123 |
| input - Per Os (Alpro vla) | 2000001123 |
| input - Per Os (Appel) | 2000001123 |
| input - Per Os (Appelmoes met eiwit) | 2000001123 |
| input - Per Os (Appelmoes verrijkt) | 2000001123 |
| input - Per Os (Appelmoes/fruitmoes) | 2000001123 |
| input - Per Os (Avonddienst) | 2000001123 |
| input - Per Os (Avonddiest) | 2000001123 |
| input - Per Os (Bakje ananas) | 2000001123 |
| input - Per Os (Beleg: Kaas) | 2000001123 |
| input - Per Os (Beschuit 2x, smeerkaas en pindakaas) | 2000001123 |
| input - Per Os (Beschuit) | 2000001123 |
| input - Per Os (Bessen sap) | 2000001123 |
| input - Per Os (Bessensap) | 2000001123 |
| input - Per Os (Biscuitje) | 2000001123 |
| input - Per Os (Boteram 1x bruin met kaas) | 2000001123 |
| input - Per Os (Boterham Kaas) | 2000001123 |
| input - Per Os (Boterham hagelslag) | 2000001123 |
| input - Per Os (Boterham jam) | 2000001123 |
| input - Per Os (Boterham kaas + ei) | 2000001123 |
| input - Per Os (Boterham kaas) | 2000001123 |
| input - Per Os (Boterham kipfilet) | 2000001123 |
| input - Per Os (Boterham met hartig beleg) | 2000001123 |
| input - Per Os (Boterham met jam) | 2000001123 |
| input - Per Os (Boterham met kaas) | 2000001123 |
| input - Per Os (Boterham oude kaas) | 2000001123 |
| input - Per Os (Boterham smeerworst) | 2000001123 |
| input - Per Os (Boterham) | 2000001123 |
| input - Per Os (Boterhammen 2x) | 2000001123 |
| input - Per Os (Boterhammen) | 2000001123 |
| input - Per Os (Bouillon ~) | 2000001123 |
| input - Per Os (Bouwsteentje) | 2000001123 |
| input - Per Os (Brood 1x) | 2000001123 |
| input - Per Os (Brood 2x) | 2000001123 |
| input - Per Os (Brood) | 2000001123 |
| input - Per Os (Broodje kaas) | 2000001123 |
| input - Per Os (Broodje met kaas ) | 2000001123 |
| input - Per Os (Bruine boterham met yam) | 2000001123 |
| input - Per Os (Bruine boterham) | 2000001123 |
| input - Per Os (Cappucino) | 2000001123 |
| input - Per Os (Caresso sap) | 2000001123 |
| input - Per Os (Carezo) | 2000001123 |
| input - Per Os (Carezzo Sinasappelsap) | 2000001123 |
| input - Per Os (Carezzo sap) | 2000001123 |
| input - Per Os (Carezzo) | 2000001123 |
| input - Per Os (Carezzosap) | 2000001123 |
| input - Per Os (Carreso sap) | 2000001123 |
| input - Per Os (Carreso) | 2000001123 |
| input - Per Os (Carresso sap) | 2000001123 |
| input - Per Os (Carresso) | 2000001123 |
| input - Per Os (Carrezo) | 2000001123 |
| input - Per Os (Carrezzo) | 2000001123 |
| input - Per Os (Cassis) | 2000001123 |
| input - Per Os (Chocolademelk warm) | 2000001123 |
| input - Per Os (Cola zero) | 2000001123 |
| input - Per Os (Correctie H2O middels sonde) | 2000001123 |
| input - Per Os (Crezzo bessen) | 2000001123 |
| input - Per Os (Cup a soup~) | 2000001123 |
| input - Per Os (Dagdienst 400) | 2000001123 |
| input - Per Os (Dagdienst tot 13:00) | 2000001123 |
| input - Per Os (Dagdienst) | 2000001123 |
| input - Per Os (Drinken gedurende de dag) | 2000001123 |
| input - Per Os (Drinkvoeding eiwitverrijkt) | 2000001123 |
| input - Per Os (Drinkvoeding sapbasis) | 2000001123 |
| input - Per Os (Drinkvoeding yoghurtbasis) | 2000001123 |
| input - Per Os (Drinkvoeding ~) | 2000001123 |
| input - Per Os (Drinkyoghurt ~) | 2000001123 |
| input - Per Os (Druivensap) | 2000001123 |
| input - Per Os (E+ sinasappelsap) | 2000001123 |
| input - Per Os (Ei) | 2000001123 |
| input - Per Os (Eitje erbij) | 2000001123 |
| input - Per Os (Eiwit verrijkte vla) | 2000001123 |
| input - Per Os (Eiwitrijk drankje chocolade) | 2000001123 |
| input - Per Os (Eiwitrijke vla ) | 2000001123 |
| input - Per Os (Eiwitverrijkt taartje) | 2000001123 |
| input - Per Os (Eiwitverrijkte pap) | 2000001123 |
| input - Per Os (Eiwitverrijkte shake) | 2000001123 |
| input - Per Os (Eiwitverrijkte vla) | 2000001123 |
| input - Per Os (Eiwitverrijkte vla~) | 2000001123 |
| input - Per Os (FRUITSAP) | 2000001123 |
| input - Per Os (Fles water) | 2000001123 |
| input - Per Os (Fortimel ~) | 2000001123 |
| input - Per Os (Fresubin 15 g) | 2000001123 |
| input - Per Os (Fresubin 15 gr in water) | 2000001123 |
| input - Per Os (Fresubin 15 gr) | 2000001123 |
| input - Per Os (Fresubin 15gr) | 2000001123 |
| input - Per Os (Fresubin Protein 15gr) | 2000001123 |
| input - Per Os (Fruit  kiwi) | 2000001123 |
| input - Per Os (Fruit --> 1/2 banaan) | 2000001123 |
| input - Per Os (Fruit 2 mandarijnen) | 2000001123 |
| input - Per Os (Fruit Banaan) | 2000001123 |
| input - Per Os (Fruit appel en manderijn) | 2000001123 |
| input - Per Os (Fruit appel) | 2000001123 |
| input - Per Os (Fruit banaan) | 2000001123 |
| input - Per Os (Fruit banaan, 2x mandarijn) | 2000001123 |
| input - Per Os (Fruit banaan, appel en mandarijn) | 2000001123 |
| input - Per Os (Fruit banaan/ mandarijn) | 2000001123 |
| input - Per Os (Fruit banan) | 2000001123 |
| input - Per Os (Fruit blauwe bessen 100gr) | 2000001123 |
| input - Per Os (Fruit mandarijn) | 2000001123 |
| input - Per Os (Fruit salade) | 2000001123 |
| input - Per Os (Fruit ~ banaan en mandarijn) | 2000001123 |
| input - Per Os (Fruit ~ banaan) | 2000001123 |
| input - Per Os (Fruit ~ mandarijn) | 2000001123 |
| input - Per Os (Fruit ~) | 2000001123 |
| input - Per Os (Fruit ~banaan) | 2000001123 |
| input - Per Os (Fruit(cocktail) ~) | 2000001123 |
| input - Per Os (Gebak) | 2000001123 |
| input - Per Os (Gehaktbal met peertjes) | 2000001123 |
| input - Per Os (Gepureerde warme maaltijd) | 2000001123 |
| input - Per Os (Geschild appeltje) | 2000001123 |
| input - Per Os (Glaasje vochtlijst) | 2000001123 |
| input - Per Os (Glaasje water) | 2000001123 |
| input - Per Os (Glutenvrij brood) | 2000001123 |
| input - Per Os (Goedemorgen ontbijt) | 2000001123 |
| input - Per Os (H2O via sonde) | 2000001123 |
| input - Per Os (Half pak rijstwafels) | 2000001123 |
| input - Per Os (Halve boterham met kaas) | 2000001123 |
| input - Per Os (Halve boterham) | 2000001123 |
| input - Per Os (Hartig beleg) | 2000001123 |
| input - Per Os (Heldere dranken) | 2000001123 |
| input - Per Os (IJs  raketje) | 2000001123 |
| input - Per Os (IJs (racketje)) | 2000001123 |
| input - Per Os (IJs (waterijs)) | 2000001123 |
| input - Per Os (IJs - raketje) | 2000001123 |
| input - Per Os (IJs 2x raket en peer) | 2000001123 |
| input - Per Os (IJs 2x) | 2000001123 |
| input - Per Os (IJs 50) | 2000001123 |
| input - Per Os (IJs Raket) | 2000001123 |
| input - Per Os (IJs blokje) | 2000001123 |
| input - Per Os (IJs peer) | 2000001123 |
| input - Per Os (IJs peer75) | 2000001123 |
| input - Per Os (IJs peerijsje) | 2000001123 |
| input - Per Os (IJs peren) | 2000001123 |
| input - Per Os (IJs raket) | 2000001123 |
| input - Per Os (IJs raketje) | 2000001123 |
| input - Per Os (IJs softijs) | 2000001123 |
| input - Per Os (IJs vanille) | 2000001123 |
| input - Per Os (IJs water) | 2000001123 |
| input - Per Os (IJs ~) | 2000001123 |
| input - Per Os (IJs ~waterijs) | 2000001123 |
| input - Per Os (IJsblok) | 2000001123 |
| input - Per Os (IJslollie ~) | 2000001123 |
| input - Per Os (Intake avonddienst) | 2000001123 |
| input - Per Os (Intake hele dag) | 2000001123 |
| input - Per Os (Intake in avonddienst ) | 2000001123 |
| input - Per Os (Intake over de avond) | 2000001123 |
| input - Per Os (Jus de orange) | 2000001123 |
| input - Per Os (Kaneelkoekje) | 2000001123 |
| input - Per Os (Karnemelk  ~) | 2000001123 |
| input - Per Os (Kip filet) | 2000001123 |
| input - Per Os (Klein pannenkoekje) | 2000001123 |
| input - Per Os (Koffie verkeerd met 3 suiker) | 2000001123 |
| input - Per Os (Koffie/water) | 2000001123 |
| input - Per Os (Krenteboterham) | 2000001123 |
| input - Per Os (Krentenboterham met boter) | 2000001123 |
| input - Per Os (Krentenbrood met kaas) | 2000001123 |
| input - Per Os (Langetje) | 2000001123 |
| input - Per Os (Limonade / sap  ~) | 2000001123 |
| input - Per Os (Limonade / sap) | 2000001123 |
| input - Per Os (Llimo) | 2000001123 |
| input - Per Os (MEDICATIE + EI+) | 2000001123 |
| input - Per Os (Maaginhoud uit maagsonde) | 2000001123 |
| input - Per Os (Maagretentie retour) | 2000001123 |
| input - Per Os (Maaltijd) | 2000001123 |
| input - Per Os (Macaroni Bolognese gemalen maaltijd) | 2000001123 |
| input - Per Os (Macdonalds) | 2000001123 |
| input - Per Os (Manderijn) | 2000001123 |
| input - Per Os (Medicatie via DDS) | 2000001123 |
| input - Per Os (Medicatie via de sonde) | 2000001123 |
| input - Per Os (Medicatie via sonde) | 2000001123 |
| input - Per Os (Melk  ~) | 2000001123 |
| input - Per Os (Melkunie proteine drank 20gram eiwit) | 2000001123 |
| input - Per Os (Melkunie proteine) | 2000001123 |
| input - Per Os (Mellk) | 2000001123 |
| input - Per Os (Movicolon + spoelen) | 2000001123 |
| input - Per Os (Muffin) | 2000001123 |
| input - Per Os (Nootjes) | 2000001123 |
| input - Per Os (Nurtri) | 2000001123 |
| input - Per Os (Nutri juice) | 2000001123 |
| input - Per Os (Nutridrink  carezzo sap) | 2000001123 |
| input - Per Os (Nutridrink Fresubin) | 2000001123 |
| input - Per Os (Nutridrink prot +) | 2000001123 |
| input - Per Os (Nutridrink proteine) | 2000001123 |
| input - Per Os (Nutridrink vegan) | 2000001123 |
| input - Per Os (Nutridrink ~) | 2000001123 |
| input - Per Os (Nutridrink� Compact) | 2000001123 |
| input - Per Os (Nutridrink� Cr�me) | 2000001123 |
| input - Per Os (Nutridrink� Fruit) | 2000001123 |
| input - Per Os (Nutridrink� Yoghurt) | 2000001123 |
| input - Per Os (Nutridrink�) | 2000001123 |
| input - Per Os (Nutrijuice) | 2000001123 |
| input - Per Os (Nutrison kwark) | 2000001123 |
| input - Per Os (ORS ) | 2000001123 |
| input - Per Os (Omelet) | 2000001123 |
| input - Per Os (Ontbijt koek) | 2000001123 |
| input - Per Os (Ontbijt) | 2000001123 |
| input - Per Os (Ontbijtkoek) | 2000001123 |
| input - Per Os (Oraal) | 2000001123 |
| input - Per Os (Orale Intake) | 2000001123 |
| input - Per Os (PEG doorspoelen) | 2000001123 |
| input - Per Os (PROsource) | 2000001123 |
| input - Per Os (Pap  ~) | 2000001123 |
| input - Per Os (Pepsi Max) | 2000001123 |
| input - Per Os (Peptamen SV) | 2000001123 |
| input - Per Os (Per Os  24u) | 2000001123 |
| input - Per Os (Per Os  350) | 2000001123 |
| input - Per Os (Per Os  van 00:00-12:00) | 2000001123 |
| input - Per Os (Per Os  ~750) | 2000001123 |
| input - Per Os (Per Os  ~Water) | 2000001123 |
| input - Per Os (Per Os) | 2000001123 |
| input - Per Os (Perenijs) | 2000001123 |
| input - Per Os (Perenijsje) | 2000001123 |
| input - Per Os (Plakje kaas) | 2000001123 |
| input - Per Os (Pleinvue ~) | 2000001123 |
| input - Per Os (Pleinvue) | 2000001123 |
| input - Per Os (Portie SV) | 2000001123 |
| input - Per Os (Portie sondevoeding) | 2000001123 |
| input - Per Os (Poteine shake) | 2000001123 |
| input - Per Os (Prakje) | 2000001123 |
| input - Per Os (ProSource  + H2O) | 2000001123 |
| input - Per Os (ProSource + spoeling) | 2000001123 |
| input - Per Os (ProSource) | 2000001123 |
| input - Per Os (Proetin shake) | 2000001123 |
| input - Per Os (Prosource SV) | 2000001123 |
| input - Per Os (Prosource ~) | 2000001123 |
| input - Per Os (Prosource) | 2000001123 |
| input - Per Os (Protein drankje ) | 2000001123 |
| input - Per Os (Protein drankje) | 2000001123 |
| input - Per Os (Protein shake) | 2000001123 |
| input - Per Os (Proteine 20g chocolade) | 2000001123 |
| input - Per Os (Proteine milkshake) | 2000001123 |
| input - Per Os (Proteine shake chocolade) | 2000001123 |
| input - Per Os (Proteine verrijkte drank) | 2000001123 |
| input - Per Os (Prote�n rode vruchten) | 2000001123 |
| input - Per Os (Prote�nedrank aardbei) | 2000001123 |
| input - Per Os (Ptoteine plus drank) | 2000001123 |
| input - Per Os (Pudding toetje) | 2000001123 |
| input - Per Os (Radler) | 2000001123 |
| input - Per Os (Raket ijsje) | 2000001123 |
| input - Per Os (Raketijsje 2x) | 2000001123 |
| input - Per Os (Resonium) | 2000001123 |
| input - Per Os (Retour maagretentie) | 2000001123 |
| input - Per Os (Rijstepap ~) | 2000001123 |
| input - Per Os (SV ) | 2000001123 |
| input - Per Os (SV 225ml) | 2000001123 |
| input - Per Os (SV Intens) | 2000001123 |
| input - Per Os (SV PPMF) | 2000001123 |
| input - Per Os (SV advanced) | 2000001123 |
| input - Per Os (SV portie) | 2000001123 |
| input - Per Os (Shake en+) | 2000001123 |
| input - Per Os (Sinasappelsap) | 2000001123 |
| input - Per Os (Sirooop) | 2000001123 |
| input - Per Os (Siroop 0% suiker) | 2000001123 |
| input - Per Os (Siroop 0.0% suiker) | 2000001123 |
| input - Per Os (Siroop) | 2000001123 |
| input - Per Os (Smeerkaas + smeerworst) | 2000001123 |
| input - Per Os (Smoothie  ~) | 2000001123 |
| input - Per Os (Soep verdikt) | 2000001123 |
| input - Per Os (Soep ~) | 2000001123 |
| input - Per Os (Sojapudding chocolade) | 2000001123 |
| input - Per Os (Sondevoeding MF prot+) | 2000001123 |
| input - Per Os (Sondevoeding Multifibre proth plus 220 ml) | 2000001123 |
| input - Per Os (Spa) | 2000001123 |
| input - Per Os (Spinazie met aardappels en rundvlees) | 2000001123 |
| input - Per Os (Suiker vrije limonade) | 2000001123 |
| input - Per Os (Suikervrije limonade) | 2000001123 |
| input - Per Os (Suikervrije linomade) | 2000001123 |
| input - Per Os (TPV) | 2000001123 |
| input - Per Os (Taart) | 2000001123 |
| input - Per Os (Tosti 2x) | 2000001123 |
| input - Per Os (Tosti ham/kaas) | 2000001123 |
| input - Per Os (Tosti ~) | 2000001123 |
| input - Per Os (Tosti) | 2000001123 |
| input - Per Os (Totaal aan vocht vanmorgen) | 2000001123 |
| input - Per Os (Totaal in 24 uur) | 2000001123 |
| input - Per Os (Tussendoortje di�tist  vla) | 2000001123 |
| input - Per Os (Tussendoortje di�tist Carezzo) | 2000001123 |
| input - Per Os (Tussendoortje di�tist Vla met verrijkte eiwitten) | 2000001123 |
| input - Per Os (Tussendoortje di�tist shake eiwit +) | 2000001123 |
| input - Per Os (Tussendoortje di�tist ~) | 2000001123 |
| input - Per Os (Vifit) | 2000001123 |
| input - Per Os (Vla  ei+) | 2000001123 |
| input - Per Os (Vla E+) | 2000001123 |
| input - Per Os (Vla Verrijkt) | 2000001123 |
| input - Per Os (Vla achtigen) | 2000001123 |
| input - Per Os (Vla appel, kaneel slagroom) | 2000001123 |
| input - Per Os (Vla choco) | 2000001123 |
| input - Per Os (Vla e+) | 2000001123 |
| input - Per Os (Vla eiwit verrijkt) | 2000001123 |
| input - Per Os (Vla eiwit) | 2000001123 |
| input - Per Os (Vla eiwitverijkt) | 2000001123 |
| input - Per Os (Vla eiwitverrijkt~) | 2000001123 |
| input - Per Os (Vla en Yogurth) | 2000001123 |
| input - Per Os (Vla en+) | 2000001123 |
| input - Per Os (Vla lactosevrij) | 2000001123 |
| input - Per Os (Vla met proteine) | 2000001123 |
| input - Per Os (Vla met slagroom) | 2000001123 |
| input - Per Os (Vla met yoghurt) | 2000001123 |
| input - Per Os (Vla pudding chocolade) | 2000001123 |
| input - Per Os (Vla verrijkt) | 2000001123 |
| input - Per Os (Vla verrijkte) | 2000001123 |
| input - Per Os (Vla zaanse hoeve eiwitrijk) | 2000001123 |
| input - Per Os (Vla+yoghurt) | 2000001123 |
| input - Per Os (Vla/pap/kwark/yoghurt) | 2000001123 |
| input - Per Os (Vla50) | 2000001123 |
| input - Per Os (Vlafilp) | 2000001123 |
| input - Per Os (Vla~ eiwitrijk) | 2000001123 |
| input - Per Os (Vla~ proteine) | 2000001123 |
| input - Per Os (Vla~eiwitrijk) | 2000001123 |
| input - Per Os (Vloeibare maaltijd) | 2000001123 |
| input - Per Os (Vocht bij Medicatie) | 2000001123 |
| input - Per Os (Vocht bij med) | 2000001123 |
| input - Per Os (Vocht bij medciatie) | 2000001123 |
| input - Per Os (Vocht bij mediatie) | 2000001123 |
| input - Per Os (Vocht bij medicatie ) | 2000001123 |
| input - Per Os (Vocht bij methyleenblauw) | 2000001123 |
| input - Per Os (Vocht met medicatie) | 2000001123 |
| input - Per Os (Vruchten yogurth) | 2000001123 |
| input - Per Os (Vruchtenkwark) | 2000001123 |
| input - Per Os (Vulling) | 2000001123 |
| input - Per Os (Warme maalltijd) | 2000001123 |
| input - Per Os (Warme maaltijd 1x) | 2000001123 |
| input - Per Os (Warme maaltijd bloemkool) | 2000001123 |
| input - Per Os (Warme maaltijd ~) | 2000001123 |
| input - Per Os (Warme pap  ~) | 2000001123 |
| input - Per Os (Warme zachte maaltijd) | 2000001123 |
| input - Per Os (Water bij Fresubin) | 2000001123 |
| input - Per Os (Water bij fresubin) | 2000001123 |
| input - Per Os (Water en Fresubin) | 2000001123 |
| input - Per Os (Water met medicatie) | 2000001123 |
| input - Per Os (Water met slimpie) | 2000001123 |
| input - Per Os (Water per os) | 2000001123 |
| input - Per Os (Water per sonde) | 2000001123 |
| input - Per Os (Water, kwark en melk) | 2000001123 |
| input - Per Os (Water/thee/appelsap) | 2000001123 |
| input - Per Os (Waterijs raket) | 2000001123 |
| input - Per Os (Waterijsje ) | 2000001123 |
| input - Per Os (Wil momenteel allen eten van haar man.) | 2000001123 |
| input - Per Os (YoCreme) | 2000001123 |
| input - Per Os (Yoghurt met banaan) | 2000001123 |
| input - Per Os (Yoghurt met musli) | 2000001123 |
| input - Per Os (Yogurth met honing) | 2000001123 |
| input - Per Os (Yogurth) | 2000001123 |
| input - Per Os (Yorhurt + 0% siroop) | 2000001123 |
| input - Per Os (Zoet beleg) | 2000001123 |
| input - Per Os (aa) | 2000001123 |
| input - Per Os (active kool) | 2000001123 |
| input - Per Os (alleen vlees) | 2000001123 |
| input - Per Os (alpro vla) | 2000001123 |
| input - Per Os (alpro yoghurt) | 2000001123 |
| input - Per Os (alprosoya chocolade) | 2000001123 |
| input - Per Os (b oullion) | 2000001123 |
| input - Per Os (babybel kaas) | 2000001123 |
| input - Per Os (beenham) | 2000001123 |
| input - Per Os (bifi worstje) | 2000001123 |
| input - Per Os (blikje cola) | 2000001123 |
| input - Per Os (bosse bol) | 2000001123 |
| input - Per Os (boter) | 2000001123 |
| input - Per Os (boterham met jam en boter) | 2000001123 |
| input - Per Os (boterham met jam) | 2000001123 |
| input - Per Os (botterham met kaas cracker met kaas) | 2000001123 |
| input - Per Os (botterham met kaas en boter) | 2000001123 |
| input - Per Os (boullion) | 2000001123 |
| input - Per Os (brood en 2 crackers) | 2000001123 |
| input - Per Os (brood maaltijd) | 2000001123 |
| input - Per Os (brood met jam en boter) | 2000001123 |
| input - Per Os (brood met kaas 2x) | 2000001123 |
| input - Per Os (brood, koek, ei, kaas, pindakaas) | 2000001123 |
| input - Per Os (broodmaaltijd kaas en jam) | 2000001123 |
| input - Per Os (broodmaaltijd) | 2000001123 |
| input - Per Os (bruine boterham met kaas) | 2000001123 |
| input - Per Os (cappucino) | 2000001123 |
| input - Per Os (capuccino) | 2000001123 |
| input - Per Os (carazzo) | 2000001123 |
| input - Per Os (carezo bosbessen sap) | 2000001123 |
| input - Per Os (carezza) | 2000001123 |
| input - Per Os (carezzo drank) | 2000001123 |
| input - Per Os (carezzo fruit drink) | 2000001123 |
| input - Per Os (carezzo sap) | 2000001123 |
| input - Per Os (carezzo sinas) | 2000001123 |
| input - Per Os (carezzo) | 2000001123 |
| input - Per Os (carezzo+H2O) | 2000001123 |
| input - Per Os (carrezo sap) | 2000001123 |
| input - Per Os (carrezo) | 2000001123 |
| input - Per Os (chocomel proth +) | 2000001123 |
| input - Per Os (cleanprep) | 2000001123 |
| input - Per Os (correctie vochtbalans) | 2000001123 |
| input - Per Os (cup a soup champignon) | 2000001123 |
| input - Per Os (dagdienst) | 2000001123 |
| input - Per Os (dextro 1x) | 2000001123 |
| input - Per Os (dextro 2x) | 2000001123 |
| input - Per Os (div) | 2000001123 |
| input - Per Os (diverse) | 2000001123 |
| input - Per Os (doorspoelen sonde) | 2000001123 |
| input - Per Os (druiven sap) | 2000001123 |
| input - Per Os (eemalig over de sonde) | 2000001123 |
| input - Per Os (ei en ontbijt koek) | 2000001123 |
| input - Per Os (ei+ vla) | 2000001123 |
| input - Per Os (eiwit+ toetje) | 2000001123 |
| input - Per Os (eiwit+toetje) | 2000001123 |
| input - Per Os (eiwitverrijkt appelmoes) | 2000001123 |
| input - Per Os (eiwitverrijkte yoghurtdrank) | 2000001123 |
| input - Per Os (energie verrijkte vla) | 2000001123 |
| input - Per Os (energieverrijkt) | 2000001123 |
| input - Per Os (euthyrox+spoel) | 2000001123 |
| input - Per Os (extra eiwitrijke vla ) | 2000001123 |
| input - Per Os (fanta ) | 2000001123 |
| input - Per Os (flexiseal spoeling) | 2000001123 |
| input - Per Os (fresubin 15  gr) | 2000001123 |
| input - Per Os (fresubin 15 gr) | 2000001123 |
| input - Per Os (fresubin 15gr in water) | 2000001123 |
| input - Per Os (fresubin) | 2000001123 |
| input - Per Os (fristi) | 2000001123 |
| input - Per Os (fruitshake) | 2000001123 |
| input - Per Os (gekookt ei) | 2000001123 |
| input - Per Os (griesmeelpap) | 2000001123 |
| input - Per Os (groenijsje) | 2000001123 |
| input - Per Os (h2o via sonde) | 2000001123 |
| input - Per Os (hagelslag) | 2000001123 |
| input - Per Os (halve beker slush) | 2000001123 |
| input - Per Os (halve maaltijd) | 2000001123 |
| input - Per Os (halve warme maaltijd ) | 2000001123 |
| input - Per Os (hartige pannenkoek) | 2000001123 |
| input - Per Os (havermout en griesmee) | 2000001123 |
| input - Per Os (havermout ~) | 2000001123 |
| input - Per Os (honing 2x) | 2000001123 |
| input - Per Os (ijs met water) | 2000001123 |
| input - Per Os (ijsje ~) | 2000001123 |
| input - Per Os (ijwater) | 2000001123 |
| input - Per Os (intake per os avond 10/7) | 2000001123 |
| input - Per Os (intake tot 11u) | 2000001123 |
| input - Per Os (intake tot 14.00) | 2000001123 |
| input - Per Os (intake vlgs lijst) | 2000001123 |
| input - Per Os (intraveneus vocht) | 2000001123 |
| input - Per Os (isodrank) | 2000001123 |
| input - Per Os (jam, ham, smeerworst) | 2000001123 |
| input - Per Os (juice) | 2000001123 |
| input - Per Os (jus de orange) | 2000001123 |
| input - Per Os (jus de organe) | 2000001123 |
| input - Per Os (kaasbroodje 3/4) | 2000001123 |
| input - Per Os (kaneelbeschuitje) | 2000001123 |
| input - Per Os (kipsate) | 2000001123 |
| input - Per Os (koffie en tussen de middag) | 2000001123 |
| input - Per Os (kol) | 2000001123 |
| input - Per Os (krentenbrood) | 2000001123 |
| input - Per Os (maagretentie retour) | 2000001123 |
| input - Per Os (maagretentie) | 2000001123 |
| input - Per Os (macaroni met kaas) | 2000001123 |
| input - Per Os (manderijn) | 2000001123 |
| input - Per Os (med (oraal)) | 2000001123 |
| input - Per Os (mediatie via de sonde) | 2000001123 |
| input - Per Os (medicatie + water per sonde) | 2000001123 |
| input - Per Os (medicatie + water) | 2000001123 |
| input - Per Os (medicatie de sonde) | 2000001123 |
| input - Per Os (medicatie met water) | 2000001123 |
| input - Per Os (medicatie per os) | 2000001123 |
| input - Per Os (medicatie v ia de sonde) | 2000001123 |
| input - Per Os (medicatie via PEG) | 2000001123 |
| input - Per Os (medicatie via de sonde) | 2000001123 |
| input - Per Os (medicatie+ water) | 2000001123 |
| input - Per Os (medicatiewater) | 2000001123 |
| input - Per Os (medicatiie via de sonde) | 2000001123 |
| input - Per Os (meds (or)) | 2000001123 |
| input - Per Os (meds) | 2000001123 |
| input - Per Os (melk, 2 boterhammen, kaas, appel, manderijn, nutridrink) | 2000001123 |
| input - Per Os (melkunie protein) | 2000001123 |
| input - Per Os (melkunie proteine drink ) | 2000001123 |
| input - Per Os (melkunie proteine shake) | 2000001123 |
| input - Per Os (melkunie proteine) | 2000001123 |
| input - Per Os (melkunie shake) | 2000001123 |
| input - Per Os (movi) | 2000001123 |
| input - Per Os (movicolon/meds) | 2000001123 |
| input - Per Os (nachtdienst) | 2000001123 |
| input - Per Os (ochtend oraal) | 2000001123 |
| input - Per Os (ontbijt koek) | 2000001123 |
| input - Per Os (ontbijtdrink) | 2000001123 |
| input - Per Os (ontbijtkoek) | 2000001123 |
| input - Per Os (oraal ) | 2000001123 |
| input - Per Os (oraal 24u) | 2000001123 |
| input - Per Os (oraal ontbijt/lunch) | 2000001123 |
| input - Per Os (oraal over 24u) | 2000001123 |
| input - Per Os (oraal per 24u) | 2000001123 |
| input - Per Os (oraal) | 2000001123 |
| input - Per Os (orale intake 0.00-24.00 uur) | 2000001123 |
| input - Per Os (orale intake 0.00-24.00uur) | 2000001123 |
| input - Per Os (orale intake 8.00-14.00uur) | 2000001123 |
| input - Per Os (orale intake totaal) | 2000001123 |
| input - Per Os (oranjetompouce) | 2000001123 |
| input - Per Os (overdag per os) | 2000001123 |
| input - Per Os (paar hapjes brood met smeerkaas) | 2000001123 |
| input - Per Os (pannekoek) | 2000001123 |
| input - Per Os (pannekoeken) | 2000001123 |
| input - Per Os (pasta) | 2000001123 |
| input - Per Os (peptamen) | 2000001123 |
| input - Per Os (per os 6.00-24.00) | 2000001123 |
| input - Per Os (per os tot 14u) | 2000001123 |
| input - Per Os (per os) | 2000001123 |
| input - Per Os (perenijsje) | 2000001123 |
| input - Per Os (picco) | 2000001123 |
| input - Per Os (plak kaas) | 2000001123 |
| input - Per Os (plein vue 2) | 2000001123 |
| input - Per Os (plein vue) | 2000001123 |
| input - Per Os (pleinvue) | 2000001123 |
| input - Per Os (portie sv) | 2000001123 |
| input - Per Os (presource) | 2000001123 |
| input - Per Os (pro source) | 2000001123 |
| input - Per Os (proccouse) | 2000001123 |
| input - Per Os (prosource) | 2000001123 |
| input - Per Os (prosure) | 2000001123 |
| input - Per Os (protein advance) | 2000001123 |
| input - Per Os (protein drankje ) | 2000001123 |
| input - Per Os (proteine drank ) | 2000001123 |
| input - Per Os (proteine drank 2) | 2000001123 |
| input - Per Os (proteine drank) | 2000001123 |
| input - Per Os (proteine shake) | 2000001123 |
| input - Per Os (proteine smoothie) | 2000001123 |
| input - Per Os (proteinedrank) | 2000001123 |
| input - Per Os (proteinehap) | 2000001123 |
| input - Per Os (proteinevla) | 2000001123 |
| input - Per Os (prote�ne drink) | 2000001123 |
| input - Per Os (prote�ne shake) | 2000001123 |
| input - Per Os (puree) | 2000001123 |
| input - Per Os (quiche stukje) | 2000001123 |
| input - Per Os (radler 0.0%) | 2000001123 |
| input - Per Os (resource desser gourmond) | 2000001123 |
| input - Per Os (retour retentie) | 2000001123 |
| input - Per Os (rivella ) | 2000001123 |
| input - Per Os (sap water) | 2000001123 |
| input - Per Os (seven up sv) | 2000001123 |
| input - Per Os (shake ) | 2000001123 |
| input - Per Os (shake eiwit energie verrijkt) | 2000001123 |
| input - Per Os (shake ml) | 2000001123 |
| input - Per Os (shortbread) | 2000001123 |
| input - Per Os (siroop) | 2000001123 |
| input - Per Os (sla) | 2000001123 |
| input - Per Os (slokjes water) | 2000001123 |
| input - Per Os (slush) | 2000001123 |
| input - Per Os (smeerworst en komijnenkaas) | 2000001123 |
| input - Per Os (smeerworst, aardbeien jam) | 2000001123 |
| input - Per Os (smeerworst, jam en banaan) | 2000001123 |
| input - Per Os (smeerworst, jam, banaan) | 2000001123 |
| input - Per Os (snoep) | 2000001123 |
| input - Per Os (soft ijsje) | 2000001123 |
| input - Per Os (sonde spoelen) | 2000001123 |
| input - Per Os (sonde voeding) | 2000001123 |
| input - Per Os (sondev) | 2000001123 |
| input - Per Os (sondevoedign) | 2000001123 |
| input - Per Os (sondevoeding ) | 2000001123 |
| input - Per Os (sondevoeding per sonde bolus) | 2000001123 |
| input - Per Os (sondevoeding per sonde) | 2000001123 |
| input - Per Os (spinazie,,puree ,ei) | 2000001123 |
| input - Per Os (spoelen flexiseal ) | 2000001123 |
| input - Per Os (spoelen) | 2000001123 |
| input - Per Os (sportdrank) | 2000001123 |
| input - Per Os (suikerwater) | 2000001123 |
| input - Per Os (sv 225 ml) | 2000001123 |
| input - Per Os (sv 235cc) | 2000001123 |
| input - Per Os (sv multifibre) | 2000001123 |
| input - Per Os (sv portie) | 2000001123 |
| input - Per Os (sv) | 2000001123 |
| input - Per Os (thee + water medicatie) | 2000001123 |
| input - Per Os (thee sap water) | 2000001123 |
| input - Per Os (thee, Cerezzo sap en water) | 2000001123 |
| input - Per Os (tosti ) | 2000001123 |
| input - Per Os (tosti ham/kaas) | 2000001123 |
| input - Per Os (tosti kaas en kipfilet) | 2000001123 |
| input - Per Os (tosti kaas zoder korst met ketchup) | 2000001123 |
| input - Per Os (tosti) | 2000001123 |
| input - Per Os (totaal per os) | 2000001123 |
| input - Per Os (totaal tot nu) | 2000001123 |
| input - Per Os (totaal) | 2000001123 |
| input - Per Os (totale intake ochtend) | 2000001123 |
| input - Per Os (via de sonde) | 2000001123 |
| input - Per Os (via duodenumsonde) | 2000001123 |
| input - Per Os (via sonde) | 2000001123 |
| input - Per Os (vifit) | 2000001123 |
| input - Per Os (vochht bij medicatie) | 2000001123 |
| input - Per Os (vochjt bij medicatie) | 2000001123 |
| input - Per Os (vochllijst 2/4 tot 14 uur) | 2000001123 |
| input - Per Os (vocht avond 6/7) | 2000001123 |
| input - Per Os (vocht bi jmedicatie) | 2000001123 |
| input - Per Os (vocht bij Fresubin) | 2000001123 |
| input - Per Os (vocht bij de medicatie) | 2000001123 |
| input - Per Os (vocht bij fresubin) | 2000001123 |
| input - Per Os (vocht bij med) | 2000001123 |
| input - Per Os (vocht bij med.) | 2000001123 |
| input - Per Os (vocht bij medcatie) | 2000001123 |
| input - Per Os (vocht bij medicatie ) | 2000001123 |
| input - Per Os (vocht bij medicatie en spoelen) | 2000001123 |
| input - Per Os (vocht bij medicatie via sonde) | 2000001123 |
| input - Per Os (vocht bij medicatie) | 2000001123 |
| input - Per Os (vocht bij merdicatie) | 2000001123 |
| input - Per Os (vocht bj medicatie) | 2000001123 |
| input - Per Os (vocht en medicatie) | 2000001123 |
| input - Per Os (vocht in op CCU) | 2000001123 |
| input - Per Os (vocht medicatie) | 2000001123 |
| input - Per Os (vocht met medicatie) | 2000001123 |
| input - Per Os (vocht metmedicatie) | 2000001123 |
| input - Per Os (vocht ochtend) | 2000001123 |
| input - Per Os (vocht orale intake vanaf 14 uur) | 2000001123 |
| input - Per Os (vocht vanaf 10u tot 14u) | 2000001123 |
| input - Per Os (vocht/ medicatie) | 2000001123 |
| input - Per Os (vochtintake 10/7 tot 23 uur) | 2000001123 |
| input - Per Os (vochtintake 4/12  t/m 14 uur) | 2000001123 |
| input - Per Os (vochtintake CCU avond 5/7) | 2000001123 |
| input - Per Os (vochtintake avond) | 2000001123 |
| input - Per Os (vochtintake over de dag) | 2000001123 |
| input - Per Os (vochtintake tot 14 uur) | 2000001123 |
| input - Per Os (vochtintake) | 2000001123 |
| input - Per Os (vochtlijst  10/7 tot 16 uur) | 2000001123 |
| input - Per Os (vochtlijst incompleet) | 2000001123 |
| input - Per Os (vochtlijst) | 2000001123 |
| input - Per Os (voxht bij med) | 2000001123 |
| input - Per Os (voxht bij medicatie) | 2000001123 |
| input - Per Os (vruchtenmoes) | 2000001123 |
| input - Per Os (warme chocomelk) | 2000001123 |
| input - Per Os (warme maaltijd ) | 2000001123 |
| input - Per Os (warme maaltijd en appelmoes) | 2000001123 |
| input - Per Os (warme maaltijd gemalen) | 2000001123 |
| input - Per Os (warme maaltijd: rijst met kipsate) | 2000001123 |
| input - Per Os (warter) | 2000001123 |
| input - Per Os (water ) | 2000001123 |
| input - Per Os (water IJs) | 2000001123 |
| input - Per Os (water bij medicatie) | 2000001123 |
| input - Per Os (water bij meds) | 2000001123 |
| input - Per Os (water en medicatie) | 2000001123 |
| input - Per Os (water over de sonde) | 2000001123 |
| input - Per Os (water over gehele dag) | 2000001123 |
| input - Per Os (water via de sonde) | 2000001123 |
| input - Per Os (water via sonde voor de PCM) | 2000001123 |
| input - Per Os (water via sonde) | 2000001123 |
| input - Per Os (water voor mdicatie) | 2000001123 |
| input - Per Os (water voor med.) | 2000001123 |
| input - Per Os (water voor medicatie) | 2000001123 |
| input - Per Os (water/siroop) | 2000001123 |
| input - Per Os (water/thee) | 2000001123 |
| input - Per Os (waterijsje half) | 2000001123 |
| input - Per Os (witte boterham met dubbel ham) | 2000001123 |
| input - Per Os (witte boterham met dubbel kaas) | 2000001123 |
| input - Per Os (worteltjes) | 2000001123 |
| input - Per Os (zout) | 2000001123 |
| input - Per Os (~ carezzo) | 2000001123 |
| input - Per Os (~ chocomelk) | 2000001123 |
| input - Per Os (~ drinken) | 2000001123 |
| input - Per Os (~ eiwit vereikte vla) | 2000001123 |
| input - Per Os (~ frisdrank) | 2000001123 |
| input - Per Os (~ ml) | 2000001123 |
| input - Per Os (~ uitsmijter) | 2000001123 |
| input - Per Os (~=medicatie) | 2000001123 |
| input - Per Os (~Totaal in 24 uur) | 2000001123 |
| input - Per Os (~appel/sinasappel) | 2000001123 |
| input - Per Os (~boterham met jam) | 2000001123 |
| input - Per Os (~fresubin) | 2000001123 |
| input - Per Os (~medicatie per sonde) | 2000001123 |
| input - Per Os (~medicatie) | 2000001123 |
| input - Per Os (~milkshake) | 2000001123 |
| input - Per Os (~totale intake) | 2000001123 |
| input - Per Os (~vocht bij medicatie) | 2000001123 |
| input - Per Os (~vocht en medicatie) | 2000001123 |

### 3007469 — Breath rate setting Ventilator — 4/21 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| AF totaal;R UMCA ICU VENTILATOR RESPIRATORY RATE  TOTAL | 3007646 |
| Adem frequentie SIMV (ingesteld)HA/SE | 3006306 |
| Ademfreq. | 3024171 |
| Zephyros Frequentie | 3024171 |

### 3008138 — Apache II score — 2/4 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| nice_ap2_orgineel_score | 2000001356 |
| nice_apache_score | 2000001356 |

### 3008152 — Bicarbonate [Moles/volume] in Arterial blood — 1/10 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| HCO3 | 3006576 |

### 3008486 — Thyroxine (T4) free [Moles/volume] in Serum or Plasma — 1/10 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| T4 | 3014620 |

### 3009065 — Inspiration/Expiration setting Ventilator — 2/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Eind exp. druk (2) | 3016226 |
| Eind insp. cyclus (Set) | 3046338 |

### 3009420 — Ganciclovir [Mass/volume] in Serum or Plasma — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Apoth (bloed) Ganciclovir | 40763136 |
| Ganciclovir (bloed) | 40763136 |

### 3010657 — Triiodothyronine (T3) Free [Mass/volume] in Serum or Plasma by Dialysis — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| T3, VRIJ;VRIJ T3 | 3026989 |

### 3011550 — Carboxyhemoglobin [Mass/volume] in Blood — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| CO-Hb (bloed) | 3023081 |

### 3011961 — Ferritin [Mass/volume] in Blood — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Ferritine in bloed | 3001122 |

### 3012410 — Tidal volume setting Ventilator — 1/14 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Vt (Bipap Vision) | 21490752 |

### 3013144 — Glasgow coma score verbal at First encounter — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| V_EMV_NICE_Opname | 2000001376 |

### 3013826 — Glucose [Moles/volume] in Serum or Plasma — 4/4 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| GLUCOSE NUCHTER PLASMA | 46236950 |
| GLUCOSE PLASMA 11 UUR | 46236950 |
| GLUCOSE PLASMA 20 UUR | 46236950 |
| Glucose (afd) in bloed | 46236950 |

### 3014218 — Bicarbonate [Moles/volume] standard in Arterial blood — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| TESTUITSLAG ZONDER AANVRAAG AMC;BICARBONAAT - BLOEDGAS ART. (AMC) | 3008152 |

### 3014308 — Physical findings of Abdomen — 2/3 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Abdomen peristaltiek | 21494966 |
| Peristaltiek | 21494961 |

### 3015182 — Deprecated Erythrocyte distribution width [Entitic volume] by Automated count — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| RDW-SD | 3002888 |

### 3016226 — PEEP Respiratory system — 2/13 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| PEEP/CPAP | 3022875 |
| Zephyros PEEP | 3022875 |

### 3016431 — Calcium.ionized [Moles/volume] adjusted to pH 7.4 in Serum or Plasma — 3/3 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| CA-ION (7.4) | 3048816 |
| CA-ION(7.4) POCT | 3048816 |
| CAION(7.4) ART. VUMC | 3041706 |

### 3016502 — Oxygen saturation in Arterial blood — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| O2-Saturatie (bloed) | 3013502 |

### 3018572 — Chloride [Moles/volume] in Blood — 1/13 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Chloor (overig) | 3013194 |

### 3018677 — aPTT in Platelet poor plasma by Coagulation assay — 8/9 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| APTT  (bloed) | 3013466 |
| APTT (bloed) | 3013466 |
| APTT Ckprest | 3013466 |
| APTT Gecorrigeerd (bloed) | 3013466 |
| OUD_APTT | 3013466 |
| Stolling (s) APTT (11 normaal plasma) | 3013466 |
| Stolling (s) APTT (heparine geneutr) | 3013466 |
| Stolling APTT | 3013466 |

### 3018913 — Phosphate [Moles/volume] in Blood — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Fosfaat in bloed | 3003458 |

### 3019550 — Sodium [Moles/volume] in Serum or Plasma — 9/10 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Chemie Natrium | 3000285 |
| NA (ONV.ISE) | 3000285 |
| NA (ONV.ISE) POCT | 3000285 |
| Na (onv.ISE) (bloed) | 3000285 |
| Na gecorrig. | 3000285 |
| Natrium | 3000285, 3002079, 3022810 |
| Natrium (bloed) | 3000285 |
| Natrium Astrup | 3000285 |
| Natrium;R RUMC IVAZ SODIUM | 3000285 |

### 3020460 — C reactive protein [Mass/volume] in Serum or Plasma — 7/7 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| C-REACTIEF PROTEÏNE (CRP) | 1091617 |
| C.REACT PR (overig) | 3035320 |
| CRP | 1091617 |
| CRP (POC) | 1091617 |
| CRP (bloed) | 1091617 |
| CRP (overig) | 3035320 |
| Chemie CRP | 1091617 |

### 3020564 — Creatinine [Moles/volume] in Serum or Plasma — 1/10 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Kreatinine (Jaff?) (overig) | 3037459 |

### 3020891 — Body temperature — 1/20 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Temperatuur Plaats 1 | 3024265 |

### 3021119 — Calcium.ionized [Moles/volume] in Blood — 2/10 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| CA++(7.4) Astrup | 3048816 |
| Ca-ion (7.4) (bloed) | 3048816 |

### 3021589 — Normoblasts [#/volume] in Blood — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Blasten abs (bloed) | 3005105 |

### 3022217 — INR in Platelet poor plasma by Coagulation assay — 7/8 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| INR | 3032080 |
| INR DEC. | 3032080 |
| INR trombosedienst | 3032080 |
| PROTHROMBINETIJD | 3032080 |
| Prothrombinetijd  (bloed) | 3032080 |
| Prothrombinetijd (bloed) | 3032080 |
| Stolling PT-INR (OAS) | 3032080 |

### 3022875 — Positive end expiratory pressure setting Ventilator — 4/23 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| CPAP (Bipap Vision) | 3035167 |
| EPAP | 2000001555 |
| Ventilator Gemeten Druk PEEP (CPAP) | 3016226 |
| Ventilator Instellingen Handmatig PEEPtot Gecontroleerd | 42527140 |

### 3024128 — Bilirubin.total [Mass/volume] in Serum or Plasma — 1/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Bil. totaal | 3006140 |

### 3024561 — Albumin [Mass/volume] in Serum or Plasma — 2/13 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| ALB.CHEM (overig) | 3002000 |
| ALB.FR. (bloed) | 3007424 |

### 3024731 — MCV [Entitic mean volume] in Red Blood Cells — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Hematologie (s) Macrocytaire RBC's | 2000001415 |

### 3024928 — Oxygen saturation in Venous blood — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| SV02;R UMCA AN SVO2 | 3018465 |

### 3024929 — Platelets [#/volume] in Blood by Automated count — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Trombocyten | 3007461 |

### 3025315 — Body weight — 1/19 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| weight | 2000001235 |

### 3025643 — Ethanol [Mass/volume] in Blood — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Apoth (bloed) Ethanol | 3012920 |
| ETHANOL;ETHANOL CHEMIE | 3012920 |

### 3026019 — Glasgow coma score eye opening at First encounter — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| E_EMV_NICE_Opname | 2000001374 |

### 3026549 — Glasgow coma score motor at First encounter — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| M_EMV_NICE_Opname | 2000001377 |

### 3026892 — Breath rate spontaneous --on ventilator — 1/6 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Adem frequentie Beademing Spontaan + beade(gemeten)OM | 3007646 |

### 3027315 — Oxygen [Partial pressure] in Blood — 1/11 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| PaO2 mmHg (converted from kPa);R UMCA IC PAO2 MMHG LAB WAARDE NICE FORMULA | 3027801 |

### 3029790 — Creatine kinase.MB [Enzymatic activity/volume] in Serum or Plasma — 1/3 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| CKMB MASSA | 3005785 |

### 3030905 — Deprecated Polymorphonuclear cells [#/volume] in Blood — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Polynucleaire cellen | 3035715 |

### 3032948 — Heparin induced platelet Ab [Presence] in Serum — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Anti heparine/PF4 (HIT scr) | 40760871 |

### 3033836 — Magnesium [Moles/volume] in Blood — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Magnesium in bloed | 3012095 |

### 3034976 — Hematocrit [Volume Fraction] of Venous blood by calculation — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Ht(v.Bgs) (bloed) | 3009542 |

### 3035167 — Continuous positive airway pressure Respiratory system — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Continuous Positive Airway Pressure - Masker | 605914 |

### 3035357 — Carbon dioxide [Partial pressure] in Exhaled gas --at end expiration — 2/21 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| ETCO2;R UMCA AN ETCO2 | 3017485 |
| EtCO2 (%) | 3017485 |

### 3036277 — Body height — 1/8 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| length | 2000001233 |

### 3039856 — Temperature of Skin — 1/9 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Temperatuur lies | 1259509 |

### 3042082 — Confusion Assessment Method (CAM) — 26/35 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Aandacht (RASS niet 0);R RUMC CAM ICU VERSIE 2 SAVEAHAART RASS NIET 0 STAP 3 | 2000001025 |
| CAM Score - aandacht vasthouden - auditieve test | 2000001025 |
| CAM Score - aandacht vasthouden - visuele test | 2000001025 |
| CAM Score - acute wijziging in mentale status | 2000001352 |
| CAM-ICU auditieve test | 2000001025 |
| CAM-ICU fluctuerend beloop | 2000001352 |
| CAM-ICU ongeorganiseerd denken opdrachten | 2000001024 |
| CAM-ICU ongeorganiseerd denken vragen | 2000001024 |
| Delirant afgelopen 24h;R RUMC CAM ICU VERSIE 2 DELIRANT GEWEEST | 2000001351 |
| Delirant bij opname?;R RUMC CAM ICU VERSIE 2  LAST SCORE DELIER <72H | 2000001353 |
| Formulier CAM-ICU Acute Verandering In Functioneren | 2000001352 |
| Formulier CAM-ICU Bewustzijn Anders dan Alert | 2000001056 |
| Formulier CAM-ICU Fluctuatie In Funtioneren | 2000001352 |
| Formulier CAM-ICU Gestoorde Aandacht | 2000001025 |
| Formulier CAM-ICU Incoherent Denken | 2000001024 |
| Ongeorganiseerd denken;R RUMC CAM ICU VERSIE 2 ONGEORGANISEERD DENKEN STAP 5 | 2000001024 |
| Psychomotorische agitatie of vertraging;R RUMC CAM ICU VERSIE 3 (AANVULLING) - VRAAG 5 (ASE) | 2000000981 |
| Punten aandacht;R RUMC CAM ICU VERSIE 3 PUNTEN AANDACHT | 2000001025 |
| Punten ongeorganiseerd denken;R RUMC CAM ICU VERSIE 3 PUNTEN ONGEORGANISEERD DENKEN | 2000001024 |
| Punten veranderd bewustzijn;R RUMC CAM ICU VERSIE 3 PUNTEN VERANDERD BEWUSTZIJN | 2000001056 |
| Stap 3: Opdracht uitvoeren;R UMCN CAM-ICU OPDRACHT | 2000001391 |
| Stap 4: Aandacht (RASS niet 0);R UMCN CAM-ICU SAVEAHAART RASS NIET 0 | 2000001025 |
| Symptoom schommelingen;R RUMC CAM ICU VERSIE 3 (AANVULLING) - VRAAG 8 (ASE) | 2000000987 |
| Veranderd bewustzijn;R RUMC CAM ICU VERSIE 2 VERANDERING BEWUSTZIJN | 2000001056 |
| Veranderd bewustzijnsniveau;R RUMC CAM ICU VERSIE 3 (AANVULLING) - VRAAG 1 (ASE) | 2000000993 |
| Veranderde cognitie;R RUMC CAM ICU VERSIE 2 COGNITIE | 2000001352 |

### 3043148 — Breath rate mechanical --on ventilator — 1/6 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| SIMV Frequentie (Set) | 3006306 |

### 3043995 — Bilirubin.conjugated+indirect [Moles/volume] in Serum or Plasma — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| BILI-TOTAAL (BLOED) AMC | 3006140 |
| Bili Totaal | 3006140 |

### 3045410 — Minute volume setting Ventilator — 2/11 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| AMVinsp ;R UMCA ICU VENTILATOR MINUUT VOLUME INSP | 21490754 |
| MinVent | 21490753 |

### 3047181 — Lactate [Moles/volume] in Blood — 1/15 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Lactaat (overig) | 3004825 |

### 4096152 — Exploratory thoracotomy — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Rethoracotomie zonder extracorporale circulatie tijdens dezelfde opname. | 2000001236 |

### 4158569 — Emergency procedure — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| NIV | 4177224 |

### 4178391 — Heat and moisture exchanger — 1/3 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Luchtweg Spreekklepje | 4256899 |

### 4201025 — High concentration oxygen therapy — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Optiflow ~ | 3655950 |

### 4337734 — Tracheobronchial lavage — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Bronchiaal toilet | 4239191 |

### 19005147 — methotrimeprazine — 2/3 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| LEVOMEPROMAZINE 12,5 MG/ML INJECTIE IN NACL 0,9% | 36850940 |
| LEVOMEPROMAZINE 25 MG/ML INJECTIE INTRAMUSCULAIR | 36850940 |

### 19014215 — sodium lauryl sulfoacetate — 2/4 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| NATRIUMLAURYLSULF/SORBITOL KLY 9/625MG/ML FL  5ML | 2000001225 |
| NATRIUMLAURYLSULFOACET/SORBITOL KLYSMA 9/625MG/ML | 2000001225 |

### 19031397 — dipyrone — 2/3 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| metamizol | 36854851 |
| metamizol injvlst 500mg/ml | 36854851 |

### 19050104 — carnitine — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| I-Carnitine (Carnitine) | 1553610 |

### 19080406 — anti-inhibitor coagulant complex — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| PROTROMBINECOMPLEX GEACTIVEERD (FEIBA) 1000 IE INJECTIEPOEDER ONOPGELOST (KLINIEK) (AMC) | 36029629 |
| PROTROMBINECOMPLEX GEACTIVEERD (FEIBA) BOLUS | 36029629 |

### 19080512 — articaine — 4/4 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| ARTICAINE/ADRE INJV 40/0,01MG/ML (HCL) PATR 1,7ML | 36030108 |
| ARTICAINE/ADRE INJV 40/0,01MG/ML (TAR) PATR 1,8ML | 36030108 |
| ARTICAINE/ADRENALINE INJV 40/0,01MG/ML PATR 1,7ML | 36030108 |
| ARTICAINE/ADRENALINE INJV 40/0,01MG/ML PATR 1,8ML | 36030108 |

### 19095164 — cholecalciferol — 1/24 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| COLECALCIFEROL DRANK  50.000IE=10ML FL (5000IE/ML) | 19009405 |

### 19113045 — heparinoids — 1/3 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| HEPARINE 25000 ie/50 ml (500 ie/ml) | 1367571 |

### 21490588 — Esophageal temperature — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| T Kern;R UMCA AN T CORE | 3025926 |

### 21490671 — Aorta blood pressure — 1/4 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Ao;(systolic) | 21490674 |

### 21490696 — Oxygen [VFr/PPres] Gas delivery system — 2/13 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| FiO2 % | 3020716 |
| Zephyros O2i | 3020716 |

### 21490724 — Inspiration/Expiration time Ratio — 2/11 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| I:E Ratio (Insp);R UMCA ICU VENTILATOR I:E RATIO INSP S | 3009065 |
| I:E Ratio (exp);R UMCA ICU VENTILATOR I:E RATIO EXP S | 3009065 |

### 21490752 — Tidal volume expired Respiratory system airway — 1/6 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Ventilator Gemeten Expired Minute Volume Exp | 21490753 |

### 21490753 — Volume expired per minute Respiratory system — 2/13 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Exp flow (l/min);R UMCA ICU VENTILATOR EXPIRATOIRE FLOW S | 21490558 |
| MVe Spontaan nieuw | 4108000 |

### 21490850 — Invasive Blood pressure — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Arteriële bloeddruk | 21490853 |

### 21490854 — Tidal volume Ventilator --on ventilator — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| TV (ml);R UMCA ICU VENTILATOR TIDAL VOLUME S | 3012410 |

### 21490855 — PEEP Respiratory system --on ventilator — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| PEEP;R MCL BEADEMING PEEP/CPAP | 3022875 |

### 21492238 — Blood pressure by Noninvasive — 1/11 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Non-invasive Blood Pressure | 21492239 |

### 21493512 — Coagulation factor X activated inhibitor [Mass/volume] in Platelet poor plasma — 1/4 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Anti Fxa  (bloed) | 4094438 |

### 35198180 — acetated ringer's solution(with glucose) — 4/4 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| RINGER INFUSIEVLOEISTOF (USP) ZAK 500ML -BOLUS- | 40166954 |
| RINGER/LACTAAT INFVLST (BRAUN/FRESENIUS) ZAK* | 40166954 |
| Ri-Lac (Ringers lactaat) | 40166954 |
| Ringer lactaat | 40166954 |

### 35884360 — Heparin Sodium — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| HEPArine natrium (Heparine -leo-) | 1367571 |
| Heparine Na | 1367571 |

### 36303816 — Tidal volume.inspired — 2/14 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| TV_ingest (liters)DE/DC | 3012410 |
| TV_ingest (ml)HA/OM | 3012410 |

### 36304672 — Inspiratory time setting Ventilator — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Ti (sec) nieuw | 3043415 |

### 36852771 — LANDIOLOL — 2/3 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| LANDIOLOL SPUIT VOOR POMP 6 MG/ML (ONVERDUND) | 35197852 |
| LANDIOLOLHYDROCHLORIDE 6MG/ML SPUITENPOMP | 35197852 |

### 36861661 — HUMAN PLASMA — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Omniplasma | 4103791 |

### 36879118 — human platelets — 6/6 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| TROMBOCYTEN 330 ml | 4103615 |
| TROMBOCYTEN 350 ml | 4103615 |
| Thrombo's (1 U = 5 donoren trombocyten) | 4103615 |
| Thrombocyten (bestraald) (1 U = 5 donoren trombocyten) | 4103615 |
| Thrombocyten suspensie | 4103615 |
| trombo transfusie | 4103615 |

### 40760768 — Flow trigger setting Ventilator — 2/11 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Trigger ingesteld  (thuisbeademing) | 36305890 |
| Triggergevoeligheid (Set) (2) | 36305890 |

### 40762351 — Hemoglobin [Moles/volume] in Blood — 2/16 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| HB IN PLASMA | 3024340 |
| Hgb;R UMCA PERF HGB | 3000963 |

### 40762387 — Lacosamide [Mass/volume] in Blood — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Lacosamide | 40762388 |

### 40763164 — OLANZapine [Mass/volume] in Blood — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Apoth (bloed) Olanzapine | 3021494 |

### 42709324 — vitamin D3 — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| TOPPHARM VITAMINE D3 KAUWTABLET 10MCG | 19095164 |
| VITAMINE D3 PROVIFORM TABLET 50MCG | 19095164 |

### 42870551 — Thromboelastography after addtion of heparinase panel - Blood — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| CT heptem | 3039608 |

### 43013090 — isoprene — 2/3 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| ISOPRENALINE 5 mg/50 ml (0,1 mg/ml) | 1183554 |
| ISOprenaline | 1183554 |

### 44122511 — factor IX complex / factor VII / Factor VIII / factor X / Prothrombin Injectable Suspension [Feiba] — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| PROTROMBINECOMPLEX INJPDR 500IE F TOEB | 36029629 |

### 44507865 — prothrombin — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| PROTROMBINECOMPLEX 25IE/ML SPUITENPOMP (BERIPLEX) | 36029629 |

### 44785020 — factor VII — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Recomb Factor VII (Novoseven) | 1352141 |

### 45892599 — ceftolozane — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| CEFTOLOZAAN/TAZOBACTAM INFUSIEPOEDER 1000/500MG FL | 778933 |

### 2000000002 — Apache IV score — 3/5 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| apache_score | 2000001358 |
| nice_ap4_score | 2000001357 |
| nice_apache_score | 2000001356 |

### 2000000124 — Cardiac function index by PiCCO — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Cardiac Index (picco) | 21490712 |

### 2000000144 — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Hb poct (bloed) | 40762351 |

### 2000000145 — Hemoglobin [Moles/volume] in Mixed venous blood — 1/4 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| TESTUITSLAG ZONDER AANVRAAG AMC;GERED.-HB - BLOEDGAS GEM. VEN. (AMC) | 3022023 |

### 2000000171 — Tracheostomy insertion time — 1/3 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Tracheostomie registratie - Datum ingreep | 4168133 |

### 2000000187 — Backup apnea interval — 1/3 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| NIV Backup Ti (Set) | 36304672 |

### 2000000190 — Inspiratory positive airway pressure setting — 1/5 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| PIP | 36306157 |

### 2000000191 — Low pressure setting Ventilator (BIPAP, APRV) — 1/2 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| EPAP (set);R MCL BEADEMING EPAP (SET) | 2000001555 |

### 2000000209 — Inspiratory pressure above PEEP set — 7/12 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| PC boven PEEP (Set) | 2000001385 |
| PS boven PEEP (Set) | 2000001382 |
| PS boven Peep (set);R MCL BEADEMING PS ABOVE PEEP (SET) | 2000001382 |
| Pcontrol (ingesteld)HA/MA | 2000001386 |
| Pcontrol;R UMCA ICU VENTILATOR PC S | 2000001385 |
| Pressure Control - Above PEEP - Set | 2000001385 |
| Pressure control             [cmH2O];R UMCN PRESSURE CONTROL | 2000001385 |

### 2000000211 — Inspiratory pressure above PEEP — 2/3 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Pressure Support - Above PEEP - Set | 2000001382 |
| Psupport above Pinsp;R UMCA ICU VENTILATOR PS ABOVE PINSP | 2000001382 |

### 2000000212 — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Respiratie Berekend Automatische Meetwaarde Pinsp | 2000001388 |
| Ventilator Gemeten Pinsp | 2000000210 |

### 2000000213 — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| PIP ;R UMCN ANE PIP INGESTELD | 2000001389 |
| Pressure Control - Set | 2000001385 |

### 2000000238 — Vent mechanics peak airway pressure — 2/11 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Piek druk | 36306157 |
| Piek druk (2) | 36306157 |

### 2000000486 — Chest drain air leakage — 1/22 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| TV Lucht Lekkage (gemeten)HA | 42868487 |

### 2000000574 — 22/22 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| CELLSAVER BLOED 200 ml | 4129595 |
| CELLSAVER BLOED 225 ml | 4129595 |
| CELLSAVER BLOED 230 ml | 4129595 |
| CELLSAVER BLOED 240 ml | 4129595 |
| CELLSAVER BLOED 250 ml | 4129595 |
| CELLSAVER BLOED 300 ml | 4129595 |
| CELLSAVER BLOED 350 ml | 4129595 |
| CELLSAVER BLOED 400 ml | 4129595 |
| CELLSAVER BLOED 420 ml | 4129595 |
| CELLSAVER BLOED 425 ml | 4129595 |
| CELLSAVER BLOED 450 ml | 4129595 |
| CELLSAVER BLOED 460 ml | 4129595 |
| CELLSAVER BLOED 480 ml | 4129595 |
| CELLSAVER BLOED 500 ml | 4129595 |
| CELLSAVER BLOED 550 ml | 4129595 |
| CELLSAVER BLOED 600 ml | 4129595 |
| CELLSAVER BLOED 650 ml | 4129595 |
| CELLSAVER BLOED 700 ml | 4129595 |
| CELLSAVER BLOED 800 ml | 4129595 |
| CELLSAVER BLOED 900 ml | 4129595 |
| CELLSAVER BLOED 925 ml | 4129595 |
| Cellsaver bloed | 4129595 |

### 2000000583 — 11/11 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Bestraalde ery's | 4336080 |
| ERYTROCYTEN | 3020416, 3027017, 4336080 |
| ERYTROCYTEN 0,1 ml | 4336080 |
| ERYTROCYTEN 280 ml | 4336080 |
| ERYTROCYTEN 288 ml | 4336080 |
| ERYTROCYTEN 3007655801,5 ml | 4336080 |
| Gefiltreerde Ery's | 4336080 |
| Gefiltreerde ery's | 4336080 |
| Gefiltreerde erytrocyten | 4336080 |
| Packed cells (niet gefiltreerd) | 4336080 |
| erythrocyten transfusie | 4336080 |

### 2000000591 — 6/6 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| FFP transfusie | 4103791 |
| FRESH FROZEN PLASMA | 4103791 |
| FRESH FROZEN PLASMA 0,1 ml | 4103791 |
| FRESH FROZEN PLASMA 200 ml | 4103791 |
| Gepasteuriseerd plasma (GPO) | 4103791 |
| Quarantaine Plasma | 4103791 |

### 2000000628 — 6/6 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| ASB | 2000001383 |
| ASB (ingesteld)DC/DE | 2000001383 |
| Assisted Spontaneous Breathing - Set | 2000001383 |
| Pressure Support (ingesteld)HA/OM/MA | 2000001382 |
| Pressure Support - Set | 2000001382 |
| Pressure support [cmH2O];R UMCN PRESSURE SUPPORT | 2000001382 |

### 2000000635 — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Luchtlekkage (ml) | 42868487 |

### 2000000656 — ICU specialty — 1/4 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| ref_spec | 2000001234 |

### 2000000657 — ICU admission type — 1/7 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| adm_type | 2000001131 |

### 2000000662 — History of diabetes — 3/6 parameters remapped

| Parameter | Now maps to |
| --- | --- |
| Diabetes;R UMCN ICU OPNAME CHRONISCHE DIAGNOSE DIABETES | 2000001345 |
| Diagn_diabetes | 2000001345 |
| diabetes | 2000001345 |

### 2000000663 — 3/3 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| COPD;R UMCN ICU OPNAME CHRONISCHE DIAGNOSE COPD | 2000001346 |
| Diagn_resp_insuf | 2000001150 |
| resp_insuf | 2000001150 |

### 2000000664 — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Diagn_cardio_vasc_insuf | 2000001303 |
| cardio_vasc_insuf | 2000001303 |

### 2000000665 — 3/3 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Cirrhose;R UMCN ICU OPNAME CHRONISCHE DIAGNOSE CIRRHOSIS | 2000001147 |
| Diagn_cirrhosis | 2000001147 |
| cirrhosis | 2000001147 |

### 2000000666 — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Diagn_neoplasm | 2000001146 |
| neoplasm | 2000001146 |

### 2000000667 — 3/3 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Diagn_hem_malign | 2000001350 |
| Hematologische maligniteit;R UMCN ICU OPNAME CHRONISCHE DIAGNOSE HEM_MALIGN | 2000001350 |
| hem_malign | 2000001350 |

### 2000000668 — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Diagn_imm_insuf | 2000001148 |
| imm_insuf | 2000001148 |

### 2000000669 — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| mech_ventil_0 | 2000001156 |

### 2000000671 — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| mech_ventil_24 | 2000001155 |

### 2000000911 — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Canule fixatie zorg;R TRACHEACANULE FIXATIE | 4295069 |

### 2000000950 — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Sofa PaO2 mmHg interval;R UMCA SOFA PAO2 MMHG INTERVAL | 2000001361 |

### 2000000951 — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| Sofa pH interval;R UMCA SOFA PH INTERVAL | 2000001362 |

### 2000000956 — 2/2 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| P/F;R MCL IC PAO2/FIO2 | 3029880 |
| Sofa PaO2/FiO2 ratio onbeademd mmHg interval;R UMCA SOFA PAO2/FIO2 RATIO ONBEADEMD INTERVAL | 2000001292 |

### 2000000990 — Intensive Care Delirium Screening Checklist result — 1/1 parameters remapped · **INVALIDATED**

| Parameter | Now maps to |
| --- | --- |
| ICDSC - Score 24h | 1447893 |

