2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender Panel Classes

A Blender panel class defines a section of the graphical interface. Its space, region, category, label, and optional context fields locate the panel, while its `draw` method adds operator buttons and property controls to the layout.

The panel does not need to reproduce property-specific widgets manually. Supplying a registered property to the layout lets Blender choose an appropriate text field, slider, checkbox, vector control, or menu. A panel therefore connects the application's typed data model to discoverable user controls.

# References

[[blenderpythonapi.pdf]]
