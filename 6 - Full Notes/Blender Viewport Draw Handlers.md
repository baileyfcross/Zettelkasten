2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]]

# Blender Viewport Draw Handlers

Viewport draw handlers arrange for a function to run whenever Blender redraws a 3D Viewport. In the API discussed by the source, they are added and removed through `SpaceView3D` functions with a drawing region and phase such as a post-pixel overlay.

The returned handle is the essential reference for later removal. Storing it on an operator class prevents it from being lost after registration. Because draw handlers can persist beyond the script execution that created them, an add-on should expose explicit on and off behavior and remove the handler during unregistration.

# References

[[blenderpythonapi.pdf]]
