# ICUdata v0.2.0
**Date:** 2026-06-28 | **Previous:** v0.1.0 | **Hospitals:** amc, aumc, cze, mcl, olvg, radboud, sfg, umcu, vumc | **Tables:** 18

## Hospitals Added

| Hospital | Tables |
|----------|--------|
| mcl | death, device_exposure, drug_exposure, measurement, observation, person, visit_occurrence |
| radboud | care_site, death, device_exposure, drug_exposure, measurement, observation, person, visit_occurrence |
| sfg | care_site, condition_occurrence, death, device_exposure, drug_exposure, measurement, observation, person, procedure_occurrence, visit_occurrence |

## Schema Changes

| Table | Change | Columns |
|-------|--------|---------|
| concept_ancestor | Added | schema |
| concept_ancestor | Removed | spark_schema |
| concept_ancestor | Type changed | ancestor_concept_id: INT32 → INT64 |
| concept_ancestor | Type changed | descendant_concept_id: INT32 → INT64 |
| concept_ancestor | Type changed | max_levels_of_separation: INT32 → INT64 |
| concept_ancestor | Type changed | min_levels_of_separation: INT32 → INT64 |
| concept_class | Added | schema |
| concept_class | Removed | spark_schema |
| concept_class | Type changed | concept_class_concept_id: INT32 → INT64 |
| concept_relationship | Added | schema |
| concept_relationship | Removed | spark_schema |
| concept_relationship | Type changed | concept_id_1: INT32 → INT64 |
| concept_relationship | Type changed | concept_id_2: INT32 → INT64 |
| concept_relationship | Type changed | invalid_reason: BYTE_ARRAY → INT32 |
| concept_relationship | Type changed | valid_end_date: INT32 → INT64 |
| concept_relationship | Type changed | valid_start_date: INT32 → INT64 |
| concept_synonym | Added | schema |
| concept_synonym | Removed | spark_schema |
| concept_synonym | Type changed | concept_id: INT32 → INT64 |
| concept_synonym | Type changed | language_concept_id: INT32 → INT64 |
| domain | Added | schema |
| domain | Removed | spark_schema |
| domain | Type changed | domain_concept_id: INT32 → INT64 |
| relationship | Added | schema |
| relationship | Removed | spark_schema |
| relationship | Type changed | defines_ancestry: INT32 → INT64 |
| relationship | Type changed | is_hierarchical: INT32 → INT64 |
| relationship | Type changed | relationship_concept_id: INT32 → INT64 |

## Concept Changes

