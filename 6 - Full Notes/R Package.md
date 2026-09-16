2026-09-06 18:44

Status: #baby

Tags: [[Statistical Computing Workflows]] · [[R Statistical Computing and Data Wrangling]] · [[R Programming Environment]]

# R Package

An R package is a distributable collection of functions, data, and documentation that extends base R. Packages let analysts assemble the capabilities required for a project instead of installing one monolithic statistical program with every possible component.

Published packages on CRAN follow documentation requirements and can be installed without licensing fees. Their flexibility creates a maintenance obligation, because a package may depend on other packages and may evolve independently of the R version used in production.

Installation and loading are separate operations: `install.packages` places a package on the system, while `library` attaches it to the current R session. This distinction lets an analysis declare the packages it uses without reinstalling them on every run.

The book further distinguishes installing a package from making it available in a session. [[R Library Attachment]] exposes exported functions on the search path, while an explicit [[R Package Namespace]] can identify the provider without attaching it.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]
