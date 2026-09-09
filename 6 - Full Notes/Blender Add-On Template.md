2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender Add-On Template

A minimal Blender add-on brings together metadata, one or more registered classes, and module-level `register` and `unregister` functions. An operator supplies an action, a panel exposes the action in the interface, and properties carry values between interface controls and execution.

The template's value is consistency. Repeated class fields and lifecycle functions make the script readable and provide known places for diagnostics, property creation, and cleanup. Exact registration helpers vary by Blender version, but the architectural obligation remains: every installed capability must be initialized and later removable.

# References

[[blenderpythonapi.pdf]]
