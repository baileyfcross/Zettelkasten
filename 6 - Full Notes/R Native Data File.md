2026-10-04 22:20

Status: #baby

Tags: [[R Data Interchange and External Formats]]

# R Native Data File

An R native data file stores one or more R objects in a form that preserves their classes and structure. `load()` restores the saved objects into an environment, while `save()` writes selected objects; because restored names can replace objects already present, the contents should be inspected before loading into an active workspace.

Native files favor exact R-to-R transfer, whereas [[Delimited Text Data]] favors portability across tools. The choice therefore depends on whether preserving R-specific objects or enabling broad interchange matters more.

# References

[[rprimer.pdf]]
