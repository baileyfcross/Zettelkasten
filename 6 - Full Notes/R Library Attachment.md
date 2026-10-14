2026-09-16 00:09

Status: #baby

Tags: [[R Programming Environment]] · [[R Package Workspace and System Operations]]

# R Library Attachment

R library attachment makes an installed package's exported objects available on the search path, commonly with `library()`. Attachment is a session operation and is distinct from installing the package.

A reproducible script should declare its attached packages near the beginning so later function calls do not depend on an analyst's interactive session history.

The primer also distinguishes detaching an attached package from unloading its namespace. Dependencies and registered methods can keep a namespace loaded after its search-path entry disappears, so a fresh session provides the clearest test of a script's declared package requirements.

# References

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]
