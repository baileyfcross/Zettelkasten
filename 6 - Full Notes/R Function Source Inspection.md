2026-10-04 22:20

Status: #baby

Tags: [[R Package Workspace and System Operations]]

# R Function Source Inspection

R function source inspection reveals the definition used by a named function so an analyst can understand behavior not fully explained by a help page. Printing a function may show ordinary R code, while namespace-aware lookup is needed for hidden methods or functions not attached on the search path.

Some functions are primitives or call compiled code, so their visible R wrapper is not the whole implementation. Source inspection complements the [[R Help System]] and should be interpreted for the installed package version.

# References

[[rprimer.pdf]]
