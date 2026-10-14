2026-09-14 20:21

Status: #baby

Tags: [[R Statistical Computing and Data Wrangling]] · [[R Data Ingestion and Review]] · [[R Data Interchange and External Formats]]

# Delimited Text Data

Delimited text data stores a rectangular table as plain text, separating fields with a consistent character such as a comma or tab. CSV and TSV files can be inspected and exchanged without requiring a particular commercial spreadsheet program.

The source recommends these formats for small life-science datasets before [[R Data Import]]. Their portability does not remove the need to document encoding, missing-value markers, headers, and variable types.

The book's case studies commonly begin with CSV resources, sometimes contained in a ZIP archive or located through a [[CKAN Data Repository]]. A successful read must be followed by dimension, type, level, and missingness checks.

R's general text-table reader exposes delimiter, decimal mark, header, quote, and missing-value controls, while CSV convenience readers supply common defaults. Export needs the same care because row names and quoting options can add fields that another program may misinterpret.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]
