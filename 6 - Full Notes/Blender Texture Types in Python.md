2026-09-08 09:04

Status: #baby

Tags: [[Automated Blender Texturing and Rendering]]

# Blender Texture Types in Python

Blender 2.78c offered image, video, environment, and parameterized procedural texture types. Image-based textures load external pixels, while procedural types generate values from adjustable parameters inside Blender.

Python tooltips and the API expose the same parameters seen in the interface, allowing a developer to reproduce manual configuration in a script. Exact texture APIs have changed in later Blender generations, but the conceptual choice remains between sampled external media and textures computed from a procedure.

# References

[[blenderpythonapi.pdf]]
