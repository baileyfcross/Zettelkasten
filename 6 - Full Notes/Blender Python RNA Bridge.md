2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender Python RNA Bridge

Blender exposes RNA-backed data to Python through an extension object that contains both the CPython object header and a [[Blender PointerRNA]]. The pointer supplies the actual DNA address and its [[Blender StructRNA]] type, allowing Python attribute operations to reach the Data API.

For `bpy.data`, Blender first creates an RNA pointer to the [[Blender Main Database]] and then wraps it as a Python object. Custom get-attribute and set-attribute functions on the extension type translate script access through [[Blender PropertyRNA]] records to the underlying DNA fields.

# References

[[coreblenderdevelopment.pdf]]

