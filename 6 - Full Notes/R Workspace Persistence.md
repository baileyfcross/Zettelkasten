2026-10-04 22:20

Status: #baby

Tags: [[R Package Workspace and System Operations]]

# R Workspace Persistence

R workspace persistence saves the objects in an environment to a file and later restores them. Saving selected objects makes the file's contents clearer than automatically preserving every interactive artifact, and restoration can overwrite objects with matching names.

A saved workspace is useful for expensive intermediate state, but reproducibility still requires the code and source data that created it. The file should be treated as a cache or exchange artifact rather than the sole record of an analysis.

# References

[[rprimer.pdf]]
