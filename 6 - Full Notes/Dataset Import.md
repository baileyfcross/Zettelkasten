2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]] · [[R Data Ingestion and Review]]

# Dataset Import

Dataset import converts a stored file into an object that statistical software can analyze. The correct reader depends on the source format, such as CSV, SAS transport, SAS data, SPSS, or Stata, and the imported object should be named without altering the authoritative source file.

Import is not complete when the command runs successfully. The analyst must perform a [[Dataset Structure Check]] to confirm the expected number of observations, columns, names, classes, and missing values before any recoding begins.

In the book's reusable pattern, the selected resource is imported into a generic working object and then checked before any substantive analysis. The resource identity and transformation path remain part of provenance even when a convenient object name is reused.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[essentialsofdatascience.pdf]]
