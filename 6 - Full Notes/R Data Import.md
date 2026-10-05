2026-09-14 20:21

Status: #baby

Tags: [[R Statistical Computing and Data Wrangling]] · [[R Data Ingestion and Review]] · [[R Data Interchange and External Formats]]

# R Data Import

R data import converts an external data file or resource into an R object such as an [[R Data Frame]]. The source uses `read.csv` with either a local path or a URL and stresses that the analyst must know which file and location the command addresses.

An import step should remain explicit and reproducible. File format, header interpretation, variable classes, and missing values must be checked before later transformations or models are trusted.

The book uses explicit readers such as `read_csv` and then assigns the result to a stable working object. Import remains only the first step: [[Dataset Dimension Review]], [[Dataset Glimpse]], and class correction establish whether the table is analytically usable.

The primer treats import as a family of format-specific translations rather than a single command. Native R files, text, spreadsheets, statistical-system files, hierarchical exchange formats, HTML, and databases produce different object structures and therefore require format-aware readers followed by inspection.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]
