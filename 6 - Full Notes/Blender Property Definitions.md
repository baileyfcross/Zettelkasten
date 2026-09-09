2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender Property Definitions

Blender property definitions add typed values such as strings, integers, floats, Booleans, vectors, enumerations, collections, and pointers to supported Blender types. Their declarations can include a name, description, default, bounds, precision, display subtype, vector size, and update callback.

Type metadata drives both validation and interface presentation. A Boolean can appear as a checkbox, a number as a bounded slider, and a color vector as a color control. The property system therefore supplies a bridge between stored add-on state and the panel layout that edits it.

# References

[[blenderpythonapi.pdf]]
