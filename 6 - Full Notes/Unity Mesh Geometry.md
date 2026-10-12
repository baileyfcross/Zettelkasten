2026-10-12 01:03

Status: #baby

Tags: [[Unity Rendering and World Building]]

# Unity Mesh Geometry

Unity mesh geometry represents a three-dimensional surface as vertices connected into faces. A model can contain one or more meshes plus other resources, but the mesh itself is the shape data that defines where a visible surface exists.

On a typical scene object, a [[Unity Mesh Filter]] supplies this geometry and a [[Unity Renderer]] draws it. Keeping geometry separate from appearance allows the same mesh to use different [[Unity Material|materials]] and lets collision rely on simpler boundaries than the rendered form.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

