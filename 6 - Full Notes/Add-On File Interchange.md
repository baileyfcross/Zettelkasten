2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Development Workflow]]

# Add-On File Interchange

An add-on can bundle model data in a standard interchange format such as OBJ and import it when the user chooses an asset. This keeps the Python logic concise and lets 3D artists inspect, replace, or extend the asset collection with tools they already use.

Interchange files are especially appropriate when detailed geometry is fixed and only needs ordinary placement or scaling. They separate content from behavior: the file describes the mesh, while the add-on describes how that mesh enters and participates in the scene.

# References

[[blenderpythonapi.pdf]]
