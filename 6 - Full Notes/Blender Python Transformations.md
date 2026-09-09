2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# Blender Python Transformations

Blender Python supports both imperative and declarative transformations. An operator can translate, rotate, or scale the selected objects by a differential amount, while assigning a location, rotation, or scale property directly sets the chosen object's state.

The distinction matters in loops and reusable toolkits. Repeated relative operators accumulate change and inherit the current selection and coordinate context; direct assignments overwrite known properties and can target a named datablock. Wrapping creation, deletion, and transformation in small utility functions can keep the main modeling algorithm focused on its data rather than repeated `bpy` setup.

# References

[[blenderpythonapi.pdf]]
