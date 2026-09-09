2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Data and Operations]]

# Pseudo-Circular Data References in bpy

Blender's Python data model allows related structures to refer through one another. An object can expose its mesh through `.data`, while nested properties can lead back toward owning or contextual structures. These paths can look circular even though they are controlled API references rather than unrestricted Python object cycles.

The benefit is abstraction: code can begin with the entity it has and navigate to the data it needs. The limitation is that not every apparent reverse path exists or permits assignment. Developers should inspect actual members and distinguish an object's container, its reusable data, and the context in which it is being used.

# References

[[blenderpythonapi.pdf]]
