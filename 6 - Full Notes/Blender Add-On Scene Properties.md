2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender Add-On Scene Properties

An add-on can register properties on Blender scene or object types so that values become accessible through the current context and can be saved with the `.blend` file. Scene properties are useful for settings that apply to the current scene rather than to a temporary local variable.

Properties closely tied to one operator or panel can be created in that class's registration method, while broader settings can be created by the module's registration function. Unregistration should delete the same properties, preventing stale interface state from surviving after the add-on is removed.

# References

[[blenderpythonapi.pdf]]