| Change | Table | Concept ID | Concept Name | Vocabulary |
|--------|-------|-----------|--------------|------------|
| Added | drug_exposure | 515671 | Neisseria meningitidis | RxNorm |
| Added | drug_exposure | 528295 | Neisseria meningitidis serogroup C capsular polysaccharide diphtheria toxoid protein conjugate vaccine | RxNorm |
| Added | drug_exposure | 528986 | Streptococcus pneumoniae serotype 14 capsular antigen diphtheria CRM197 protein conjugate vaccine | RxNorm |
| Added | drug_exposure | 586491 | cytomegalovirus immune globulin | RxNorm |
| Added | device_exposure | 605799 | Tracheostomy tube cannula | SNOMED |
| Added | device_exposure | 605914 | Continuous positive airway pressure bilevel positive airway pressure face mask | SNOMED |
| Added | measurement | 606289 | 6 minute walk test distance | SNOMED |
| Added | drug_exposure | 701322 | memantine | RxNorm |
| Added | measurement | 722043 | Critical Care Pain Observation Tool (CPOT): Total score | OMOP Extension |
| Added | measurement | 722052 | Critical Care Pain Observation Tool (CPOT): Muscle tension score | OMOP Extension |
| Added | measurement | 722060 | Critical Care Pain Observation Tool (CPOT): Vocalization score | OMOP Extension |
| Added | drug_exposure | 742185 | atomoxetine | RxNorm |
| Added | drug_exposure | 742594 | trichloroacetaldehyde | RxNorm |
| Added | drug_exposure | 756018 | fluphenazine | RxNorm |
| Added | drug_exposure | 778797 | amylase / lipase / pancreatin / protease | RxNorm |
| Added | drug_exposure | 778873 | Streptococcus pneumoniae serotype 1 capsular antigen diphtheria CRM197 protein conjugate vaccine / Streptococcus pneumoniae serotype 14 capsular antigen diphtheria CRM197 protein conjugate vaccine / Streptococcus pneumoniae serotype 18C capsular antige... | RxNorm |
| Added | drug_exposure | 778948 | insulin degludec / liraglutide | RxNorm |
| Added | drug_exposure | 779231 | cranberry seed extract | RxNorm |
| Added | drug_exposure | 792777 | varicella zoster virus glycoprotein E | RxNorm |
| Added | drug_exposure | 792993 | benralizumab | RxNorm |
| Added | drug_exposure | 794147 | maprotiline | RxNorm |
| Added | drug_exposure | 903893 | emedastine | RxNorm |
| Added | drug_exposure | 904356 | methenamine | RxNorm |
| Added | drug_exposure | 908523 | mineral oil | RxNorm |
| Added | drug_exposure | 908921 | calcipotriene | RxNorm |
| Added | drug_exposure | 910888 | cysteamine | RxNorm |
| Added | drug_exposure | 911891 | fiber | RxNorm |
| Added | drug_exposure | 915855 | olopatadine | RxNorm |
| Added | drug_exposure | 915935 | pimecrolimus | RxNorm |
| Added | drug_exposure | 916282 | olsalazine | RxNorm |
| Added | drug_exposure | 925636 | oxymetazoline | RxNorm |
| Added | drug_exposure | 932815 | levobunolol | RxNorm |
| Added | drug_exposure | 934075 | azelastine | RxNorm |
| Added | drug_exposure | 935529 | benoxinate | RxNorm |
| Added | drug_exposure | 939881 | capsaicin | RxNorm |
| Added | drug_exposure | 948487 | polyethylene glycol 300 | RxNorm |
| Added | drug_exposure | 951279 | prilocaine | RxNorm |
| Added | drug_exposure | 954853 | flavoxate | RxNorm |
| Added | drug_exposure | 974140 | hydrochloric acid | RxNorm |
| Added | drug_exposure | 977421 | rimexolone | RxNorm |
| Added | drug_exposure | 979096 | zinc acetate | RxNorm |
| Added | drug_exposure | 981691 | imiquimod | RxNorm |
| Added | drug_exposure | 985247 | aluminum hydroxide | RxNorm |
| Added | drug_exposure | 986790 | azelate | RxNorm |
| Added | drug_exposure | 990499 | sodium phosphate, monobasic | RxNorm |
| Added | drug_exposure | 994341 | meclizine | RxNorm |
| Added | drug_exposure | 996625 | fluorescein | RxNorm |
| Added | measurement | 1002216 | Hemoglobin [Moles/volume] in Venous blood | LOINC |
| Added | observation | 1073572 | Rotational thromboelastometry technique | SNOMED |
| Added | measurement | 1091049 | Amphetamine [Presence] in Urine | LOINC |
| Added | measurement | 1091075 | Enterovirus RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 1091136 | Microscopic observation [Identifier] in Specimen | LOINC |
| Added | measurement | 1091160 | Enterovirus RNA [Presence] in Sputum by NAA with probe detection | LOINC |
| Added | measurement | 1091174 | Human metapneumovirus RNA [Presence] in Specimen by Molecular genetics method | LOINC |
| Added | measurement | 1091199 | SARS-CoV-2 (COVID-19) RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 1091289 | Parainfluenza virus 2 RNA [Presence] in Specimen by Molecular genetics method | LOINC |
| Added | measurement | 1091495 | Parainfluenza virus 4 RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 1091559 | Human coronavirus RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 1091660 | Rhinovirus RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 1091836 | Parainfluenza virus 1 RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 1092022 | Parainfluenza virus 4 RNA [Presence] in Specimen by Molecular genetics method | LOINC |
| Added | measurement | 1092055 | Human bocavirus DNA [Presence] in Nasopharynx by NAA with probe detection | LOINC |
| Added | measurement | 1092086 | Parechovirus RNA [Presence] in Nasopharynx by NAA with probe detection | LOINC |
| Added | measurement | 1092158 | Clostridioides difficile toxin genes [Presence] in Stool by Molecular genetics method | LOINC |
| Added | measurement | 1092215 | Amorphous sediment [Presence] in Urine sediment | LOINC |
| Added | measurement | 1092251 | Bacteria identified in Bronchoalveolar lavage by Culture | LOINC |
| Added | measurement | 1092255 | Campylobacter sp DNA [Identifier] in Stool by NAA with probe detection | LOINC |
| Added | measurement | 1092289 | Mycoplasma pneumoniae DNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 1092347 | Parainfluenza virus 2 RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 1092357 | Rhinovirus RNA [Presence] in Sputum by NAA with probe detection | LOINC |
| Added | drug_exposure | 1112807 | aspirin | RxNorm |
| Added | drug_exposure | 1113648 | nabumetone | RxNorm |
| Added | drug_exposure | 1116031 | zolmitriptan | RxNorm |
| Added | drug_exposure | 1119510 | dextromethorphan | RxNorm |
| Added | drug_exposure | 1135710 | phenylbutazone | RxNorm |
| Added | drug_exposure | 1136980 | ketorolac | RxNorm |
| Added | drug_exposure | 1146633 | remimazolam | RxNorm |
| Added | drug_exposure | 1146810 | piroxicam | RxNorm |
| Added | drug_exposure | 1152631 | cromolyn | RxNorm |
| Added | drug_exposure | 1156378 | flurbiprofen | RxNorm |
| Added | measurement | 1175790 | Dipeptidyl aminopeptidase-like protein 6 Ab [Presence] in Cerebral spinal fluid by Cell binding immunofluorescent assay | LOINC |
| Added | measurement | 1175969 | NMDAR subunit 1 Ab [Presence] in Cerebral spinal fluid by Cell binding immunofluorescent assay | LOINC |
| Added | measurement | 1175984 | Myelin oligodendrocyte glycoprotein IgG1 Ab [Presence] in Serum or Plasma by Flow cytometry (FC) | LOINC |
| Added | measurement | 1176096 | Amphiphysin Ab [Presence] in Cerebral spinal fluid by Immunofluorescence | LOINC |
| Added | measurement | 1176263 | PCA-1 Ab [Presence] in Cerebral spinal fluid by Immunofluorescence | LOINC |
| Added | measurement | 1176364 | PCA-Tr Ab [Presence] in Cerebral spinal fluid by Immunofluorescence | LOINC |
| Added | drug_exposure | 1188114 | dexchlorpheniramine | RxNorm |
| Added | measurement | 1259611 | SARS-CoV-2 (COVID-19) RNA [Presence] in Respiratory system specimen | LOINC |
| Added | measurement | 1259612 | Oxygen consumption (VO2) --peak | LOINC |
| Added | drug_exposure | 1305637 | methylergonovine | RxNorm |
| Added | drug_exposure | 1315027 | cranberry preparation | RxNorm |
| Added | drug_exposure | 1315286 | nilutamide | RxNorm |
| Added | drug_exposure | 1319193 | gefitinib | RxNorm |
| Added | drug_exposure | 1319998 | acebutolol | RxNorm |
| Added | drug_exposure | 1327256 | treprostinil | RxNorm |
| Added | drug_exposure | 1329415 | dinoprostone | RxNorm |
| Added | drug_exposure | 1336539 | sunitinib | RxNorm |
| Added | drug_exposure | 1337620 | capecitabine | RxNorm |
| Added | drug_exposure | 1343039 | triptorelin | RxNorm |
| Added | drug_exposure | 1344354 | epirubicin | RxNorm |
| Added | drug_exposure | 1387426 | folate | RxNorm |
| Added | drug_exposure | 1388796 | leucovorin | RxNorm |
| Added | drug_exposure | 1390051 | chlorambucil | RxNorm |
| Added | drug_exposure | 1391248 | devil's claw preparation | RxNorm |
| Added | drug_exposure | 1391889 | Ginkgo biloba extract | RxNorm |
| Added | drug_exposure | 1398039 | St. John's wort extract | RxNorm |
| Added | measurement | 1447532 | Richmond Agitation Sedation Scale | SNOMED |
| Added | measurement | 1447893 | Intensive Care Delirium Screening Checklist | SNOMED |
| Added | measurement | 1469569 | Legionella pneumophila DNA [Presence] in Bronchoalveolar lavage by NAA with non-probe detection | LOINC |
| Added | observation | 1469651 | Method of oxygen delivery | LOINC |
| Added | drug_exposure | 1501309 | thyroid (USP) | RxNorm |
| Added | drug_exposure | 1503184 | mestranol | RxNorm |
| Added | drug_exposure | 1510363 | andexanet alfa | RxNorm |
| Added | drug_exposure | 1512480 | ibandronate | RxNorm |
| Added | drug_exposure | 1513876 | insulin lispro protamine, human | RxNorm |
| Added | drug_exposure | 1531601 | insulin aspart protamine, human | RxNorm |
| Added | drug_exposure | 1537655 | salmon calcitonin | RxNorm |
| Added | drug_exposure | 1593457 | ocrelizumab | RxNorm |
| Added | drug_exposure | 1593467 | dupilumab | RxNorm |
| Added | drug_exposure | 1594333 | safinamide | RxNorm |
| Added | measurement | 1616347 | PCA-Tr Ab [Presence] in Serum | LOINC |
| Added | measurement | 1616355 | Renal [Score] SOFA | LOINC |
| Added | measurement | 1616732 | Quick SOFA score SOFA.quick | LOINC |
| Added | measurement | 1616896 | Coagulation [Score] SOFA | LOINC |
| Added | measurement | 1616922 | Base excess in Central venous blood by calculation | LOINC |
| Added | measurement | 1617534 | Cardiovascular [Score] SOFA | LOINC |
| Added | drug_exposure | 1718850 | rucaparib | RxNorm |
| Added | drug_exposure | 1726228 | aminosalicylic acid | RxNorm |
| Added | drug_exposure | 1729323 | adefovir | RxNorm |
| Added | drug_exposure | 1729720 | penicillin V | RxNorm |
| Added | measurement | 1761323 | Chloride [Moles/volume] in Mixed venous blood | LOINC |
| Added | measurement | 1761753 | Glucose [Moles/volume] in Mixed venous blood | LOINC |
| Added | drug_exposure | 1792429 | proguanil | RxNorm |
| Added | drug_exposure | 1798476 | clofazimine | RxNorm |
| Added | measurement | 1988101 | Effluent pressure Renal replacement therapy circuit | LOINC |
| Added | measurement | 1988377 | Body temperature - Hand surface | LOINC |
| Added | measurement | 1988449 | Erythrocytes.dysmorphic/Erythrocytes in Urine by Automated count | LOINC |
| Added | measurement | 1988508 | Peritoneal dialysis fluid infused [Volume] | LOINC |
| Added | measurement | 1988543 | Pre-filter replacement fluid rate Renal replacement therapy circuit | LOINC |
| Added | measurement | 1988610 | Blood flow rate Renal replacement therapy circuit | LOINC |
| Added | measurement | 1988683 | Continuous renal replacement therapy fluid removal goal [Volume] 1 hour | LOINC |
| Added | measurement | 1988717 | Continuous renal replacement therapy mode Renal replacement therapy circuit | LOINC |
| Added | measurement | 1988731 | Hemodialysis fluid removed [Volume] | LOINC |
| Added | measurement | 1989128 | Pacemaker Atrial sensitivity setting | LOINC |
| Added | measurement | 1989136 | Peritoneal dialysis fluid drained [Volume] | LOINC |
| Added | measurement | 1989384 | Post-filter replacement fluid rate Renal replacement therapy circuit | LOINC |
| Added | measurement | 1989404 | Body temperature - Foot surface | LOINC |
| Added | measurement | 1989449 | Temporary pacemaker Ventricular stimulation setting | LOINC |
| Added | measurement | 1989451 | Pacemaker type | LOINC |
| Added | measurement | 1989569 | Pacemaker Ventricular sensitivity setting | LOINC |
| Added | drug_exposure | 2997891 | Rurioctocog Alfa Pegol | RxNorm Extension |
| Added | measurement | 3000058 | Para nitrophenol/Creatinine [Mass Ratio] in Urine | LOINC |
| Added | measurement | 3000144 | Amphetamine [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 3000185 | Iron saturation [Mass Fraction] in Serum or Plasma | LOINC |
| Added | measurement | 3000259 | Yeast [Presence] in Urine sediment by Light microscopy | LOINC |
| Added | measurement | 3000330 | Specific gravity of Urine by Test strip | LOINC |
| Added | measurement | 3000348 | Leukocyte esterase [Presence] in Urine by Test strip | LOINC |
| Added | measurement | 3000378 | Morphine [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3000456 | Dacrocytes [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3000475 | Leukocytes [#/volume] in Synovial fluid | LOINC |
| Added | measurement | 3000493 | Elliptocytes [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3000569 | Left ventricular Cardiac index by Indicator dilution | LOINC |
| Added | measurement | 3000570 | Elastase.pancreatic [Mass/mass] in Stool | LOINC |
| Added | measurement | 3000722 | Carnitine free (C0) [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3000764 | Benzodiazepines [Presence] in Urine | LOINC |
| Added | measurement | 3000787 | Salicylates [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3001079 | Blood group antibody screen [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3001102 | Acetylcholine receptor Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3001179 | ST wave end displacement in lead II | LOINC |
| Added | measurement | 3001355 | Fungus identified in Sputum by Culture | LOINC |
| Added | measurement | 3001362 | Plasma cells [#/volume] in Blood | LOINC |
| Added | measurement | 3001405 | CD3+CD8+ (T8 suppressor) cells [#/volume] in Blood | LOINC |
| Added | measurement | 3001501 | Glucose [Moles/volume] in Capillary blood by Glucometer | LOINC |
| Added | measurement | 3001719 | Right ventricular End-diastolic volume by Imaging | LOINC |
| Added | measurement | 3001981 | E Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3002000 | Albumin [Mass/volume] in Specimen | LOINC |
| Added | measurement | 3002020 | Barbiturates [Presence] in Urine | LOINC |
| Added | measurement | 3002148 | Methylenedioxymethamphetamine [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 3002171 | Fy sup(a) Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3002179 | Metamyelocytes/Leukocytes in Blood | LOINC |
| Added | measurement | 3002260 | Type of Gastrostomy tube | LOINC |
| Added | measurement | 3002394 | K Ag [Presence] on Red Blood Cells | LOINC |
| Added | measurement | 3002516 | Microscopic observation [Identifier] in Sputum by Gram stain | LOINC |
| Added | measurement | 3002620 | Howell-Jolly bodies [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3002623 | Legionella pneumophila Ag [Presence] in Urine by Latex agglutination | LOINC |
| Added | measurement | 3002799 | Nitrogen [Mass/time] in 24 hour Urine | LOINC |
| Added | measurement | 3002864 | Erythrocytes [#/volume] in Urine by Automated count | LOINC |
| Added | measurement | 3002971 | Nuclear Ab [Titer] in Serum by Immunofluorescence | LOINC |
| Added | measurement | 3003129 | Base excess in Capillary blood by calculation | LOINC |
| Added | measurement | 3003159 | Erythrocytes [#/volume] in Body fluid by Automated count | LOINC |
| Added | measurement | 3003291 | Casts [Presence] in Urine sediment by Light microscopy | LOINC |
| Added | measurement | 3003310 | Rh [Type] in Blood | LOINC |
| Added | measurement | 3003344 | Hemoglobin [Presence] in Urine | LOINC |
| Added | measurement | 3003351 | S Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3003377 | Respiration pause setting [Time] Ventilator | LOINC |
| Added | measurement | 3003412 | Glucose [Mass/volume] in Serum or Plasma --30 minutes post dose lactose PO | LOINC |
| Added | measurement | 3003487 | Left ventricular Cardiac output by Fick method | LOINC |
| Added | measurement | 3003540 | Lymphocytes/Leukocytes in Body fluid by Manual count | LOINC |
| Added | measurement | 3003598 | Drugs identified in Unknown substance by Screen method | LOINC |
| Added | measurement | 3003612 | Inferior vena cava Mean blood pressure | LOINC |
| Added | measurement | 3003693 | Protein intake Estimated | LOINC |
| Added | measurement | 3003715 | Dohle body [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3003932 | Carbon dioxide [Partial pressure] in Arterial cord blood | LOINC |
| Added | measurement | 3004106 | Pulse wave form Posterior tibial artery - left by US.doppler | LOINC |
| Added | measurement | 3004195 | Bilirubin.direct [Moles/volume] in Body fluid | LOINC |
| Added | measurement | 3004198 | Follitropin [Units/volume] in Serum or Plasma --baseline | LOINC |
| Added | measurement | 3004206 | Cells Counted Total [#] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3004227 | Saccharopolyspora rectivirgula IgG Ab [Presence] in Serum | LOINC |
| Added | measurement | 3004239 | Creatinine [Mass/time] in 24 hour Urine | LOINC |
| Added | measurement | 3004249 | Systolic blood pressure | LOINC |
| Added | measurement | 3004381 | Toxic granules [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3004411 | Monocytes/Leukocytes in Body fluid by Manual count | LOINC |
| Added | measurement | 3004501 | Glucose [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3004562 | Bacteria [Presence] in Urine sediment by Light microscopy | LOINC |
| Added | measurement | 3004739 | Amitriptyline+Nortriptyline [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3004764 | Prealbumin/Protein.total in Cerebral spinal fluid by Electrophoresis | LOINC |
| Added | measurement | 3004831 | Methemoglobin [Presence] in Blood | LOINC |
| Added | measurement | 3004959 | Base excess in Arterial cord blood by calculation | LOINC |
| Added | measurement | 3005029 | Protein [Mass/volume] in Body fluid | LOINC |
| Added | measurement | 3005058 | Barbiturates [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 3005105 | Blasts [#/volume] in Blood | LOINC |
| Added | measurement | 3005107 | Weight [Mass/time] of 24 hour Stool | LOINC |
| Added | measurement | 3005186 | little c Ag [Presence] on Red Blood Cells | LOINC |
| Added | measurement | 3005222 | little e Ag [Presence] on Red Blood Cells | LOINC |
| Added | measurement | 3005353 | Prothrombin activity actual/normal in Platelet poor plasma by Coagulation assay | LOINC |
| Added | measurement | 3005386 | K Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3005478 | Glucose [Mass/time] in 24 hour Urine | LOINC |
| Added | measurement | 3005481 | Spherocytes [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3005577 | Microalbumin [Mass/time] in 24 hour Urine | LOINC |
| Added | measurement | 3005723 | Lu sup(a) Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3005755 | Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma by With P-5'-P | LOINC |
| Added | measurement | 3005770 | Creatinine renal clearance in 24 hour Urine and Serum or Plasma | LOINC |
| Added | measurement | 3005797 | Superior vena cava Oxygen saturation | LOINC |
| Added | measurement | 3006006 | Tricyclic antidepressants [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 3006217 | Methemoglobin/Hemoglobin.total in Arterial blood | LOINC |
| Added | measurement | 3006225 | Type of Enteral tube | LOINC |
| Added | measurement | 3006257 | Acetylcholine receptor Ab [Moles/volume] in Serum | LOINC |
| Added | measurement | 3006567 | Chloride [Moles/time] in 24 hour Urine | LOINC |
| Added | measurement | 3006588 | Cancer Ag 15-3 [Units/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3006598 | pH of Arterial cord blood | LOINC |
| Added | measurement | 3006706 | IgM [Mass/volume] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3006768 | little s Ag [Presence] on Red Blood Cells | LOINC |
| Added | measurement | 3006772 | Delta aminolevulinate [Mass/volume] in 24 hour Urine | LOINC |
| Added | measurement | 3006777 | Left ventriclar Stroke work | LOINC |
| Added | measurement | 3006872 | clomiPRAMINE+Norclomipramine [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3006887 | Glucose [Mass/volume] in Serum or Plasma --pre dose lactose PO | LOINC |
| Added | measurement | 3006893 | Glucose [Moles/volume] in Specimen | LOINC |
| Added | measurement | 3007055 | Right eye Position | LOINC |
| Added | measurement | 3007153 | Bile [Presence] in Stool | LOINC |
| Added | measurement | 3007527 | Weight of Stone | LOINC |
| Added | measurement | 3007591 | Band form neutrophils/Leukocytes in Blood by Manual count | LOINC |
| Added | measurement | 3007612 | Type of Urine tube | LOINC |
| Added | measurement | 3007682 | Benzodiazepines [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 3007808 | Renin [Enzymatic activity/volume] in Plasma | LOINC |
| Added | measurement | 3007847 | Interleukin 2 Receptor Soluble [Units/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3007913 | Alveolar-arterial oxygen Partial pressure difference | LOINC |
| Added | measurement | 3007955 | Atmospheric pressure | LOINC |
| Added | measurement | 3008037 | Lactate [Moles/volume] in Venous blood | LOINC |
| Added | measurement | 3008071 | Urine output 24 hour | LOINC |
| Added | measurement | 3008108 | Hematocrit [Volume Fraction] of Body fluid by calculation | LOINC |
| Added | measurement | 3008114 | Pulse intensity Posterior tibial artery - left by palpation | LOINC |
| Added | measurement | 3008136 | Dog epithelium IgE Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3008204 | Clarity of Urine | LOINC |
| Added | measurement | 3008278 | IgA [Mass/volume] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3008338 | Lactate dehydrogenase [Enzymatic activity/volume] in Body fluid | LOINC |
| Added | measurement | 3008467 | Voriconazole [Susceptibility] | LOINC |
| Added | measurement | 3008515 | Right ventricular End diastolic blood pressure | LOINC |
| Added | measurement | 3008751 | Glomerular basement membrane IgG Ab [Units/volume] in Serum by Immunoassay | LOINC |
| Added | measurement | 3008839 | Basophils/Leukocytes in Body fluid by Manual count | LOINC |
| Added | measurement | 3008984 | Volume of Body fluid | LOINC |
| Added | measurement | 3009041 | Cardiolipin IgG Ab [Units/volume] in Serum by Immunoassay | LOINC |
| Added | measurement | 3009131 | Hemoglobin A/Hemoglobin.total in Blood by Electrophoresis | LOINC |
| Added | measurement | 3009210 | Methanol [Mass/volume] in Blood | LOINC |
| Added | measurement | 3009261 | Glucose [Presence] in Urine by Test strip | LOINC |
| Added | measurement | 3009343 | pH of Capillary blood | LOINC |
| Added | measurement | 3009354 | Benzodiazepines screen method [Identifier] in Urine | LOINC |
| Added | measurement | 3009435 | Left ventricular Intrachamber systolic pressure | LOINC |
| Added | measurement | 3009461 | 5-Hydroxyindoleacetate [Moles/time] in 24 hour Urine | LOINC |
| Added | measurement | 3009603 | Volume expired 1 minute | LOINC |
| Added | measurement | 3009666 | O-desmethylvenlafaxine [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3009710 | Isopropanol [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3009713 | Pulmonary vascular Resistance index | LOINC |
| Added | measurement | 3009767 | Physical findings of Left cornea Narrative | LOINC |
| Added | measurement | 3009797 | Basophils/Leukocytes in Blood by Manual count | LOINC |
| Added | measurement | 3009966 | Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay | LOINC |
| Added | measurement | 3010024 | Jk sup(b) Ag [Presence] on Red Blood Cells | LOINC |
| Added | measurement | 3010109 | Ethanol [Presence] in Urine | LOINC |
| Added | measurement | 3010409 | Erythrocytes [#/volume] in Cerebral spinal fluid by Manual count | LOINC |
| Added | measurement | 3010488 | Prolactin [Mass/volume] in Serum or Plasma --1st specimen post XXX challenge | LOINC |
| Added | measurement | 3010503 | CD19 cells [#/volume] in Blood | LOINC |
| Added | measurement | 3010566 | Parathyrin.intact [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3010657 | Triiodothyronine (T3) Free [Mass/volume] in Serum or Plasma by Dialysis | LOINC |
| Added | measurement | 3010683 | Neuronal nuclear type 2 Ab [Presence] in Serum | LOINC |
| Added | measurement | 3010747 | HIV 1 RNA [#/volume] (viral load) in Serum or Plasma by NAA with probe detection | LOINC |
| Added | measurement | 3010866 | Cholinesterase [Enzymatic activity/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3010884 | Ethanol [Mass/volume] in Serum or Plasma by Gas chromatography | LOINC |
| Added | measurement | 3010889 | Jk sup(a) Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3011149 | Choriogonadotropin.beta subunit [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3011164 | Constant gas flow setting Ventilator | LOINC |
| Added | measurement | 3011367 | Oxygen saturation Calculated from oxygen partial pressure in Blood | LOINC |
| Added | measurement | 3011368 | Poikilocytosis [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3011391 | Calcitriol [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3011402 | Methamphetamine [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 3011412 | CD3 cells [#/volume] in Blood | LOINC |
| Added | measurement | 3011520 | Treponema pallidum Ab [Presence] in Serum by Immunoassay | LOINC |
| Added | measurement | 3011570 | Cholesterol [Moles/volume] in Body fluid | LOINC |
| Added | measurement | 3011681 | Plasma cells/Leukocytes in Body fluid | LOINC |
| Added | measurement | 3011884 | Cholesterol in HDL [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3011937 | Urate/Total in Stone | LOINC |
| Added | measurement | 3011951 | Aspergillus fumigatus IgE Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3011961 | Ferritin [Mass/volume] in Blood | LOINC |
| Added | measurement | 3012030 | MCH [Entitic mass] by Automated count | LOINC |
| Added | measurement | 3012255 | ST wave end displacement in lead V5 | LOINC |
| Added | measurement | 3012347 | Physical findings of Right cornea Narrative | LOINC |
| Added | measurement | 3012471 | Hemoglobin.gastrointestinal.lower [Presence] in Stool by Immunoassay | LOINC |
| Added | measurement | 3012565 | Volume of 24 hour Urine | LOINC |
| Added | measurement | 3012582 | Chlamydophila pneumoniae DNA [Presence] in Sputum or Bronchial by Probe with amplification | LOINC |
| Added | measurement | 3012764 | Erythrocyte [Morphology] in Blood | LOINC |
| Added | measurement | 3012796 | Blood product type | LOINC |
| Added | measurement | 3012984 | Norclozapine [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3012996 | ST wave end displacement in lead I | LOINC |
| Added | measurement | 3013080 | Insulin Ab [Mass/volume] in Serum | LOINC |
| Added | measurement | 3013142 | Albumin/Protein.total in 24 hour Urine by Electrophoresis | LOINC |
| Added | measurement | 3013247 | Albumin in CSF/Albumin in Serum or Plasma | LOINC |
| Added | measurement | 3013429 | Basophils [#/volume] in Blood by Automated count | LOINC |
| Added | measurement | 3013539 | Creatinine [Moles/volume] in 24 hour Urine | LOINC |
| Added | measurement | 3013542 | traMADol [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 3013604 | Glucose [Mass/volume] in Serum or Plasma --30 minutes post 75 g glucose PO | LOINC |
| Added | measurement | 3013667 | Stools [Appearance] | LOINC |
| Added | measurement | 3013707 | Erythrocyte sedimentation rate [Velocity] in Red Blood Cells by Westergren method | LOINC |
| Added | measurement | 3013807 | Legionella sp identified in Bronchial specimen by Organism specific culture | LOINC |
| Added | measurement | 3013882 | Canary feather IgE Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3013888 | Pyruvate [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3013959 | ST wave end displacement in lead V4 | LOINC |
| Added | measurement | 3014019 | Protein intake Measured | LOINC |
| Added | measurement | 3014188 | Size [Entitic volume] of Stone | LOINC |
| Added | measurement | 3014295 | Oxygen saturation in Arterial cord blood | LOINC |
| Added | measurement | 3014300 | Beta 2 glycoprotein 1 IgM Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3014429 | Appearance of Body fluid | LOINC |
| Added | measurement | 3014485 | Sodium [Moles/volume] in 24 hour Urine | LOINC |
| Added | measurement | 3014507 | Right atrial Intrachamber mean pressure | LOINC |
| Added | measurement | 3014594 | Urea [Moles/volume] in Body fluid | LOINC |
| Added | measurement | 3014605 | Amiodarone [Mass/volume] in Body fluid | LOINC |
| Added | measurement | 3014646 | Fractional oxyhemoglobin in Blood | LOINC |
| Added | measurement | 3014694 | little c Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3014791 | Apolipoprotein B [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3014995 | M Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3015153 | Gamma hydroxybutyrate [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3015196 | Fat [Mass/time] in 24 hour Stool | LOINC |
| Added | measurement | 3015233 | Abnormal lymphocytes/Leukocytes in Blood | LOINC |
| Added | measurement | 3015235 | Bicarbonate [Moles/volume] in Capillary blood | LOINC |
| Added | measurement | 3015273 | Consistency of Stool | LOINC |
| Added | measurement | 3015377 | Calcium [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3015399 | Transferrin receptor.soluble [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3015529 | Ketamine [Presence] in Urine | LOINC |
| Added | measurement | 3015608 | Urea nitrogen [Mass/volume] in 24 hour Urine | LOINC |
| Added | measurement | 3015654 | D Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3015672 | Urea [Moles/volume] in 24 hour Urine | LOINC |
| Added | measurement | 3015813 | Cardiolipin IgM Ab [Units/volume] in Serum by Immunoassay | LOINC |
| Added | measurement | 3015816 | F5 gene p.Arg506Gln [Presence] in Blood or Tissue by Molecular genetics method | LOINC |
| Added | measurement | 3015820 | 5-Hydroxyindoleacetate/Creatinine [Molar ratio] in Urine | LOINC |
| Added | measurement | 3015916 | Alpha-1-Fetoprotein [Units/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3015956 | Eosinophils/Leukocytes in Blood by Manual count | LOINC |
| Added | measurement | 3016075 | Rhythm segment [Interpretation] Narrative by EKG | LOINC |
| Added | measurement | 3016087 | Cholesterol.total/Cholesterol in HDL [Molar ratio] in Serum or Plasma | LOINC |
| Added | measurement | 3016095 | Left ventricular Oxygen saturation | LOINC |
| Added | measurement | 3016278 | Endomysium IgA Ab [Presence] in Serum | LOINC |
| Added | measurement | 3016293 | Bicarbonate [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3016431 | Calcium.ionized [Moles/volume] adjusted to pH 7.4 in Serum or Plasma | LOINC |
| Added | measurement | 3016452 | Inferior vena cava Oxygen saturation | LOINC |
| Added | measurement | 3016543 | Leukocytes [#/volume] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3016750 | Collection duration of Urine | LOINC |
| Added | measurement | 3016816 | Cytomegalovirus IgG Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3016879 | Cocaine [Presence] in Urine | LOINC |
| Added | measurement | 3016881 | Enterovirus RNA [Presence] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 3016932 | Type of Oral tube | LOINC |
| Added | measurement | 3017044 | Thyrotropin receptor Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3017143 | Hepatitis C virus Ab [Presence] in Serum | LOINC |
| Added | measurement | 3017391 | Smooth muscle IgG Ab [Presence] in Serum | LOINC |
| Added | measurement | 3017394 | Zinc [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3017457 | Urea nitrogen [Mass/time] in 24 hour Urine | LOINC |
| Added | measurement | 3017579 | Pulse wave form Posterior tibial artery - right by US.doppler | LOINC |
| Added | measurement | 3017597 | Amitriptyline [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3017644 | Pyruvate kinase [Enzymatic activity/volume] in Red Blood Cells | LOINC |
| Added | measurement | 3017750 | Porphobilinogen [Mass/volume] in Urine | LOINC |
| Added | measurement | 3017809 | Bicarbonate [Moles/volume] in Arterial cord blood | LOINC |
| Added | measurement | 3017937 | Magnesium [Moles/time] in 24 hour Urine | LOINC |
| Added | measurement | 3017974 | Hemoglobin S [Presence] in Blood by Solubility test | LOINC |
| Added | measurement | 3017980 | Sjogrens syndrome-B extractable nuclear IgG Ab [Units/volume] in Serum by Immunoassay | LOINC |
| Added | measurement | 3018095 | Leukocytes [#/volume] in Urine | LOINC |
| Added | measurement | 3018100 | Left ventricular End diastolic blood pressure | LOINC |
| Added | measurement | 3018173 | Methanol [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3018480 | Type of Chest tube | LOINC |
| Added | measurement | 3018658 | Beta 2 glycoprotein 1 IgG Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3018672 | pH of Body fluid | LOINC |
| Added | measurement | 3018676 | Antithrombin [Units/volume] in Platelet poor plasma by Chromogenic method | LOINC |
| Added | measurement | 3018834 | Bilirubin.total [Presence] in Urine by Test strip | LOINC |
| Added | measurement | 3018913 | Phosphate [Moles/volume] in Blood | LOINC |
| Added | measurement | 3018954 | Choriogonadotropin [Presence] in Urine | LOINC |
| Added | measurement | 3018994 | Lactate dehydrogenase [Enzymatic activity/volume] in Body fluid by Lactate to pyruvate reaction | LOINC |
| Added | measurement | 3019050 | Tissue transglutaminase IgA Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3019105 | Plasmin inhibitor Ag [Mass/volume] in Platelet poor plasma by Immunoassay | LOINC |
| Added | measurement | 3019153 | Superior vena cava Mean blood pressure | LOINC |
| Added | measurement | 3019170 | Thyrotropin [Units/volume] in Serum or Plasma by Detection limit <= 0.005 mIU/L | LOINC |
| Added | measurement | 3019250 | Coagulation factor VIII activity actual/normal in Platelet poor plasma by Coagulation assay | LOINC |
| Added | measurement | 3019286 | Body position head tilt angle | LOINC |
| Added | measurement | 3019410 | Aspergillus fumigatus IgG Ab [Presence] in Serum | LOINC |
| Added | measurement | 3019531 | Acetone [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3019575 | Right ventricular Intrachamber systolic pressure | LOINC |
| Added | measurement | 3019591 | Physical findings of Chest | LOINC |
| Added | measurement | 3019805 | Aspergillus fumigatus IgG Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3019916 | ST wave end displacement in lead V3 | LOINC |
| Added | measurement | 3019947 | Neutrophils/Leukocytes in Body fluid by Manual count | LOINC |
| Added | measurement | 3020044 | Glucose [Moles/volume] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3020063 | Urinary bladder Volume by derived from height, width and length (US) | LOINC |
| Added | measurement | 3020064 | Aortic valve Orifice area by US | LOINC |
| Added | measurement | 3020222 | IgG clearance/Albumin clearance [Ratio] in Serum and CSF | LOINC |
| Added | measurement | 3020331 | Lead [Mass/volume] in Blood | LOINC |
| Added | measurement | 3020358 | CD16+CD56+ cells [#/volume] in Blood | LOINC |
| Added | measurement | 3020416 | Erythrocytes [#/volume] in Blood by Automated count | LOINC |
| Added | measurement | 3020475 | Ethylene glycol [Mass/volume] in Serum, Plasma or Blood | LOINC |
| Added | measurement | 3020565 | Legionella pneumophila DNA [Presence] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 3020650 | Glucose [Presence] in Urine | LOINC |
| Added | measurement | 3020672 | Legionella sp identified in Sputum by Organism specific culture | LOINC |
| Added | measurement | 3020804 | Pelger Huet cells [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3020845 | [Type] of Body fluid | LOINC |
| Added | measurement | 3021009 | Hemoglobin A2/Hemoglobin.total in Blood by Electrophoresis | LOINC |
| Added | measurement | 3021016 | oxyCODONE [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 3021322 | Cryoglobulin [Presence] in Serum | LOINC |
| Added | measurement | 3021494 | OLANZapine [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3021502 | Macrocytes [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3021601 | Nitrite [Presence] in Urine by Test strip | LOINC |
| Added | measurement | 3021614 | Rheumatoid factor [Units/volume] in Serum or Plasma | LOINC |
| Added | observation | 3021690 | Hospital discharge date | LOINC |
| Added | measurement | 3021835 | Urate [Mass/time] in 24 hour Urine | LOINC |
| Added | measurement | 3021855 | Mononuclear cells [#/volume] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3021901 | Oxygen saturation in Capillary blood | LOINC |
| Added | measurement | 3022113 | Urinalysis microscopic panel - Urine sediment | LOINC |
| Added | measurement | 3022174 | Leukocytes [#/volume] in Body fluid | LOINC |
| Added | measurement | 3022192 | Triglyceride [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3022231 | Eosinophils/Leukocytes in Body fluid by Manual count | LOINC |
| Added | measurement | 3022250 | Lactate dehydrogenase [Enzymatic activity/volume] in Serum or Plasma by Lactate to pyruvate reaction | LOINC |
| Added | measurement | 3022338 | Retinol [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3022356 | Deprecated Polymorphonuclear cells/100 leukocytes in Cerebral spinal fluid | LOINC |
| Added | measurement | 3022405 | Physical findings of Knee | LOINC |
| Added | measurement | 3022407 | Monocytes/Leukocytes in Blood by Manual count | LOINC |
| Added | measurement | 3022408 | ST wave end displacement in lead AVR | LOINC |
| Added | measurement | 3022481 | Fat [Presence] in Stool | LOINC |
| Added | measurement | 3022620 | Valproate [Mass/volume] in Serum or Plasma --trough | LOINC |
| Added | measurement | 3022621 | pH of Urine by Test strip | LOINC |
| Added | measurement | 3022632 | Rheumatoid factor IgM [Units/volume] in Serum | LOINC |
| Added | measurement | 3022683 | Crystals [type] in Synovial fluid by Light microscopy | LOINC |
| Added | measurement | 3022695 | Caffeine [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3022730 | Type of Stool collection device | LOINC |
| Added | measurement | 3022761 | Ku Ab [Presence] in Serum | LOINC |
| Added | measurement | 3022810 | Sodium [Moles/volume] in Body fluid | LOINC |
| Added | measurement | 3022819 | Cystine crystals [Presence] in Stone by Infrared spectroscopy | LOINC |
| Added | measurement | 3022826 | Microalbumin/Creatinine [Ratio] in Urine | LOINC |
| Added | measurement | 3022839 | Insertion depth Gastrointestinal tract upper EGD | LOINC |
| Added | measurement | 3022907 | Direct antiglobulin test.polyspecific reagent [Presence] on Red Blood Cells | LOINC |
| Added | measurement | 3023024 | Carbon dioxide [Partial pressure] in Capillary blood | LOINC |
| Added | observation | 3023170 | Hospital admission date | LOINC |
| Added | measurement | 3023199 | Leukocytes [#/volume] in Pleural fluid | LOINC |
| Added | measurement | 3023314 | Hematocrit [Volume Fraction] of Blood by Automated count | LOINC |
| Added | measurement | 3023410 | Appearance of Cerebral spinal fluid | LOINC |
| Added | measurement | 3023456 | Valproate Free/Valproate.total in Serum or Plasma | LOINC |
| Added | measurement | 3023515 | Verapamil [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3023560 | House dust Greer IgE Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3023599 | MCV [Entitic mean volume] in Red Blood Cells by Automated count | LOINC |
| Added | measurement | 3023694 | Leukocytes [#/volume] in Cerebral spinal fluid by Manual count | LOINC |
| Added | measurement | 3023725 | Urinary bladder Volume by derived by EMP (US) | LOINC |
| Added | measurement | 3023851 | Copper [Mass/time] in 24 hour Urine | LOINC |
| Added | measurement | 3023863 | Haddock IgE Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3024139 | IgG subclass 3 [Mass/volume] in Serum | LOINC |
| Added | measurement | 3024390 | 25-hydroxyvitamin D3 [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3024448 | Jk sup(a) Ag [Presence] on Red Blood Cells | LOINC |
| Added | measurement | 3024461 | Microorganism identified in Specimen by Culture | LOINC |
| Added | measurement | 3024666 | Lithium [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3024783 | Stomatocytes [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3024841 | Left ventricular stroke work index | LOINC |
| Added | measurement | 3024889 | Methemoglobin/Hemoglobin.total in Venous blood | LOINC |
| Added | measurement | 3024929 | Platelets [#/volume] in Blood by Automated count | LOINC |
| Added | measurement | 3024942 | Coagulation factor VIII inhibitor [Units/volume] in Platelet poor plasma by Coagulation assay | LOINC |
| Added | measurement | 3024959 | Parrot feather IgE Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3024980 | IgG subclass 4 [Mass/volume] in Serum | LOINC |
| Added | measurement | 3025008 | F2 gene c.20210G>A [Genotype] in Blood or Tissue by Molecular genetics method Nominal | LOINC |
| Added | measurement | 3025046 | Opiates [Identifier] in Urine | LOINC |
| Added | measurement | 3025084 | Appearance of Gastric fluid | LOINC |
| Added | measurement | 3025105 | Cocaine [Presence] in Serum or Plasma by Confirmatory method | LOINC |
| Added | measurement | 3025113 | Glucose [Mass/volume] in Serum or Plasma --15 minutes post dose lactose PO | LOINC |
| Added | measurement | 3025220 | Type of Body temperature device | LOINC |
| Added | measurement | 3025428 | Microscopic observation [Identifier] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3025481 | Topiramate [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3025547 | Thyroglobulin Ab [Units/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3025570 | Left atrial Intrachamber mean pressure | LOINC |
| Added | measurement | 3025616 | Target cells [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3025643 | Ethanol [Mass/volume] in Blood | LOINC |
| Added | measurement | 3025673 | Glucose [Mass/volume] in Serum or Plasma --2 hours post 75 g glucose PO | LOINC |
| Added | measurement | 3025809 | Q-T interval | LOINC |
| Added | measurement | 3025857 | Cortisol [Mass/volume] in Serum or Plasma --AM peak specimen | LOINC |
| Added | measurement | 3025879 | Neuronal nuclear Ab [Presence] in Serum | LOINC |
| Added | measurement | 3025886 | Oxalate [Mass/time] in 24 hour Urine | LOINC |
| Added | measurement | 3025887 | Neutrophils.hypersegmented/Leukocytes in Blood by Manual count | LOINC |
| Added | measurement | 3025926 | Body temperature - Core | LOINC |
| Added | measurement | 3025965 | Pulse intensity by palpation | LOINC |
| Added | measurement | 3026008 | Bacteria identified in Urine by Culture | LOINC |
| Added | measurement | 3026029 | Penicillin V IgE Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3026101 | Triglyceride [Moles/volume] in Body fluid | LOINC |
| Added | measurement | 3026238 | Oxygen/Inspired gas Respiratory system --on ventilator | LOINC |
| Added | measurement | 3026572 | PHENobarbital [Mass/volume] in Urine by Confirmatory method | LOINC |
| Added | measurement | 3026729 | Phosphate [Mass/volume] in Urine | LOINC |
| Added | measurement | 3026904 | Basophilic stippling [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3027008 | Opiates [Presence] in Urine | LOINC |
| Added | measurement | 3027017 | Erythrocytes [#/volume] in Blood by Manual count | LOINC |
| Added | measurement | 3027126 | Copper [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3027135 | IgG subclass 1 [Mass/volume] in Serum | LOINC |
| Added | measurement | 3027162 | Color of Urine | LOINC |
| Added | measurement | 3027260 | Neuronal nuclear Ab [Presence] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3027288 | Volume expired per minute/Body weight --on ventilator | LOINC |
| Added | measurement | 3027401 | Testosterone Free/Testosterone.total in Serum or Plasma | LOINC |
| Added | measurement | 3027476 | Ascorbate [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3027598 | Mean blood pressure | LOINC |
| Added | measurement | 3027772 | Cannabinoids [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3027929 | Blood product unit ID [#] | LOINC |
| Added | measurement | 3027944 | Amphetamines [Presence] in Urine | LOINC |
| Added | measurement | 3027945 | Reticulocytes/Erythrocytes in Blood | LOINC |
| Added | measurement | 3028167 | CD3+CD4+ (T4 helper) cells [#/volume] in Blood | LOINC |
| Added | measurement | 3028192 | IgG subclass 2 [Mass/volume] in Serum | LOINC |
| Added | measurement | 3028193 | Bilirubin.total [Mass/volume] in Body fluid | LOINC |
| Added | measurement | 3028271 | Lactate [Moles/volume] in Capillary blood | LOINC |
| Added | measurement | 3028300 | Cannabinoids [Presence] in Urine | LOINC |
| Added | measurement | 3028348 | Apolipoprotein A-I/Apolipoprotein B [Mass Ratio] in Serum or Plasma | LOINC |
| Added | measurement | 3028468 | Fragments [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3028612 | Thyroperoxidase Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3028626 | Oxygen [Partial pressure] in Capillary blood | LOINC |
| Added | measurement | 3028638 | Bilirubin.direct [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3028653 | Carboxyhemoglobin/Hemoglobin.total in Arterial blood | LOINC |
| Added | measurement | 3028707 | Methadone [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 3028878 | Tube cuff pressure Intubation tube | LOINC |
| Added | measurement | 3028879 | Pathologic findings | LOINC |
| Added | measurement | 3028899 | Airway temperature setting Ventilator | LOINC |
| Added | measurement | 3029103 | Nuclear Ab [Presence] in Serum by Immunofluorescence | LOINC |
| Added | measurement | 3029217 | Referral lab test identifier and name [Identifier] | LOINC |
| Added | measurement | 3029254 | Adenovirus DNA [#/volume] (viral load) in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 3029315 | Leukocytes [#/volume] in Urine by Automated count | LOINC |
| Added | measurement | 3029435 | Natriuretic peptide.B prohormone N-Terminal [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3029529 | Darunavir [Susceptibility] by Phenotype method | LOINC |
| Added | measurement | 3029794 | Leukocyte clumps [#/volume] in Urine by Automated count | LOINC |
| Added | measurement | 3029800 | Calcium oxalate dihydrate/Total in Stone by Infrared spectroscopy | LOINC |
| Added | measurement | 3029880 | Horowitz index in Blood | LOINC |
| Added | measurement | 3030081 | Atrial natriuretic factor [Moles/volume] in Plasma | LOINC |
| Added | measurement | 3030260 | Glucose [Presence] in Urine by Automated test strip | LOINC |
| Added | measurement | 3030367 | Cyclic citrullinated peptide IgG Ab [Units/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3030408 | 3-Methoxytyramine [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3030661 | Acylcarnitine pattern [Interpretation] in Urine | LOINC |
| Added | measurement | 3030687 | Bacterial susceptibility panel by Minimum inhibitory concentration (MIC) | LOINC |
| Added | measurement | 3030703 | Everolimus [Mass/volume] in Blood | LOINC |
| Added | measurement | 3030817 | Heptacarboxylporphyrin/Creatinine [Molar ratio] in Urine | LOINC |
| Added | measurement | 3030845 | Lymphocytes [#/volume] in Pleural fluid | LOINC |
| Added | measurement | 3030855 | CV2 Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 3030884 | Deprecated Polymorphonuclear cells [#/volume] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3031040 | Bacteria [#/volume] in Urine by Automated count | LOINC |
| Added | measurement | 3031076 | Corticotropin [Mass/volume] in Plasma --baseline | LOINC |
| Added | measurement | 3031163 | Eosinophils [#/volume] in Cerebral spinal fluid | LOINC |
| Added | measurement | 3031219 | Potassium [Moles/volume] in Mixed venous blood | LOINC |
| Added | measurement | 3031248 | Chloride [Moles/volume] in Arterial blood | LOINC |
| Added | measurement | 3031282 | Methemoglobin/Hemoglobin.total in Mixed venous blood | LOINC |
| Added | measurement | 3031478 | Chlamydophila pneumoniae DNA [Presence] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 3031579 | Sodium [Moles/volume] in Mixed venous blood | LOINC |
| Added | measurement | 3031624 | CD55 Granulocytes [Presence] in Blood | LOINC |
| Added | measurement | 3031735 | Monocytes [#/volume] in Pleural fluid | LOINC |
| Added | measurement | 3031911 | Cytomegalovirus DNA [#/volume] (viral load) in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 3032080 | INR in Blood by Coagulation assay | LOINC |
| Added | measurement | 3032370 | Actin IgG Ab [Units/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3032674 | Salmonella sp DNA [Presence] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 3032700 | Glomerular basement membrane Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3033019 | Pneumocystis jirovecii DNA [#/volume] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 3033306 | Mononuclear cells/Leukocytes in Cerebral spinal fluid | LOINC |
| Added | measurement | 3033308 | Hyaline casts [Presence] in Urine sediment by Light microscopy | LOINC |
| Added | measurement | 3033427 | Fungus identified in Specimen | LOINC |
| Added | measurement | 3033455 | IgG in CSF/IgG in serum | LOINC |
| Added | measurement | 3033489 | Left ventricular Intrachamber diastolic pressure | LOINC |
| Added | measurement | 3033575 | Monocytes [#/volume] in Blood by Automated count | LOINC |
| Added | measurement | 3033589 | ST wave end displacement in lead AVF | LOINC |
| Added | measurement | 3033605 | Complement C3 fragment [Mass/volume] in Red Blood Cells | LOINC |
| Added | measurement | 3033640 | ST wave end displacement in lead III | LOINC |
| Added | measurement | 3033705 | Calcium.ionized [Moles/volume] in Venous blood | LOINC |
| Added | measurement | 3033780 | Tidal volume inspired spontaneous+mechanical --on ventilator | LOINC |
| Added | measurement | 3033794 | Temperature setting Humidifier | LOINC |
| Added | measurement | 3033870 | Appearance of Spun Cerebral spinal fluid | LOINC |
| Added | measurement | 3033882 | Carnitine [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3034030 | Carboxyhemoglobin/Hemoglobin.total in Mixed venous blood | LOINC |
| Added | measurement | 3034037 | Hematocrit [Volume Fraction] of Mixed venous blood by calculation | LOINC |
| Added | measurement | 3034126 | ST wave end displacement in lead AVL | LOINC |
| Added | measurement | 3034429 | Barbiturates screen method [Identifier] in Urine | LOINC |
| Added | measurement | 3034484 | ST wave end displacement in lead V1 | LOINC |
| Added | measurement | 3034488 | Physical findings of Motor function | LOINC |
| Added | measurement | 3034548 | Prostate specific Ag [Mass/volume] in Serum or Plasma by Detection limit <= 0.01 ng/mL | LOINC |
| Added | measurement | 3034578 | Cells Counted Total [#] in Body fluid | LOINC |
| Added | measurement | 3034739 | Osmolality of Serum or Plasma by calculated by sum of electrolytes | LOINC |
| Added | measurement | 3034780 | Angiotensin converting enzyme [Enzymatic activity/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3034896 | Calcium oxalate monohydrate/Total in Stone | LOINC |
| Added | measurement | 3035012 | ST wave end displacement in lead V2 | LOINC |
| Added | measurement | 3035124 | Erythrocytes [#/area] in Urine sediment by Microscopy high power field | LOINC |
| Added | measurement | 3035285 | Chloride [Moles/volume] in Venous blood | LOINC |
| Added | measurement | 3035350 | Ketones [Presence] in Urine by Test strip | LOINC |
| Added | measurement | 3035544 | Cardiolipin IgG Ab [Units/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3035583 | Leukocytes [#/area] in Urine sediment by Microscopy high power field | LOINC |
| Added | measurement | 3035708 | Gamma hydroxybutyrate [Presence] in Urine | LOINC |
| Added | measurement | 3035729 | Glucose [Moles/volume] in Body fluid | LOINC |
| Added | measurement | 3035878 | Pulse intensity Femoral artery - right by palpation | LOINC |
| Added | measurement | 3035954 | Pulse intensity Femoral artery - left by palpation | LOINC |
| Added | measurement | 3036180 | Methadone [Presence] in Urine | LOINC |
| Added | measurement | 3036219 | Type of Wound drain device | LOINC |
| Added | measurement | 3036243 | Potassium [Moles/volume] in Body fluid | LOINC |
| Added | measurement | 3036453 | Pain severity [Score] Visual analog score | LOINC |
| Added | measurement | 3036472 | Blood group antibodies identified in Serum or Plasma | LOINC |
| Added | measurement | 3036535 | Thyroglobulin [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3036603 | Volume of Urine | LOINC |
| Added | measurement | 3036931 | Citrate [Mass/volume] in 24 hour Urine | LOINC |
| Added | measurement | 3037081 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma by With P-5'-P | LOINC |
| Added | measurement | 3037106 | Fluid intake total Measured | LOINC |
| Added | measurement | 3037310 | Renin [Mass/volume] in Plasma | LOINC |
| Added | measurement | 3037492 | Cardiolipin IgM Ab [Units/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3037522 | Nuclear Ab [Titer] in Serum | LOINC |
| Added | measurement | 3037524 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/volume] in Red Blood Cells | LOINC |
| Added | measurement | 3037577 | Monocytes/Leukocytes in Cerebral spinal fluid | LOINC |
| Added | measurement | 3037701 | Pyridoxine [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3037745 | PARoxetine [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3037816 | CD4+CD8+ cells/cells in Blood | LOINC |
| Added | measurement | 3037885 | Microcytes [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3038077 | Color of Cerebral spinal fluid | LOINC |
| Added | measurement | 3038080 | Amino acid pattern [Interpretation] in Serum or Plasma | LOINC |
| Added | measurement | 3038098 | Enterovirus RNA [Presence] in Nose by NAA with probe detection | LOINC |
| Added | measurement | 3038106 | Epithelial casts [Presence] in Urine sediment by Light microscopy | LOINC |
| Added | measurement | 3038136 | Choriogonadotropin.beta subunit [Units/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3038315 | Erythrocytes.dysmorphic/Erythrocytes in Urine sediment by Light microscopy | LOINC |
| Added | measurement | 3038515 | Glucose [Moles/volume] in Venous blood | LOINC |
| Added | measurement | 3038522 | Human metapneumovirus RNA [Identifier] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 3038776 | Pigeon serum proteins+feathers+droppings IgG Ab [Presence] in Serum | LOINC |
| Added | measurement | 3038988 | Cholesterol in LDL [Moles/volume] in Serum or Plasma by calculation | LOINC |
| Added | measurement | 3039426 | Oxygen saturation Calculated from oxygen partial pressure in Arterial blood | LOINC |
| Added | measurement | 3040197 | Anisochromasia [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 3040677 | Delta aminolevulinate/Creatinine [Molar ratio] in Urine | LOINC |
| Added | measurement | 3040891 | Heart rate --resting | LOINC |
| Added | measurement | 3041253 | Oxygen saturation Calculated from oxygen partial pressure in Venous blood | LOINC |
| Added | measurement | 3041354 | Potassium [Moles/volume] in Venous blood | LOINC |
| Added | measurement | 3041423 | Sjogrens syndrome-A extractable nuclear 60kD Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3041455 | Color of Wound base | LOINC |
| Added | measurement | 3041473 | Sodium [Moles/volume] in Venous blood | LOINC |
| Added | measurement | 3041748 | Fungus identified in Urine by Culture | LOINC |
| Added | measurement | 3041816 | Color of Dialysis fluid | LOINC |
| Added | measurement | 3042009 | Drugs identified in Urine by Confirmatory method | LOINC |
| Added | measurement | 3042027 | Normetanephrine Free [Moles/volume] in Serum or Plasma | LOINC |
| Added | measurement | 3042208 | Human coronavirus RNA [Identifier] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 3042272 | von Willebrand factor (vWf) cleaving protease actual/normal in Platelet poor plasma by Chromogenic method | LOINC |
| Added | measurement | 3042301 | Urate [Moles/volume] in Synovial fluid | LOINC |
| Added | measurement | 3042784 | Coproporphyrin 3/Creatinine [Molar ratio] in Urine | LOINC |
| Added | measurement | 3042951 | Complement C1q Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3043409 | Potassium [Moles/volume] in Arterial blood | LOINC |
| Added | measurement | 3043415 | Inspiratory breath [Time] --on ventilator | LOINC |
| Added | measurement | 3043662 | Wound assessment panel | LOINC |
| Added | measurement | 3043688 | Hemoglobin [Mass/volume] in Body fluid | LOINC |
| Added | measurement | 3043870 | Heparin induced platelet Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3043937 | Drugs identified in Specimen by Confirmatory method | LOINC |
| Added | measurement | 3044048 | Fat [Mass/mass] in 24 hour Stool | LOINC |
| Added | measurement | 3044152 | Coproporphyrin 1/Creatinine [Molar ratio] in Urine | LOINC |
| Added | measurement | 3044341 | Pentacarboxylporphyrins/Creatinine [Molar ratio] in Urine | LOINC |
| Added | measurement | 3044355 | Beta 2 glycoprotein 1 IgG Ab [Units/volume] in Serum or Plasma by Immunoassay | LOINC |
| Added | measurement | 3044376 | Amphetamines [Presence] in Urine by Screen method >500 ng/mL | LOINC |
| Added | measurement | 3044458 | Uroporphyrin/Creatinine [Molar ratio] in Urine | LOINC |
| Added | measurement | 3044597 | Porphobilinogen/Creatinine [Molar ratio] in Urine | LOINC |
| Added | measurement | 3044870 | Hemoglobin C/Hemoglobin.total in Blood by Electrophoresis | LOINC |
| Added | measurement | 3044904 | Oxygen content in Blood | LOINC |
| Added | measurement | 3044920 | Orthostatic blood pressure | LOINC |
| Added | measurement | 3045424 | Erythrocytes [Presence] in Urine | LOINC |
| Added | measurement | 3045462 | Protein/Creatinine [Ratio] in Urine | LOINC |
| Added | measurement | 3045706 | Amphiphysin Ab [Presence] in Serum | LOINC |
| Added | measurement | 3045815 | Ganglioside GD1b IgM Ab [Presence] in Serum | LOINC |
| Added | measurement | 3046004 | Intubation tube depth Respiratory system | LOINC |
| Added | measurement | 3046034 | DNA double strand IgG Ab [Units/volume] in Serum or Plasma by Immunoassay | LOINC |
| Added | measurement | 3046040 | Inspiratory.pause setting [Time] Ventilator | LOINC |
| Added | measurement | 3046171 | Beta 2 glycoprotein 1 IgM Ab [Units/volume] in Serum or Plasma by Immunoassay | LOINC |
| Added | measurement | 3046210 | Cortisol [Mass/volume] in Serum or Plasma --baseline | LOINC |
| Added | measurement | 3046315 | Type of Intubation tube | LOINC |
| Added | measurement | 3046326 | RBC casts [Presence] in Urine sediment by Light microscopy | LOINC |
| Added | measurement | 3046338 | Breath termination sensitivity setting Ventilator | LOINC |
| Added | measurement | 3046592 | Airway suction location | LOINC |
| Added | measurement | 3046665 | Ganglioside GD1b IgG Ab [Presence] in Serum | LOINC |
| Added | measurement | 3046838 | Edema site | LOINC |
| Added | measurement | 3047171 | Jo-1 extractable nuclear IgG Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3047226 | Benzoylecgonine [Presence] in Urine by Screen method >150 ng/mL | LOINC |
| Added | measurement | 3048548 | Porphyrins [Interpretation] in Urine Narrative | LOINC |
| Added | measurement | 3048762 | Shigella sp DNA [Presence] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 3049082 | CYP2C9 gene allele [Genotype] in Blood or Tissue by Molecular genetics method Nominal | LOINC |
| Added | measurement | 3049178 | Platelets Large/Platelets in Blood by Automated count | LOINC |
| Added | measurement | 3049202 | Albumin and Immunoglobulin Quotient [Interpretation] in Serum and CSF | LOINC |
| Added | measurement | 3049236 | Origin of Stone | LOINC |
| Added | measurement | 3049804 | Myeloperoxidase IgG Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3050001 | Acylcarnitine pattern [Interpretation] in Serum or Plasma | LOINC |
| Added | measurement | 3051387 | C reactive protein [Mass/volume] in Capillary blood | LOINC |
| Added | measurement | 3052524 | SCL-70 extractable nuclear IgG Ab [Units/volume] in Serum by Immunoassay | LOINC |
| Added | measurement | 3052708 | Transferrin.carbohydrate deficient/Transferrin.total in Serum or Plasma | LOINC |
| Added | measurement | 3052840 | Varicella zoster virus DNA [#/volume] (viral load) in Cerebral spinal fluid by NAA with probe detection | LOINC |
| Added | measurement | 3052912 | Proteinase 3 IgG Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 3052996 | IgG.intrathecally synthesized [Mass/volume] in Serum and CSF | LOINC |
| Added | measurement | 3053000 | Hemoglobin pattern [Interpretation] in Blood by Electrophoresis | LOINC |
| Added | measurement | 3053209 | Kappa light chains.free/Lambda light chains.free [Mass Ratio] in Serum | LOINC |
| Added | measurement | 3053287 | Hemoglobin pattern [Interpretation] in Blood Narrative | LOINC |
| Added | measurement | 3965131 | Sapovirus genogroup V RNA [Presence] in Stool by NAA with probe detection | LOINC |
| Added | measurement | 3966163 | Shigella sp DNA [Presence] in Stool by NAA with probe detection | LOINC |
| Added | measurement | 3966351 | Clostridioides difficile DNA [Presence] in Stool by NAA with probe detection | LOINC |
| Added | measurement | 4015171 | Neutrophil count, automated, cerebrospinal fluid | SNOMED |
| Added | observation | 4043369 | Activity of daily living | SNOMED |
| Added | device_exposure | 4044008 | Tracheostomy tube | SNOMED |
| Added | device_exposure | 4063122 | Nasogastric tube | SNOMED |
| Added | device_exposure | 4070667 | Urinary catheter | SNOMED |
| Added | observation | 4083588 | Patient sex | SNOMED |
| Added | measurement | 4089159 | Grip strength | SNOMED |
| Added | measurement | 4089233 | Consistency of sputum | SNOMED |
| Added | observation | 4091068 | Consistency of liquor | SNOMED |
| Added | measurement | 4092014 | Cardiac axis | SNOMED |
| Added | device_exposure | 4097216 | Endotracheal tube | SNOMED |
| Added | measurement | 4105091 | Ramsay sedation scale | SNOMED |
| Added | device_exposure | 4106029 | Laryngeal mask | SNOMED |
| Added | measurement | 4108000 | Spontaneous minute volume | SNOMED |
| Added | measurement | 4108453 | Train of four ratio | SNOMED |
| Added | device_exposure | 4117709 | Suprapubic catheter | SNOMED |
| Added | device_exposure | 4118298 | Arterial catheter | SNOMED |
| Added | device_exposure | 4119547 | Wound drain | SNOMED |
| Added | device_exposure | 4121351 | Chest drain | SNOMED |
| Added | device_exposure | 4124377 | Venous catheter | SNOMED |
| Added | observation | 4125279 | Ability to initiate swallowing reflex | SNOMED |
| Added | device_exposure | 4126195 | Arterial line | SNOMED |
| Added | observation | 4127794 | Decubitus | SNOMED |
| Added | observation | 4137801 | Coughing | SNOMED |
| Added | observation | 4146379 | Cough reflex | SNOMED |
| Added | device_exposure | 4147758 | Cerebrospinal catheter | SNOMED |
| Added | measurement | 4147814 | Vital capacity | SNOMED |
| Added | measurement | 4147864 | Urine cocaine metabolite screening | SNOMED |
| Added | device_exposure | 4148006 | Epidural catheter | SNOMED |
| Added | observation | 4150612 | Respiratory pattern | SNOMED |
| Added | measurement | 4158877 | Visual analog scale | SNOMED |
| Added | device_exposure | 4161814 | Peripherally inserted central catheter | SNOMED |
| Added | observation | 4168193 | Intubation technique | SNOMED |
| Added | device_exposure | 4178391 | Heat and moisture exchanger | SNOMED |
| Added | device_exposure | 4179206 | Central venous catheter | SNOMED |
| Added | observation | 4183166 | Orientation | SNOMED |
| Added | observation | 4185148 | Cardiac pacing rate | SNOMED |
| Added | measurement | 4192887 | Urine methadone screen | SNOMED |
| Added | measurement | 4193843 | Oxygenation index measurement | SNOMED |
| Added | measurement | 4196583 | FEV1/FVC percent | SNOMED |
| Added | device_exposure | 4224054 | Fecal collector | SNOMED |
| Added | device_exposure | 4225137 | Colostomy bag | SNOMED |
| Added | device_exposure | 4225145 | Urostomy bag | SNOMED |
| Added | measurement | 4230629 | Creatinine measurement, 24 hour urine | SNOMED |
| Added | device_exposure | 4236069 | Peritoneal dialysis catheter | SNOMED |
| Added | measurement | 4241837 | Forced expired volume in 1 second | SNOMED |
| Added | measurement | 4259496 | Corneal pachymetry | SNOMED |
| Added | device_exposure | 4262295 | Pulmonary artery catheter | SNOMED |
| Added | device_exposure | 4272956 | Cervical collar | SNOMED |
| Added | observation | 4273031 | Color of sputum - finding | SNOMED |
| Added | observation | 4287468 | Body position | SNOMED |
| Added | observation | 4297089 | Natural death | SNOMED |
| Added | measurement | 4304958 | Vancomycin resistant Enterococcus culture | SNOMED |
| Added | measurement | 4353622 | Expiratory time | SNOMED |
| Added | measurement | 4353950 | Train of four count | SNOMED |
| Added | drug_exposure | 19000498 | mefloquine | RxNorm |
| Added | drug_exposure | 19004539 | lacidipine | RxNorm |
| Added | drug_exposure | 19005129 | clobetasone | RxNorm |
| Added | drug_exposure | 19005147 | methotrimeprazine | RxNorm |
| Added | drug_exposure | 19007737 | mianserin | RxNorm |
| Added | drug_exposure | 19008012 | tiapride | RxNorm |
| Added | drug_exposure | 19008264 | vinblastine | RxNorm |
| Added | drug_exposure | 19015726 | cisatracurium | RxNorm |
| Added | drug_exposure | 19015768 | methoxy polyethylene glycol-epoetin beta | RxNorm |
| Added | drug_exposure | 19016670 | docosahexaenoate | RxNorm |
| Added | drug_exposure | 19018910 | cannabinol | RxNorm |
| Added | drug_exposure | 19020068 | nitric oxide | RxNorm |
| Added | drug_exposure | 19022479 | fomepizole | RxNorm |
| Added | drug_exposure | 19024770 | biotin | RxNorm |
| Added | drug_exposure | 19026710 | capreomycin | RxNorm |
| Added | drug_exposure | 19030059 | alginic acid | RxNorm |
| Added | drug_exposure | 19031583 | gadoxetate | RxNorm |
| Added | drug_exposure | 19037989 | dothiepin | RxNorm |
| Added | drug_exposure | 19039298 | sevoflurane | RxNorm |
| Added | drug_exposure | 19042550 | triazulenone | RxNorm |
| Added | drug_exposure | 19047076 | pizotyline | RxNorm |
| Added | drug_exposure | 19048699 | corticotropin-releasing hormone | RxNorm |
| Added | drug_exposure | 19050016 | ethiodized oil | RxNorm |
| Added | drug_exposure | 19050461 | prazepam | RxNorm |
| Added | drug_exposure | 19053171 | obidoxime | RxNorm |
| Added | drug_exposure | 19055156 | flumethasone | RxNorm |
| Added | drug_exposure | 19066274 | selenite | RxNorm |
| Added | drug_exposure | 19066894 | silicones | RxNorm |
| Added | drug_exposure | 19069075 | hydroquinidine | RxNorm |
| Added | drug_exposure | 19071967 | creatine | RxNorm |
| Added | drug_exposure | 19072030 | curcumin | RxNorm |
| Added | drug_exposure | 19080406 | anti-inhibitor coagulant complex | RxNorm |
| Added | drug_exposure | 19080512 | articaine | RxNorm |
| Added | drug_exposure | 19086712 | peppermint oil | RxNorm |
| Added | drug_exposure | 19088167 | ambroxol | RxNorm |
| Added | drug_exposure | 19091804 | magnesium sulfate heptahydrate | RxNorm |
| Added | drug_exposure | 19092061 | zinc citrate | RxNorm |
| Added | drug_exposure | 19092433 | ebastine | RxNorm |
| Added | drug_exposure | 19095002 | chlorprothixene | RxNorm |
| Added | drug_exposure | 19106287 | vitamin K2 | RxNorm |
| Added | drug_exposure | 19112524 | aluminum acetotartrate | RxNorm |
| Added | drug_exposure | 19115051 | risedronic acid | RxNorm |
| Added | drug_exposure | 19129738 | paraffin | RxNorm |
| Added | drug_exposure | 19136207 | lymphocyte immune globulin, anti-thymocyte globulin | RxNorm |
| Added | measurement | 21490551 | Gas delivery system inspiratory Sevoflurane setting [VFr/PPres] | LOINC |
| Added | measurement | 21490552 | Sevoflurane [VFr/PPres] Gas delivery system | LOINC |
| Added | measurement | 21490558 | Expiratory gas flow Respiratory system airway --on ventilator | LOINC |
| Added | measurement | 21490563 | Gas delivery system inspiratory Oxygen setting [VFr/PPres] | LOINC |
| Added | measurement | 21490564 | Trapped lung volume --at end expiration | LOINC |
| Added | measurement | 21490566 | Minimum alveolar concentration (MAC) for anesthesia.XXX Anesthetic agent.XXX | LOINC |
| Added | measurement | 21490578 | Apnea duration | LOINC |
| Added | measurement | 21490587 | Arterial blood temperature | LOINC |
| Added | measurement | 21490613 | Isoflurane [VFr/PPres] Gas delivery system | LOINC |
| Added | measurement | 21490618 | Sevoflurane [VFr/PPres] Airway adaptor | LOINC |
| Added | measurement | 21490622 | Physiological dead space [Volume] Respiratory system --on ventilator | LOINC |
| Added | measurement | 21490633 | Sevoflurane [VFr/PPres] Airway adaptor --during inspiration | LOINC |
| Added | measurement | 21490634 | Sevoflurane [VFr/PPres] Airway adaptor --at end expiration | LOINC |
| Added | measurement | 21490648 | Oxygen [VFr/PPres] Airway adaptor --at end expiration | LOINC |
| Added | measurement | 21490651 | Mean airway pressure --during inspiration | LOINC |
| Added | measurement | 21490671 | Aorta blood pressure | LOINC |
| Added | measurement | 21490672 | Aorta Diastolic blood pressure | LOINC |
| Added | measurement | 21490673 | Aorta Mean blood pressure | LOINC |
| Added | measurement | 21490674 | Aorta Systolic blood pressure | LOINC |
| Added | measurement | 21490676 | Central venous pressure (CVP) Diastolic | LOINC |
| Added | measurement | 21490677 | Central venous pressure (CVP) Systolic | LOINC |
| Added | measurement | 21490679 | Left atrial pressure Systolic | LOINC |
| Added | measurement | 21490681 | Right atrial pressure Diastolic | LOINC |
| Added | measurement | 21490682 | Right atrial pressure Systolic | LOINC |
| Added | measurement | 21490690 | Burst suppression ratio [Ratio] Cerebral cortex Electroencephalogram (EEG) | LOINC |
| Added | measurement | 21490696 | Oxygen [VFr/PPres] Gas delivery system | LOINC |
| Added | measurement | 21490711 | Bispectral index Cerebral cortex Electroencephalogram (EEG) | LOINC |
| Added | measurement | 21490725 | Inspiratory time percent | LOINC |
| Added | measurement | 21490726 | Left atrial pressure Diastolic | LOINC |
| Added | measurement | 21490736 | Heart rate by Noninvasive | LOINC |
| Added | measurement | 21490744 | Signal quality index EEG device Calculated | LOINC |
| Added | measurement | 21490769 | Venous blood temperature | LOINC |
| Added | measurement | 21490770 | Left ventricular End diastolic volume | LOINC |
| Added | measurement | 21490784 | Physiological dead space/Tidal volume Respiratory system | LOINC |
| Added | measurement | 21490786 | Airway occlusion pressure | LOINC |
| Added | measurement | 21490788 | Temperature difference | LOINC |
| Added | measurement | 21490789 | Tidal volume expired Respiratory system airway --on ventilator | LOINC |
| Added | measurement | 21490790 | Sevoflurane liquid delivered.total [Volume] in Reporting period from Gas delivery system | LOINC |
| Added | measurement | 21490855 | PEEP Respiratory system --on ventilator | LOINC |
| Added | measurement | 21490866 | Respiratory quotient Respiratory system | LOINC |
| Added | measurement | 21490876 | Pulmonary capillary Diastolic blood pressure | LOINC |
| Added | measurement | 21490877 | Pulmonary capillary Mean blood pressure | LOINC |
| Added | measurement | 21490886 | PCA dose number.max 1 hour Infusion pump | LOINC |
| Added | measurement | 21492394 | Mycobacterium tuberculosis DNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 21492832 | Wound assessment [Interpretation] | LOINC |
| Added | measurement | 21492837 | Skin assessment [Interpretation] | LOINC |
| Added | measurement | 21493079 | Fluid intake enteral tube nutritional formula volume 24 hour | LOINC |
| Added | measurement | 21493338 | Parainfluenza virus 2 RNA [Presence] in Nasopharynx by NAA with non-probe detection | LOINC |
| Added | measurement | 21493339 | Parainfluenza virus 3 RNA [Presence] in Nasopharynx by NAA with non-probe detection | LOINC |
| Added | measurement | 21493340 | Parainfluenza virus 4 RNA [Presence] in Nasopharynx by NAA with non-probe detection | LOINC |
| Added | measurement | 21493470 | Yersinia enterocolitica DNA [Presence] in Stool by NAA with non-probe detection | LOINC |
| Added | measurement | 21494260 | Myeloperoxidase IgG Ab [Presence] in Serum or Plasma by Immunoassay | LOINC |
| Added | measurement | 21494702 | CYP3A4 and CYP3A5 gene targeted mutation analysis in Blood or Tissue by Molecular genetics method | LOINC |
| Added | measurement | 21494967 | Amount of Stool | LOINC |
| Added | measurement | 21494972 | Heart murmur assessment panel | LOINC |
| Added | measurement | 21494991 | Pupil assessment [Interpretation] | LOINC |
| Added | measurement | 21494992 | Neurological assessment [Interpretation] | LOINC |
| Added | measurement | 21494994 | Pain scale [Type] | LOINC |
| Added | measurement | 21494997 | Breath sounds by Auscultation | LOINC |
| Added | drug_exposure | 35197852 | landiolol hydrochloride | RxNorm Extension |
| Added | drug_exposure | 35197905 | freeze-dried pepsin-treated human normal immunoglobulin | RxNorm Extension |
| Added | drug_exposure | 35198039 | polyethylene glycol-treated human normal immunoglobulin | RxNorm Extension |
| Added | drug_exposure | 35200286 | stiripentol | RxNorm |
| Added | drug_exposure | 35602991 | patiromer | RxNorm |
| Added | drug_exposure | 35603277 | cariprazine | RxNorm |
| Added | drug_exposure | 35604657 | alectinib | RxNorm |
| Added | drug_exposure | 35606016 | cytisine | RxNorm |
| Added | drug_exposure | 35891916 | Filgotinib | RxNorm Extension |
| Added | drug_exposure | 36027520 | glucosamine hydrochloride / glucosamine sulfate | RxNorm |
| Added | drug_exposure | 36027614 | Cobalamins / Vitamin B 12 | RxNorm |
| Added | drug_exposure | 36027680 | alendronate / cholecalciferol | RxNorm |
| Added | drug_exposure | 36027963 | triamcinolone / urea | RxNorm |
| Added | drug_exposure | 36028155 | penicillin G benzathine / penicillin G sodium | RxNorm |
| Added | drug_exposure | 36028197 | clindamycin / glucose | RxNorm |
| Added | drug_exposure | 36028258 | Fluoride Ion / Sodium Fluoride | RxNorm |
| Added | drug_exposure | 36028482 | meningococcal group A polysaccharide / meningococcal group C polysaccharide / meningococcal polysaccharide vaccine group W-135 / meningococcal polysaccharide vaccine group Y | RxNorm |
| Added | drug_exposure | 36028497 | alginic acid / aluminum hydroxide | RxNorm |
| Added | drug_exposure | 36028499 | lidocaine / zinc sulfate | RxNorm |
| Added | drug_exposure | 36028635 | Calcium Carbonate / Magnesium Oxide / Vitamin D | RxNorm |
| Added | drug_exposure | 36028653 | sodium phosphate / sodium phosphate, monobasic | RxNorm |
| Added | drug_exposure | 36028821 | Calcium Carbonate / Magnesium Oxide / Zinc Sulfate | RxNorm |
| Added | drug_exposure | 36028870 | amlodipine / hydrochlorothiazide / olmesartan | RxNorm |
| Added | drug_exposure | 36029114 | beclomethasone / clioquinol | RxNorm |
| Added | drug_exposure | 36029214 | ropivacaine / Sufentanil | RxNorm |
| Added | drug_exposure | 36029257 | aluminum hydroxide / dimethicone / magnesium hydroxide | RxNorm |
| Added | drug_exposure | 36029284 | lidocaine / methylprednisolone | RxNorm |
| Added | drug_exposure | 36029291 | epinephrine / lidocaine | RxNorm |
| Added | drug_exposure | 36029292 | chlorhexidine / lidocaine | RxNorm |
| Added | drug_exposure | 36029447 | linagliptin / metformin | RxNorm |
| Added | drug_exposure | 36029629 | factor IX / factor VII / factor X / protein C / protein S / prothrombin | RxNorm |
| Added | drug_exposure | 36029671 | naloxone / oxycodone | RxNorm |
| Added | drug_exposure | 36029787 | insulin glargine / lixisenatide | RxNorm |
| Added | drug_exposure | 36029814 | dolutegravir / rilpivirine | RxNorm |
| Added | drug_exposure | 36029832 | polyethylene glycol 3350 / potassium chloride / sodium chloride / sodium sulfate | RxNorm |
| Added | drug_exposure | 36029924 | captopril / hydrochlorothiazide | RxNorm |
| Added | drug_exposure | 36029967 | diclofenac / misoprostol | RxNorm |
| Added | drug_exposure | 36030084 | aspirin / dipyridamole | RxNorm |
| Added | drug_exposure | 36030139 | ethinyl estradiol / norethindrone | RxNorm |
| Added | drug_exposure | 36030222 | acetic acid / hydrocortisone | RxNorm |
| Added | drug_exposure | 36030275 | calcium carbonate / risedronate | RxNorm |
| Added | drug_exposure | 36030544 | polyethylene glycol 400 / propylene glycol | RxNorm |
| Added | drug_exposure | 36030575 | acetic acid / salicylic acid | RxNorm |
| Added | drug_exposure | 36030789 | aliskiren / hydrochlorothiazide | RxNorm |
| Added | drug_exposure | 36030859 | phenylephrine / tropicamide | RxNorm |
| Added | drug_exposure | 36030888 | estradiol / progesterone | RxNorm |
| Added | drug_exposure | 36030995 | hydrochlorothiazide / ramipril | RxNorm |
| Added | drug_exposure | 36031123 | dienogest / estradiol | RxNorm |
| Added | measurement | 36031214 | Diastolic blood pressure mean | LOINC |
| Added | measurement | 36032082 | Norfentanyl [Presence] in Urine by Screen method | LOINC |
| Added | measurement | 36032223 | Transpulmonary pressure gradient | LOINC |
| Added | measurement | 36032397 | Sleep quality - 1-5 numeric rating [Score] 24 hour | LOINC |
| Added | measurement | 36033651 | SARS-CoV-2 (COVID-19) sequencing and identification panel - Specimen by Molecular genetics method | LOINC |
| Added | measurement | 36303653 | Glomerular basement membrane Ab [Presence] in Serum by Line blot | LOINC |
| Added | measurement | 36303772 | Mean pressure Respiratory system airway --on ventilator | LOINC |
| Added | measurement | 36303914 | Fungus identified in Bronchoalveolar lavage by Culture | LOINC |
| Added | measurement | 36303943 | Heart rate --W exercise | LOINC |
| Added | measurement | 36303946 | Pressure.plateau Respiratory system airway --on ventilator | LOINC |
| Added | measurement | 36304443 | Parechovirus RNA [Presence] in Stool by NAA with probe detection | LOINC |
| Added | measurement | 36304810 | Presence of wound exudate | LOINC |
| Added | measurement | 36305572 | Microscopic observation [Presence] in Specimen by Auramine fluorochrome stain | LOINC |
| Added | measurement | 36305767 | Norovirus genogroups I and II RNA panel - Stool by NAA with probe detection | LOINC |
| Added | measurement | 36306016 | Hyaline casts [#/area] in Urine sediment | LOINC |
| Added | observation | 36659961 | Intensive care unit (ICU) admission date | LOINC |
| Added | measurement | 36660625 | Protein.monoclonal [Presence] in Serum or Plasma | LOINC |
| Added | device_exposure | 36674387 | Nasoduodenal feeding tube | SNOMED |
| Added | device_exposure | 36676722 | Nasojejunal feeding tube | SNOMED |
| Added | device_exposure | 36717545 | Wound irrigation cannula | SNOMED |
| Added | drug_exposure | 36849343 | COAGULATION FACTOR VIIA HUMAN | RxNorm Extension |
| Added | drug_exposure | 36850694 | METHYLMETHIONINE | RxNorm Extension |
| Added | drug_exposure | 36852771 | LANDIOLOL | RxNorm Extension |
| Added | drug_exposure | 36852971 | KRYPTON KR-81M | RxNorm Extension |
| Added | drug_exposure | 36854399 | DOTA-NOC GA-68 | RxNorm Extension |
| Added | drug_exposure | 36855301 | VERAPAMIL, (-)- | RxNorm Extension |
| Added | drug_exposure | 36878602 | Taurolidine | RxNorm Extension |
| Added | drug_exposure | 36878617 | Influenza Virus Fragmented, Inactivated, Strain A / Switzerland / 9715293/2013 H3N2 - Analogue Strain A / South Australia / 55/2014 Ivr-175 | RxNorm Extension |
| Added | drug_exposure | 36878723 | Neisseria meningitidis Group B Membrane vesicles External Omv | RxNorm Extension |
| Added | drug_exposure | 37002370 | oxybate | RxNorm |
| Added | measurement | 37017370 | Frailty Index | SNOMED |
| Added | measurement | 37019589 | Parainfluenza virus 1 RNA [Presence] in Respiratory system specimen by NAA with probe detection | LOINC |
| Added | measurement | 37019690 | Mycoplasma pneumoniae DNA [Presence] in Upper respiratory specimen by NAA with probe detection | LOINC |
| Added | measurement | 37020574 | Lean body weight | LOINC |
| Added | measurement | 37020808 | Human metapneumovirus RNA [Presence] in Respiratory system specimen by NAA with probe detection | LOINC |
| Added | measurement | 37020937 | Giardia lamblia DNA [Presence] in Stool by NAA with probe detection | LOINC |
| Added | measurement | 37021247 | Adenovirus 40+41 DNA [Presence] in Stool by NAA with probe detection | LOINC |
| Added | measurement | 37021465 | Parainfluenza virus 3 RNA [Presence] in Respiratory system specimen by NAA with probe detection | LOINC |
| Added | measurement | 37030869 | Rapid shallow breathing index | LOINC |
| Added | measurement | 37172182 | Aortic valve ventriculoarterial peak gradient | SNOMED |
| Added | measurement | 37172203 | Flucytosine mass concentration in serum | SNOMED |
| Added | measurement | 37174480 | Severe acute respiratory syndrome coronavirus 2 vaccination status | SNOMED |
| Added | observation | 37397718 | Difficult intubation | SNOMED |
| Added | drug_exposure | 37493796 | Epithiazide | RxNorm Extension |
| Added | drug_exposure | 37496482 | pretomanid | RxNorm |
| Added | drug_exposure | 37497667 | nicotinamide ribotide | RxNorm |
| Added | drug_exposure | 37499009 | bempedoic acid | RxNorm |
| Added | drug_exposure | 40161669 | canakinumab | RxNorm |
| Added | drug_exposure | 40167554 | pazopanib | RxNorm |
| Added | drug_exposure | 40170680 | dalfampridine | RxNorm |
| Added | drug_exposure | 40175900 | polidocanol | RxNorm |
| Added | drug_exposure | 40226579 | fingolimod | RxNorm |
| Added | drug_exposure | 40241969 | brentuximab vedotin | RxNorm |
| Added | measurement | 40482942 | Clinical chronic obstructive pulmonary disease questionnaire | SNOMED |
| Added | measurement | 40492202 | Modified early warning score scale | SNOMED |
| Added | measurement | 40493498 | AVPU - alert voice pain unresponsive scale | SNOMED |
| Added | measurement | 40758294 | Paroxysmal nocturnal panel - Blood | LOINC |
| Added | measurement | 40758301 | Cytoplasmic Ab pattern [Interpretation] in Serum by Immunofluorescence | LOINC |
| Added | measurement | 40758414 | Glasgow coma score special circumstances | LOINC |
| Added | observation | 40758416 | Time of death | LOINC |
| Added | measurement | 40758858 | Erythrocytes.fetal/Erythrocytes [Ratio] in Blood by Flow cytometry (FC) | LOINC |
| Added | measurement | 40758895 | Direct antiglobulin test.complement C3d specific reagent [Presence] on Red Blood Cells | LOINC |
| Added | measurement | 40759128 | Platelet aggregation arachidonate induced in Blood --500 umol/L | LOINC |
| Added | measurement | 40759195 | Circumference Neck | LOINC |
| Added | measurement | 40759301 | Aspergillus fumigatus IgG4 Ab [Mass/volume] in Serum | LOINC |
| Added | measurement | 40759660 | Glutamate decarboxylase 65 Ab [Units/volume] in Serum by Immunoassay | LOINC |
| Added | measurement | 40759668 | U1 small nuclear ribonucleoprotein IgG Ab [Units/volume] in Serum by Immunoassay | LOINC |
| Added | measurement | 40759839 | Ma+Ta Ab [Presence] in Serum by Immunoblot | LOINC |
| Added | measurement | 40759863 | PL-7 Ab [Presence] in Serum by Immunoblot | LOINC |
| Added | measurement | 40759864 | PL-12 Ab [Presence] in Serum by Immunoblot | LOINC |
| Added | measurement | 40759883 | Oligoclonal Bands IgG [Presence] in Cerebral spinal fluid by Isoelectric focusing | LOINC |
| Added | measurement | 40760078 | Neuronal nuclear type 2 Ab [Presence] in Cerebral spinal fluid by Immunofluorescence | LOINC |
| Added | measurement | 40760564 | Ma+Ta Ab [Presence] in Cerebral spinal fluid by Immunoblot | LOINC |
| Added | measurement | 40760845 | Protein [Presence] in Urine by Automated test strip | LOINC |
| Added | measurement | 40760871 | Heparin induced platelet Ab [Presence] in Serum or Plasma by Immunoassay | LOINC |
| Added | measurement | 40760954 | Leukocytes [#/volume] in Body fluid by Automated count | LOINC |
| Added | measurement | 40761010 | Clostridioides difficile glutamate dehydrogenase [Presence] in Stool | LOINC |
| Added | measurement | 40761074 | Ganglioside GD1a IgG Ab [Presence] in Serum | LOINC |
| Added | measurement | 40761075 | Ganglioside GD1a IgM Ab [Presence] in Serum | LOINC |
| Added | measurement | 40761175 | Wr sup(a) Ab [Presence] in Serum or Plasma | LOINC |
| Added | measurement | 40762352 | Hemoglobin A1c/Hemoglobin.total in Blood by IFCC protocol | LOINC |
| Added | measurement | 40762365 | Oxygen content in Arterial blood by calculation | LOINC |
| Added | measurement | 40762388 | Lacosamide [Mass/volume] in Serum or Plasma | LOINC |
| Added | measurement | 40762525 | Clinical biochemist review of results | LOINC |
| Added | measurement | 40763528 | Reticulocytes [#/volume] in Blood by Automated count | LOINC |
| Added | measurement | 40763580 | Pseudo Pelger Huet cells [Presence] in Blood by Light microscopy | LOINC |
| Added | measurement | 40763791 | Oxygen content in Venous blood by calculation | LOINC |
| Added | measurement | 40765161 | Human bocavirus DNA [Presence] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 40765210 | Herpes simplex virus 1 DNA [#/volume] (viral load) in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 40765214 | Herpes simplex virus 2 DNA [#/volume] (viral load) in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 40765591 | Rotavirus RNA [Presence] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 40765948 | CV2 Ab [Presence] in Cerebral spinal fluid by Immunofluorescence | LOINC |
| Added | measurement | 40765975 | Ganglioside GM1 IgG Ab [Presence] in Serum by Immunoassay | LOINC |
| Added | measurement | 40765979 | Ganglioside GM1 IgM Ab [Presence] in Serum by Immunoassay | LOINC |
| Added | measurement | 40765980 | Ganglioside GM2 IgG Ab [Presence] in Serum by Immunoassay | LOINC |
| Added | measurement | 40765982 | Ganglioside GM2 IgM Ab [Presence] in Serum by Immunoassay | LOINC |
| Added | measurement | 40765986 | Ganglioside GQ1b IgG Ab [Presence] in Serum by Immunoassay | LOINC |
| Added | measurement | 40765987 | Ganglioside GQ1b IgM Ab [Presence] in Serum by Immunoassay | LOINC |
| Added | measurement | 40766170 | Aquaporin 4 water channel IgG Ab [Presence] in Serum or Plasma by Immunofluorescence | LOINC |
| Added | measurement | 40766217 | Epithelial cells.squamous [Presence] in Bronchoalveolar lavage | LOINC |
| Added | measurement | 40769111 | Beta hydroxybutyrate [Moles/volume] in Blood by Test strip | LOINC |
| Added | measurement | 40769150 | CYP2C19 gene targeted mutation analysis in Blood by Molecular genetics method | LOINC |
| Added | measurement | 40769783 | Troponin T.cardiac [Mass/volume] in Serum or Plasma by High sensitivity method | LOINC |
| Added | measurement | 40770974 | Glomerular basement membrane IgG Ab [Presence] in Serum by Immunoassay | LOINC |
| Added | measurement | 40771507 | IgG.intrathecally synthesized/IgG.total in Cerebral spinal fluid | LOINC |
| Added | measurement | 40771570 | Coagulation specialist review of results | LOINC |
| Added | drug_exposure | 40798859 | General Nutrients | RxNorm Extension |
| Added | drug_exposure | 40798876 | Human Alpha1 Proteinase Inhibitor | RxNorm Extension |
| Added | drug_exposure | 40799192 | Vernakalant | RxNorm Extension |
| Added | measurement | 42527088 | Pulmonary artery wedge Systolic blood pressure | LOINC |
| Added | measurement | 42527120 | Expired minute Volume during Mechanical ventilation | LOINC |
| Added | measurement | 42527121 | Inspired minute Volume during Mechanical ventilation | LOINC |
| Added | measurement | 42527137 | Airway pressure delta setting Ventilator | LOINC |
| Added | measurement | 42527138 | Airway pressure delta --on ventilator | LOINC |
| Added | measurement | 42527661 | Body height Mother | LOINC |
| Added | measurement | 42527807 | PCA-1 Ab [Presence] in Serum by Immunofluorescence | LOINC |
| Added | measurement | 42527814 | GABABR Ab [Presence] in Serum by Immunofluorescence | LOINC |
| Added | measurement | 42528504 | Current nebulization cycle time.elapsed Nebulizer | LOINC |
| Added | measurement | 42528593 | TIF1-gamma Ab [Presence] in Serum by Line blot | LOINC |
| Added | measurement | 42528889 | AMPAR1+AMPAR2 IgG Ab [Presence] in Cerebral spinal fluid by Immunofluorescence | LOINC |
| Added | measurement | 42529053 | Jo-1 extractable nuclear IgG Ab [Presence] in Serum by Line blot | LOINC |
| Added | measurement | 42529067 | Signal Recognition Particle (SRP) IgG Ab [Presence] in Serum by Line blot | LOINC |
| Added | measurement | 42529069 | Smith extractable nuclear D IgG Ab [Units/volume] in Serum | LOINC |
| Added | measurement | 42529115 | GABABR IgG Ab [Presence] in Cerebral spinal fluid by Immunofluorescence | LOINC |
| Added | measurement | 42529116 | Leucine-rich glioma-inactivated protein 1 IgG Ab [Presence] in Cerebral spinal fluid by Immunofluorescence | LOINC |
| Added | measurement | 42529117 | Contactin-associated protein 2 IgG Ab [Presence] in Cerebral spinal fluid by Immunofluorescence | LOINC |
| Added | measurement | 42529124 | Mi-2 beta IgG Ab [Presence] in Serum by Line blot | LOINC |
| Added | measurement | 42529210 | Digoxin [Mass/volume] in Serum or Plasma by Immunoassay | LOINC |
| Added | measurement | 42529265 | OJ IgG Ab [Presence] in Serum by Line blot | LOINC |
| Added | measurement | 42529529 | Ej Ab [Presence] in Serum by Line blot | LOINC |
| Added | measurement | 42529582 | MDA5 Ab [Presence] in Serum by Line blot | LOINC |
| Added | measurement | 42529598 | SUMO-activating enzyme subunit 1 Ab [Presence] in Serum by Line blot | LOINC |
| Added | measurement | 42536432 | CHA2DS2-VASc (congestive heart failure, hypertension, age 2, diabetes mellitus, stroke 2, vascular disease, age, sex category) score | SNOMED |
| Added | measurement | 42868428 | Astrovirus RNA [Presence] in Specimen by NAA with probe detection | LOINC |
| Added | measurement | 42868446 | Proteinase 3 IgG Ab [Presence] in Serum by Immunoassay | LOINC |
| Added | measurement | 42868623 | Benzodiazepines [Presence] in Urine by Screen method >200 ng/mL | LOINC |
| Added | measurement | 42868627 | Methadone [Presence] in Urine by Screen method >300 ng/mL | LOINC |
| Added | measurement | 42868643 | Hematocrit [Volume Fraction] of Pleural fluid by calculation | LOINC |
| Added | measurement | 42868724 | Islet cell 512 IgG Ab [Presence] in Serum or Plasma by Immunoassay | LOINC |
| Added | measurement | 42868729 | Sjogrens syndrome-A extractable nuclear 52kD IgG Ab [Units/volume] in Serum by Immunoassay | LOINC |
| Added | measurement | 42869446 | Mononuclear cells [#/volume] in Body fluid by Automated count | LOINC |
| Added | measurement | 42869453 | Granulocytes/Leukocytes in Body fluid by Automated count | LOINC |
| Added | measurement | 42869454 | Mononuclear cells/Leukocytes in Body fluid by Automated count | LOINC |
| Added | measurement | 42869455 | Granulocytes [#/volume] in Body fluid by Automated count | LOINC |
| Added | measurement | 42869591 | Oxyhemoglobin/Hemoglobin.total [Pure mass fraction] in Venous blood | LOINC |
| Added | measurement | 42869592 | Oxyhemoglobin/Hemoglobin.total [Pure mass fraction] in Mixed venous blood | LOINC |
| Added | measurement | 42869594 | Oxyhemoglobin/Hemoglobin.total [Pure mass fraction] in Arterial blood | LOINC |
| Added | measurement | 42870557 | Ma1 Ab [Presence] in Serum by Immunoblot | LOINC |
| Added | measurement | 42870558 | Ma1 Ab [Presence] in Cerebral spinal fluid by Immunoblot | LOINC |
| Added | measurement | 42870588 | Differential panel, method unspecified - Blood | LOINC |
| Added | measurement | 42870632 | 1-Hydroxymidazolam [Mass/volume] in Serum or Plasma | LOINC |
| Added | drug_exposure | 42874054 | oxidronate | RxNorm |
| Added | drug_exposure | 42900401 | bosutinib | RxNorm |
| Added | drug_exposure | 42900505 | linaclotide | RxNorm |
| Added | drug_exposure | 43012292 | cabozantinib | RxNorm |
| Added | drug_exposure | 43012518 | bedaquiline | RxNorm |
| Added | drug_exposure | 43014237 | pomalidomide | RxNorm |
| Added | measurement | 43055141 | Pain severity - 0-10 verbal numeric rating [Score] - Reported | LOINC |
| Added | measurement | 43055226 | Bilirubin excess [Moles/volume] in Serum and CSF | LOINC |
| Added | measurement | 43055228 | Oxyhemoglobin [Moles/volume] in Cerebral spinal fluid | LOINC |
| Added | measurement | 43055265 | Wound type | LOINC |
| Added | measurement | 43055442 | Apixaban [Mass/volume] in Serum or Plasma | LOINC |
| Added | drug_exposure | 43526465 | canagliflozin | RxNorm |
| Added | drug_exposure | 43532326 | dimethicone 200 | RxNorm |
| Added | measurement | 43533388 | Cannabinoids [Presence] in Urine by Screen method >50 ng/mL | LOINC |
| Added | measurement | 43533393 | Opiates [Presence] in Urine by Screen method >300 ng/mL | LOINC |
| Added | measurement | 43533603 | Anion gap in Venous blood by Calculated.4Ions | LOINC |
| Added | measurement | 43533604 | Anion gap in Mixed venous blood by Calculated.4Ions | LOINC |
| Added | measurement | 43533606 | Anion gap in Arterial blood by Calculated.4Ions | LOINC |
| Added | measurement | 43533701 | Voriconazole [Mass/volume] in Serum or Plasma --trough | LOINC |
| Added | measurement | 43534000 | von Willebrand factor (vWf).activity [Units/volume] in Platelet poor plasma by Immunoassay | LOINC |
| Added | drug_exposure | 44122511 | factor IX complex / factor VII / Factor VIII / factor X / Prothrombin Injectable Suspension [Feiba] | RxNorm Extension |
| Added | drug_exposure | 44506753 | lipegfilgrastim | RxNorm |
| Added | measurement | 44782837 | Metabolic equivalent of task | SNOMED |
| Added | drug_exposure | 44785066 | sucroferric oxyhydroxide | RxNorm |
| Added | measurement | 44786640 | Carbapenem resistance blaNDM gene [Presence] by Molecular method | LOINC |
| Added | measurement | 44786747 | Hexacarboxylporphyrin III/Creatinine [Molar ratio] in Urine | LOINC |
| Added | measurement | 44786754 | Tacrolimus [Mass/volume] in Blood by LC/MS/MS | LOINC |
| Added | measurement | 44786763 | Proteinase 3 IgG Ab [Units/volume] in Serum or Plasma by Immunoassay | LOINC |
| Added | measurement | 44787085 | Pyridoxal phosphate [Moles/volume] in Blood | LOINC |
| Added | measurement | 44787087 | Thiamine pyrophosphate [Moles/volume] in Blood | LOINC |
| Added | measurement | 44802884 | Duration of haemodialysis | SNOMED |
| Added | observation | 44808537 | Assessment of ileostomy | SNOMED |
| Added | measurement | 44811981 | Serum free PSA (prostate specific antigen) measurement | SNOMED |
| Added | measurement | 44812145 | Urine benzodiazepine screening test | SNOMED |
| Added | measurement | 44816798 | Bilirubin.total [Moles/volume] in Cerebral spinal fluid | LOINC |
| Added | drug_exposure | 44818461 | siltuximab | RxNorm |
| Added | device_exposure | 45758063 | Patient monitoring system module, cardiac output | SNOMED |
| Added | device_exposure | 45763425 | Gastrostomy tube | SNOMED |
| Added | device_exposure | 45763519 | Hyperthermia system temperature mapping unit | SNOMED |
| Added | device_exposure | 45772272 | Nasogastric feeding tube | SNOMED |
| Added | drug_exposure | 45775146 | peginterferon beta-1a | RxNorm |
| Added | drug_exposure | 45775351 | bicarbonate ion | RxNorm |
| Added | drug_exposure | 45775372 | dabigatran | RxNorm |
| Added | measurement | 46234969 | Mycobacterium sp identified in Bronchoalveolar lavage by Organism specific culture | LOINC |
| Added | measurement | 46235127 | Lupus anticoagulant two screening tests W Reflex [interpretation] | LOINC |
| Added | measurement | 46235749 | Adenovirus DNA [Presence] in Nasopharynx by NAA with probe detection | LOINC |
| Added | measurement | 46235750 | Aspergillus sp DNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 46235753 | Enterovirus RNA [Presence] in Nasopharynx by NAA with probe detection | LOINC |
| Added | measurement | 46235754 | Galactomannan Ag [Units/volume] in Bronchoalveolar lavage | LOINC |
| Added | measurement | 46235756 | Influenza virus A RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 46235757 | Influenza virus A RNA [Presence] in Nasopharynx by NAA with probe detection | LOINC |
| Added | measurement | 46235758 | Influenza virus B RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 46235759 | Influenza virus B RNA [Presence] in Nasopharynx by NAA with probe detection | LOINC |
| Added | measurement | 46235763 | Parainfluenza virus 1 RNA [Presence] in Nasopharynx by NAA with probe detection | LOINC |
| Added | measurement | 46235767 | Respiratory syncytial virus RNA [Presence] in Bronchoalveolar lavage by NAA with probe detection | LOINC |
| Added | measurement | 46235794 | Respiratory syncytial virus RNA [Presence] in Nasopharynx by NAA with probe detection | LOINC |
| Added | measurement | 46236735 | Rhinovirus RNA [Presence] in Nasopharynx by NAA with probe detection | LOINC |
| Added | drug_exposure | 46274210 | ceftaroline fosamil | RxNorm |
| Added | drug_exposure | 46275300 | brexpiprazole | RxNorm |
| Added | measurement | 2000000000 |  |  |
| Added | measurement | 2000000022 | Blood flow CVVHD | ICUdata |
| Added | measurement | 2000000026 | Calcium suppletion dose CVVHD | ICUdata |
| Added | measurement | 2000000029 | Citrate dosage CVVHD | ICUdata |
| Added | measurement | 2000000031 | CRRT dialysate solution | ICUdata |
| Added | measurement | 2000000049 | Pre filter pressure CVVHD | ICUdata |
| Added | measurement | 2000000052 | Pressure drop CVVH | ICUdata |
| Added | measurement | 2000000054 | Return pressure CVVHD | ICUdata |
| Added | measurement | 2000000055 | Substitution anticoagulants CVVH | ICUdata |
| Added | measurement | 2000000060 | Transmembrane pressure CVVHD | ICUdata |
| Added | measurement | 2000000076 | Cumulative fluid balance | ICUdata |
| Added | measurement | 2000000079 | Fluid intake CVVH dialysis | ICUdata |
| Added | measurement | 2000000094 | Gastric retention | ICUdata |
| Added | measurement | 2000000134 | Coagulation factor X activated inhibitor [Mass/volume] in Platelet poor plasma --ufh | ICUdata |
| Added | measurement | 2000000136 | Calcium ratio | ICUdata |
| Added | measurement | 2000000174 | Tracheostomy cuff inflated | ICUdata |
| Added | measurement | 2000000202 | fio2 --nice | ICUdata |
| Added | measurement | 2000000215 | Inspiratory rise time perc | ICUdata |
| Added | drug_exposure | 2000000255 | Enteral feeding | ICUdata |
| Added | measurement | 2000000280 | Delirium observation screening - question 9 | ICUdata |
| Added | measurement | 2000000303 | Delirium observation screening - question 2 | ICUdata |
| Added | measurement | 2000000304 | Delirium observation screening - question 1 | ICUdata |
| Added | measurement | 2000000306 | Delirium observation screening - question 8 | ICUdata |
| Added | measurement | 2000000318 | decubitus score - nose | ICUdata |
| Added | measurement | 2000000320 | Delirium observation screening - question 13 | ICUdata |
| Added | measurement | 2000000329 | eligibility to be a tissue donor | ICUdata |
| Added | measurement | 2000000336 | Length source | ICUdata |
| Added | measurement | 2000000339 | Weight source | ICUdata |
| Added | measurement | 2000000340 | eligibility to be an organ donor | ICUdata |
| Added | measurement | 2000000357 | fluid output - dialysis | ICUdata |
| Added | measurement | 2000000376 | level - chest tube | ICUdata |
| Added | measurement | 2000000460 | Blood gas sampling site | ICUdata |
| Added | measurement | 2000000473 | feeding tube suction pressure | ICUdata |
| Added | measurement | 2000000496 | Chest tube placement | ICUdata |
| Added | measurement | 2000000503 | feeding tube position | ICUdata |
| Added | measurement | 2000000569 | level - gastric suction drain | ICUdata |
| Added | drug_exposure | 2000000590 | pantoprazol / amoxicilline / claritromycine | ICUdata |
| Added | measurement | 2000000599 | Reason for physical restraint | ICUdata |
| Added | measurement | 2000000604 | Physical restraint description | ICUdata |
| Added | measurement | 2000000621 | Replacement fluid CVVH - order | ICUdata |
| Added | measurement | 2000000915 | Inhaled oxygen flow rate --on high flow | ICUdata |
| Added | measurement | 2000000916 | Oxygen/Inspired gas Respiratory system --on high flow | ICUdata |
| Added | measurement | 2000000922 | Fluid output faeces | ICUdata |
| Added | measurement | 2000000923 | Pulmonary vascular permeability index | ICUdata |
| Added | measurement | 2000000924 | Fluid intake transfusion | ICUdata |
| Added | measurement | 2000000930 | Vacuum wound therapy negative pressure | ICUdata |
| Added | measurement | 2000000940 | Automatic tube compensation level | ICUdata |
| Added | measurement | 2000000941 | Vancomycine target | ICUdata |
| Added | measurement | 2000000944 | Dialysate temperature setting | ICUdata |
| Added | measurement | 2000000946 | Work of breathing by ventilator | ICUdata |
| Added | measurement | 2000000948 | Nurse workload | ICUdata |
| Added | measurement | 2000000949 | Transfusion threshold | ICUdata |
| Added | measurement | 2000000950 | Last validated paO2 | ICUdata |
| Added | measurement | 2000000951 | Last validated pH | ICUdata |
| Added | measurement | 2000000952 | Last validated paCO2 | ICUdata |
| Added | measurement | 2000000955 | Blood sampling site | ICUdata |
| Added | measurement | 2000000956 | Last validated PaO2/FiO2 ratio | ICUdata |
| Added | observation | 2000000961 | Critical Care Pain Observation Tool facial expression | ICUdata |
| Added | observation | 2000000962 | Critical Care Pain Observation Tool body movements | ICUdata |
| Added | measurement | 2000000966 | Central venous catheter location | ICUdata |
| Added | measurement | 2000000970 | Gastric tube depth | ICUdata |
| Added | measurement | 2000000974 | Pacemaker leads location | ICUdata |
| Added | measurement | 2000000979 | Intensive Care Delirium Screening Checklist inattention score | ICUdata |
| Added | measurement | 2000000980 | Intensive Care Delirium Screening Checklist sleep/wake cycle score | ICUdata |
| Added | measurement | 2000000981 | Intensive Care Delirium Screening Checklist agitation score | ICUdata |
| Added | measurement | 2000000982 | Intensive Care Delirium Screening Checklist disorentation score | ICUdata |
| Added | measurement | 2000000983 | Intensive Care Delirium Screening Checklist hallucinations score | ICUdata |
| Added | measurement | 2000000984 | Intensive Care Delirium Screening Checklist speech/mood score | ICUdata |
| Added | observation | 2000000986 | Ventilator trigger mode | ICUdata |
| Added | observation | 2000000987 | Intensive Care Delirium Screening Checklist fluctuation score | ICUdata |
| Added | observation | 2000000990 | Intensive Care Delirium Screening Checklist result | ICUdata |
| Added | observation | 2000000993 | Intensive Care Delirium Screening Checklist consciousness score | ICUdata |
| Added | measurement | 2000001008 | Euroscore II predicted mortality | ICUdata |
| Added | measurement | 2000001033 | Fluid intake epidural | ICUdata |
| Added | measurement | 2000001037 | CPAX total | ICUdata |
| Added | measurement | 2000001123 | Total fluid input oral | ICUdata |
| Removed | condition_occurrence | 22955 | Perforation of esophagus | SNOMED |
| Removed | condition_occurrence | 23220 | Chronic tonsillitis | SNOMED |
| Removed | condition_occurrence | 23325 | Heartburn | SNOMED |
| Removed | condition_occurrence | 23986 | Disorder of pituitary gland | SNOMED |
| Removed | condition_occurrence | 24609 | Hypoglycemia | SNOMED |
| Removed | condition_occurrence | 24818 | Injury of neck | SNOMED |
| Removed | condition_occurrence | 26638 | Primary malignant neoplasm of esophagus | SNOMED |
| Removed | condition_occurrence | 26711 | Chronic pharyngitis | SNOMED |
| Removed | condition_occurrence | 26727 | Hematemesis | SNOMED |
| Removed | condition_occurrence | 26942 | Hemoglobin SS disease with crisis | SNOMED |
| Removed | condition_occurrence | 27674 | Nausea and vomiting | SNOMED |
| Removed | condition_occurrence | 28109 | Carcinoma in situ of esophagus | SNOMED |
| Removed | condition_occurrence | 28457 | Hypertrophy of tonsils | SNOMED |
| Removed | condition_occurrence | 28779 | Bleeding esophageal varices | SNOMED |
| Removed | condition_occurrence | 30437 | Gastro-esophageal reflux disease with esophagitis | SNOMED |
| Removed | condition_occurrence | 31317 | Dysphagia | SNOMED |
| Removed | condition_occurrence | 31610 | Disorder of esophagus | SNOMED |
| Removed | condition_occurrence | 31884 | Acquired diverticulum of esophagus | SNOMED |
| Removed | condition_occurrence | 72576 | Benign neoplasm of breast | SNOMED |
| Removed | condition_occurrence | 73001 | Myositis | SNOMED |
| Removed | condition_occurrence | 73300 | Radial styloid tenosynovitis | SNOMED |
| Removed | condition_occurrence | 74188 | Closed fracture of rib | SNOMED |
| Removed | condition_occurrence | 74582 | Primary malignant neoplasm of rectum | SNOMED |
| Removed | condition_occurrence | 74635 | Lumbosacral radiculopathy | SNOMED |
| Removed | condition_occurrence | 75311 | Fibrosclerosis of breast | SNOMED |
| Removed | condition_occurrence | 75344 | Intervertebral disc disorder | SNOMED |
| Removed | condition_occurrence | 75860 | Constipation | SNOMED |
| Removed | condition_occurrence | 75865 | Disorder of urinary system | SNOMED |
| Removed | condition_occurrence | 75909 | Disorder of bone | SNOMED |
| Removed | condition_occurrence | 75910 | Osteitis deformans | SNOMED |
| Removed | condition_occurrence | 75911 | Acquired hallux valgus | SNOMED |
| Removed | condition_occurrence | 76482 | Missed miscarriage | SNOMED |
| Removed | condition_occurrence | 77030 | Disorder of breast | SNOMED |
| Removed | condition_occurrence | 77076 | Diastasis of muscle | SNOMED |
| Removed | condition_occurrence | 77079 | Spinal stenosis | SNOMED |
| Removed | condition_occurrence | 77630 | Disorder of shoulder | SNOMED |
| Removed | condition_occurrence | 77670 | Chest pain | SNOMED |
| Removed | condition_occurrence | 78200 | Benign mammary dysplasia | SNOMED |
| Removed | condition_occurrence | 78474 | Hypertrophy of breast | SNOMED |
| Removed | condition_occurrence | 79833 | Ménière's disease | SNOMED |
| Removed | condition_occurrence | 79864 | Hematuria syndrome | SNOMED |
| Removed | condition_occurrence | 79936 | Polyuria | SNOMED |
| Removed | condition_occurrence | 79938 | Closed fracture of scapula | SNOMED |
| Removed | condition_occurrence | 80045 | Primary malignant neoplasm of anus | SNOMED |
| Removed | condition_occurrence | 80502 | Osteoporosis | SNOMED |
| Removed | condition_occurrence | 81250 | Carcinoma in situ of breast | SNOMED |
| Removed | condition_occurrence | 81390 | Idiopathic osteoporosis | SNOMED |
| Removed | condition_occurrence | 81878 | Benign paroxysmal positional vertigo | SNOMED |
| Removed | condition_occurrence | 81893 | Ulcerative colitis | SNOMED |
| Removed | condition_occurrence | 81902 | Urinary tract infectious disease | SNOMED |
| Removed | condition_occurrence | 132412 | Post-laminectomy syndrome | SNOMED |
| Removed | condition_occurrence | 132702 | Erythema multiforme | SNOMED |
| Removed | condition_occurrence | 132703 | Lichen planus | SNOMED |
| Removed | condition_occurrence | 132797 | Sepsis | SNOMED |
| Removed | condition_occurrence | 133141 | Tinea pedis | SNOMED |
| Removed | condition_occurrence | 133147 | Primary malignant neoplasm of skin of trunk | SNOMED |
| Removed | condition_occurrence | 133424 | Primary malignant neoplasm of thyroid gland | SNOMED |
| Removed | condition_occurrence | 133566 | Necrotizing fasciitis | SNOMED |
| Removed | condition_occurrence | 133713 | Malignant melanoma of skin of face | SNOMED |
| Removed | condition_occurrence | 133729 | Hyperparathyroidism | SNOMED |
| Removed | condition_occurrence | 134159 | Precordial pain | SNOMED |
| Removed | condition_occurrence | 134603 | Chronic myeloid leukemia | SNOMED |
| Removed | condition_occurrence | 134681 | Diffuse spasm of esophagus | SNOMED |
| Removed | condition_occurrence | 134738 | Acute osteomyelitis of multiple sites | SNOMED |
| Removed | condition_occurrence | 134898 | Non-toxic uninodular goiter | SNOMED |
| Removed | condition_occurrence | 135214 | Polycythemia vera (clinical) | SNOMED |
| Removed | condition_occurrence | 135526 | Spinal cord disease | SNOMED |
| Removed | condition_occurrence | 135777 | Neoplasm of uncertain behavior of skin | SNOMED |
| Removed | condition_occurrence | 135778 | Toxic multinodular goiter | SNOMED |
| Removed | condition_occurrence | 136496 | Cellulitis and abscess of face | SNOMED |
| Removed | condition_occurrence | 136580 | Dehiscence of surgical wound | SNOMED |
| Removed | condition_occurrence | 136788 | Spinal stenosis of lumbar region | SNOMED |
| Removed | condition_occurrence | 136917 | Primary malignant neoplasm of skin of face | SNOMED |
| Removed | condition_occurrence | 136960 | Vascular myelopathy | SNOMED |
| Removed | condition_occurrence | 137005 | Tracheostomy complication | SNOMED |
| Removed | condition_occurrence | 137077 | Chronic osteomyelitis of ankle and/or foot | SNOMED |
| Removed | condition_occurrence | 137275 | Disorder of muscle | SNOMED |
| Removed | condition_occurrence | 137548 | Cervical radiculopathy | SNOMED |
| Removed | condition_occurrence | 138346 | Erysipelas | SNOMED |
| Removed | condition_occurrence | 138387 | Thyrotoxicosis | SNOMED |
| Removed | condition_occurrence | 138388 | Secondary hyperparathyroidism | SNOMED |
| Removed | condition_occurrence | 138717 | Toxic diffuse goiter | SNOMED |
| Removed | condition_occurrence | 138825 | Actinic keratosis | SNOMED |
| Removed | condition_occurrence | 138994 | Myelodysplastic syndrome (clinical) | SNOMED |
| Removed | condition_occurrence | 139737 | Pediculosis corporis | SNOMED |
| Removed | condition_occurrence | 139750 | Primary malignant neoplasm of skin | SNOMED |
| Removed | condition_occurrence | 139900 | Urticaria | SNOMED |
| Removed | condition_occurrence | 140362 | Hypoparathyroidism | SNOMED |
| Removed | condition_occurrence | 140821 | Spasm | SNOMED |
| Removed | condition_occurrence | 140949 | Infestation by Sarcoptes scabiei var hominis | SNOMED |
| Removed | condition_occurrence | 141004 | Lesion of radial nerve | SNOMED |
| Removed | condition_occurrence | 141249 | Benign neoplasm of thyroid gland | SNOMED |
| Removed | condition_occurrence | 141253 | Disorder of thyroid gland | SNOMED |
| Removed | condition_occurrence | 141456 | Chilblains | SNOMED |
| Removed | condition_occurrence | 192273 | Benign neoplasm of adrenal gland | SNOMED |
| Removed | condition_occurrence | 192353 | Disorder of gallbladder | SNOMED |
| Removed | condition_occurrence | 192357 | Paralytic ileus | SNOMED |
| Removed | condition_occurrence | 192359 | Renal failure syndrome | SNOMED |
| Removed | condition_occurrence | 192367 | Dysplasia of cervix | SNOMED |
| Removed | condition_occurrence | 192450 | Retention of urine | SNOMED |
| Removed | condition_occurrence | 192671 | Gastrointestinal hemorrhage | SNOMED |
| Removed | condition_occurrence | 192675 | Biliary cirrhosis | SNOMED |
| Removed | condition_occurrence | 192953 | Intestinal adhesions with obstruction | SNOMED |
| Removed | condition_occurrence | 192956 | Cholecystitis | SNOMED |
| Removed | condition_occurrence | 192957 | Perforation of bile duct | SNOMED |
| Removed | condition_occurrence | 193165 | Disorder of adrenal gland | SNOMED |
| Removed | condition_occurrence | 193242 | Perforation of intestine | SNOMED |
| Removed | condition_occurrence | 193439 | Benign neoplasm of body of uterus | SNOMED |
| Removed | condition_occurrence | 193518 | Intestinal obstruction | SNOMED |
| Removed | condition_occurrence | 193520 | Urinary bladder stone | SNOMED |
| Removed | condition_occurrence | 193722 | Benign tumor of endocrine pancreas | SNOMED |
| Removed | condition_occurrence | 194071 | Pylorospasm | SNOMED |
| Removed | condition_occurrence | 194081 | Acute cystitis | SNOMED |
| Removed | condition_occurrence | 194408 | Hydroureter | SNOMED |
| Removed | condition_occurrence | 194421 | Endometriosis of intestine | SNOMED |
| Removed | condition_occurrence | 194526 | Injury of trunk | SNOMED |
| Removed | condition_occurrence | 194589 | Primary malignant neoplasm of biliary tract | SNOMED |
| Removed | condition_occurrence | 194683 | Obstructed umbilical hernia | SNOMED |
| Removed | condition_occurrence | 194807 | Injury of inferior vena cava | SNOMED |
| Removed | condition_occurrence | 194990 | Inflammatory disease of liver | SNOMED |
| Removed | condition_occurrence | 194995 | Disorder of ureter | SNOMED |
| Removed | condition_occurrence | 194997 | Prostatitis | SNOMED |
| Removed | condition_occurrence | 195009 | Leukoplakia of penis | SNOMED |
| Removed | condition_occurrence | 195197 | Primary malignant neoplasm of vulva | SNOMED |
| Removed | condition_occurrence | 195313 | Urethral abscess | SNOMED |
| Removed | condition_occurrence | 195314 | Nephrotic syndrome | SNOMED |
| Removed | condition_occurrence | 195321 | Postmenopausal bleeding | SNOMED |
| Removed | condition_occurrence | 195401 | Contusion of hip | SNOMED |
| Removed | condition_occurrence | 195498 | Benign neoplasm of kidney | SNOMED |
| Removed | condition_occurrence | 195559 | Ruptured abdominal aortic aneurysm | SNOMED |
| Removed | condition_occurrence | 195562 | Hemorrhoids | SNOMED |
| Removed | condition_occurrence | 195588 | Cystitis | SNOMED |
| Removed | condition_occurrence | 195590 | Urethral stricture | SNOMED |
| Removed | condition_occurrence | 195596 | Chronic pancreatitis | SNOMED |
| Removed | condition_occurrence | 195603 | Vulval and/or perineal noninflammatory disorders | SNOMED |
| Removed | condition_occurrence | 195793 | Neoplasm of uncertain behavior of uterus | SNOMED |
| Removed | condition_occurrence | 195856 | Cholangitis | SNOMED |
| Removed | condition_occurrence | 195906 | Disorder of lumbar spine | SNOMED |
| Removed | condition_occurrence | 196044 | Primary malignant neoplasm of stomach | SNOMED |
| Removed | condition_occurrence | 196048 | Primary malignant neoplasm of vagina | SNOMED |
| Removed | condition_occurrence | 196151 | Functional disorder of intestine | SNOMED |
| Removed | condition_occurrence | 196152 | Peritonitis | SNOMED |
| Removed | condition_occurrence | 196160 | Fistula of intestine | SNOMED |
| Removed | condition_occurrence | 196168 | Irregular periods | SNOMED |
| Removed | condition_occurrence | 196359 | Primary malignant neoplasm of uterine cervix | SNOMED |
| Removed | condition_occurrence | 196360 | Primary malignant neoplasm of urinary bladder | SNOMED |
| Removed | condition_occurrence | 196431 | Hypersensitivity angiitis | SNOMED |
| Removed | condition_occurrence | 196463 | Alcoholic cirrhosis | SNOMED |
| Removed | condition_occurrence | 197034 | Intussusception of intestine | SNOMED |
| Removed | condition_occurrence | 197136 | Injury of small intestine without open wound into abdominal cavity | SNOMED |
| Removed | condition_occurrence | 197151 | Injury of abdominal aorta | SNOMED |
| Removed | condition_occurrence | 197236 | Uterine leiomyoma | SNOMED |
| Removed | condition_occurrence | 197237 | Benign neoplasm of prostate | SNOMED |
| Removed | condition_occurrence | 197253 | Hemolytic uremic syndrome | SNOMED |
| Removed | condition_occurrence | 197304 | Ulcer of lower extremity | SNOMED |
| Removed | condition_occurrence | 197320 | Acute kidney injury | SNOMED |
| Removed | condition_occurrence | 197500 | Primary malignant neoplasm of colon | SNOMED |
| Removed | condition_occurrence | 197593 | Impaction of intestine | SNOMED |
| Removed | condition_occurrence | 197603 | Intestinal volvulus | SNOMED |
| Removed | condition_occurrence | 197605 | Inflammatory disorder of male genital organ | SNOMED |
| Removed | condition_occurrence | 197607 | Excessive and frequent menstruation | SNOMED |
| Removed | condition_occurrence | 197672 | Urinary incontinence | SNOMED |
| Removed | condition_occurrence | 197675 | Incontinence of feces | SNOMED |
| Removed | condition_occurrence | 197917 | Disorder of biliary tract | SNOMED |
| Removed | condition_occurrence | 198010 | Injury of stomach without open wound into abdominal cavity | SNOMED |
| Removed | condition_occurrence | 198019 | Iliac blood vessel injury | SNOMED |
| Removed | condition_occurrence | 198202 | Cystocele | SNOMED |
| Removed | condition_occurrence | 198401 | Neoplasm of uncertain behavior of urinary bladder | SNOMED |
| Removed | condition_occurrence | 198402 | Neoplasm of uncertain behavior of kidney | SNOMED |
| Removed | condition_occurrence | 198446 | Embolism and thrombosis of the abdominal aorta | SNOMED |
| Removed | condition_occurrence | 198464 | Incisional hernia | SNOMED |
| Removed | condition_occurrence | 198465 | Acquired megacolon | SNOMED |
| Removed | condition_occurrence | 198475 | Gallstone ileus | SNOMED |
| Removed | condition_occurrence | 198571 | Cardiogenic shock | SNOMED |
| Removed | condition_occurrence | 198803 | Benign prostatic hyperplasia | SNOMED |
| Removed | condition_occurrence | 198809 | Acute cholecystitis | SNOMED |
| Removed | condition_occurrence | 198892 | Internal injury of abdominal organs without open wound into cavity | SNOMED |
| Removed | condition_occurrence | 198985 | Primary malignant neoplasm of kidney | SNOMED |
| Removed | condition_occurrence | 198988 | Primary malignant neoplasm of pelvis | SNOMED |
| Removed | condition_occurrence | 199064 | Chronic vascular insufficiency of intestine | SNOMED |
| Removed | condition_occurrence | 199074 | Acute pancreatitis | SNOMED |
| Removed | condition_occurrence | 199075 | Neurogenic urinary bladder | SNOMED |
| Removed | condition_occurrence | 199754 | Primary malignant neoplasm of pancreas | SNOMED |
| Removed | condition_occurrence | 199764 | Benign neoplasm of ovary | SNOMED |
| Removed | condition_occurrence | 199837 | Portal vein thrombosis | SNOMED |
| Removed | condition_occurrence | 199860 | Hernia of abdominal cavity | SNOMED |
| Removed | condition_occurrence | 199868 | Incisional hernia with gangrene | SNOMED |
| Removed | condition_occurrence | 200051 | Primary malignant neoplasm of ovary | SNOMED |
| Removed | condition_occurrence | 200052 | Primary malignant neoplasm of uterine adnexa | SNOMED |
| Removed | condition_occurrence | 200054 | Primary malignant neoplasm of ureter | SNOMED |
| Removed | condition_occurrence | 200174 | Disorder of skin and/or subcutaneous tissue | SNOMED |
| Removed | condition_occurrence | 200219 | Abdominal pain | SNOMED |
| Removed | condition_occurrence | 200447 | Gastrointestinal complication | SNOMED |
| Removed | condition_occurrence | 200675 | Neoplasm of uncertain behavior of ovary | SNOMED |
| Removed | condition_occurrence | 200831 | Congenital anomaly of penis | SNOMED |
| Removed | condition_occurrence | 200962 | Primary malignant neoplasm of prostate | SNOMED |
| Removed | condition_occurrence | 201061 | Diaphragmatic hernia | SNOMED |
| Removed | condition_occurrence | 201254 | Type 1 diabetes mellitus | SNOMED |
| Removed | condition_occurrence | 201265 | Disorder of spleen | SNOMED |
| Removed | condition_occurrence | 201337 | Disorder of urinary bladder | SNOMED |
| Removed | condition_occurrence | 201338 | Urethral fistula | SNOMED |
| Removed | condition_occurrence | 201353 | Radiation cystitis | SNOMED |
| Removed | condition_occurrence | 201606 | Crohn's disease | SNOMED |
| Removed | condition_occurrence | 201618 | Disorder of intestine | SNOMED |
| Removed | condition_occurrence | 201620 | Kidney stone | SNOMED |
| Removed | condition_occurrence | 201820 | Diabetes mellitus | SNOMED |
| Removed | condition_occurrence | 201824 | Benign neoplasm of urinary bladder | SNOMED |
| Removed | condition_occurrence | 201826 | Type 2 diabetes mellitus | SNOMED |
| Removed | condition_occurrence | 201894 | Acute vascular insufficiency of intestine | SNOMED |
| Removed | condition_occurrence | 201909 | Female infertility | SNOMED |
| Removed | condition_occurrence | 201916 | Ureteric stone | SNOMED |
| Removed | condition_occurrence | 201956 | Congenital anomaly of lower limb | SNOMED |
| Removed | condition_occurrence | 201965 | Shock | SNOMED |
| Removed | condition_occurrence | 253321 | Stridor | SNOMED |
| Removed | condition_occurrence | 253796 | Pneumothorax | SNOMED |
| Removed | condition_occurrence | 254061 | Pleural effusion | SNOMED |
| Removed | condition_occurrence | 254761 | Cough | SNOMED |
| Removed | condition_occurrence | 255302 | Spontaneous pneumothorax | SNOMED |
| Removed | condition_occurrence | 255573 | Chronic obstructive pulmonary disease | SNOMED |
| Removed | condition_occurrence | 255848 | Pneumonia | SNOMED |
| Removed | condition_occurrence | 256722 | Bronchopneumonia | SNOMED |
| Removed | condition_occurrence | 256723 | Pneumonia and influenza | SNOMED |
| Removed | condition_occurrence | 257012 | Chronic sinusitis | SNOMED |
| Removed | condition_occurrence | 257293 | Disorder of visual pathways | SNOMED |
| Removed | condition_occurrence | 257315 | Bacterial pneumonia | SNOMED |
| Removed | condition_occurrence | 257628 | Systemic lupus erythematosus | SNOMED |
| Removed | condition_occurrence | 257907 | Disorder of lung | SNOMED |
| Removed | condition_occurrence | 260131 | Disorder of bronchus | SNOMED |
| Removed | condition_occurrence | 261255 | Benign neoplasm of bronchus and lung | SNOMED |
| Removed | condition_occurrence | 261325 | Pulmonary emphysema | SNOMED |
| Removed | condition_occurrence | 261326 | Viral pneumonia | SNOMED |
| Removed | condition_occurrence | 261687 | Hemoptysis | SNOMED |
| Removed | condition_occurrence | 261880 | Atelectasis | SNOMED |
| Removed | condition_occurrence | 312327 | Acute myocardial infarction | SNOMED |
| Removed | condition_occurrence | 312437 | Dyspnea | SNOMED |
| Removed | condition_occurrence | 312938 | Hypertensive encephalopathy | SNOMED |
| Removed | condition_occurrence | 313459 | Sleep apnea | SNOMED |
| Removed | condition_occurrence | 314054 | Aortic valve disorder | SNOMED |
| Removed | condition_occurrence | 314658 | Cardiomegaly | SNOMED |
| Removed | condition_occurrence | 314659 | Arteritis | SNOMED |
| Removed | condition_occurrence | 314963 | Giant cell arteritis | SNOMED |
| Removed | condition_occurrence | 315078 | Palpitations | SNOMED |
| Removed | condition_occurrence | 315116 | Injury of carotid artery | SNOMED |
| Removed | condition_occurrence | 315273 | Mitral valve stenosis | SNOMED |
| Removed | condition_occurrence | 315286 | Chronic ischemic heart disease | SNOMED |
| Removed | condition_occurrence | 315296 | Preinfarction syndrome | SNOMED |
| Removed | condition_occurrence | 315564 | Aortic valve regurgitation | SNOMED |
| Removed | condition_occurrence | 315586 | Priapism | SNOMED |
| Removed | condition_occurrence | 316135 | Atrioventricular block | SNOMED |
| Removed | condition_occurrence | 316139 | Heart failure | SNOMED |
| Removed | condition_occurrence | 316457 | Mallory-Weiss syndrome | SNOMED |
| Removed | condition_occurrence | 316822 | Heart murmur | SNOMED |
| Removed | condition_occurrence | 316998 | Left bundle branch block | SNOMED |
| Removed | condition_occurrence | 316999 | Conduction disorder of the heart | SNOMED |
| Removed | condition_occurrence | 317002 | Low blood pressure | SNOMED |
| Removed | condition_occurrence | 317003 | Compression of vein | SNOMED |
| Removed | condition_occurrence | 317009 | Asthma | SNOMED |
| Removed | condition_occurrence | 317299 | Disorder of vitreous body | SNOMED |
| Removed | condition_occurrence | 317305 | Stricture of artery | SNOMED |
| Removed | condition_occurrence | 317814 | Benign neoplasm of heart | SNOMED |
| Removed | condition_occurrence | 317895 | Renovascular hypertension | SNOMED |
| Removed | condition_occurrence | 318736 | Migraine | SNOMED |
| Removed | condition_occurrence | 318772 | Disorder of pericardium | SNOMED |
| Removed | condition_occurrence | 319034 | Hypertensive heart disease without congestive heart failure | SNOMED |
| Removed | condition_occurrence | 319041 | Orthostatic hypotension | SNOMED |
| Removed | condition_occurrence | 319826 | Secondary hypertension | SNOMED |
| Removed | condition_occurrence | 319835 | Congestive heart failure | SNOMED |
| Removed | condition_occurrence | 319844 | Acute ischemic heart disease | SNOMED |
| Removed | condition_occurrence | 320116 | Acute pericarditis | SNOMED |
| Removed | condition_occurrence | 320128 | Essential hypertension | SNOMED |
| Removed | condition_occurrence | 320136 | Disorder of respiratory system | SNOMED |
| Removed | condition_occurrence | 320425 | Heart block | SNOMED |
| Removed | condition_occurrence | 320563 | Injury of heart without open wound into thorax | SNOMED |
| Removed | condition_occurrence | 320739 | Dissection of aorta | SNOMED |
| Removed | condition_occurrence | 320741 | Thrombophlebitis | SNOMED |
| Removed | condition_occurrence | 320744 | Complete atrioventricular block | SNOMED |
| Removed | condition_occurrence | 321042 | Cardiac arrest | SNOMED |
| Removed | condition_occurrence | 321052 | Peripheral vascular disease | SNOMED |
| Removed | condition_occurrence | 321107 | Congenital insufficiency of aortic valve | SNOMED |
| Removed | condition_occurrence | 321314 | Abdominal aortic aneurysm without rupture | SNOMED |
| Removed | condition_occurrence | 321318 | Angina pectoris | SNOMED |
| Removed | condition_occurrence | 321319 | Cardiomyopathy | SNOMED |
| Removed | condition_occurrence | 321588 | Heart disease | SNOMED |
| Removed | condition_occurrence | 321596 | Peripheral venous insufficiency | SNOMED |
| Removed | condition_occurrence | 321822 | Peripheral vascular disorder due to diabetes mellitus | SNOMED |
| Removed | condition_occurrence | 321886 | Rupture of artery | SNOMED |
| Removed | condition_occurrence | 321887 | Disorder of artery | SNOMED |
| Removed | condition_occurrence | 372324 | Eustachian tube disorder | SNOMED |
| Removed | condition_occurrence | 372328 | Otitis media | SNOMED |
| Removed | condition_occurrence | 372604 | Movement disorder | SNOMED |
| Removed | condition_occurrence | 372635 | Corneal degeneration | SNOMED |
| Removed | condition_occurrence | 372652 | Chronic tympanitis | SNOMED |
| Removed | condition_occurrence | 372887 | Disorder of brain | SNOMED |
| Removed | condition_occurrence | 372900 | Drug-induced dystonia | SNOMED |
| Removed | condition_occurrence | 373175 | Organic hallucinosis | SNOMED |
| Removed | condition_occurrence | 373176 | Organic mood disorder | SNOMED |
| Removed | condition_occurrence | 373474 | Diplopia | SNOMED |
| Removed | condition_occurrence | 373503 | Transient cerebral ischemia | SNOMED |
| Removed | condition_occurrence | 373852 | Neuralgia | SNOMED |
| Removed | condition_occurrence | 373995 | Delirium | SNOMED |
| Removed | condition_occurrence | 374009 | Organic mental disorder | SNOMED |
| Removed | condition_occurrence | 374027 | Lesion of ulnar nerve | SNOMED |
| Removed | condition_occurrence | 374034 | Visual disturbance | SNOMED |
| Removed | condition_occurrence | 374221 | Injury of brachial plexus | SNOMED |
| Removed | condition_occurrence | 374360 | Disorder of optic nerve | SNOMED |
| Removed | condition_occurrence | 374375 | Impacted cerumen | SNOMED |
| Removed | condition_occurrence | 374640 | Serous retinal detachment | SNOMED |
| Removed | condition_occurrence | 374915 | Focal epilepsy | SNOMED |
| Removed | condition_occurrence | 374919 | Multiple sclerosis | SNOMED |
| Removed | condition_occurrence | 374923 | Bell's palsy | SNOMED |
| Removed | condition_occurrence | 375415 | Injury of head | SNOMED |
| Removed | condition_occurrence | 375519 | Alcohol withdrawal | SNOMED |
| Removed | condition_occurrence | 375545 | Cataract | SNOMED |
| Removed | condition_occurrence | 375801 | Demyelinating disease of central nervous system | SNOMED |
| Removed | condition_occurrence | 376063 | Benign neoplasm of cerebral meninges | SNOMED |
| Removed | condition_occurrence | 376208 | Disorder of soft tissue | SNOMED |
| Removed | condition_occurrence | 376382 | Tension-type headache | SNOMED |
| Removed | condition_occurrence | 376387 | Spasmodic torticollis | SNOMED |
| Removed | condition_occurrence | 376647 | Primary malignant neoplasm of soft tissues | SNOMED |
| Removed | condition_occurrence | 377263 | Myoneural disorder | SNOMED |
| Removed | condition_occurrence | 377270 | Hereditary retinal dystrophy | SNOMED |
| Removed | condition_occurrence | 377573 | Central perforation of tympanic membrane | SNOMED |
| Removed | condition_occurrence | 377574 | Presbycusis | SNOMED |
| Removed | condition_occurrence | 377830 | Alcohol withdrawal delirium | SNOMED |
| Removed | condition_occurrence | 377845 | Anoxic encephalopathy | SNOMED |
| Removed | condition_occurrence | 377877 | Esotropia | SNOMED |
| Removed | condition_occurrence | 378253 | Headache | SNOMED |
| Removed | condition_occurrence | 378416 | Retinal disorder | SNOMED |
| Removed | condition_occurrence | 378419 | Alzheimer's disease | SNOMED |
| Removed | condition_occurrence | 378741 | Brachial plexus disorder | SNOMED |
| Removed | condition_occurrence | 379832 | Mixed conductive AND sensorineural hearing loss | SNOMED |
| Removed | condition_occurrence | 380055 | Primary malignant neoplasm of brain | SNOMED |
| Removed | condition_occurrence | 380094 | Carpal tunnel syndrome | SNOMED |
| Removed | condition_occurrence | 380102 | Corneal edema | SNOMED |
| Removed | condition_occurrence | 380378 | Epilepsy | SNOMED |
| Removed | condition_occurrence | 380731 | Otitis externa | SNOMED |
| Removed | condition_occurrence | 381270 | Parkinson's disease | SNOMED |
| Removed | condition_occurrence | 381295 | Senile cataract | SNOMED |
| Removed | condition_occurrence | 381316 | Cerebrovascular accident | SNOMED |
| Removed | condition_occurrence | 381549 | Migraine with aura | SNOMED |
| Removed | condition_occurrence | 381575 | Disorder of external ear | SNOMED |
| Removed | condition_occurrence | 381581 | Chalazion | SNOMED |
| Removed | condition_occurrence | 381854 | Disorder of conjunctiva | SNOMED |
| Removed | condition_occurrence | 381862 | Paralytic strabismus | SNOMED |
| Removed | condition_occurrence | 432257 | Primary malignant neoplasm of transverse colon | SNOMED |
| Removed | condition_occurrence | 432545 | Bacterial infectious disease | SNOMED |
| Removed | condition_occurrence | 432574 | Diffuse large B-cell lymphoma | SNOMED |
| Removed | condition_occurrence | 432582 | Neoplastic disease of uncertain behavior | SNOMED |
| Removed | condition_occurrence | 432585 | Blood coagulation disorder | SNOMED |
| Removed | condition_occurrence | 432595 | Amyloidosis | SNOMED |
| Removed | condition_occurrence | 432612 | Mild intellectual disability | SNOMED |
| Removed | condition_occurrence | 432621 | Purulent endophthalmitis | SNOMED |
| Removed | condition_occurrence | 432719 | Panniculitis | SNOMED |
| Removed | condition_occurrence | 432791 | Angioedema | SNOMED |
| Removed | condition_occurrence | 432795 | Traumatic or non-traumatic injury | SNOMED |
| Removed | condition_occurrence | 432796 | Poisoning by anesthetic agent | SNOMED |
| Removed | condition_occurrence | 432833 | Primary malignant neoplasm of oropharynx | SNOMED |
| Removed | condition_occurrence | 432837 | Primary malignant neoplasm of cecum | SNOMED |
| Removed | condition_occurrence | 432838 | Primary malignant neoplasm of cardia of stomach | SNOMED |
| Removed | condition_occurrence | 432843 | Primary malignant neoplasm of tail of pancreas | SNOMED |
| Removed | condition_occurrence | 432851 | Metastatic malignant neoplasm | SNOMED |
| Removed | condition_occurrence | 432870 | Thrombocytopenic disorder | SNOMED |
| Removed | condition_occurrence | 433316 | Dizziness and giddiness | SNOMED |
| Removed | condition_occurrence | 433329 | Closed fracture of second cervical vertebra | SNOMED |
| Removed | condition_occurrence | 433456 | Acute pain | SNOMED |
| Removed | condition_occurrence | 433515 | Chronic gastrojejunal ulcer with hemorrhage | SNOMED |
| Removed | condition_occurrence | 433524 | Disorder of appendix | SNOMED |
| Removed | condition_occurrence | 433527 | Endometriosis (clinical) | SNOMED |
| Removed | condition_occurrence | 433577 | Hammer toe | SNOMED |
| Removed | condition_occurrence | 433595 | Edema | SNOMED |
| Removed | condition_occurrence | 433716 | Primary malignant neoplasm of testis | SNOMED |
| Removed | condition_occurrence | 433736 | Obesity | SNOMED |
| Removed | condition_occurrence | 433741 | Familial erythrocytosis | SNOMED |
| Removed | condition_occurrence | 433811 | Hydronephrosis | SNOMED |
| Removed | condition_occurrence | 433991 | Recurrent major depression in remission | SNOMED |
| Removed | condition_occurrence | 434008 | White blood cell disorder | SNOMED |
| Removed | condition_occurrence | 434337 | Retinal vascular disorder | SNOMED |
| Removed | condition_occurrence | 434494 | Closed fracture of upper end of humerus | SNOMED |
| Removed | condition_occurrence | 434500 | Closed fracture of neck of femur | SNOMED |
| Removed | condition_occurrence | 434502 | Closed fracture of phalanx of foot | SNOMED |
| Removed | condition_occurrence | 434559 | Miliary tuberculosis | SNOMED |
| Removed | condition_occurrence | 434610 | Hyperkalemia | SNOMED |
| Removed | condition_occurrence | 434663 | Acute endocarditis | SNOMED |
| Removed | condition_occurrence | 434750 | Feeding difficulties and mismanagement | SNOMED |
| Removed | condition_occurrence | 434822 | Complication of internal prosthetic device | SNOMED |
| Removed | condition_occurrence | 434824 | Injury of cranial nerve | SNOMED |
| Removed | condition_occurrence | 434889 | Dissociative disorder | SNOMED |
| Removed | condition_occurrence | 434926 | Iridocyclitis | SNOMED |
| Removed | condition_occurrence | 435028 | Puerperal pyrexia of unknown origin | SNOMED |
| Removed | condition_occurrence | 435082 | Closed fracture of nasal bones | SNOMED |
| Removed | condition_occurrence | 435216 | Disorder due to type 1 diabetes mellitus | SNOMED |
| Removed | condition_occurrence | 435220 | Severe recurrent major depression without psychotic features | SNOMED |
| Removed | condition_occurrence | 435243 | Alcohol dependence | SNOMED |
| Removed | condition_occurrence | 435262 | Primary open angle glaucoma | SNOMED |
| Removed | condition_occurrence | 435371 | Hypothermia | SNOMED |
| Removed | condition_occurrence | 435508 | Adrenal cortical hypofunction | SNOMED |
| Removed | condition_occurrence | 435515 | Hypo-osmolality and or hyponatremia | SNOMED |
| Removed | condition_occurrence | 435524 | Sleep disorder | SNOMED |
| Removed | condition_occurrence | 435565 | Embolism and thrombosis of the vena cava | SNOMED |
| Removed | condition_occurrence | 435613 | Cellulitis | SNOMED |
| Removed | condition_occurrence | 435752 | Primary malignant neoplasm of duodenum | SNOMED |
| Removed | condition_occurrence | 435783 | Schizophrenia | SNOMED |
| Removed | condition_occurrence | 435785 | Meningitis | SNOMED |
| Removed | condition_occurrence | 435839 | Lymphedema | SNOMED |
| Removed | condition_occurrence | 435875 | Complication of pregnancy, childbirth and/or puerperium | SNOMED |
| Removed | condition_occurrence | 435928 | Abnormal weight loss | SNOMED |
| Removed | condition_occurrence | 436062 | Benign neoplasm of duodenum | SNOMED |
| Removed | condition_occurrence | 436091 | Bacterial meningitis | SNOMED |
| Removed | condition_occurrence | 436096 | Chronic pain | SNOMED |
| Removed | condition_occurrence | 436230 | Blood chemistry outside reference range | SNOMED |
| Removed | condition_occurrence | 436251 | Closed fracture of proximal end of ulna | SNOMED |
| Removed | condition_occurrence | 436252 | Closed fracture of shaft of tibia | SNOMED |
| Removed | condition_occurrence | 436389 | Cocaine dependence | SNOMED |
| Removed | condition_occurrence | 436398 | Glaucoma associated with ocular disorder | SNOMED |
| Removed | condition_occurrence | 436635 | Primary malignant neoplasm of sigmoid colon | SNOMED |
| Removed | condition_occurrence | 436659 | Iron deficiency anemia | SNOMED |
| Removed | condition_occurrence | 436665 | Bipolar disorder | SNOMED |
| Removed | condition_occurrence | 436682 | Moderate intellectual disability | SNOMED |
| Removed | condition_occurrence | 436700 | Exophthalmos | SNOMED |
| Removed | condition_occurrence | 436785 | Spinal stenosis in cervical region | SNOMED |
| Removed | condition_occurrence | 436839 | Closed fracture of metacarpal bone | SNOMED |
| Removed | condition_occurrence | 436996 | Thoracoabdominal aortic aneurysm | SNOMED |
| Removed | condition_occurrence | 437038 | Blood in urine | SNOMED |
| Removed | condition_occurrence | 437116 | Closed fracture of distal end of radius | SNOMED |
| Removed | condition_occurrence | 437233 | Multiple myeloma | SNOMED |
| Removed | condition_occurrence | 437306 | Transient global amnesia | SNOMED |
| Removed | condition_occurrence | 437461 | Disorder of prosthetic cardiac valve | SNOMED |
| Removed | condition_occurrence | 437496 | Epidemic vertigo | SNOMED |
| Removed | condition_occurrence | 437530 | Disorder of lipid metabolism | SNOMED |
| Removed | condition_occurrence | 437540 | Central retinal artery occlusion | SNOMED |
| Removed | condition_occurrence | 437541 | Glaucoma | SNOMED |
| Removed | condition_occurrence | 437611 | Ectopic pregnancy | SNOMED |
| Removed | condition_occurrence | 437643 | Abnormal gait | SNOMED |
| Removed | condition_occurrence | 437663 | Fever | SNOMED |
| Removed | condition_occurrence | 437671 | Abnormal feces | SNOMED |
| Removed | condition_occurrence | 437827 | Pure hypercholesterolemia | SNOMED |
| Removed | condition_occurrence | 437828 | Disorder of calcium metabolism | SNOMED |
| Removed | condition_occurrence | 437833 | Hypokalemia | SNOMED |
| Removed | condition_occurrence | 437904 | Laryngeal spasm | SNOMED |
| Removed | condition_occurrence | 437993 | Closed fracture of cervical spine | SNOMED |
| Removed | condition_occurrence | 438028 | Poisoning by drug AND/OR medicinal substance | SNOMED |
| Removed | condition_occurrence | 438120 | Opioid dependence | SNOMED |
| Removed | condition_occurrence | 438252 | Spontaneous ecchymosis | SNOMED |
| Removed | condition_occurrence | 438368 | Primary malignant neoplasm of thymus | SNOMED |
| Removed | condition_occurrence | 438406 | Severe major depression, single episode, with psychotic features | SNOMED |
| Removed | condition_occurrence | 438608 | Injury of axillary artery | SNOMED |
| Removed | condition_occurrence | 438688 | Sarcoidosis | SNOMED |
| Removed | condition_occurrence | 438693 | Primary malignant neoplasm of mediastinum | SNOMED |
| Removed | condition_occurrence | 438699 | Primary malignant neoplasm of rectosigmoid junction | SNOMED |
| Removed | condition_occurrence | 438887 | Closed fracture of shaft of femur | SNOMED |
| Removed | condition_occurrence | 439002 | Eating disorder | SNOMED |
| Removed | condition_occurrence | 439082 | Menopausal syndrome | SNOMED |
| Removed | condition_occurrence | 439254 | Bipolar affective disorder, current episode depression | SNOMED |
| Removed | condition_occurrence | 439297 | Nuclear senile cataract | SNOMED |
| Removed | condition_occurrence | 439404 | Primary malignant neoplasm of oral cavity | SNOMED |
| Removed | condition_occurrence | 439727 | Human immunodeficiency virus infection | SNOMED |
| Removed | condition_occurrence | 439776 | Autism spectrum disorder | SNOMED |
| Removed | condition_occurrence | 439777 | Anemia | SNOMED |
| Removed | condition_occurrence | 439846 | Left heart failure | SNOMED |
| Removed | condition_occurrence | 439907 | Non-traumatic tendon rupture | SNOMED |
| Removed | condition_occurrence | 439926 | Malaise and fatigue | SNOMED |
| Removed | condition_occurrence | 439928 | Gangrenous disorder | SNOMED |
| Removed | condition_occurrence | 440005 | Complication of medical care | SNOMED |
| Removed | condition_occurrence | 440029 | Viral disease | SNOMED |
| Removed | condition_occurrence | 440072 | Hypogammaglobulinemia | SNOMED |
| Removed | condition_occurrence | 440078 | Bipolar affective disorder, current episode manic | SNOMED |
| Removed | condition_occurrence | 440238 | Closed fracture of metatarsal bone | SNOMED |
| Removed | condition_occurrence | 440276 | Infection AND/OR inflammatory reaction due to internal prosthetic device, implant AND/OR graft | SNOMED |
| Removed | condition_occurrence | 440374 | Obsessive-compulsive disorder | SNOMED |
| Removed | condition_occurrence | 440392 | Retinal vascular occlusion | SNOMED |
| Removed | condition_occurrence | 440409 | Disorder of orbit proper | SNOMED |
| Removed | condition_occurrence | 440417 | Pulmonary embolism | SNOMED |
| Removed | condition_occurrence | 440548 | Closed fracture of femur, distal end | SNOMED |
| Removed | condition_occurrence | 440615 | Effect of exposure to external cause | SNOMED |
| Removed | condition_occurrence | 440649 | Primary malignant neoplasm of head of pancreas | SNOMED |
| Removed | condition_occurrence | 440703 | Trigeminal nerve disorder | SNOMED |
| Removed | condition_occurrence | 440971 | Neoplasm of uncertain behavior of testis | SNOMED |
| Removed | condition_occurrence | 441051 | Thoracic aortic aneurysm without rupture | SNOMED |
| Removed | condition_occurrence | 441207 | Adverse reaction to drug | SNOMED |
| Removed | condition_occurrence | 441225 | Primary malignant neoplasm of ampulla of Vater | SNOMED |
| Removed | condition_occurrence | 441259 | Non-thrombocytopenic purpura | SNOMED |
| Removed | condition_occurrence | 441269 | Autoimmune hemolytic anemia | SNOMED |
| Removed | condition_occurrence | 441364 | Complication of the puerperium | SNOMED |
| Removed | condition_occurrence | 441534 | Severe major depression, single episode, without psychotic features | SNOMED |
| Removed | condition_occurrence | 441553 | Myoclonus | SNOMED |
| Removed | condition_occurrence | 441641 | Delivery normal | SNOMED |
| Removed | condition_occurrence | 441800 | Primary malignant neoplasm of descending colon | SNOMED |
| Removed | condition_occurrence | 441818 | Hemangioma | SNOMED |
| Removed | condition_occurrence | 441829 | Hyperosmolality and or hypernatremia | SNOMED |
| Removed | condition_occurrence | 441830 | Disorder of fluid AND/OR electrolyte | SNOMED |
| Removed | condition_occurrence | 441838 | Personality disorder | SNOMED |
| Removed | condition_occurrence | 441840 | Clinical finding | SNOMED |
| Removed | condition_occurrence | 441875 | Thoracic aortic aneurysm which has ruptured | SNOMED |
| Removed | condition_occurrence | 441973 | Closed fracture of proximal end of radius | SNOMED |
| Removed | condition_occurrence | 442019 | Complication of procedure | SNOMED |
| Removed | condition_occurrence | 442108 | Benign neoplasm of cecum | SNOMED |
| Removed | condition_occurrence | 442129 | Neoplasm of uncertain behavior of ureter | SNOMED |
| Removed | condition_occurrence | 442263 | Basilar artery stenosis | SNOMED |
| Removed | condition_occurrence | 442553 | Injury of urinary bladder | SNOMED |
| Removed | condition_occurrence | 442562 | Poisoning | SNOMED |
| Removed | condition_occurrence | 442615 | Carotid artery stenosis | SNOMED |
| Removed | condition_occurrence | 442639 | Injury of colon without open wound into abdominal cavity | SNOMED |
| Removed | condition_occurrence | 442752 | Muscle pain | SNOMED |
| Removed | condition_occurrence | 442793 | Complication due to diabetes mellitus | SNOMED |
| Removed | condition_occurrence | 443344 | Barrett's esophagus | SNOMED |
| Removed | condition_occurrence | 443454 | Cerebral infarction | SNOMED |
| Removed | condition_occurrence | 443597 | Chronic kidney disease stage 3 | SNOMED |
| Removed | condition_occurrence | 443605 | Vascular dementia | SNOMED |
| Removed | condition_occurrence | 443611 | Chronic kidney disease stage 5 | SNOMED |
| Removed | condition_occurrence | 443612 | Chronic kidney disease stage 4 | SNOMED |
| Removed | condition_occurrence | 443614 | Chronic kidney disease stage 1 | SNOMED |
| Removed | condition_occurrence | 443617 | Conduct disorder | SNOMED |
| Removed | condition_occurrence | 443727 | Diabetic ketoacidosis | SNOMED |
| Removed | condition_occurrence | 443732 | Disorder due to type 2 diabetes mellitus | SNOMED |
| Removed | condition_occurrence | 443782 | Tremor | SNOMED |
| Removed | condition_occurrence | 443792 | Calculus of bile duct | SNOMED |
| Removed | condition_occurrence | 443929 | Postpartum hemorrhage | SNOMED |
| Removed | condition_occurrence | 443943 | Herpes zoster | SNOMED |
| Removed | condition_occurrence | 443962 | Mitral valve regurgitation | SNOMED |
| Removed | condition_occurrence | 444070 | Tachycardia | SNOMED |
| Removed | condition_occurrence | 444079 | Psychogenic fugue | SNOMED |
| Removed | condition_occurrence | 444084 | Hypersensitivity pneumonitis | SNOMED |
| Removed | condition_occurrence | 444095 | Injury of ureter without open wound into abdominal cavity | SNOMED |
| Removed | condition_occurrence | 444100 | Mood disorder | SNOMED |
| Removed | condition_occurrence | 444187 | Open wound | SNOMED |
| Removed | condition_occurrence | 444239 | Postprocedural state finding | SNOMED |
| Removed | condition_occurrence | 444264 | Thrombosis of iliac artery | SNOMED |
| Removed | condition_occurrence | 444459 | Benign neoplasm of sigmoid colon | SNOMED |
| Removed | condition_occurrence | 606805 | Poisoning caused by opioid receptor agonist | SNOMED |
| Removed | condition_occurrence | 607208 | Acute alcohol intoxication | SNOMED |
| Removed | condition_occurrence | 608027 | Poisoning caused by gaseous substance | SNOMED |
| Removed | condition_occurrence | 619430 | Lichen sclerosus | SNOMED |
| Removed | drug_exposure | 702006 | technetium | RxNorm |
| Removed | drug_exposure | 702007 | florbetaben | RxNorm |
| Removed | drug_exposure | 702291 | maribavir | RxNorm |
| Removed | drug_exposure | 735843 | natalizumab | RxNorm |
| Removed | drug_exposure | 778806 | drospirenone / estradiol | RxNorm |
| Removed | drug_exposure | 778978 | cytarabine / daunorubicin | RxNorm |
| Removed | drug_exposure | 779055 | casirivimab / imdevimab | RxNorm |
| Removed | drug_exposure | 902725 | Doxorubicin pegylated liposomal | RxNorm Extension |
| Removed | drug_exposure | 902730 | Cytarabine liposomal | RxNorm Extension |
| Removed | drug_exposure | 905078 | trifluridine | RxNorm |
| Removed | drug_exposure | 977968 | sodium citrate | RxNorm |
| Removed | condition_occurrence | 1075809 | Lesion of femoral nerve | SNOMED |
| Removed | measurement | 1091076 | Dacrocytes [Presence] in Blood | LOINC |
| Removed | measurement | 1091281 | Kappa light chains.free/Lambda light chains.free [Mass Ratio] in Serum or Plasma | LOINC |
| Removed | measurement | 1091352 | Poikilocytosis [Presence] in Blood | LOINC |
| Removed | measurement | 1091481 | Hyaline casts [Presence] in Urine sediment | LOINC |
| Removed | measurement | 1091589 | Elliptocytes [Presence] in Blood | LOINC |
| Removed | measurement | 1091726 | Schistocytes [Presence] in Blood | LOINC |
| Removed | measurement | 1092029 | Giardia lamblia DNA [Presence] in Stool | LOINC |
| Removed | measurement | 1092210 | Target cells [Presence] in Blood | LOINC |
| Removed | measurement | 1092437 | Dohle body [Presence] in Blood | LOINC |
| Removed | measurement | 1092441 | Hematocrit [Pure volume fraction] of Blood by calculation | LOINC |
| Removed | condition_occurrence | 1245117 | Vasopressin-related polyuria | SNOMED |
| Removed | drug_exposure | 1333357 | busulfan | RxNorm |
| Removed | drug_exposure | 1333379 | arsenic trioxide | RxNorm |
| Removed | drug_exposure | 1335301 | phenoxybenzamine | RxNorm |
| Removed | drug_exposure | 1343346 | vinorelbine | RxNorm |
| Removed | drug_exposure | 1350066 | carmustine | RxNorm |
| Removed | drug_exposure | 1367268 | irinotecan | RxNorm |
| Removed | drug_exposure | 1378509 | topotecan | RxNorm |
| Removed | drug_exposure | 1389112 | Echinacea preparation | RxNorm |
| Removed | drug_exposure | 1395773 | iron sucrose | RxNorm |
| Removed | condition_occurrence | 1450471 | Chronic primary bladder pain syndrome | SNOMED |
| Removed | drug_exposure | 1523280 | diazoxide | RxNorm |
| Removed | drug_exposure | 1586346 | insulin, regular, pork | RxNorm |
| Removed | drug_exposure | 1745072 | cidofovir | RxNorm |
| Removed | measurement | 3001258 | Hemoglobin C/Hemoglobin.total in Blood | LOINC |
| Removed | measurement | 3002364 | Opiates [Mass/volume] in Urine | LOINC |
| Removed | measurement | 3003985 | Beta hydroxybutyrate [Moles/volume] in Serum or Plasma | LOINC |
| Removed | measurement | 3004582 | Left ventricular Cardiac output by US.doppler | LOINC |
| Removed | measurement | 3006796 | Barbiturates [Mass/volume] in Urine | LOINC |
| Removed | measurement | 3008649 | Pulse wave form Femoral artery - right by US.doppler | LOINC |
| Removed | measurement | 3008793 | Fluid output biliary drain | LOINC |
| Removed | measurement | 3009083 | Pulse wave form Brachial artery - right by US.doppler | LOINC |
| Removed | measurement | 3009337 | Methadone [Mass/volume] in Urine | LOINC |
| Removed | measurement | 3011258 | Bilirubin.total [Presence] in Urine | LOINC |
| Removed | measurement | 3011974 | Cocaine [Mass/volume] in Serum or Plasma | LOINC |
| Removed | measurement | 3012516 | Albumin [Mass/volume] in Urine | LOINC |
| Removed | measurement | 3013803 | Aspergillus fumigatus IgG Ab [Mass/volume] in Serum | LOINC |
| Removed | measurement | 3014415 | Pulse wave form Brachial artery - left by US.doppler | LOINC |
| Removed | measurement | 3015528 | Cannabinoids [Mass/volume] in Serum or Plasma | LOINC |
| Removed | measurement | 3017680 | Myelocytes [#/volume] in Blood by Manual count | LOINC |
| Removed | measurement | 3020401 | E Ag [Presence] on Red Blood Cells from Donor | LOINC |
| Removed | measurement | 3020428 | Hemoglobin A/Hemoglobin.total in Blood | LOINC |
| Removed | measurement | 3020725 | Methylenedioxymethamphetamine [Mass/volume] in Urine | LOINC |
| Removed | measurement | 3020784 | Hemoglobin A2/Hemoglobin.total in Blood | LOINC |
| Removed | measurement | 3022445 | Amphetamines [Mass/volume] in Serum or Plasma | LOINC |
| Removed | measurement | 3024342 | Plasma cells [#/volume] in Blood by Manual count | LOINC |
| Removed | measurement | 3024456 | Kell group Ag [Type] on Red Blood Cells | LOINC |
| Removed | measurement | 3025408 | Oxygen/Inspired gas Respiratory system by O2 Analyzer --on ventilator | LOINC |
| Removed | measurement | 3025770 | Benzodiazepines [Mass/volume] in Urine | LOINC |
| Removed | measurement | 3027035 | Albumin [Mass/time] in 24 hour Urine | LOINC |
| Removed | measurement | 3027238 | Thyroperoxidase Ab [Units/volume] in Serum or Plasma | LOINC |
| Removed | measurement | 3033195 | Leukocytes other [#/volume] in Synovial fluid | LOINC |
| Removed | measurement | 3034387 | Apolipoprotein B-100 [Mass/volume] in Serum or Plasma | LOINC |
| Removed | measurement | 3037185 | Protein [Presence] in Urine | LOINC |
| Removed | measurement | 3038691 | Anisocytosis [Presence] in Blood | LOINC |
| Removed | measurement | 3046071 | Choriogonadotropin.intact+Beta subunit [Units/volume] in Serum or Plasma | LOINC |
| Removed | condition_occurrence | 3655118 | Respiratory condition caused by chemical fumes | SNOMED |
| Removed | condition_occurrence | 3663197 | Glaucoma suspect | SNOMED |
| Removed | condition_occurrence | 4000609 | Disorder of upper gastrointestinal tract | SNOMED |
| Removed | condition_occurrence | 4000968 | Biceps tendinitis | SNOMED |
| Removed | condition_occurrence | 4001336 | Concussion injury of brain | SNOMED |
| Removed | condition_occurrence | 4001664 | Intrahepatic bile duct carcinoma | SNOMED |
| Removed | condition_occurrence | 4001666 | Mesothelioma of peritoneum | SNOMED |
| Removed | condition_occurrence | 4001670 | Ductal carcinoma in situ of breast | SNOMED |
| Removed | condition_occurrence | 4002497 | Acute promyelocytic leukemia, FAB M3 | SNOMED |
| Removed | condition_occurrence | 4006971 | Tricuspid valve regurgitation | SNOMED |
| Removed | condition_occurrence | 4009610 | Closed fracture proximal femur, subtrochanteric | SNOMED |
| Removed | condition_occurrence | 4010333 | Postmenopausal osteoporosis | SNOMED |
| Removed | condition_occurrence | 4010658 | Difficulty passing urine | SNOMED |
| Removed | condition_occurrence | 4013596 | Closed fracture thoracic vertebra | SNOMED |
| Removed | condition_occurrence | 4013604 | Closed fracture lumbar vertebra | SNOMED |
| Removed | condition_occurrence | 4013613 | Fracture of lumbar spine and/or pelvis | SNOMED |
| Removed | condition_occurrence | 4013643 | Pulmonary arterial hypertension | SNOMED |
| Removed | condition_occurrence | 4014023 | Palliative care | SNOMED |
| Removed | condition_occurrence | 4014781 | Closed traumatic subdural hemorrhage | SNOMED |
| Removed | condition_occurrence | 4016548 | Closed injury of pleura | SNOMED |
| Removed | condition_occurrence | 4021166 | Care regime | SNOMED |
| Removed | condition_occurrence | 4022569 | Eating / feeding / drinking finding | SNOMED |
| Removed | condition_occurrence | 4027460 | Closed pertrochanteric fracture | SNOMED |
| Removed | condition_occurrence | 4030065 | Hyposplenism | SNOMED |
| Removed | condition_occurrence | 4032243 | Dialysis procedure | SNOMED |
| Removed | condition_occurrence | 4032334 | Hyperbilirubinemia | SNOMED |
| Removed | condition_occurrence | 4033319 | Lipoma of skin and subcutaneous tissue of trunk | SNOMED |
| Removed | condition_occurrence | 4033837 | Melanocytic nevus of trunk | SNOMED |
| Removed | condition_occurrence | 4038835 | Hodgkin's disease (clinical) | SNOMED |
| Removed | condition_occurrence | 4038838 | Non-Hodgkin's lymphoma (clinical) | SNOMED |
| Removed | condition_occurrence | 4039691 | Necrotizing vasculitis | SNOMED |
| Removed | condition_occurrence | 4040820 | Rheumatic disease of mitral AND aortic valves | SNOMED |
| Removed | condition_occurrence | 4043371 | Inflammatory disorder of digestive tract | SNOMED |
| Removed | condition_occurrence | 4043731 | Infarction - precerebral | SNOMED |
| Removed | condition_occurrence | 4043738 | Hydrocephalus | SNOMED |
| Removed | condition_occurrence | 4044404 | Lumbosacral plexus neuropathy | SNOMED |
| Removed | condition_occurrence | 4045733 | Cerebrovascular and spinal vascular disorders | SNOMED |
| Removed | condition_occurrence | 4046205 | Discitis | SNOMED |
| Removed | condition_occurrence | 4046500 | Acute peptic ulcer with hemorrhage | SNOMED |
| Removed | condition_occurrence | 4049659 | Subcortical hemorrhage | SNOMED |
| Removed | condition_occurrence | 4050977 | Wernicke's disease | SNOMED |
| Removed | condition_occurrence | 4051005 | Open wound of nose | SNOMED |
| Removed | condition_occurrence | 4051140 | Open wound of anterior abdominal wall | SNOMED |
| Removed | condition_occurrence | 4052213 | Injury to blood vessels of lower limb | SNOMED |
| Removed | condition_occurrence | 4053272 | Injury of spleen | SNOMED |
| Removed | condition_occurrence | 4053584 | Superficial injury | SNOMED |
| Removed | condition_occurrence | 4053597 | Open wound of neck | SNOMED |
| Removed | condition_occurrence | 4053604 | Open wound of lower leg | SNOMED |
| Removed | condition_occurrence | 4054671 | Corrosion of esophagus | SNOMED |
| Removed | condition_occurrence | 4054884 | Multiple open wounds of hip and/or thigh | SNOMED |
| Removed | condition_occurrence | 4055224 | Toxic liver disease | SNOMED |
| Removed | condition_occurrence | 4055341 | Calculus of bile duct with cholangitis | SNOMED |
| Removed | condition_occurrence | 4056770 | Breast signs and symptoms | SNOMED |
| Removed | condition_occurrence | 4057953 | Acute gastric ulcer with perforation | SNOMED |
| Removed | condition_occurrence | 4059290 | Steatotic liver disease | SNOMED |
| Removed | condition_occurrence | 4059379 | Mitochondrial myopathy | SNOMED |
| Removed | condition_occurrence | 4060036 | Obstructed labor due to breech presentation | SNOMED |
| Removed | condition_occurrence | 4061074 | Periodic paralysis | SNOMED |
| Removed | condition_occurrence | 4062771 | Examination for suspected neoplasm | SNOMED |
| Removed | condition_occurrence | 4062856 | Examination for suspected cardiovascular disease | SNOMED |
| Removed | condition_occurrence | 4063519 | Examination for suspected mental disorder | SNOMED |
| Removed | condition_occurrence | 4064036 | Generalized skin eruption caused by drug and medicament | SNOMED |
| Removed | condition_occurrence | 4064161 | Cirrhosis of liver | SNOMED |
| Removed | condition_occurrence | 4064522 | Medical examination for suspected condition | SNOMED |
| Removed | condition_occurrence | 4067311 | Lumbar discitis | SNOMED |
| Removed | condition_occurrence | 4068155 | Atrial arrhythmia | SNOMED |
| Removed | condition_occurrence | 4077577 | Moderate recurrent major depression | SNOMED |
| Removed | condition_occurrence | 4079749 | Osteoarthritis of hip | SNOMED |
| Removed | condition_occurrence | 4079750 | Osteoarthritis of knee | SNOMED |
| Removed | condition_occurrence | 4080762 | Psychoactive substance dependence | SNOMED |
| Removed | condition_occurrence | 4082463 | Monoclonal gammopathy of uncertain significance | SNOMED |
| Removed | condition_occurrence | 4083100 | Fasciitis with eosinophilia syndrome | SNOMED |
| Removed | condition_occurrence | 4085922 | Infection screening | SNOMED |
| Removed | condition_occurrence | 4085923 | Examination for accident | SNOMED |
| Removed | condition_occurrence | 4086195 | Superficial injury of head | SNOMED |
| Removed | condition_occurrence | 4088051 | Closed fracture of phalanx of finger | SNOMED |
| Removed | condition_occurrence | 4089462 | Ventricular premature complex | SNOMED |
| Removed | condition_occurrence | 4092686 | Human immunodeficiency virus infection with secondary clinical infectious disease | SNOMED |
| Removed | condition_occurrence | 4093228 | Disorder of soft tissue of lower limb | SNOMED |
| Removed | condition_occurrence | 4094235 | Psychosomatic factor in physical condition | SNOMED |
| Removed | condition_occurrence | 4094283 | Lower limb joint arthritis | SNOMED |
| Removed | condition_occurrence | 4094822 | Foreign body in respiratory tract | SNOMED |
| Removed | condition_occurrence | 4096479 | Traumatic amputation | SNOMED |
| Removed | condition_occurrence | 4096682 | Bleeding from nose | SNOMED |
| Removed | condition_occurrence | 4097550 | Legionella infection | SNOMED |
| Removed | condition_occurrence | 4097962 | Open wound of lower limb | SNOMED |
| Removed | condition_occurrence | 4098597 | Waldenström macroglobulinemia | SNOMED |
| Removed | condition_occurrence | 4100184 | Pustular psoriasis of palms and soles | SNOMED |
| Removed | condition_occurrence | 4100857 | Extreme obesity with alveolar hypoventilation | SNOMED |
| Removed | condition_occurrence | 4101149 | Non-organic psychosis | SNOMED |
| Removed | condition_occurrence | 4101256 | Cocaine intoxication | SNOMED |
| Removed | condition_occurrence | 4102177 | Iris and ciliary body vascular disorder | SNOMED |
| Removed | condition_occurrence | 4102631 | Acute tubulointerstitial nephritis | SNOMED |
| Removed | condition_occurrence | 4102739 | Screening for cardiovascular system disease | SNOMED |
| Removed | condition_occurrence | 4103295 | Ventricular tachycardia | SNOMED |
| Removed | condition_occurrence | 4103399 | Emotionally unstable personality disorder | SNOMED |
| Removed | condition_occurrence | 4103532 | Immune thrombocytopenia | SNOMED |
| Removed | condition_occurrence | 4103638 | Amputated above knee | SNOMED |
| Removed | condition_occurrence | 4103703 | Melena | SNOMED |
| Removed | condition_occurrence | 4105773 | Acute epiglottitis | SNOMED |
| Removed | condition_occurrence | 4108235 | Combined disorders of mitral, aortic and tricuspid valves | SNOMED |
| Removed | condition_occurrence | 4108637 | Superficial injury of nose | SNOMED |
| Removed | condition_occurrence | 4108814 | Pericardial effusion - noninflammatory | SNOMED |
| Removed | condition_occurrence | 4111566 | Disorders of both mitral and tricuspid valves | SNOMED |
| Removed | condition_occurrence | 4111700 | Ventricular fibrillation and flutter | SNOMED |
| Removed | condition_occurrence | 4111917 | Malignant mesothelioma of pleura | SNOMED |
| Removed | condition_occurrence | 4112839 | Pneumonitis caused by inhalation of regurgitated food | SNOMED |
| Removed | condition_occurrence | 4113129 | Benign tumor of soft tissue of head, face and neck | SNOMED |
| Removed | condition_occurrence | 4115173 | Atrial premature complex | SNOMED |
| Removed | condition_occurrence | 4115282 | Trichilemmal cyst | SNOMED |
| Removed | condition_occurrence | 4116209 | Acute inflammation of lacrimal passages | SNOMED |
| Removed | condition_occurrence | 4118910 | Maternal hypertension | SNOMED |
| Removed | condition_occurrence | 4119130 | Malignant lymphoma - small lymphocytic | SNOMED |
| Removed | condition_occurrence | 4119460 | Infective endocarditis | SNOMED |
| Removed | condition_occurrence | 4119786 | Interstitial lung disease | SNOMED |
| Removed | condition_occurrence | 4120088 | Cardiac arrest with successful resuscitation | SNOMED |
| Removed | condition_occurrence | 4124693 | Hypertrophic cardiomyopathy | SNOMED |
| Removed | condition_occurrence | 4126119 | Toxic nephropathy | SNOMED |
| Removed | condition_occurrence | 4127726 | Functional disorder of penis | SNOMED |
| Removed | condition_occurrence | 4130852 | Injury of lower limb | SNOMED |
| Removed | condition_occurrence | 4133224 | Lobar pneumonia | SNOMED |
| Removed | condition_occurrence | 4134162 | Subarachnoid hemorrhage due to traumatic injury | SNOMED |
| Removed | condition_occurrence | 4134455 | Mononeuropathy | SNOMED |
| Removed | condition_occurrence | 4134552 | Hereditary motor and sensory neuropathy | SNOMED |
| Removed | condition_occurrence | 4134603 | Vascular disorder of intestine | SNOMED |
| Removed | condition_occurrence | 4135466 | Hemothorax | SNOMED |
| Removed | condition_occurrence | 4135822 | Primary biliary cholangitis | SNOMED |
| Removed | condition_occurrence | 4136335 | Thrombosis of arteries of upper extremity | SNOMED |
| Removed | condition_occurrence | 4138149 | Dislocation of acromioclavicular joint | SNOMED |
| Removed | condition_occurrence | 4141028 | Cervical disc disorder | SNOMED |
| Removed | condition_occurrence | 4141360 | Chronic atrial fibrillation | SNOMED |
| Removed | condition_occurrence | 4144111 | Gastroesophageal reflux disease without esophagitis | SNOMED |
| Removed | condition_occurrence | 4144835 | Crushing injury of chest | SNOMED |
| Removed | condition_occurrence | 4144895 | Flaccid neurogenic urinary bladder | SNOMED |
| Removed | condition_occurrence | 4145825 | Anorectal disorder | SNOMED |
| Removed | condition_occurrence | 4146116 | Nystagmus and other irregular eye movements | SNOMED |
| Removed | condition_occurrence | 4147411 | Follicular lymphoma | SNOMED |
| Removed | condition_occurrence | 4147498 | Encephalitis, myelitis and encephalomyelitis | SNOMED |
| Removed | condition_occurrence | 4148906 | Spontaneous subarachnoid hemorrhage | SNOMED |
| Removed | condition_occurrence | 4150301 | Stenosis and insufficiency of lacrimal passages | SNOMED |
| Removed | condition_occurrence | 4150799 | Dissociative motor disorder | SNOMED |
| Removed | condition_occurrence | 4151109 | Partial thickness burn of wrist and hand | SNOMED |
| Removed | condition_occurrence | 4151134 | Cyst of pancreas | SNOMED |
| Removed | condition_occurrence | 4151250 | Malignant neoplasm of upper lobe, bronchus or lung | SNOMED |
| Removed | condition_occurrence | 4152169 | Failure of genital response | SNOMED |
| Removed | condition_occurrence | 4152592 | Spinal stenosis of lumbosacral region | SNOMED |
| Removed | condition_occurrence | 4152780 | Presence of orthopedic joint implant | SNOMED |
| Removed | condition_occurrence | 4153292 | Schizoaffective disorder, manic type | SNOMED |
| Removed | condition_occurrence | 4153359 | Arthritis of spine | SNOMED |
| Removed | condition_occurrence | 4153739 | Open wound of larynx and trachea | SNOMED |
| Removed | condition_occurrence | 4153877 | Post-traumatic wound infection | SNOMED |
| Removed | condition_occurrence | 4154290 | Paroxysmal atrial fibrillation | SNOMED |
| Removed | condition_occurrence | 4155910 | Generalized edema | SNOMED |
| Removed | condition_occurrence | 4159691 | Poisoning by anti-psychotic agent | SNOMED |
| Removed | condition_occurrence | 4162253 | Primary malignant neoplasm of breast | SNOMED |
| Removed | condition_occurrence | 4164770 | Guillain-Barré syndrome | SNOMED |
| Removed | condition_occurrence | 4164898 | Diverticulosis of large intestine without diverticulitis | SNOMED |
| Removed | condition_occurrence | 4165998 | Generalized enlarged lymph nodes | SNOMED |
| Removed | condition_occurrence | 4166844 | Intraventricular conduction defect | SNOMED |
| Removed | condition_occurrence | 4167217 | Family history of clinical finding | SNOMED |
| Removed | condition_occurrence | 4168700 | Localized enlarged lymph nodes | SNOMED |
| Removed | condition_occurrence | 4169095 | Bradycardia | SNOMED |
| Removed | condition_occurrence | 4169287 | Itching of skin | SNOMED |
| Removed | condition_occurrence | 4170137 | Non-suppurative otitis media | SNOMED |
| Removed | condition_occurrence | 4170143 | Respiratory tract infection | SNOMED |
| Removed | condition_occurrence | 4171594 | Family history of malignant neoplasm | SNOMED |
| Removed | condition_occurrence | 4171917 | Localized edema | SNOMED |
| Removed | condition_occurrence | 4173746 | Hallucinogen intoxication | SNOMED |
| Removed | condition_occurrence | 4173824 | B-cell chronic lymphocytic leukemia variant | SNOMED |
| Removed | condition_occurrence | 4174262 | Polyneuropathy | SNOMED |
| Removed | condition_occurrence | 4175154 | Disorder of the peripheral nervous system | SNOMED |
| Removed | condition_occurrence | 4176725 | Retroperitoneal fibrosis | SNOMED |
| Removed | condition_occurrence | 4177112 | Malignant tumor of trachea | SNOMED |
| Removed | condition_occurrence | 4177206 | Tubulointerstitial nephritis | SNOMED |
| Removed | condition_occurrence | 4179963 | Family history of breast cancer | SNOMED |
| Removed | condition_occurrence | 4181064 | Inflammatory disorder of extremity | SNOMED |
| Removed | condition_occurrence | 4181705 | Varicose veins of lower limb without ulcer and without inflammation | SNOMED |
| Removed | condition_occurrence | 4182210 | Dementia | SNOMED |
| Removed | condition_occurrence | 4182562 | Lower abdominal pain | SNOMED |
| Removed | condition_occurrence | 4182711 | Vasculitis of the skin | SNOMED |
| Removed | condition_occurrence | 4184976 | Angioimmunoblastic T-cell lymphoma | SNOMED |
| Removed | condition_occurrence | 4187067 | Disorder of coronary artery | SNOMED |
| Removed | condition_occurrence | 4188155 | Hernia of anterior abdominal wall | SNOMED |
| Removed | condition_occurrence | 4189293 | Vascular disorder of lower extremity | SNOMED |
| Removed | condition_occurrence | 4189343 | Aortic valve stenosis | SNOMED |
| Removed | condition_occurrence | 4191479 | Allergic asthma | SNOMED |
| Removed | condition_occurrence | 4192174 | Illness | SNOMED |
| Removed | condition_occurrence | 4193868 | Sedative, hypnotic AND/OR anxiolytic-related disorder | SNOMED |
| Removed | condition_occurrence | 4194894 | Muscle and tendon injury | SNOMED |
| Removed | condition_occurrence | 4195694 | Acute respiratory distress syndrome | SNOMED |
| Removed | condition_occurrence | 4195847 | Acute peritonitis | SNOMED |
| Removed | condition_occurrence | 4200520 | Neck swelling | SNOMED |
| Removed | condition_occurrence | 4201174 | Injury of lung | SNOMED |
| Removed | condition_occurrence | 4201387 | Tracheostomy present | SNOMED |
| Removed | condition_occurrence | 4201717 | Ileostomy present | SNOMED |
| Removed | condition_occurrence | 4203625 | Chronic constrictive pericarditis | SNOMED |
| Removed | condition_occurrence | 4206148 | Syncope and collapse | SNOMED |
| Removed | condition_occurrence | 4208719 | Pharyngeal hemorrhage | SNOMED |
| Removed | condition_occurrence | 4209746 | Duodenal ulcer without hemorrhage AND without perforation | SNOMED |
| Removed | condition_occurrence | 4211657 | Closed fracture of lower leg | SNOMED |
| Removed | condition_occurrence | 4213373 | Dislocation of shoulder joint | SNOMED |
| Removed | condition_occurrence | 4214376 | Hyperglycemia | SNOMED |
| Removed | condition_occurrence | 4216397 | Nerve root disorder | SNOMED |
| Removed | condition_occurrence | 4216493 | Cocaine withdrawal | SNOMED |
| Removed | condition_occurrence | 4216972 | Bursitis of hip | SNOMED |
| Removed | condition_occurrence | 4217075 | Infectious pericarditis | SNOMED |
| Removed | condition_occurrence | 4220631 | Injury of kidney | SNOMED |
| Removed | condition_occurrence | 4221821 | Thrombophlebitis of deep veins of lower extremity | SNOMED |
| Removed | condition_occurrence | 4224926 | Obstruction of esophagus | SNOMED |
| Removed | condition_occurrence | 4229897 | Stupor | SNOMED |
| Removed | condition_occurrence | 4232181 | Chronic duodenal ulcer with hemorrhage | SNOMED |
| Removed | condition_occurrence | 4232337 | Valvular endocarditis | SNOMED |
| Removed | condition_occurrence | 4232697 | Persistent atrial fibrillation | SNOMED |
| Removed | condition_occurrence | 4233244 | Paralysis of larynx | SNOMED |
| Removed | condition_occurrence | 4234083 | Traumatic pneumothorax | SNOMED |
| Removed | condition_occurrence | 4235863 | Spinal cord injury | SNOMED |
| Removed | condition_occurrence | 4236905 | Thrombosis of arteries of lower extremity | SNOMED |
| Removed | condition_occurrence | 4237062 | Mural thrombus of heart | SNOMED |
| Removed | condition_occurrence | 4237458 | Fracture of clavicle | SNOMED |
| Removed | condition_occurrence | 4238648 | Angiodysplasia of small intestine | SNOMED |
| Removed | condition_occurrence | 4238808 | Empyema of pleura | SNOMED |
| Removed | condition_occurrence | 4241033 | Acute abdomen | SNOMED |
| Removed | condition_occurrence | 4241530 | Asymptomatic human immunodeficiency virus infection | SNOMED |
| Removed | condition_occurrence | 4241777 | Carcinoma in situ of endometrium | SNOMED |
| Removed | condition_occurrence | 4242348 | Benign neoplasm of intrathoracic organs | SNOMED |
| Removed | condition_occurrence | 4242574 | Intertrigo | SNOMED |
| Removed | condition_occurrence | 4242814 | Benign neoplasm of parotid gland | SNOMED |
| Removed | condition_occurrence | 4242816 | Benign neoplasm of pituitary gland | SNOMED |
| Removed | condition_occurrence | 4243445 | Benign neoplasm of pancreas | SNOMED |
| Removed | condition_occurrence | 4245646 | Congenital septal defect of heart | SNOMED |
| Removed | condition_occurrence | 4245975 | Hepatic failure | SNOMED |
| Removed | condition_occurrence | 4247238 | Primary malignant neoplasm of endometrium | SNOMED |
| Removed | condition_occurrence | 4247350 | Primary malignant neoplasm of skin of ear | SNOMED |
| Removed | condition_occurrence | 4247719 | Primary malignant neoplasm of ascending colon | SNOMED |
| Removed | condition_occurrence | 4247802 | Muscular dystrophy | SNOMED |
| Removed | condition_occurrence | 4247842 | Primary malignant neoplasm of myometrium | SNOMED |
| Removed | condition_occurrence | 4248429 | Gastric ulcer without hemorrhage AND without perforation | SNOMED |
| Removed | condition_occurrence | 4251304 | Intervertebral disc prolapse | SNOMED |
| Removed | condition_occurrence | 4254477 | Counseling | SNOMED |
| Removed | condition_occurrence | 4263360 | Fracture of pubis | SNOMED |
| Removed | condition_occurrence | 4263508 | Ophthalmic examination and evaluation | SNOMED |
| Removed | condition_occurrence | 4265479 | Acute duodenal ulcer with perforation | SNOMED |
| Removed | condition_occurrence | 4266367 | Influenza | SNOMED |
| Removed | condition_occurrence | 4266809 | Diverticular disease | SNOMED |
| Removed | condition_occurrence | 4270024 | Acute non-ST segment elevation myocardial infarction | SNOMED |
| Removed | condition_occurrence | 4271013 | Melanocytic nevus | SNOMED |
| Removed | condition_occurrence | 4274575 | Idiopathic generalized epilepsy | SNOMED |
| Removed | condition_occurrence | 4275423 | Supraventricular tachycardia | SNOMED |
| Removed | condition_occurrence | 4276360 | Undernutrition | SNOMED |
| Removed | condition_occurrence | 4280942 | Acute gastrojejunal ulcer with perforation | SNOMED |
| Removed | condition_occurrence | 4282316 | Recurrent major depression | SNOMED |
| Removed | condition_occurrence | 4283942 | Bronchopulmonary dysplasia of newborn | SNOMED |
| Removed | condition_occurrence | 4284492 | Guttate psoriasis | SNOMED |
| Removed | condition_occurrence | 4285898 | Polyp of colon | SNOMED |
| Removed | condition_occurrence | 4288544 | Inguinal hernia | SNOMED |
| Removed | condition_occurrence | 4292673 | Artefactual skin disease | SNOMED |
| Removed | condition_occurrence | 4293175 | Mental state, behavior and/or psychosocial function finding | SNOMED |
| Removed | condition_occurrence | 4296653 | Acute ST segment elevation myocardial infarction | SNOMED |
| Removed | condition_occurrence | 4296728 | Polyneuritis | SNOMED |
| Removed | condition_occurrence | 4297400 | Mild neurocognitive disorder | SNOMED |
| Removed | condition_occurrence | 4297894 | Greater trochanteric pain syndrome | SNOMED |
| Removed | condition_occurrence | 4298809 | Nephritic syndrome | SNOMED |
| Removed | condition_occurrence | 4299094 | Opioid intoxication | SNOMED |
| Removed | condition_occurrence | 4299440 | Vascular disorder of pelvis | SNOMED |
| Removed | condition_occurrence | 4302066 | Physical abuse | SNOMED |
| Removed | condition_occurrence | 4302537 | Digestive system finding | SNOMED |
| Removed | condition_occurrence | 4303233 | Gastric polyp | SNOMED |
| Removed | condition_occurrence | 4304002 | Eosinophil count above reference range | SNOMED |
| Removed | condition_occurrence | 4306292 | Upper abdominal pain | SNOMED |
| Removed | condition_occurrence | 4306943 | Epidural intracranial hemorrhage | SNOMED |
| Removed | condition_occurrence | 4307024 | Follow-up encounter | SNOMED |
| Removed | condition_occurrence | 4307820 | Unplanned pregnancy | SNOMED |
| Removed | condition_occurrence | 4307925 | Psoriasis vulgaris | SNOMED |
| Removed | condition_occurrence | 4308093 | Dupuytren's disease of palm | SNOMED |
| Removed | condition_occurrence | 4310400 | Acute appendicitis | SNOMED |
| Removed | condition_occurrence | 4310821 | Bipolar disorder in remission | SNOMED |
| Removed | condition_occurrence | 4311115 | Intracranial mass | SNOMED |
| Removed | condition_occurrence | 4311499 | Primary malignant neoplasm of respiratory tract | SNOMED |
| Removed | condition_occurrence | 4312685 | Primary malignant neoplasm of skin of lower limb | SNOMED |
| Removed | condition_occurrence | 4313365 | Neoplasm of uncertain behavior of brain | SNOMED |
| Removed | condition_occurrence | 4316995 | Neoplasm of uncertain behavior of renal pelvis | SNOMED |
| Removed | condition_occurrence | 4317685 | Neoplasm of uncertain behavior of respiratory tract | SNOMED |
| Removed | condition_occurrence | 4317816 | Neoplasm of uncertain behavior of small intestine | SNOMED |
| Removed | condition_occurrence | 4318699 | Disorder of lacrimal gland | SNOMED |
| Removed | condition_occurrence | 4319447 | Urolithiasis | SNOMED |
| Removed | condition_occurrence | 4322306 | Poisoning caused by acetaminophen | SNOMED |
| Removed | condition_occurrence | 4332304 | Status epilepticus | SNOMED |
| Removed | condition_occurrence | 4334245 | Retinal artery occlusion | SNOMED |
| Removed | condition_occurrence | 4335169 | Acute transient psychotic disorder | SNOMED |
| Removed | condition_occurrence | 4338120 | Altered bowel function | SNOMED |
| Removed | condition_occurrence | 4338523 | Amaurosis fugax | SNOMED |
| Removed | condition_occurrence | 4338843 | Disorder of pleura | SNOMED |
| Removed | condition_occurrence | 4339214 | Secondary pulmonary hypertension | SNOMED |
| Removed | condition_occurrence | 4340383 | Alcoholic hepatitis | SNOMED |
| Removed | condition_occurrence | 4340493 | Alcohol-induced acute pancreatitis | SNOMED |
| Removed | condition_occurrence | 4344258 | Bursitis of shoulder | SNOMED |
| Removed | drug_exposure | 19001311 | epoetin beta | RxNorm |
| Removed | drug_exposure | 19002829 | tolazoline | RxNorm |
| Removed | drug_exposure | 19011437 | icodextrin | RxNorm |
| Removed | drug_exposure | 19012585 | asparaginase | RxNorm |
| Removed | drug_exposure | 19017810 | amsacrine | RxNorm |
| Removed | drug_exposure | 19018407 | adrenalone | RxNorm |
| Removed | drug_exposure | 19024728 | decitabine | RxNorm |
| Removed | drug_exposure | 19037624 | acetylcholine | RxNorm |
| Removed | drug_exposure | 19039874 | sodium metabisulfite | RxNorm |
| Removed | drug_exposure | 19045045 | ergocalciferol | RxNorm |
| Removed | drug_exposure | 19045317 | digoxin antibodies Fab fragments | RxNorm |
| Removed | drug_exposure | 19058572 | calcium citrate | RxNorm |
| Removed | drug_exposure | 19066865 | silicon dioxide | RxNorm |
| Removed | drug_exposure | 19069076 | hydroxyethyl cellulose | RxNorm |
| Removed | drug_exposure | 19092377 | lysine | RxNorm |
| Removed | drug_exposure | 19095275 | potassium iodate | RxNorm |
| Removed | drug_exposure | 19101454 | lauromacrogols | RxNorm |
| Removed | drug_exposure | 19105879 | ajmaline | RxNorm |
| Removed | drug_exposure | 19112623 | solfenacin | RxNorm |
| Removed | drug_exposure | 19126774 | mucins | RxNorm |
| Removed | drug_exposure | 19136716 | taurine | RxNorm |
| Removed | drug_exposure | 19137385 | thiotepa | RxNorm |
| Removed | measurement | 21490846 | Respiratory rate by Airway flow measurement | LOINC |
| Removed | drug_exposure | 35197944 | l-glutamine | RxNorm Extension |
| Removed | drug_exposure | 35606087 | zinc sulfide | RxNorm |
| Removed | condition_occurrence | 35624213 | Secondary cataract | SNOMED |
| Removed | condition_occurrence | 35624320 | Acute adrenal insufficiency | SNOMED |
| Removed | condition_occurrence | 35624825 | Obstructed bilateral inguinal hernia | SNOMED |
| Removed | drug_exposure | 36027924 | magnesium sulfate / potassium sulfate / sodium sulfate | RxNorm |
| Removed | drug_exposure | 36028193 | ferrous fumarate / polysaccharide iron complex | RxNorm |
| Removed | drug_exposure | 36028316 | alginic acid / sodium bicarbonate | RxNorm |
| Removed | drug_exposure | 36028646 | chondroitin sulfates / glucosamine | RxNorm |
| Removed | drug_exposure | 36028719 | lidocaine / norepinephrine | RxNorm |
| Removed | drug_exposure | 36028785 | benzocaine / oxyquinoline | RxNorm |
| Removed | drug_exposure | 36028982 | calcium carbonate / magnesium trisilicate | RxNorm |
| Removed | drug_exposure | 36029208 | chlorhexidine / didecyldimethylammonium chloride | RxNorm |
| Removed | drug_exposure | 36029616 | allantoin / zinc oxide | RxNorm |
| Removed | drug_exposure | 36029651 | atenolol / chlorthalidone | RxNorm |
| Removed | drug_exposure | 36029755 | Glycopyrrolate / Indacterol | RxNorm |
| Removed | drug_exposure | 36029920 | calcium carbonate / magnesium carbonate | RxNorm |
| Removed | drug_exposure | 36029974 | enalapril / hydrochlorothiazide | RxNorm |
| Removed | drug_exposure | 36029982 | estradiol / norethindrone | RxNorm |
| Removed | drug_exposure | 36029999 | hydrochlorothiazide / irbesartan | RxNorm |
| Removed | drug_exposure | 36030000 | hydrochlorothiazide / lisinopril | RxNorm |
| Removed | drug_exposure | 36030003 | hydrochlorothiazide / metoprolol | RxNorm |
| Removed | drug_exposure | 36030057 | glucose / potassium chloride | RxNorm |
| Removed | drug_exposure | 36030108 | articaine / epinephrine | RxNorm |
| Removed | drug_exposure | 36030109 | atovaquone / proguanil | RxNorm |
| Removed | drug_exposure | 36030121 | iodine / potassium iodide | RxNorm |
| Removed | drug_exposure | 36030126 | buprenorphine / naloxone | RxNorm |
| Removed | drug_exposure | 36030184 | carbidopa / entacapone / levodopa | RxNorm |
| Removed | drug_exposure | 36030331 | desoximetasone / salicylic acid | RxNorm |
| Removed | drug_exposure | 36030536 | hydrocortisone / polymyxin B | RxNorm |
| Removed | drug_exposure | 36030600 | betamethasone / calcipotriene | RxNorm |
| Removed | drug_exposure | 36030964 | hydrochlorothiazide / olmesartan | RxNorm |
| Removed | drug_exposure | 36086759 | Antithymocyte immunoglobulin (equine) | RxNorm Extension |
| Removed | measurement | 36304468 | Casts [Presence] in Urine | LOINC |
| Removed | condition_occurrence | 36712702 | Preterm labor with preterm delivery | SNOMED |
| Removed | condition_occurrence | 36712821 | Postprocedural infection | SNOMED |
| Removed | condition_occurrence | 36712846 | Persistent proteinuria | SNOMED |
| Removed | condition_occurrence | 36713107 | Lumbar spondylolisthesis | SNOMED |
| Removed | condition_occurrence | 36715792 | Acquired absence of breast | SNOMED |
| Removed | condition_occurrence | 36716163 | Excessive skin and subcutaneous tissue | SNOMED |
| Removed | condition_occurrence | 36716270 | Cyst of kidney | SNOMED |
| Removed | condition_occurrence | 36716700 | Perforation and abscess of large intestine co-occurrent and due to diverticulitis | SNOMED |
| Removed | condition_occurrence | 36716712 | Calculus of gallbladder without cholecystitis or cholangitis | SNOMED |
| Removed | drug_exposure | 36848804 | PRITELIVIR | RxNorm Extension |
| Removed | drug_exposure | 36850450 | MEDOSULEPINE | RxNorm Extension |
| Removed | drug_exposure | 36854608 | LOPIRAZEPAM | RxNorm Extension |
| Removed | drug_exposure | 36855381 | SENNOSIDES A AND B ACIDS | RxNorm Extension |
| Removed | drug_exposure | 36855567 | FLUMAZENIL C-11 | RxNorm Extension |
| Removed | drug_exposure | 36856245 | BRENTUXIMAB | RxNorm Extension |
| Removed | drug_exposure | 36858667 | METHYLTHIONITAZENE | RxNorm Extension |
| Removed | drug_exposure | 36861098 | PYRIDOXINE PHOSPHATE | RxNorm Extension |
| Removed | drug_exposure | 36863154 | METAZOCINE | RxNorm Extension |
| Removed | drug_exposure | 36878978 | amidotrizoate lysine | RxNorm Extension |
| Removed | drug_exposure | 36879073 | Iron isomaltoside 1000 | RxNorm Extension |
| Removed | drug_exposure | 36879148 | Factor XI | RxNorm Extension |
| Removed | condition_occurrence | 37017263 | Lymphadenopathy co-occurrent with human immunodeficiency virus infection | SNOMED |
| Removed | condition_occurrence | 37109944 | Bodily distress disorder | SNOMED |
| Removed | condition_occurrence | 37110282 | Venous complication of pregnancy | SNOMED |
| Removed | condition_occurrence | 37110437 | Psychotic disorder caused by cocaine | SNOMED |
| Removed | condition_occurrence | 37118664 | Injury of femoral artery | SNOMED |
| Removed | condition_occurrence | 37158897 | Finding of risk level | SNOMED |
| Removed | condition_occurrence | 37162280 | Disorder caused by psychoactive substance | SNOMED |
| Removed | condition_occurrence | 37164793 | Organic mental disorder caused by ethanol | SNOMED |
| Removed | condition_occurrence | 37167847 | Injury of blood vessel of abdomen | SNOMED |
| Removed | condition_occurrence | 37311060 | Suspected COVID-19 | SNOMED |
| Removed | condition_occurrence | 37311061 | COVID-19 | SNOMED |
| Removed | condition_occurrence | 37311320 | Extracellular fluid volume depletion | SNOMED |
| Removed | drug_exposure | 40171076 | sodium selenate | RxNorm |
| Removed | drug_exposure | 40238188 | ipilimumab | RxNorm |
| Removed | condition_occurrence | 40326053 | Dysphonia | SNOMED |
| Removed | condition_occurrence | 40481901 | Mantle cell lymphoma | SNOMED |
| Removed | condition_occurrence | 40481919 | Coronary atherosclerosis | SNOMED |
| Removed | condition_occurrence | 40482507 | Incipient senile cataract | SNOMED |
| Removed | condition_occurrence | 40482662 | Disorder of joint of ankle and/or foot | SNOMED |
| Removed | condition_occurrence | 40482893 | Extranodal marginal zone B-cell lymphoma of mucosa-associated lymphoid tissue (MALT-lymphoma) | SNOMED |
| Removed | condition_occurrence | 40483172 | Stimulant dependence | SNOMED |
| Removed | condition_occurrence | 40483287 | Disorder of kidney and/or ureter | SNOMED |
| Removed | condition_occurrence | 40483613 | Inflammatory disease of female genital structure | SNOMED |
| Removed | condition_occurrence | 40486896 | Primary malignant neoplasm of extrahepatic bile duct | SNOMED |
| Removed | condition_occurrence | 40487059 | Sepsis caused by Staphylococcus | SNOMED |
| Removed | condition_occurrence | 40489907 | Sepsis caused by Staphylococcus aureus | SNOMED |
| Removed | condition_occurrence | 40492458 | Neoplasm of uncertain behavior of digestive organ | SNOMED |
| Removed | condition_occurrence | 40493038 | Sepsis caused by Gram negative bacteria | SNOMED |
| Removed | measurement | 40757494 | Bilirubin.total [Moles/volume] in Blood | LOINC |
| Removed | measurement | 40765038 | 1,25-Dihydroxyvitamin D [Mass/volume] in Serum or Plasma | LOINC |
| Removed | observation | 40766929 | How many cigarettes do you smoke per day now [PhenX] | LOINC |
| Removed | drug_exposure | 40798873 | Herbal extract | RxNorm Extension |
| Removed | condition_occurrence | 42536547 | Ischemia of kidney | SNOMED |
| Removed | condition_occurrence | 42536886 | Ischemia of muscle due to traumatic injury | SNOMED |
| Removed | condition_occurrence | 42537727 | Degeneration of posterior pole of eye | SNOMED |
| Removed | condition_occurrence | 42537748 | Acquired absence of organ | SNOMED |
| Removed | condition_occurrence | 42538119 | Transplanted heart valve present | SNOMED |
| Removed | condition_occurrence | 42539146 | Psychotic disorder caused by stimulant | SNOMED |
| Removed | condition_occurrence | 42539502 | Transplanted kidney present | SNOMED |
| Removed | drug_exposure | 42709318 | tocopherol | RxNorm |
| Removed | drug_exposure | 42800027 | varicella-zoster virus vaccine live (Oka-Merck) strain | RxNorm |
| Removed | drug_exposure | 42801287 | pertuzumab | RxNorm |
| Removed | measurement | 42868484 | Type of Positive airway pressure device | LOINC |
| Removed | measurement | 42868674 | Cholesterol in HDL/Cholesterol.total [Molar ratio] in Serum or Plasma | LOINC |
| Removed | drug_exposure | 42873638 | carfilzomib | RxNorm |
| Removed | drug_exposure | 42904275 | cranberry juice | RxNorm |
| Removed | condition_occurrence | 43530674 | Spontaneous cerebellar hemorrhage | SNOMED |
| Removed | condition_occurrence | 43530714 | Sensory disorder of smell and/or taste | SNOMED |
| Removed | condition_occurrence | 43530727 | Spontaneous cerebral hemorrhage | SNOMED |
| Removed | condition_occurrence | 43530807 | Allergic disposition | SNOMED |
| Removed | measurement | 43533850 | Gamma hydroxybutyrate [Mass/volume] in Serum, Plasma or Blood | LOINC |
| Removed | condition_occurrence | 44784217 | Cardiac arrhythmia | SNOMED |
| Removed | condition_occurrence | 44806251 | Biliary acute pancreatitis | SNOMED |
| Removed | measurement | 44816698 | Lithium [Moles/volume] in Serum or Plasma --trough | LOINC |
| Removed | measurement | 44816815 | Nortriptyline [Mass/volume] in Serum or Plasma --trough | LOINC |
| Removed | condition_occurrence | 45757291 | Closed fracture of orbital floor | SNOMED |
| Removed | condition_occurrence | 45766058 | Sterilization procedure | SNOMED |
| Removed | condition_occurrence | 45766075 | Acute anterior ST segment elevation myocardial infarction | SNOMED |
| Removed | condition_occurrence | 45766116 | Acute ST segment elevation myocardial infarction of inferior wall | SNOMED |
| Removed | condition_occurrence | 45766714 | Inflammatory dermatosis | SNOMED |
| Removed | condition_occurrence | 45770892 | Primary malignant neoplasm of uterus | SNOMED |
| Removed | condition_occurrence | 45772085 | Anal abscess | SNOMED |
| Removed | condition_occurrence | 45772120 | Gastroduodenal disorder | SNOMED |
| Removed | condition_occurrence | 45773181 | Phantom limb syndrome with pain | SNOMED |
| Removed | drug_exposure | 45774639 | vedolizumab | RxNorm |
| Removed | drug_exposure | 45775636 | meningococcal group B vaccine | RxNorm |
| Removed | drug_exposure | 45892531 | blinatumomab | RxNorm |
| Removed | drug_exposure | 45892628 | nivolumab | RxNorm |
| Removed | condition_occurrence | 46271022 | Chronic kidney disease | SNOMED |
| Removed | condition_occurrence | 46272242 | Intestinal obstruction co-occurrent and due to decreased peristalsis | SNOMED |
| Removed | condition_occurrence | 46273463 | Upper respiratory tract infection caused by Influenza virus | SNOMED |
| Removed | condition_occurrence | 46287148 | Acute stimulant intoxication | SNOMED |
| Removed | measurement | 2000000003 |  |  |
| Removed | measurement | 2000000004 |  |  |
| Removed | measurement | 2000000011 |  |  |
| Removed | measurement | 2000000014 |  |  |
| Removed | measurement | 2000000015 |  |  |
| Removed | measurement | 2000000016 |  |  |
| Removed | measurement | 2000000018 |  |  |
| Removed | measurement | 2000000025 |  |  |
| Removed | measurement | 2000000034 |  |  |
| Removed | measurement | 2000000038 |  |  |
| Removed | measurement | 2000000084 |  |  |
| Removed | measurement | 2000000085 |  |  |
| Removed | measurement | 2000000090 |  |  |
| Removed | measurement | 2000000098 |  |  |
| Removed | measurement | 2000000100 |  |  |
| Removed | measurement | 2000000140 |  |  |
| Removed | measurement | 2000000154 |  |  |
| Removed | measurement | 2000000164 |  |  |
| Removed | measurement | 2000000175 |  |  |
| Removed | measurement | 2000000176 |  |  |
| Removed | measurement | 2000000193 |  |  |
| Removed | measurement | 2000000194 |  |  |
| Removed | measurement | 2000000199 |  |  |
| Removed | measurement | 2000000201 |  |  |
| Removed | measurement | 2000000204 |  |  |
| Removed | measurement | 2000000205 |  |  |
| Removed | measurement | 2000000208 |  |  |
| Removed | measurement | 2000000214 |  |  |
| Removed | measurement | 2000000218 |  |  |
| Removed | measurement | 2000000222 |  |  |
| Removed | measurement | 2000000227 |  |  |
| Removed | measurement | 2000000228 |  |  |
| Removed | measurement | 2000000229 |  |  |
| Removed | measurement | 2000000232 |  |  |
| Removed | measurement | 2000000234 |  |  |
| Removed | measurement | 2000000235 |  |  |
| Removed | measurement | 2000000239 |  |  |
| Removed | measurement | 2000000240 |  |  |
| Removed | measurement | 2000000241 |  |  |
| Removed | measurement | 2000000242 |  |  |
| Removed | measurement | 2000000243 |  |  |
| Removed | measurement | 2000000244 |  |  |
| Removed | measurement | 2000000245 |  |  |
| Removed | measurement | 2000000246 |  |  |
| Removed | measurement | 2000000249 |  |  |
| Removed | measurement | 2000000251 |  |  |
| Removed | measurement | 2000000252 |  |  |
| Removed | measurement | 2000000338 |  |  |
| Removed | measurement | 2000000348 |  |  |
| Removed | measurement | 2000000353 | fluid output - wound flush drain | ICUdata |
| Removed | measurement | 2000000373 | fluid output - urine splint drain left | ICUdata |
| Removed | measurement | 2000000400 |  |  |
| Removed | measurement | 2000000444 |  |  |
| Removed | measurement | 2000000449 |  |  |
| Removed | measurement | 2000000471 |  |  |
| Removed | device_exposure | 2000000476 |  |  |
| Removed | measurement | 2000000497 |  |  |
| Removed | device_exposure | 2000000520 |  |  |
| Removed | measurement | 2000000529 |  |  |
| Removed | device_exposure | 2000000552 |  |  |
| Removed | drug_exposure | 2000000573 |  |  |
| Removed | measurement | 2000000606 |  |  |
| Removed | measurement | 2000000622 |  |  |
| Removed | measurement | 2000000629 |  |  |
| Removed | measurement | 2000000640 |  |  |
| Removed | measurement | 2000000650 |  |  |
| Removed | device_exposure | 2000000801 |  |  |
| Removed | device_exposure | 2000000802 |  |  |
| Removed | observation | 2000000903 |  |  |
| Removed | measurement | 2000000905 |  |  |

## Parameter Remappings

Source codes that previously mapped to one concept and now map to another. 

### 2000000084 — 714/714 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Enlive | 3006552 Fluid intake oral Estimated |
| IJswater | 3006552 Fluid intake oral Estimated |
| Ijsje | 3006552 Fluid intake oral Estimated |
| Karnemelk | 3006552 Fluid intake oral Estimated |
| Melk | 3006552 Fluid intake oral Estimated |
| Nutridrink | 3006552 Fluid intake oral Estimated |
| Pap voeding | 3006552 Fluid intake oral Estimated |
| Soep | 3006552 Fluid intake oral Estimated |
| Water (Drinken of via Sonde) | 3006552 Fluid intake oral Estimated |
| Water/Thee/Lim./koffie | 3006552 Fluid intake oral Estimated |
| Yoghurt | 3006552 Fluid intake oral Estimated |
| input - Per Os | 3006552 Fluid intake oral Estimated |
| input - Per Os (.water ijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (1/2 warme maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (1/3 deel van warme maaltijd op) | 3006552 Fluid intake oral Estimated |
| input - Per Os (1/4 boterham met smeerkaas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (1/4 warme maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (2 beschuit) | 3006552 Fluid intake oral Estimated |
| input - Per Os (2 boterhammen) | 3006552 Fluid intake oral Estimated |
| input - Per Os (2 maal ijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (2 x mousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (2x ijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (2x thee) | 3006552 Fluid intake oral Estimated |
| input - Per Os (3 boterhammen met beleg) | 3006552 Fluid intake oral Estimated |
| input - Per Os (3 x mousse PREPARE) | 3006552 Fluid intake oral Estimated |
| input - Per Os (3/4 warme maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (300 cc avondeten.) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Aardbei shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Aardbei-Framboos Eiwt+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Alpro Chocomel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Alpro chocolade) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Alpro vanille vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel Perensap E+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel frambozen moes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel peer eiwit +) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel peer sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel peren sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel-peren sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel-perensap eiwit +) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel-perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel/peren E+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel/peren sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appel/perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appelmoes ~ Nutilis) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appelmoes ~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appelmoes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appelmoes/ -moes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appelperensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Appelsap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Aqua) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Arizona) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Banaan) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Bitter Lemon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Boost buddies) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Boost drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Boostbuddy) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Booster buddies) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Booster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Bouillon zoutloos) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Bouillon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Buddy boost) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Buddy booster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Buddybooster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (CHOCOMELK) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Catharina shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Chocolademelk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Chocoladevla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Chocomel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Chocomelk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Cola Zero) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Cola) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Compot) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Compote) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Correctie sondevoeding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Custard pudding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Dessert) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Drink yoghurt eiwit +) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Drink yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Drinken ontbijt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Drinken tussendoor) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Drinken) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Drinkyoghurt Eiwit+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Drinkyoghurt eiwit verrijkt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Drinkyoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Duo van mousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (E+ appel perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (E+ appel/peren) | 3006552 Fluid intake oral Estimated |
| input - Per Os (E+ appel/perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (E+ drinkyoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (E+ sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (E+ shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (E+ vruchtensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (E+ yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwit ass plus) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwit shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwit supershake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwit verrijkt yoghurt drink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwit verrijkte drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwit+ drinken) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwit+ shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitdrink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitrijke drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitrijke milkshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitverreikte drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitverrijkt appelsap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitverrijkt drinkyoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitverrijkte shake sinasappel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitverrijkte smoothie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwitverrijkte yoghurt sinaasappeldrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Eiwtishake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (En+ drankje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (En+ nutridrink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Energiebooster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fanta Lemon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fanta lemon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fanta met ijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fanta) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Flesvoeding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Flesvoeding~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fortimel compact) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fortimel créme) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fortimel jucy) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fortimel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fresubin) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Frisdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fruit compote) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fruit) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fruitmoes eiwitverrijkt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Fruitshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Gal) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Gecrucht ijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas Eiwitshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas Fanta) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas chocolademelk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas chocomelk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas eiwitrijke smoothie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas eiwitshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas fanta) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas limo) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas limonade) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glasappel/perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glassupershake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas~chocomelk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas~fanta lemon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas~fanta) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas~lemon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas~limo) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Glas~limonade) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Griekse Yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Griekse yoghurt + vruchten) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Griekse yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (H20 via maagsonde voor medicatie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (HAPJES) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Halve warme maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Havermout pap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Havermout) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Havermoutpap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (IJs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (IJs-gruis) | 3006552 Fluid intake oral Estimated |
| input - Per Os (IJsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (IJsklontjes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (IJswater) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ice tea) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ijsblokjes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ijsgruis) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ijsthee) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Intake dag) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Intake ochtend) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Intake per os avond) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Joghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Karnemelk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Koffie  ~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Koffie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Koffie, water appelsap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Kwark eiwitver) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Kwark) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Limonade) | 3006552 Fluid intake oral Estimated |
| input - Per Os (MILKSHAKE) | 3006552 Fluid intake oral Estimated |
| input - Per Os (MOVIPREP) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Maaltijd mix prepare) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Maaltijdmix) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Mandarijn) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Med ( moviprep) toegevoegd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Med toegevoegd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Med.( moviprep) met water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Melk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Milk shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Milkshake eiwit++) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Milkshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Mousse trio) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Movicolon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Moviprep met water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Moviprep) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutilis aqua) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutilis fruit) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutrdrink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutri) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink compact fibre) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink compact proteine) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink compact) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink creme) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink fruit dessert) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink ijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink juice style) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink multi fibre) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink yoghurt style) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutridrink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Nutrilon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Orale intake avond) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Orale intake middag) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Orale intake ochtend) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Orale intake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (PREPARE mousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (PREPARE voeding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Pap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Per Os  ~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Per os dagdienst) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Per os ontbijt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Peren vla en+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Perensap eiwit +) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Peresap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Persensap eiwitverrijkt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Pre pare mouse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Prepare dessert) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Prepare mousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Prepare zuivel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Prepare) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Proteine shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Proteine vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Proteineshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Proteïneshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Pudding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Raket Waterijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Raket) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Raketje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ranja / sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ranja verdikt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ranja) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Ranja, suikervrij en ingedikt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (SOEP) | 3006552 Fluid intake oral Estimated |
| input - Per Os (SV) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Shake 125 ml) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Shake aardbei) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Shake sinaasappel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Shake vanille + suiker) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sinaasappel smoothie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sinaasappelsap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sinas Lemon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sinas suikervrij) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sinas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Slimpie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Smoothie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Soep) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Soja kwark) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sojadrink ~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sojapudding ~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sondevoeding 186 ml) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sondevoeding 2.0) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sondevoeding via Maagsonde) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Sondevoeding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Soya vanille) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Spa rood) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Suikervrije aanmaaklimonade ~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Super Smoothie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Super shake boost) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Super shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Superbooster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Supershake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Supershakes avond) | 3006552 Fluid intake oral Estimated |
| input - Per Os (THEE) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Thee  ~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Thee) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Toetje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Tomatensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Tomatensoep) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Totaal) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Trio van mouse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Trio van mousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vanille vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vis spinazie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla (alpro)) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla + yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla / Yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla /yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla bosvr.) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla caramel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla chocolade) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla proteine) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla sinasappel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla vanille) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla, vanille + slagroom) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla/pap/kwark/yoghurt  ~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vlaflip) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla~choc) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla~choc./vanille) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla~vanille) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vla~vanille/choc) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vocht bij medicatie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vocht infusen compensatie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vruchten compote) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vruchten kwark) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vruchtenmoes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Vruchtenmousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (WATER) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Warme maaltijd (gepureerd)) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Water  ~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Water bij medicatie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Water ijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Water ijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Water met Moviprep) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Water via sonde) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Water, koffie, melk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Water, soep en thee) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Waterijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Waterijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Yoghurt drink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Yoghurtdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Yoghurtdrink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (Zalmmouse en hammouse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (a/perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (aardbeien shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (alpro choc vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (alpro vanille) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel peer sap eiwit +) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel peer sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel peren sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel peren/sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel perenap eiwit+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel perensap E+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel/ peren sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel/peer sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel/peren sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel/perenmoes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel/perensap E+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel/perensap eiwit+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appel/perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appelmoes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appelpeer sap energ+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appelperen sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appelperensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appelsap en+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appelsap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (appeslap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (aquarius) | 3006552 Fluid intake oral Estimated |
| input - Per Os (asap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (avg) | 3006552 Fluid intake oral Estimated |
| input - Per Os (avond maaltijd 1/2) | 3006552 Fluid intake oral Estimated |
| input - Per Os (avondeten) | 3006552 Fluid intake oral Estimated |
| input - Per Os (avondmaaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (banaan) | 3006552 Fluid intake oral Estimated |
| input - Per Os (barle duc) | 3006552 Fluid intake oral Estimated |
| input - Per Os (beschuit 3 stuks) | 3006552 Fluid intake oral Estimated |
| input - Per Os (beschuit met jam) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bessensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bier) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bij lunch) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bij ontbijt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bitter lemon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bitterlemon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (blikje fanta) | 3006552 Fluid intake oral Estimated |
| input - Per Os (boerenvla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (boerenyoghurt + jam) | 3006552 Fluid intake oral Estimated |
| input - Per Os (boerenyoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bonenspread) | 3006552 Fluid intake oral Estimated |
| input - Per Os (boost buddy) | 3006552 Fluid intake oral Estimated |
| input - Per Os (boost) | 3006552 Fluid intake oral Estimated |
| input - Per Os (booster shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (booster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bosvruchtenshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (boterham kaas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (boterham met kaas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bouillon maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bouillon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bouilon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (boulion) | 3006552 Fluid intake oral Estimated |
| input - Per Os (bouwsteentje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (broodje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (buddy boddies) | 3006552 Fluid intake oral Estimated |
| input - Per Os (buddy boost) | 3006552 Fluid intake oral Estimated |
| input - Per Os (buddy booster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (buddybooster framb) | 3006552 Fluid intake oral Estimated |
| input - Per Os (buddybooster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (cath shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (chocolade melk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (chocolademelk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (chocoladevla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (chocomel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (chocomelk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (chocovla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (citroenkwark) | 3006552 Fluid intake oral Estimated |
| input - Per Os (cola zero) | 3006552 Fluid intake oral Estimated |
| input - Per Os (cola) | 3006552 Fluid intake oral Estimated |
| input - Per Os (compensatie sondevoeding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (compot) | 3006552 Fluid intake oral Estimated |
| input - Per Os (compote) | 3006552 Fluid intake oral Estimated |
| input - Per Os (coolbest) | 3006552 Fluid intake oral Estimated |
| input - Per Os (correctie SV) | 3006552 Fluid intake oral Estimated |
| input - Per Os (correctie sondevoeding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (correctie sv) | 3006552 Fluid intake oral Estimated |
| input - Per Os (correctie vrij water via sonde) | 3006552 Fluid intake oral Estimated |
| input - Per Os (cup a soup) | 3006552 Fluid intake oral Estimated |
| input - Per Os (dessert) | 3006552 Fluid intake oral Estimated |
| input - Per Os (dikke yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (diner) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drank bij ontbijt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drank bij prepare) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drank ochtend /middag) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinken bij ontbijt / tussendoor) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinken lunch) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinken ontbij) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinken) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinkyoghurt eiwit+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinkyoghurt energieverrijkt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinkyoghurt supershake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinkyoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinkyogurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (drinkyohgurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (e+ shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ei) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eitwit shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eitwitdrankje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eitwitshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiweitdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit + smoothie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit energieverijkte shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit verrijkt drink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit verrijkt sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit verrijkt yoghurtdrink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit verrijkt/verdikt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit verrijkte shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit verrijkte yoghurt drink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit+ drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit+ drinken) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwit+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitdrink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitrijk appelperensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitrijk sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitrijke drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitrijke drinkyogurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitrijke shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitshake aardbei/framboos) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverijkt sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverrijkt sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverrijkt shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverrijkte drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverrijkte sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverrijkte shake framboos) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverrijkte shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverrijkte smoothie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverrijkte supershake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (eiwitverrijkte yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (energie + drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (energie +, vla, thee) | 3006552 Fluid intake oral Estimated |
| input - Per Os (energie verrijkt sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (energie/eiwit + drinken) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ewit shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (fanta lemon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (fanta light) | 3006552 Fluid intake oral Estimated |
| input - Per Os (fanta) | 3006552 Fluid intake oral Estimated |
| input - Per Os (fruit) | 3006552 Fluid intake oral Estimated |
| input - Per Os (fruitcompote) | 3006552 Fluid intake oral Estimated |
| input - Per Os (fruitmoes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (fruitmousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (gemalen maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (glas tomatensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (griekse yogh + compote) | 3006552 Fluid intake oral Estimated |
| input - Per Os (griekse yoghurt met 2x honing) | 3006552 Fluid intake oral Estimated |
| input - Per Os (griekse yoghurt met honing) | 3006552 Fluid intake oral Estimated |
| input - Per Os (griekse yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (griekse yogurt met honing) | 3006552 Fluid intake oral Estimated |
| input - Per Os (groentehap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (h20) | 3006552 Fluid intake oral Estimated |
| input - Per Os (halve warme maaltijd op) | 3006552 Fluid intake oral Estimated |
| input - Per Os (halve warme maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (havermout pap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (havermout) | 3006552 Fluid intake oral Estimated |
| input - Per Os (havermoutenpap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (hele maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (houmous) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ice tea) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ija) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ijsblokje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ijsblokjes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ijsgruis) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ijsje/solero) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ijsthee) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ijswater) | 3006552 Fluid intake oral Estimated |
| input - Per Os (intake avond) | 3006552 Fluid intake oral Estimated |
| input - Per Os (intake ochtend oraal) | 3006552 Fluid intake oral Estimated |
| input - Per Os (intake ochtend) | 3006552 Fluid intake oral Estimated |
| input - Per Os (isotone sportdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (isotoon sportdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (jogidrink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (jus d + kwark) | 3006552 Fluid intake oral Estimated |
| input - Per Os (jus d'orange) | 3006552 Fluid intake oral Estimated |
| input - Per Os (jus) | 3006552 Fluid intake oral Estimated |
| input - Per Os (karnemelk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (karnemelk, volle yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (kippensoep) | 3006552 Fluid intake oral Estimated |
| input - Per Os (knijpfruit) | 3006552 Fluid intake oral Estimated |
| input - Per Os (koffie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (koffie, nutri juice, 2 x jus d'orange) | 3006552 Fluid intake oral Estimated |
| input - Per Os (koud water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (kwark) | 3006552 Fluid intake oral Estimated |
| input - Per Os (kwart warme ,maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (kwart warme maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (lim) | 3006552 Fluid intake oral Estimated |
| input - Per Os (limonade fanta) | 3006552 Fluid intake oral Estimated |
| input - Per Os (limonade ivm hypo) | 3006552 Fluid intake oral Estimated |
| input - Per Os (limonade ivm hypoglycemie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (limonade) | 3006552 Fluid intake oral Estimated |
| input - Per Os (maaltijd mix gemalen) | 3006552 Fluid intake oral Estimated |
| input - Per Os (maaltijdmix) | 3006552 Fluid intake oral Estimated |
| input - Per Os (mandarijn) | 3006552 Fluid intake oral Estimated |
| input - Per Os (medicatie via sonde) | 3006552 Fluid intake oral Estimated |
| input - Per Os (medicatie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (melk en water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (melk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (melk/ sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (milkshake eiwitrijk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (milkshake eiwitverrijkt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (milkshake sinasappel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (milkshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (moes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (mokka vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (mouse prepare) | 3006552 Fluid intake oral Estimated |
| input - Per Os (mouse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (mousse prepare) | 3006552 Fluid intake oral Estimated |
| input - Per Os (mousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (movicolon) | 3006552 Fluid intake oral Estimated |
| input - Per Os (moviprep) | 3006552 Fluid intake oral Estimated |
| input - Per Os (norit + natriumdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (nutri) | 3006552 Fluid intake oral Estimated |
| input - Per Os (nutridrink appel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (nutridrink compact proteine) | 3006552 Fluid intake oral Estimated |
| input - Per Os (nutridrink compact) | 3006552 Fluid intake oral Estimated |
| input - Per Os (nutridrink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (nutrison sv) | 3006552 Fluid intake oral Estimated |
| input - Per Os (nutrison) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ochtend drinken) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ochtend intake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (omelet) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ontbijt drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ontbijt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (optimel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (orale intake avond) | 3006552 Fluid intake oral Estimated |
| input - Per Os (orale intake ochtend tot 1500u) | 3006552 Fluid intake oral Estimated |
| input - Per Os (orange juice) | 3006552 Fluid intake oral Estimated |
| input - Per Os (paella) | 3006552 Fluid intake oral Estimated |
| input - Per Os (pap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (peren sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (peren/ appel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (perenijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (perensmoothie ijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (peresap eiwit +) | 3006552 Fluid intake oral Estimated |
| input - Per Os (peresap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (pre pare) | 3006552 Fluid intake oral Estimated |
| input - Per Os (prepare hapjes) | 3006552 Fluid intake oral Estimated |
| input - Per Os (prepare mousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (prepare stracciatella) | 3006552 Fluid intake oral Estimated |
| input - Per Os (prepare) | 3006552 Fluid intake oral Estimated |
| input - Per Os (proteino) | 3006552 Fluid intake oral Estimated |
| input - Per Os (pudding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (racket ijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (racketje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (radler) | 3006552 Fluid intake oral Estimated |
| input - Per Os (raketje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ranja) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ranja, water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (ringer liep buiten de pomp) | 3006552 Fluid intake oral Estimated |
| input - Per Os (roomvla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sap E+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sap peren) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sapje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sazt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (shake booster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (shake ijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (shaker boost) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sinaasappel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sinaasappelsap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sinas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (slimpie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (slokje water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (smoothie booster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (smoothie eiwitrijk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (smoothie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (smoothy) | 3006552 Fluid intake oral Estimated |
| input - Per Os (soep prepare) | 3006552 Fluid intake oral Estimated |
| input - Per Os (soep) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sondevoeding correctie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (sondevoeding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (spa rood bij medicatie) | 3006552 Fluid intake oral Estimated |
| input - Per Os (spa rood) | 3006552 Fluid intake oral Estimated |
| input - Per Os (super boost) | 3006552 Fluid intake oral Estimated |
| input - Per Os (super shake boost framboos) | 3006552 Fluid intake oral Estimated |
| input - Per Os (super shake sinaasappel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (super shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (super shaker) | 3006552 Fluid intake oral Estimated |
| input - Per Os (superboost framboos) | 3006552 Fluid intake oral Estimated |
| input - Per Os (superboost) | 3006552 Fluid intake oral Estimated |
| input - Per Os (superbooster) | 3006552 Fluid intake oral Estimated |
| input - Per Os (supershake + perensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (supershake framboos) | 3006552 Fluid intake oral Estimated |
| input - Per Os (supershake sinasappel) | 3006552 Fluid intake oral Estimated |
| input - Per Os (supershake sinasappelsap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (supershake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (supershaker) | 3006552 Fluid intake oral Estimated |
| input - Per Os (thee , water, vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (thee ingedikt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (thee) | 3006552 Fluid intake oral Estimated |
| input - Per Os (toetje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (tomatensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (trio mousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (trio van mousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (turkse yoghurt en chocolade vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (van. vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vanille vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vanille vla, thee, water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vanille/ yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vanillevla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vla + jus) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vla + yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vlaflip) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vloeibaar voeding) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vocht bij ontbijt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vocht prepare) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vochtintake nacht) | 3006552 Fluid intake oral Estimated |
| input - Per Os (volle vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (volledig warme maatlijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (volledige maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (volledige warme maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vrij water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruchten compote) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruchten shake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruchtenVla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruchtencompote) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruchtendrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruchtenkwark) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruchtensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruchtenshake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruchtenvla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (vruhctnesap eiwitrijk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (warme maaltijd half bord) | 3006552 Fluid intake oral Estimated |
| input - Per Os (warme maaltijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (warme maaltijd.) | 3006552 Fluid intake oral Estimated |
| input - Per Os (warme maatlijd) | 3006552 Fluid intake oral Estimated |
| input - Per Os (warme melk) | 3006552 Fluid intake oral Estimated |
| input - Per Os (water ijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (water met ijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (water) | 3006552 Fluid intake oral Estimated |
| input - Per Os (water/ thee) | 3006552 Fluid intake oral Estimated |
| input - Per Os (waterijs) | 3006552 Fluid intake oral Estimated |
| input - Per Os (waterijsje) | 3006552 Fluid intake oral Estimated |
| input - Per Os (watert) | 3006552 Fluid intake oral Estimated |
| input - Per Os (watyer) | 3006552 Fluid intake oral Estimated |
| input - Per Os (yoghdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (yoghurt drank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (yoghurt drink) | 3006552 Fluid intake oral Estimated |
| input - Per Os (yoghurt met fruit) | 3006552 Fluid intake oral Estimated |
| input - Per Os (yoghurt met vla) | 3006552 Fluid intake oral Estimated |
| input - Per Os (yoghurt) | 3006552 Fluid intake oral Estimated |
| input - Per Os (yoghurtdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (yoghurtdrink E+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (yogurtdrank) | 3006552 Fluid intake oral Estimated |
| input - Per Os (zalm en bonen) | 3006552 Fluid intake oral Estimated |
| input - Per Os (zalm mouse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (zalmmoot) | 3006552 Fluid intake oral Estimated |
| input - Per Os (zalmmouse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (zalmmousse) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~ brood met kaas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~1,5 snee wit met kaas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~2 boterhammen met beleg) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~2x brood met beleg) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~banaan) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~boterham met kaas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~brood met kaas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~cola) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~drinkjoghurt ei+) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~eiwit++ persensap) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~fruit) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~gekookt ei) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~krentebrood met kaas) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~omelet) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~supershake eiwit++) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~supershake) | 3006552 Fluid intake oral Estimated |
| input - Per Os (~warme maaltijd) | 3006552 Fluid intake oral Estimated |

### 2000000520 — 9/9 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Miditracheotomie | 4044008 Tracheostomy tube |
| Mini-tracheacanule | 4044008 Tracheostomy tube |
| Tracheacanule | 605799 Tracheostomy tube cannula, 4044008 Tracheostomy tube |
| Tracheacanule (Trachea) | 4044008 Tracheostomy tube |
| Tracheostoma | 4044008 Tracheostomy tube |
| Tracheotomie (Portex) | 4044008 Tracheostomy tube |
| Xx-Niet meer gebruiken Miditracheotomie(= Proces Tracheostoma) | 4044008 Tracheostomy tube |
| Xx-Niet meer gebruiken Tracheostoma (Portex) (= Proces Tracheostoma) | 4044008 Tracheostomy tube |
| Xx-Niet meer gebruiken Tracheostoma (Shiley)(= Proces Tracheostoma) | 4044008 Tracheostomy tube |

### 2000000204 — 8/8 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Fi02 (gemeten);R UMCA AN FIO2 GEMETEN | 3020716 Inhaled oxygen concentration |
| Fi02 inst;R UMCA AN VENT FI02 | 3026238 Oxygen/Inspired gas Respiratory system --on ventilator |
| FiO2 | 21490563 Gas delivery system inspiratory Oxygen setting [VFr/PPres] |
| FiO2 (%);R UMCA ICU FIO2 S | 3026238 Oxygen/Inspired gas Respiratory system --on ventilator |
| FiO2 (set) | 21490563 Gas delivery system inspiratory Oxygen setting [VFr/PPres] |
| O2 Fractie - Inspiratoir Set | 21490563 Gas delivery system inspiratory Oxygen setting [VFr/PPres] |
| O2 concentratie | 3020716 Inhaled oxygen concentration |
| O2 concentratie (Set) | 21490696 Oxygen [VFr/PPres] Gas delivery system |

### 42868484 — Type of Positive airway pressure device (LOINC) — 8/8 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| CPAP/High flow ademweg;R UMCA ADEMWEG CPAP ONGEKOPPELD | 1469651 Method of oxygen delivery |
| Methode van O2 toediening | 1469651 Method of oxygen delivery |
| O2 Toedieningssysteem numeric;R O2 TOEDIENINGSSYSTEEM NUMERIC | 1469651 Method of oxygen delivery |
| O2-toediening prehospitaal;R ED PRE-ARRIVAL O2 DEVICE | 1469651 Method of oxygen delivery |
| O2-toedieningssysteem;R TOEDIENINGSSYSTEEM O2 | 1469651 Method of oxygen delivery |
| Toedieningsweg | 1469651 Method of oxygen delivery |
| Zuurstof - methode van toediening | 1469651 Method of oxygen delivery |
| Zuurstof toedieningswijze | 1469651 Method of oxygen delivery |

### 2000000016 — 7/7 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Formulier CAM-ICU RASS Score | 1447532 Richmond Agitation Sedation Scale |
| RASS (Richmond Agitation Sedation Scale) | 1447532 Richmond Agitation Sedation Scale |
| RASS + Deltascan score | 1447532 Richmond Agitation Sedation Scale |
| RASS score | 1447532 Richmond Agitation Sedation Scale |
| RASS score;R UMCA RASS SCORE | 1447532 Richmond Agitation Sedation Scale |
| Richmond Aggitation Sedation Scale | 1447532 Richmond Agitation Sedation Scale |
| Transport RASS score | 1447532 Richmond Agitation Sedation Scale |

### 2000000229 — 7/7 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Aspect Sputum | 4273031 Color of sputum - finding |
| Aspect SputumOud | 4273031 Color of sputum - finding |
| Kleur Sputum | 4273031 Color of sputum - finding |
| Luchtweg Sputum Consistentie | 4273031 Color of sputum - finding |
| Luchtweg Sputum Kleur | 4273031 Color of sputum - finding |
| Sputum classificatie | 4273031 Color of sputum - finding |
| TBT Aspect | 4273031 Color of sputum - finding |

### 2000000629 — 6/6 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Actuele tubediepte (cm);R UMCA TUBE DIEPTE | 3046004 Intubation tube depth Respiratory system |
| Luchtweg Event Diepte tube (cm) | 3046004 Intubation tube depth Respiratory system |
| Niet meer gebruiken Diepte Tube | 3046004 Intubation tube depth Respiratory system |
| Tube diepte | 3046004 Intubation tube depth Respiratory system |
| Tubediepte | 3046004 Intubation tube depth Respiratory system |
| Tubediepte (cm) bij inbrengen;R UMCA TUBE DIEPTE BIJ INBRENGEN | 3046004 Intubation tube depth Respiratory system |

### 2000000034 — 5/5 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Niervervangende therapie | 1988717 Continuous renal replacement therapy mode Renal replacement therapy circuit |
| Prismaflex Instelling Therapie Type | 1988717 Continuous renal replacement therapy mode Renal replacement therapy circuit |
| Prismaflex Therapie Status | 1988717 Continuous renal replacement therapy mode Renal replacement therapy circuit |
| Soort;R UMCA DIALYSE SOORT | 1988717 Continuous renal replacement therapy mode Renal replacement therapy circuit |
| Type behandeling;R UMCA ICU CVVH TYPE BEHANDELING | 1988717 Continuous renal replacement therapy mode Renal replacement therapy circuit |

### 2000000205 — 5/5 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| FIO2 | 21490696 Oxygen [VFr/PPres] Gas delivery system |
| FiO2 % | 21490696 Oxygen [VFr/PPres] Gas delivery system |
| FiO2 onbeademd gecorrigeerd;R FIO2 ONBEADEMD GECORRIGEERD | 21490696 Oxygen [VFr/PPres] Gas delivery system |
| Zephyros FiO2 | 21490696 Oxygen [VFr/PPres] Gas delivery system |
| Zephyros O2i | 21490696 Oxygen [VFr/PPres] Gas delivery system |

### 2000000222 — 5/5 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| AMV spont;R UMCA AN AMVSPONT | 4108000 Spontaneous minute volume |
| AMV spont;R UMCA ICU VENTILATOR AMV SPONT | 4108000 Spontaneous minute volume |
| Adem Minuut Volume - Spontaan | 4108000 Spontaneous minute volume |
| Mv Spontaan | 4108000 Spontaneous minute volume |
| Mv Spontaan(2) | 4108000 Spontaneous minute volume |

### 2000000552 — 5/5 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Blaaskatheter | 4070667 Urinary catheter |
| Blaaskatheter (Blaas) | 4070667 Urinary catheter |
| Catheter a demeure | 4070667 Urinary catheter |
| Nefrostomie drain | 4070667 Urinary catheter |
| Urine-Catheter (CAD) | 4070667 Urinary catheter |

### 36028719 — lidocaine / norepinephrine (RxNorm) — 5/5 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| LIDOCAINE/ADRENALINE INJVL 10MG/ 5UG/ML FL 20ML | 989878 lidocaine, 36029291 epinephrine / lidocaine |
| LIDOCAINE/ADRENALINE INJVL 10MG/ 5UG/ML FL 20MLOUD | 989878 lidocaine |
| LIDOCAINE/ADRENALINE INJVL 20MG/ 5UG/ML FL 20ML | 989878 lidocaine |
| LIDOCAINE/ADRENALINE INJVL 20MG/ 5UG/ML FL 20MLOUD | 989878 lidocaine |
| LIDOCAINE/ADRENALINE INJVL 20MG/12,5UG/ML PATR 1,8 | 989878 lidocaine |

### 2000000015 — 4/4 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Ramsay Sedatie | 4105091 Ramsay sedation scale |
| Ramsay score | 4105091 Ramsay sedation scale |
| Ramsey Score | 4105091 Ramsay sedation scale |
| Sedatiescore | 4105091 Ramsay sedation scale |

### 36030108 — articaine / epinephrine (RxNorm) — 4/4 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ARTICAINE/ADRE INJV 40/0,01MG/ML (HCL) PATR 1,7ML | 19080512 articaine |
| ARTICAINE/ADRE INJV 40/0,01MG/ML (TAR) PATR 1,8ML | 19080512 articaine |
| ARTICAINE/ADRENALINE INJV 40/0,01MG/ML PATR 1,7ML | 19080512 articaine |
| ARTICAINE/ADRENALINE INJV 40/0,01MG/ML PATR 1,8ML | 19080512 articaine |

### 2000000090 — 3/3 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Drain periodieke output (algemene drain) | 3006376 Fluid output wound drain |
| Redonse drain 5 productie | 3006376 Fluid output wound drain |
| Vacuum Assisted Drain 2 Uur | 3006376 Fluid output wound drain |

### 2000000154 — 3/3 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Chemie (s) Transferrineverzadiging | 3000185 Iron saturation [Mass Fraction] in Serum or Plasma |
| TYBC/transf-verz | 3000185 Iron saturation [Mass Fraction] in Serum or Plasma |
| Transferrineverzadiging | 3009814 Iron saturation [Molar fraction] in Serum or Plasma |

### 2000000194 — 3/3 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Hoestprikkel | 4146379 Cough reflex |
| Hoestprikkel;R UMCA HOESTPRIKKEL | 4146379 Cough reflex |
| Motoriek Hoestreflex | 4146379 Cough reflex |

### 2000000199 — 3/3 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Exparation Time | 4353622 Expiratory time |
| T exp;R UMCA AN TEXP | 4353622 Expiratory time |
| Texp (s);R UMCA ICU VENTILATOR EXP TIME | 4353622 Expiratory time |

### 2000000476 — 3/3 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Kunstneuzen | 4178391 Heat and moisture exchanger |
| Luchtweg Spreekklepje | 4178391 Heat and moisture exchanger |
| Spreekklep | 4178391 Heat and moisture exchanger |

### 2000000497 — 3/3 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Cuff druk | 3028878 Tube cuff pressure Intubation tube |
| Cuff druk;R UMCA TUBE CUFF DRUK | 3028878 Tube cuff pressure Intubation tube |
| Cuffdruk | 3028878 Tube cuff pressure Intubation tube |

### 2000000573 — 3/3 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| NATRIUMLAURYLSULF/SORBITOL KLY 9/625MG/ML FL  5ML | 19014215 sodium lauryl sulfoacetate |
| NATRIUMLAURYLSULFOACET/SORBITOL KLYSMA 9/625MG/ML | 19014215 sodium lauryl sulfoacetate |
| PICOZWAVELZUUR/MGO/CITROENZUUR PDR (PICOPREP) | 19136048 sodium |

### 36030184 — carbidopa / entacapone / levodopa (RxNorm) — 3/3 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| LEVODOPA/CARBIDOPA/ENTACAPON TABLET  75/18,7/200MG | 789578 levodopa |
| LEVODOPA/CARBIDOPA/ENTACAPON TABLET 100/25/200MG | 789578 levodopa |
| LEVODOPA/CARBIDOPA/ENTACAPON TABLET 150/37,5/200MG | 789578 levodopa |

### 36030600 — betamethasone / calcipotriene (RxNorm) — 3/3 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| BETAMETHASON/CALCIPOTRIOL GEL 0,5MG/50UG/G | 908921 calcipotriene |
| BETAMETHASON/CALCIPOTRIOL SCHUIM CUTAAN 0,5MG/50UG | 908921 calcipotriene |
| BETAMETHASON/CALCIPOTRIOL ZALF 0,5MG/50UG/G | 908921 calcipotriene |

### 19001311 — epoetin beta (RxNorm) — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| EPOETINE BETA INJV WWSP 30000IE=0,6ML(50.000IE/ML) | 1301125 epoetin alfa |
| EPOETINE BETA INJV WWSP 3000IE=0,3ML(10.000IE/ML) | 1301125 epoetin alfa |

### 19008867 — cromoglycate (RxNorm) — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| CROMOGLICINEZUUR NEUSSPRAY 20MG/ML | 1152631 cromolyn |
| CROMOGLICINEZUUR OOGDRUPPELS 20MG/ML FL 10ML | 1152631 cromolyn |

### 19018407 — adrenalone (RxNorm) — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ZZ-ADRENALINE 0,1 MG/ML INJECTIE IN NACL 0,9% (ONE-STEP MED) | 1343916 epinephrine |
| ZZ-ADRENALINE 1 MG/ML INJECTIE (ONE-STEP MED) | 1343916 epinephrine |

### 19112623 — solfenacin (RxNorm) — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| SOLIFENACINE TABLET  5MG | 916005 solifenacin |
| SOLIFENACINESUCCINAAT AUROBINDO TABLET FILMOMH 5MG | 916005 solifenacin |

### 2000000014 — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Pijnscore VAS | 4158877 Visual analog scale |
| VAS score | 4158877 Visual analog scale |

### 2000000038 — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| CAPD Dialyse duur | 44802884 Duration of haemodialysis |
| Dialyse duur  (minuten);R UMCA HD DURATION OF TREATMENT | 44802884 Duration of haemodialysis |

### 2000000098 — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ST Segment analyse - Afleiding V | 3012255 ST wave end displacement in lead V5 |
| ST V;R UMCA AN STV | 3012255 ST wave end displacement in lead V5 |

### 2000000201 — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Optiflow - FiO2 | 2000000916 Oxygen/Inspired gas Respiratory system --on high flow |
| Optiflow - Ingestelde Flow | 2000000915 Inhaled oxygen flow rate --on high flow |

### 2000000227 — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Rapid Shallow Breathing | 37030869 Rapid shallow breathing index |
| SBI (Zwakke ademhalingsindex) | 37030869 Rapid shallow breathing index |

### 2000000228 — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Motoriek Slikreflex | 4125279 Ability to initiate swallowing reflex |
| Slikken | 4125279 Ability to initiate swallowing reflex |

### 2000000249 — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Trilogy 100 Instellingen Handmatig Modus | 3004921 Ventilation mode Ventilator |
| Ventilator Instellingen Handmatige Modus ICC | 3004921 Ventilation mode Ventilator |

### 2000000801 — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Endotracheale tube | 4097216 Endotracheal tube |
| Tube | 4097216 Endotracheal tube |

### 2000000903 — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Spraak (gedetubeerde patiënt) | 722060 Critical Care Pain Observation Tool (CPOT): Vocalization score |
| Spraak gedetubeerde patient;R UMCA CCPOT SPRAAK | 722060 Critical Care Pain Observation Tool (CPOT): Vocalization score |

### 21060563 — bimatoprost / Timolol Ophthalmic Solution (RxNorm Extension) — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| TIMOLOL/BIMATOPROST OOGDR 5/0,3MG/ML FL 3ML+B(OUD) | 902427 timolol |
| TIMOLOL/BIMATOPROST OOGDR 5/0,3MG/ML FL 3ML+BENZAL | 902427 timolol |

### 36030126 — buprenorphine / naloxone (RxNorm) — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| BUPRENORFINE/NALOXON TABLET SUBLINGU  2/0,5MG | 1133201 buprenorphine |
| BUPRENORFINE/NALOXON TABLET SUBLINGU  8/2MG | 1133201 buprenorphine |

### 42709318 — tocopherol (RxNorm) — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| TOCOFEROL DL-ALFA DRANK 50MG/ML | 19009540 vitamin E |
| TOCOFEROL DL-ALFA TABLET 50MG | 19009540 vitamin E |

### 45775370 — 2-mercaptoethanesulfonic acid (RxNorm) — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| MERCAPTO-ETHAANSULFONZUUR (MESNA) TABLET 400MG | 1354698 mesna |
| MERCAPTO-ETHAANSULFONZUUR 100 MG/ML INJECTIE | 1354698 mesna |

### 778917 — brimonidine / brinzolamide (RxNorm) — 2/2 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| BRINZOLAMIDE/BRIMONIDI OOGDR 10/2MG/ML FL 5ML BENZ | 938044 brinzolamide |
| BRINZOLAMIDE/BRIMONIDINE OOGDR 10/2MG/ML FL 5ML | 938044 brinzolamide |

### 1091076 — Dacrocytes [Presence] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Teardrop cellen | 3000456 Dacrocytes [Presence] in Blood by Light microscopy |

### 1091281 — Kappa light chains.free/Lambda light chains.free [Mass Ratio] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Vrije lichte ketens kappa/lambda | 3053209 Kappa light chains.free/Lambda light chains.free [Mass Ratio] in Serum |

### 1091352 — Poikilocytosis [Presence] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Poikilocytose | 3011368 Poikilocytosis [Presence] in Blood by Light microscopy |

### 1091481 — Hyaline casts [Presence] in Urine sediment (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Hyalinecilinders | 3033308 Hyaline casts [Presence] in Urine sediment by Light microscopy |

### 1091558 — Toxic granules [Presence] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Toxische korreling | 3004381 Toxic granules [Presence] in Blood by Light microscopy |

### 1091589 — Elliptocytes [Presence] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Elliptocyten | 3000493 Elliptocytes [Presence] in Blood by Light microscopy |

### 1091726 — Schistocytes [Presence] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Fragmentocyten | 3028468 Fragments [Presence] in Blood by Light microscopy |

### 1092029 — Giardia lamblia DNA [Presence] in Stool (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Giardia lambliae PCR in feces | 37020937 Giardia lamblia DNA [Presence] in Stool by NAA with probe detection |

### 1092210 — Target cells [Presence] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Targetcellen | 3025616 Target cells [Presence] in Blood by Light microscopy |

### 1092437 — Dohle body [Presence] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Lichaam van Dohle | 3003715 Dohle body [Presence] in Blood by Light microscopy |

### 1395773 — iron sucrose (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| IJZER(III)OX.HYDROX.SACCH.ZETM.COMPL KAUWT 500MGFE | 44785066 sucroferric oxyhydroxide |

### 19069076 — hydroxyethyl cellulose (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| HYDROXYETHYLZETMEEL 60MG/ML INFUUS | 19077117 hetastarch |

### 19101454 — lauromacrogols (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| LAUROMACROGOL 30 MG/ML INJECTIE | 40175900 polidocanol |

### 2000000003 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| AVPU | 40493498 AVPU - alert voice pain unresponsive scale |

### 2000000004 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| CPOT | 722043 Critical Care Pain Observation Tool (CPOT): Total score |

### 2000000011 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| MEWS totaal;R UMCA MEWS TOTAL SCORE | 40492202 Modified early warning score scale |

### 2000000140 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Erythrocyten | 3026361 Erythrocytes [#/volume] in Blood, 3027017 Erythrocytes [#/volume] in Blood by Manual count |

### 2000000175 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| TOF count;R UMCA AN TOFCOUNT | 4353950 Train of four count |

### 2000000176 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| TOF Ratio;R UMCA AN TOF RATIO | 4108453 Train of four ratio |

### 2000000193 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Pauze tijd (s);R UMCA ICU VENTILATOR PAUZE TIJD (S) S | 3003377 Respiration pause setting [Time] Ventilator |

### 2000000338 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Natuurlijke dood | 4297089 Natural death |

### 2000000444 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Urine verz Verzamelperiode | 3016750 Collection duration of Urine |

### 2000000449 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Hematologie (s) Blasten | 3005105 Blasts [#/volume] in Blood |

### 2000000471 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| #Monocyten (MONA) | 3001604 Monocytes [#/volume] in Blood |

### 2000000529 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Locatie sonde;R UMCA SONDE LOCATIE | 2000000503 feeding tube position |

### 2000000640 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ACLS Intubatie | 4168193 Intubation technique |

### 2000000802 — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| CPAP | 605914 Continuous positive airway pressure bilevel positive airway pressure face mask |

### 3000963 — Hemoglobin [Mass/volume] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Hemoglobine | 3012471 Hemoglobin.gastrointestinal.lower [Presence] in Stool by Immunoassay, 40762351 Hemoglobin [Moles/volume] in Blood |

### 3001258 — Hemoglobin C/Hemoglobin.total in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Hemoglobine C | 3044870 Hemoglobin C/Hemoglobin.total in Blood by Electrophoresis |

### 3002364 — Opiates [Mass/volume] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Opiaten | 3027008 Opiates [Presence] in Urine |

### 3003985 — Beta hydroxybutyrate [Moles/volume] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Beta hydroxy butyraat | 40769111 Beta hydroxybutyrate [Moles/volume] in Blood by Test strip |

### 3005480 — E Ag [Presence] on Red Blood Cells (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Bloedgroep antigeen e | 3005222 little e Ag [Presence] on Red Blood Cells |

### 3006796 — Barbiturates [Mass/volume] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Barbituraten | 3002020 Barbiturates [Presence] in Urine |

### 3009337 — Methadone [Mass/volume] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Methadon | 3028707 Methadone [Presence] in Urine by Screen method |

### 3011087 — Output.stool [Volume] (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| output - Faeces | 2000000922 Fluid output faeces |

### 3011258 — Bilirubin.total [Presence] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Bilirubine | 3018834 Bilirubin.total [Presence] in Urine by Test strip, 44816798 Bilirubin.total [Moles/volume] in Cerebral spinal fluid |

### 3011974 — Cocaine [Mass/volume] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Cocaine | 3016879 Cocaine [Presence] in Urine |

### 3012392 — Metamyelocytes [#/volume] in Blood by Manual count (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Metamyelocyten microscop. | 3024507 Metamyelocytes [#/volume] in Blood |

### 3012516 — Albumin [Mass/volume] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Albumine (u) | 3000034 Microalbumin [Mass/volume] in Urine |

### 3013803 — Aspergillus fumigatus IgG Ab [Mass/volume] in Serum (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Aspergillus fumigatus IgG | 3019805 Aspergillus fumigatus IgG Ab [Units/volume] in Serum |

### 3014576 — Chloride [Moles/volume] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Chloride | 3006567 Chloride [Moles/time] in 24 hour Urine, 3007733 Chloride [Moles/volume] in Urine, 3018572 Chloride [Moles/volume] in Blood |

### 3015528 — Cannabinoids [Mass/volume] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Cannabis | 3028300 Cannabinoids [Presence] in Urine |

### 3017680 — Myelocytes [#/volume] in Blood by Manual count (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Myelocyten microscop. | 3021120 Myelocytes [#/volume] in Blood |

### 3020401 — E Ag [Presence] on Red Blood Cells from Donor (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Bloedgroep antigeen E | 3005480 E Ag [Presence] on Red Blood Cells |

### 3020428 — Hemoglobin A/Hemoglobin.total in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Hemoglobine A | 3009131 Hemoglobin A/Hemoglobin.total in Blood by Electrophoresis |

### 3020725 — Methylenedioxymethamphetamine [Mass/volume] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| XTC | 3002148 Methylenedioxymethamphetamine [Presence] in Urine by Screen method |

### 3020784 — Hemoglobin A2/Hemoglobin.total in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Hemoglobine A2 | 3021009 Hemoglobin A2/Hemoglobin.total in Blood by Electrophoresis |

### 3022445 — Amphetamines [Mass/volume] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Amfetamine | 3000144 Amphetamine [Presence] in Urine by Screen method |

### 3024153 — Promyelocytes [#/volume] in Blood by Manual count (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Promyelocyten microscop. | 3022709 Promyelocytes [#/volume] in Blood |

### 3024342 — Plasma cells [#/volume] in Blood by Manual count (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Plasmacellen microscop. | 3001362 Plasma cells [#/volume] in Blood |

### 3024456 — Kell group Ag [Type] on Red Blood Cells (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Bloedgroep antigeen K | 3002394 K Ag [Presence] on Red Blood Cells |

### 3025408 — Oxygen/Inspired gas Respiratory system by O2 Analyzer --on ventilator (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| FiO2;R UMCA ICU VENTILATOR FIO2 M | 3026238 Oxygen/Inspired gas Respiratory system --on ventilator |

### 3025770 — Benzodiazepines [Mass/volume] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Benzodiazepines | 3000764 Benzodiazepines [Presence] in Urine |

### 3027035 — Albumin [Mass/time] in 24 hour Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Albumine | 3005577 Microalbumin [Mass/time] in 24 hour Urine, 3024474 Albumin [Mass/volume] in Cerebral spinal fluid, 3024561 Albumin [Mass/volume] in Serum or Plasma |

### 3027238 — Thyroperoxidase Ab [Units/volume] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Anti thyroid peroxidase | 3028612 Thyroperoxidase Ab [Presence] in Serum or Plasma |

### 3028893 — Ketones [Presence] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Ketostoffen | 3035350 Ketones [Presence] in Urine by Test strip |

### 3033195 — Leukocytes other [#/volume] in Synovial fluid (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Leukocyten (sv) | 3000475 Leukocytes [#/volume] in Synovial fluid |

### 3034107 — Monocytes [#/volume] in Blood by Manual count (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Monocyten microscop. | 3001604 Monocytes [#/volume] in Blood |

### 3034387 — Apolipoprotein B-100 [Mass/volume] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Apo-lipoproteine B100 | 3014791 Apolipoprotein B [Mass/volume] in Serum or Plasma |

### 3037185 — Protein [Presence] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Eiwit | 40760845 Protein [Presence] in Urine by Automated test strip |

### 3038691 — Anisocytosis [Presence] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Anisoplanie | 3040197 Anisochromasia [Presence] in Blood by Light microscopy |

### 3040151 — Glucose [Moles/volume] in Capillary blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Glucose (POC) art/cap | 3001501 Glucose [Moles/volume] in Capillary blood by Glucometer |

### 3042812 — Nitrite [Presence] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Nitriet | 3021601 Nitrite [Presence] in Urine by Test strip |

### 3044630 — ABO and Rh group panel - Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Bloedgroep rhesus D conclusie | 3003694 ABO and Rh group [Type] in Blood |

### 3045414 — Leukocytes [Presence] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Leukocyten | 3000348 Leukocyte esterase [Presence] in Urine by Test strip, 3010813 Leukocytes [#/volume] in Blood |

### 3046071 — Choriogonadotropin.intact+Beta subunit [Units/volume] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| HCG (+ beta-subunits) | 3038136 Choriogonadotropin.beta subunit [Units/volume] in Serum or Plasma |

### 36027016 — betamethasone / salicylic acid (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| BETAMETHASON/SALICYLZUUR ZALF 0,5/ 30MG/G | 920458 betamethasone |

### 36027059 — miconazole / zinc oxide (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| MICONAZOL 2% ZINKOXIDESMEERSEL | 907879 miconazole |

### 36028316 — alginic acid / sodium bicarbonate (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ALGINEZUUR/NATRIUMWATERSTOFCARBON SUSP 50/27MG/ML | 19030059 alginic acid |

### 36028785 — benzocaine / oxyquinoline (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| OXYBUPROCAINE OOGDR 4MG/ML MINIM 0,4ML Z BENZ | 935529 benoxinate |

### 36029208 — chlorhexidine / didecyldimethylammonium chloride (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| NATRIUMCHLORIDE BLAASSPOELING 9MG/ML ZAK (SHELL) | 967823 sodium chloride |

### 36029293 — bupivacaine / epinephrine (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| BUPIVACAINE/ADRENALINE INJVLST 5MG/5UG/ML FL 20ML | 732893 bupivacaine |

### 36029616 — allantoin / zinc oxide (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ZINKOXIDE ZALF 100MG/G | 911064 zinc oxide |

### 36029651 — atenolol / chlorthalidone (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ATENOLOL/CHLOORTALIDON TABLET  50/12,5MG | 1314002 atenolol |

### 36029755 — Glycopyrrolate / Indacterol (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| INDACAT/GLYCOPYRRO INHALCAP 110/50UG (85/43UG) INH | 36029758 glycopyrronium / indacaterol |

### 36029974 — enalapril / hydrochlorothiazide (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ENALAPRIL/HYDROCHLOORTHIAZIDE TABLET 20/12,5MG | 1341927 enalapril |

### 36029982 — estradiol / norethindrone (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ESTRADIOL/NORETHISTERON TAB (TRISEQUENS) | 36030139 ethinyl estradiol / norethindrone |

### 36029999 — hydrochlorothiazide / irbesartan (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| IRBESARTAN/HYDROCHLOORTHIAZIDE TABLET 150/12,5MG | 1347384 irbesartan |

### 36030000 — hydrochlorothiazide / lisinopril (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| LISINOPRIL/HYDROCHLOORTHIAZIDE TABLET 20/12,5MG | 1308216 lisinopril |

### 36030109 — atovaquone / proguanil (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ATOVAQUON/PROGUANIL TABLET FO 250/100MG | 1792429 proguanil |

### 36030331 — desoximetasone / salicylic acid (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| DESOXIMETASON/SALICYLZUUR EMULSIE CUT 2,5/100MG/G | 917336 desoximetasone |

### 36030536 — hydrocortisone / polymyxin B (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| HYDROCORTISON/OXYTETRACYCL/POLYMYX B OOGZALF 3,5G | 975125 hydrocortisone |

### 36030964 — hydrochlorothiazide / olmesartan (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| OLMESARTAN/HYDROCHLOORTHIAZIDE TABLET 40/25MG | 40226742 olmesartan |

### 36086759 — Antithymocyte immunoglobulin (equine) (RxNorm Extension) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| THYMOCYTENIMMUNOGLOBULINE INFUUS | 19136207 lymphocyte immune globulin, anti-thymocyte globulin |

### 36304468 — Casts [Presence] in Urine (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Cylinders | 3003291 Casts [Presence] in Urine sediment by Light microscopy |

### 36850450 — MEDOSULEPINE (RxNorm Extension) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| DOSULEPINE CAPSULE 25MG | 19037989 dothiepin |

### 36854608 — LOPIRAZEPAM (RxNorm Extension) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| LOPRAZOLAM TABLET 1MG | 19042550 triazulenone |

### 36878978 — amidotrizoate lysine (RxNorm Extension) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| AMIDOTRIZOINEZUUR DRANK/KLYSMACONC 370MGI/ML | 45775324 diatrizoic acid |

### 40171076 — sodium selenate (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| NATRIUMSELENIET INJVLST 50UG SE/ML FL 10ML | 19066274 selenite |

### 40757494 — Bilirubin.total [Moles/volume] in Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Bilirubine Totaal | 3006140 Bilirubin.total [Moles/volume] in Serum or Plasma |

### 40765038 — 1,25-Dihydroxyvitamin D [Mass/volume] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Vitamine D | 3024390 25-hydroxyvitamin D3 [Moles/volume] in Serum or Plasma |

### 42800027 — varicella-zoster virus vaccine live (Oka-Merck) strain (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ZOSTERVACCIN INJPDR 50UG (RECOMBINANT) FL | 792777 varicella zoster virus glycoprotein E |

### 42868453 — Bicarbonate [Moles/volume] standard in Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Standaard bicarbonaat | 3014218 Bicarbonate [Moles/volume] standard in Arterial blood |

### 42868674 — Cholesterol in HDL/Cholesterol.total [Molar ratio] in Serum or Plasma (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Cholesterol-HDL Ratio | 3016087 Cholesterol.total/Cholesterol in HDL [Molar ratio] in Serum or Plasma |

### 42904275 — cranberry juice (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| CRANBERRY BALANS TABLET | 36878782 Multivitamin preparation |

### 43533850 — Gamma hydroxybutyrate [Mass/volume] in Serum, Plasma or Blood (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Gammahydroxyboterzuur | 3035708 Gamma hydroxybutyrate [Presence] in Urine |

### 44816698 — Lithium [Moles/volume] in Serum or Plasma --trough (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Lithium dal | 3024666 Lithium [Moles/volume] in Serum or Plasma |

### 44816815 — Nortriptyline [Mass/volume] in Serum or Plasma --trough (LOINC) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| Nortryptiline dal | 3007857 Nortriptyline [Mass/volume] in Serum or Plasma |

### 45775636 — meningococcal group B vaccine (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| MENINGOKOKKENVACCIN B(BEXSERO) WWSP 0,5ML | 36878723 Neisseria meningitidis Group B Membrane vesicles External Omv |

### 778806 — drospirenone / estradiol (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| ETHINYLESTRADIOL/DROSPIRENON TAB 30UG/3MG | 36031101 drospirenone / ethinyl estradiol |

### 778911 — azelastine / fluticasone (RxNorm) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| AZELASTINE/FLUTICASON NEUSSPRAY 137/50UG/DO 120 DO | 1149380 fluticasone |

### 902725 — Doxorubicin pegylated liposomal (RxNorm Extension) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| DOXORUBICINE LIPOSOMAAL INFUUS <90MG | 1338512 doxorubicin |

### 902730 — Cytarabine liposomal (RxNorm Extension) — 1/1 parameters remapped ·  **

| Parameter | Now maps to |
|-----------|-------------|
| CYTARABINE LIPOSOMAAL 10MG/ML INJECTIE INTRATHECAAL | 1311078 cytarabine |

### 19054245 — protamines (RxNorm) — 42/45 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| PROTAMINE 1000 IE/ML INJECTIE | 19054242 protamine sulfate (USP) |
| PROTAMINE 12600 ie/9 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 1400 ie/1 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 14000 ie/10 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 16000 ie/11,4 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 16100 ie/11,5 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 16240 ie/11,6 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 16800 ie/12 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 18 mg/1,8 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 19600 ie/14 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 19880 ie/14,2 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 20 mg/2 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 20000 ie/14,3 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 20020 ie/14,3 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 21000 ie/15 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 22000 ie/15,7 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 22400 ie/16 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 23800 ie/17 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 23940 ie/17,1 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 24000 ie/17,1 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 25 mg/2,5 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 25200 ie/18 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 26600 ie/19 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 2800 ie/2 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 28000 ie/20 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 33320 ie/23,8 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 35 mg/3,5 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 35000 ie/25 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 36400 ie/26 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 4200 ie/3 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 4900 ie/3,5 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 49000 ie/35 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 50 mg/5 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 5000 ie/3,6 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 5600 ie/4 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 7000 ie/5 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 7500 ie/5,4 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE 9800 ie/7 ml | 19054242 protamine sulfate (USP) |
| PROTAMINE INJ 1400IE/ML (SULFAAT,10MG/ML) AMP 5ML | 19054242 protamine sulfate (USP) |
| PROTAMINE INJVLST 1000IE/ML (HCL) AMP 5ML | 19054242 protamine sulfate (USP) |
| PROTAMINE KORTLOPEND INFUUS | 19054242 protamine sulfate (USP) |
| PROTAMINE KORTLOPEND INFUUS ONVERDUND | 19054242 protamine sulfate (USP) |

### 1551099 — prednisone (RxNorm) — 11/20 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| PREDNISOLON 25 MG/ML INJECTIE INTRATHECAAL | 1550557 prednisolone |
| PREDNISOLON DRANK 1MG/ML | 1550557 prednisolone |
| PREDNISOLON DRANK 5MG/ML | 1550557 prednisolone |
| PREDNISOLON LANGLOPEND INFUUS | 1550557 prednisolone |
| PREDNISOLON NA-SUCCINAAT 25MG/ML INJECTIE KIND | 1550557 prednisolone |
| PREDNISOLON NA-SUCCINAAT INJ 25MG FL (PARENTERAAL) | 1550557 prednisolone |
| PREDNISOLON OOGDR  5MG/ML M 0,5ML | 1550557 prednisolone |
| PREDNISOLON OOGDR SUSP 10MG/ML FL 5ML BENZALKONIUM | 1550557 prednisolone |
| PREDNISOLON OOGDR, SUSP 10MG/ML FL 5ML | 1550557 prednisolone |
| PREDNISOLON TABLET 30MG | 1550557 prednisolone |
| ZZ-PREDNISOLON 25 MG/ML INJECTIE (ONE-STEP MED) | 1550557 prednisolone |

### 36256123 — calcium gluconolactaat (RxNorm Extension) — 7/9 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| CALCIUMGLUCONAAT 1000 mg/0,01 ml | 19037038 calcium gluconate |
| CALCIUMGLUCONAAT 1000 mg/0,1 ml | 19037038 calcium gluconate |
| CALCIUMGLUCONAAT 1000 mg/100 ml | 19037038 calcium gluconate |
| CALCIUMGLUCONAAT 2000 mg/20 ml | 19037038 calcium gluconate |
| CALCIUMGLUCONAAT 3000 mg/30 ml | 19037038 calcium gluconate |
| CALCIUMGLUCONAAT 5000 mg/50 ml (100 mg/ml) | 19037038 calcium gluconate |
| CALCIUMGLUCONAAT INJ 100MG/ML(0,225MMOL CA/ML)10ML | 19037038 calcium gluconate |

### 46221581 — insulin isophane (RxNorm) — 7/9 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| HUMULINE NPH INJ 100IE/ML PATROON 3ML | 19091621 insulin, protamine zinc, human |
| INSULATARD FLEXPEN INJ 100IE/ML PEN 3ML | 19091621 insulin, protamine zinc, human |
| INSULATARD INJ 100IE/ML FLACON 10ML | 19091621 insulin, protamine zinc, human |
| INSULINE ISOFAAN (HUMULINE NPH) PENFILL 100IE/ML PATR 3ML | 19091621 insulin, protamine zinc, human |
| INSULINE ISOFAAN (INSULATARD) 100IE/ML FLEXPEN | 19091621 insulin, protamine zinc, human |
| INSULINE ISOFAAN (INSULATARD) 100IE/ML PENFILL | 19091621 insulin, protamine zinc, human |
| INSULINE ISOFAAN INJSUSP PEN 300IE=3ML (100IE/ML) | 19091621 insulin, protamine zinc, human |

### 1718517 — acetylsalicylsalicylic acid (RxNorm) — 6/19 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| ACETYLSALICYLZUUR CARDIO AUROBINDO DISP TABL 80MG | 1112807 aspirin |
| ACETYLSALICYLZUUR CARDIO TEVA DISP TABLET 80MG | 1112807 aspirin |
| ACETYLSALICYLZUUR TABLET  80MG | 1112807 aspirin |
| ACETYLSALICYLZUUR TABLET 500MG | 1112807 aspirin |
| ZZ-ACETYLSALICYLZUUR 100MG/ML INJECTIE (ONE-STEP MED) | 1112807 aspirin |
| ZZ-ACETYLSALICYLZUUR DISPERTABLET 80MG (ONE-STEP MED) | 1112807 aspirin |

### 2000000577 — Albumine 20% (ICUdata) — 6/9 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| ALBUMINE 20000 mg/100 ml | 1344143 albumin human, USP |
| ALBUMINE 20000 mg/100 ml (200 mg/ml) | 1344143 albumin human, USP |
| ALBUMINE 40000 mg/200 ml | 1344143 albumin human, USP |
| ALBUMINE 40000 mg/200 ml (200 mg/ml) | 1344143 albumin human, USP |
| ALBUMINE 48000 mg/240 ml | 1344143 albumin human, USP |
| ALBUMINE 80000 mg/400 ml (200 mg/ml) | 1344143 albumin human, USP |

### 19095164 — cholecalciferol (RxNorm) — 5/20 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| COLECALCIFEROL BENFEROL CAPSULE   5600IE | 19009405 vitamin D |
| COLECALCIFEROL CAPSULE  25.000IE | 19009405 vitamin D |
| COLECALCIFEROL DRUPPELS 960IE/ML | 19009405 vitamin D |
| D-CURA DRANK  25000IE AMPUL 1ML | 19009405 vitamin D |
| VITAMINE D ADDED CAPSULE 400IE | 19009405 vitamin D |

### 19111620 — folic acid (RxNorm) — 5/17 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| FOLINEZUUR 10MG/ML INJECTIE | 1388796 leucovorin |
| FOLINEZUUR INJVLST 10MG/ML FL 5ML | 1388796 leucovorin |
| FOLINEZUUR KORTLOPEND INFUUS <100 MG IN NACL 0,9% | 1388796 leucovorin |
| FOLINEZUUR OOGDRUPPELS 0,3MG/ML FL 10ML BENZ | 1388796 leucovorin |
| FOLINEZUUR POEDER VOOR INJECTIE | 1388796 leucovorin |

### 35198096 — insulin aspart (RxNorm Extension) — 5/29 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| FIASP FLEXTOUCH INJVLST 100E/ML PEN 3ML | 1567198 insulin aspart, human |
| INSULINE ASPART FLEXPEN 100E/ML AANGEPAST BIJSPUITSCHEMA | 1567198 insulin aspart, human |
| INSULINE ASPART INJVLST 100E/ML PENFILL PATROON 3ML | 1567198 insulin aspart, human |
| INSULINE ASPART PENFILL | 1567198 insulin aspart, human |
| NOVORAPID FLEXPEN INJVLST 100E/ML PEN 3ML | 1567198 insulin aspart, human |

### 36027314 — insulin aspart protamine, human / insulin aspart, human (RxNorm) — 5/8 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| INSULINE ASPAR/PROT PEN 90/210E=3ML (30/70E/ML) | 1531601 insulin aspart protamine, human |
| INSULINE ASPAR/PROT PENFILL 90/210E=3ML (30/70E/ML) | 1531601 insulin aspart protamine, human |
| INSULINE ASPART/PROTAMINE INJS 30/70E/ML PATR 3ML | 1531601 insulin aspart protamine, human |
| NOVOMIX 30 FLEXPEN INJ 100E/ML PEN 3ML | 1531601 insulin aspart protamine, human |
| NOVOMIX 30 PENFILL INJ 100E/ML PATROON 3ML | 1531601 insulin aspart protamine, human |

### 36030344 — dorzolamide / timolol (RxNorm) — 5/6 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| TIMOLOL/DORZOLAM OOGDR 5/20MG/ML M 0,2ML Z CON OUD | 902427 timolol |
| TIMOLOL/DORZOLAMID OOGDR 5/20MG/ML FL 5ML BENZ | 902427 timolol |
| TIMOLOL/DORZOLAMIDE OOGDR 5/20MG/ML FL 10ML Z BENZ | 902427 timolol |
| TIMOLOL/DORZOLAMIDE OOGDR 5/20MG/ML M 0,2ML Z BENZ | 902427 timolol |
| TIMOLOL/DORZOLAMIDE OOGDRUPPELS 5/20MG/ML FL  5ML | 902427 timolol |

### 36029225 — carbidopa / levodopa (RxNorm) — 4/16 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| LEVODOPA/CARBIDOPA GEL GASTRO-ENT 20/5MG/ML 100ML | 789578 levodopa |
| LEVODOPA/CARBIDOPA TABLET   50/12,5MG | 789578 levodopa |
| LEVODOPA/CARBIDOPA TABLET  250/25MG | 789578 levodopa |
| LEVODOPA/CARBIDOPA TABLET MGA 100/25MG | 789578 levodopa |

### 36029811 — amoxicillin / clavulanate (RxNorm) — 4/19 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| AMOXICILLINE/CLAVULAANZUUR (1000/200MG) KORTLOPEND INFUUS | 1713332 amoxicillin |
| AMOXICILLINE/CLAVULAANZUUR 50/5 MG/ML INJECTIE | 1713332 amoxicillin |
| AMOXICILLINE/CLAVULAANZUUR INJPDR  500/50MG FL | 1713332 amoxicillin |
| AMOXICILLINE/CLAVULAANZUUR TABLET 875/125MG | 1713332 amoxicillin |

### 948515 — polyethylene glycols (RxNorm) — 4/11 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| MACROGOL POEDER V DRANK  4G | 948487 polyethylene glycol 300 |
| MACROGOL POEDER V DRANK 10G | 948487 polyethylene glycol 300 |
| MACROGOL/ZOUTEN CONC. V DRANK | 36030544 polyethylene glycol 400 / propylene glycol |
| MACROGOL/ZOUTEN PDR V DRANK (KLEAN PREP) | 948487 polyethylene glycol 300 |

### 21490851 — Invasive Diastolic blood pressure (LOINC) — 3/10 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| ABP S/D 2;R UMCA  ABP S/D ARTLIJN 2 | 21490850 Invasive Blood pressure |
| ABP S/D;R UMCA AN ABP S/D | 21490850 Invasive Blood pressure |
| ABP s/d;R UMCA  ABP S/D ARTLIJN 1 | 21490850 Invasive Blood pressure |

### 21490853 — Invasive Systolic blood pressure (LOINC) — 3/12 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| ABP S/D 2;R UMCA  ABP S/D ARTLIJN 2 | 21490850 Invasive Blood pressure |
| ABP S/D;R UMCA AN ABP S/D | 21490850 Invasive Blood pressure |
| ABP s/d;R UMCA  ABP S/D ARTLIJN 1 | 21490850 Invasive Blood pressure |

### 1355889 — amifampridine (RxNorm) — 2/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| FAMPRIDINE TABLET 5MG | 40170680 dalfampridine |
| FAMPRIDINE TABLET 7,5MG | 40170680 dalfampridine |

### 19124906 — magnesium (RxNorm) — 2/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| MAGNESIUM CITRAAT LIVSANE TABLET | 967861 magnesium citrate |
| MAGNESIUMCHL INJ CONC 101,6MG/ML (0,5MMOL/ML) 5ML | 19092849 magnesium chloride |

### 2000000580 — dexamethasone / framycetin / gramicidin (ICUdata) — 2/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| DEXAMETHASON/FRAMYCETINE/GRAMICIDINE OOGDR FL 8OUD | 1518254 dexamethasone |
| DEXAMETHASON/FRAMYCETINE/GRAMICIDINE OORDR | 1518254 dexamethasone |

### 36030001 — hydrochlorothiazide / losartan (RxNorm) — 2/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| LOSARTAN/HYDROCHLOORTHIAZIDE TAB OMHULD  50/12,5MG | 1367500 losartan |
| LOSARTAN/HYDROCHLOORTHIAZIDE TABLET 100/12,5MG | 1367500 losartan |

### 36030113 — hydrochlorothiazide / telmisartan (RxNorm) — 2/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| TELMISARTAN/HYDROCHLOORTHIAZIDE TABLET 40/12,5MG | 1317640 telmisartan |
| TELMISARTAN/HYDROCHLOORTHIAZIDE TABLET 80/12,5MG | 1317640 telmisartan |

### 36030140 — latanoprost / timolol (RxNorm) — 2/6 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| TIMOLOL/LATANOPROST OOGDR 5MG/50UG/ML 2,5ML BENZAL | 902427 timolol |
| TIMOLOL/LATANOPROST OOGDR 5MG/50UG/ML 2,5ML Z CONS | 902427 timolol |

### 36850940 — LEVOMETIOMEPRAZINE (RxNorm Extension) — 2/6 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| LEVOMEPROMAZINE 12,5 MG/ML INJECTIE IN NACL 0,9% | 19005147 methotrimeprazine |
| LEVOMEPROMAZINE 25 MG/ML INJECTIE INTRAMUSCULAIR | 19005147 methotrimeprazine |

### 793127 — magnesium sulfite (RxNorm) — 2/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| MAGNESIUMSULFAAT 100 MG/ML INJECTIE | 19093848 magnesium sulfate |
| MAGNESIUMSULFAAT INJVLST 200MG/ML FL 50ML | 19093848 magnesium sulfate |

### 1183554 — isoproterenol (RxNorm) — 1/7 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| ISOPRENALINE 5 mg/50 ml (0,1 mg/ml) | 43013090 isoprene |

### 1502905 — insulin glargine (RxNorm) — 1/14 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| APIDRA SOLOSTAR INJ 100E/ML PEN 3ML | 1544838 insulin glulisine, human |

### 1549786 — ethinyl estradiol (RxNorm) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| ETHINYLESTRADIOL TABLET 0,05MG | 1503184 mestranol |

### 19005046 — pyridoxine (RxNorm) — 1/6 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| PYRIDOXINE TABLET  50MG | 1353228 vitamin B6 |

### 19010128 — vitamin K (RxNorm) — 1/6 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| FYTOMENADION CONCENTRAAT 10MG/ML DRUPPELS | 19044727 vitamin K1 |

### 19012565 — mycophenolic acid (RxNorm) — 1/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| MYCOFENOLZUUR TABLET MSR 360MG | 19003999 mycophenolate mofetil |

### 19078126 — sodium polystyrene sulfonate (RxNorm) — 1/9 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| POLYSTYREENSULFONAAT NATRIUM (RESONIUM A) POEDER 999,34MG/G | 45775570 polystyrene sulfonate |

### 19112563 — calcium polystyrene sulfonate product (RxNorm) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| POLYSTYREENSULFONAAT CALCIUM (SORBISTERIT) POEDER 900MG/G | 45775570 polystyrene sulfonate |

### 2000000431 — Pacemaker frequency (ICUdata) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Ventriculaire frequentie;R UMCA PACEMAKER VENTRICULAR RATE | 4185148 Cardiac pacing rate |

### 2000000458 — Vitamin B6 [Moles/volume] in Serum or Plasma (ICUdata) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Vitamine B6 | 44787085 Pyridoxal phosphate [Moles/volume] in Blood |

### 2000000581 — dexamethasone / gentamicin (ICUdata) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| DEXAMETHASON/GENTAMICINE OOGZALF 0,3/3MG/G TUBE 3G | 1518254 dexamethasone |

### 21490752 — Tidal volume expired Respiratory system airway (LOINC) — 1/7 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Exp. tidal volume | 21490789 Tidal volume expired Respiratory system airway --on ventilator |

### 3000461 — Pressure support setting Ventilator (LOINC) — 1/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Ventilator Instellingen Handmatig Pressure Support | 2000000628 inspiratory pressure on pressure support |

### 3001308 — Cholesterol in LDL [Moles/volume] in Serum or Plasma (LOINC) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| LDL Cholesterol | 3038988 Cholesterol in LDL [Moles/volume] in Serum or Plasma by calculation |

### 3002030 — Lymphocytes/Leukocytes in Blood (LOINC) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Lymfocyten | 3007357 Lymphoma cells/Leukocytes in Blood, 3019198 Lymphocytes [#/volume] in Blood |

### 3003181 — Sodium [Moles/volume] in Urine (LOINC) — 1/6 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Natrium | 3000285 Sodium [Moles/volume] in Blood, 3002079 Sodium [Moles/time] in 24 hour Urine, 3019550 Sodium [Moles/volume] in Serum or Plasma |

### 3003573 — C Ag [Presence] on Red Blood Cells (LOINC) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Rhesus c antigeen | 3005186 little c Ag [Presence] on Red Blood Cells |

### 3004410 — Hemoglobin A1c/Hemoglobin.total in Blood (LOINC) — 1/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| HbA1c | 40762352 Hemoglobin A1c/Hemoglobin.total in Blood by IFCC protocol |

### 3006315 — Basophils [#/volume] in Blood (LOINC) — 1/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Basofielen | 3013429 Basophils [#/volume] in Blood by Automated count, 3022096 Basophils/Leukocytes in Blood |

### 3006576 — Bicarbonate [Moles/volume] in Blood (LOINC) — 1/6 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Standaard bicarbonaat | 3014218 Bicarbonate [Moles/volume] standard in Arterial blood |

### 3007461 — Platelets [#/volume] in Blood (LOINC) — 1/10 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Trombocyten | 3024929 Platelets [#/volume] in Blood by Automated count |

### 3009306 — Alpha-1-Fetoprotein [Mass/volume] in Serum or Plasma (LOINC) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| AFP (alfa-foetoproteine) | 3015916 Alpha-1-Fetoprotein [Units/volume] in Serum or Plasma |

### 3009932 — Eosinophils [#/volume] in Blood by Manual count (LOINC) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Eosinofielen microscop. | 3013115 Eosinophils [#/volume] in Blood |

### 3010421 — pH of Blood (LOINC) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| pH | 3015736 pH of Urine |

### 3011335 — Digoxin [Mass/volume] in Serum or Plasma (LOINC) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| digoxine | 1326303 digoxin |

### 3012501 — Base excess in Blood by calculation (LOINC) — 1/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Base excess | 3003396 Base excess in Arterial blood by calculation |

### 3013603 — Prostate specific Ag [Mass/volume] in Serum or Plasma (LOINC) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| PSA totaal | 3034548 Prostate specific Ag [Mass/volume] in Serum or Plasma by Detection limit <= 0.01 ng/mL |

### 3016502 — Oxygen saturation in Arterial blood (LOINC) — 1/5 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| SO2 | 3011367 Oxygen saturation Calculated from oxygen partial pressure in Blood, 3024928 Oxygen saturation in Venous blood |

### 3018133 — Calcium [Moles/volume] in Urine (LOINC) — 1/8 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Calcium | 3005162 Calcium [Moles/volume] in Blood, 3010838 Calcium [Moles/time] in 24 hour Urine, 3015377 Calcium [Moles/volume] in Serum or Plasma |

### 3018199 — Band form neutrophils [#/volume] in Blood (LOINC) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Staafkernigen microscop. | 3007591 Band form neutrophils/Leukocytes in Blood by Manual count |

### 3019597 — S Ag [Presence] on Red Blood Cells (LOINC) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Bloedgroep antigeen s | 3006768 little s Ag [Presence] on Red Blood Cells |

### 3023520 — Reticulocytes [#/volume] in Blood (LOINC) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Reticulocyten | 40763528 Reticulocytes [#/volume] in Blood by Automated count |

### 3023669 — Thiamine [Moles/volume] in Serum or Plasma (LOINC) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Vitamine B1 | 44787087 Thiamine pyrophosphate [Moles/volume] in Blood |

### 3024171 — Respiratory rate (LOINC) — 1/10 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Ademfreq. | 3007469 Breath rate setting Ventilator |

### 3026782 — Osmolality of Urine (LOINC) — 1/5 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Osmolaliteit | 3008295 Osmolality of Serum or Plasma |

### 3027651 — Basophils [#/volume] in Blood by Manual count (LOINC) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Basofielen microscop. | 3013429 Basophils [#/volume] in Blood by Automated count |

### 3027874 — Urate [Moles/volume] in Urine (LOINC) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Urinezuur | 3026493 Urate [Moles/volume] in Serum or Plasma |

### 3029187 — Natriuretic peptide.B prohormone N-Terminal [Mass/volume] in Serum or Plasma (LOINC) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| NT-proBNP | 3029435 Natriuretic peptide.B prohormone N-Terminal [Moles/volume] in Serum or Plasma |

### 3033543 — Specific gravity of Urine (LOINC) — 1/5 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Soortelijk gewicht | 3000330 Specific gravity of Urine by Test strip |

### 3034551 — Parathyrin [Mass/volume] in Serum or Plasma --baseline (LOINC) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| Parathormoon | 3010566 Parathyrin.intact [Moles/volume] in Serum or Plasma |

### 35894860 — Psyllium husks (RxNorm Extension) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| PLANTAGO OVATA POEDER 3,4G | 19132965 Plantago seed, 42899921 Plantago ovata seed extract |

### 36029071 — amlodipine / olmesartan (RxNorm) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| OLMESARTAN/AMLODIPINE/HCT TAB 20/5/12,5MG | 36028870 amlodipine / hydrochlorothiazide / olmesartan |

### 36029153 — aluminum oxide / magnesium hydroxide (RxNorm) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| ALGELDRAAT/MAGNESIUMHYDROXIDE SUSP ZAKJE 900/600MG | 992956 magnesium hydroxide |

### 36029713 — avibactam / ceftazidime (RxNorm) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| CEFTAZIDIM/AVIBACTAM INFUSIEPOEDER 2000/500MG FL | 1776684 ceftazidime |

### 36029883 — amiloride / hydrochlorothiazide (RxNorm) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| AMILORIDE/HYDROCHLOORTHIAZIDE TABLET 5/50MG | 974166 hydrochlorothiazide |

### 36030110 — candesartan / hydrochlorothiazide (RxNorm) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| CANDESARTAN/HYDROCHLOORTHIAZIDE TABLET 16/12,5MG | 1351557 candesartan |

### 36030141 — indapamide / perindopril (RxNorm) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| PERINDOPRIL/INDAPAMIDE TABLET  4/1,25MG (ERBUMINE) | 1373225 perindopril |

### 36030258 — brimonidine / timolol (RxNorm) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| TIMOLOL/BRIMONIDINE OOGDR 5/2MG/ML FL 5ML BENZ | 902427 timolol |

### 36030306 — benserazide / levodopa (RxNorm) — 1/8 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| LEVODOPA/BENSERAZIDE DISPERTABLET 100/25MG | 789578 levodopa |

### 36030773 — piperacillin / tazobactam (RxNorm) — 1/9 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| PIPERACILLINE/TAZOBACTAM 200/25 MG/ML INJECTIE | 1746114 piperacillin |

### 36031113 — dexamethasone / tobramycin (RxNorm) — 1/6 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| DEXAMETHASON/TOBRAMYCINE OOGZALF 1/3MG/G TUBE 3,5G | 1518254 dexamethasone |

### 36859517 — SUXETHONIUM (RxNorm Extension) — 1/4 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| SUXAMETHONIUM 50 MG/ML INJECTIE | 836208 succinylcholine |

### 36878782 — Multivitamin preparation (RxNorm Extension) — 1/14 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| OTC TABLET MET O.A. VITAMINE K | 19010128 vitamin K |

### 40798855 — Glycerophosphoric Acid (RxNorm Extension) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| GLYCEROFOSFORZ. INFCONC 1MMOL/ML(FOSFAAT) FL 20ML | 43526717 glyceryl phosphate |

### 42900359 — calcitonin (RxNorm) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| CALCITONINE 100IE/ML INJECTIE | 1537655 salmon calcitonin |

### 778785 — amylase / lipase / protease (RxNorm) — 1/10 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| AMYLA/LIPA/PROTEA CA MSR (CREO F+25000/GEN/PANTRI) | 778797 amylase / lipase / pancreatin / protease |

### 778933 — ceftolozane / tazobactam (RxNorm) — 1/2 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| CEFTOLOZAAN/TAZOBACTAM INFUSIEPOEDER 1000/500MG FL | 45892599 ceftolozane |

### 917336 — desoximetasone (RxNorm) — 1/5 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| ZZ-DEXAMETHASON 4 MG/ML INJECTIE (ONE-STEP MED) | 1518254 dexamethasone |

### 929549 — acetic acid (RxNorm) — 1/3 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| AZIJNZUUR/TRIAMCINOLONACETONIDE OORDR 7,2/1MG/G | 903963 triamcinolone |

### 965748 — scopolamine (RxNorm) — 1/5 parameters remapped

| Parameter | Now maps to |
|-----------|-------------|
| SCOPOLAMINEBUTYL ZETPIL 10MG | 40234201 butylscopolamine |

