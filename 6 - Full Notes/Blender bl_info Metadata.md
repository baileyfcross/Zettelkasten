2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender bl_info Metadata

The `bl_info` dictionary identifies a Blender add-on to the application and its users. It records fields such as the add-on name, author, version, supported Blender version, interface location, description, documentation link, category, and optional support or warning information.

In the version described by the source, Blender parses this dictionary near the beginning of the file, so it belongs at the top. The metadata does not implement the add-on's behavior; it determines how the add-on is described, discovered, categorized, and activated in user preferences.

# References

[[blenderpythonapi.pdf]]
