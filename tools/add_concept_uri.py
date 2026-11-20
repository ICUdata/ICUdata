"""Voeg resolvable URI-kolommen toe aan de ICUdata dictionary.

Gebruik:  python add_concept_uri.py <pad/naar/dictionary.csv> [<uitvoer.csv>]
Zonder uitvoerpad wordt het invoerbestand overschreven.

Kolommen die erbij komen:
  concept_uri  - OHDSI Athena-pagina van het OMOP-concept (alle standaardconcepten),
                 of de ICUdata-conceptpagina voor eigen concepten (concept_id >= 2.000.000.000)
  source_uri   - canonieke URI in de bronvocabulaire (SNOMED, LOINC, RxNorm), anders leeg

Voor <tabel>_values.csv komen er concept_uri en value_uri bij (voor het gecodeerde antwoord).

Bij de volledige dictionary.csv schrijft het script ook een Markdown-pagina met alle eigen ICUdata-concepten
(icudata_concepts.md naast het uitvoerbestand), waar concept_uri naar verwijst.
"""
import sys
from urllib.parse import quote

import pandas as pd
from pathlib import Path

ATHENA = "https://athena.ohdsi.org/search-terms/terms/{id}"
# Pas aan als de pagina met eigen concepten ergens anders komt te staan.
ICUDATA = "https://github.com/ICUdata/ICUdata/blob/main/concepts/icudata_concepts.md#c{id}"

SOURCE = {
    "SNOMED": "http://snomed.info/id/{code}",
    "LOINC": "https://loinc.org/{code}/",
    "RxNorm": "http://purl.bioontology.org/ontology/RXNORM/{code}",
}
CUSTOM_MIN = 2_000_000_000


def is_custom(row):
    return int(row.concept_id) >= CUSTOM_MIN or getattr(row, "vocabulary_id", "") == "ICUdata"


def uri_for_id(concept_id):
    if not concept_id or concept_id == "0":
        return ""
    tpl = ICUDATA if int(concept_id) >= CUSTOM_MIN else ATHENA
    return tpl.format(id=concept_id)


def concept_uri(row):
    tpl = ICUDATA if is_custom(row) else ATHENA
    return tpl.format(id=row.concept_id)


def source_uri(row):
    tpl = SOURCE.get(row.vocabulary_id)
    if not tpl or not row.concept_code:
        return ""
    return tpl.format(code=quote(str(row.concept_code), safe="-"))


def write_custom_page(rows, path):
    """Eén vast anker per eigen concept, zodat elke concept_uri ergens naartoe leidt."""
    rows = rows.drop_duplicates("concept_id").sort_values("concept_id")
    lines = [
        "# Eigen ICUdata-concepten / Custom ICUdata concepts",
        "",
        "Concepten met `concept_id` vanaf 2.000.000.000 zitten niet in een standaardvocabulaire.",
        "Deze pagina is hun persistente referentie. / Concepts with `concept_id` from 2,000,000,000",
        "are not in a standard vocabulary; this page is their persistent reference.",
        "",
    ]
    for r in rows.itertuples():
        lines += [
            f'<a id="c{r.concept_id}"></a>',
            f"### {r.concept_id} — {r.concept_name}",
            f"- Domain: {r.domain_id} · Class: {r.concept_class_id} · Table: `{r.table_name}`",
            "",
        ]
    path.write_text("\n".join(lines), encoding="utf-8")


def place_after(cols, new, anchor):
    cols.remove(new)
    cols.insert(cols.index(anchor) + 1, new)


def main(src, dst=None):
    # alles als tekst inlezen, zodat getallen exact behouden blijven
    d = pd.read_csv(src, dtype=str, keep_default_na=False)
    out = Path(dst or src)

    if "value_as_concept_id" in d.columns:
        # <tabel>_values.csv: concept en gecodeerd antwoord, geen vocabulary-kolommen
        d["concept_uri"] = d["concept_id"].map(uri_for_id)
        d["value_uri"] = d["value_as_concept_id"].map(uri_for_id)
        cols = list(d.columns)
        place_after(cols, "concept_uri", "concept_name")
        place_after(cols, "value_uri", "value_concept_name")
        d[cols].to_csv(out, index=False)
        print(f"{len(d)} antwoorden; concept_uri en value_uri toegevoegd")
        return

    d["concept_uri"] = d.apply(concept_uri, axis=1)
    d["source_uri"] = d.apply(source_uri, axis=1)
    # zet de URI's direct achter concept_code, zodat ze opvallen
    cols = list(d.columns)
    place_after(cols, "concept_uri", "concept_code")
    place_after(cols, "source_uri", "concept_uri")
    d[cols].to_csv(out, index=False)
    custom_rows = d[d.apply(is_custom, axis=1)]
    # de pagina met eigen concepten alleen vanuit de volledige dictionary maken
    if Path(src).name == "dictionary.csv":
        write_custom_page(custom_rows, out.with_name("icudata_concepts.md"))
    custom = len(custom_rows)
    print(f"{len(d)} concepten; {len(d) - custom} met Athena-URI, {custom} eigen ICUdata-concepten; "
          f"{(d.source_uri != '').sum()} met bron-URI")


if __name__ == "__main__":
    main(*sys.argv[1:3])
