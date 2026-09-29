2026-09-28 20:13

Status: #baby

Tags: [[Blender Scene Recovery and Configuration]]

# Making Linked Blender Data Local

Making linked data local breaks some or all of its dependency on an external `.blend` library and converts the chosen datablocks into editable project-owned data. Blender 2.7x exposed variants that localized only the selected object or also localized related data.

The scope matters because an object, its mesh, and its materials can be separate datablocks. Localizing too little leaves an important dependency read-only; localizing everything forfeits useful centralized updates.

# References

[[howtocheatinblender27x.pdf]]
