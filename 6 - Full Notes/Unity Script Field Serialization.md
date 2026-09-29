2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity Script Field Serialization

Unity script field serialization stores supported component fields as project data and exposes authorable fields in the [[Unity Inspector]]. This allows numeric parameters, object references, assets, and other configuration to vary by component instance without changing code.

Serialization turns a script into a designer-facing tool, but the saved Inspector value becomes authoritative for that instance and may differ from the initializer written in the source. Clear names, ranges, grouping, and defaults help prevent the editable surface from becoming an undocumented second program.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

