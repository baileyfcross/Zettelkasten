2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender Operator Classes

A Blender operator class packages an action that can be registered with the application and invoked from the interface or through `bpy.ops`. It inherits from Blender's operator type, declares an identifier and label, and implements an `execute` method that receives the current context.

The identifier maps the class to an operator namespace and must follow Blender's naming rules. A successful execution reports completion, while class-level registration methods can create closely associated properties. The operator turns ordinary Python logic into an action Blender can discover and call consistently.

# References

[[blenderpythonapi.pdf]]
