2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender Add-On Registration

Registration makes an add-on's classes and properties available to Blender; unregistration removes them when the add-on is disabled or reloaded. Dependent classes should be registered in a logical order and unregistered in reverse order so that no component is removed while another still relies on it.

The source describes both explicit per-class calls and module-wide helpers available in Blender 2.78c. Its development template favors a clean slate before registering newly evaluated classes. Regardless of version-specific functions, reliable add-ons make activation repeatable, cleanup complete, and accidental duplicate registration visible.

# References

[[blenderpythonapi.pdf]]
