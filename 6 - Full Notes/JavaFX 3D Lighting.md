2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Graphics and 3D]]

# JavaFX 3D Lighting

JavaFX 3D lighting is built from the abstract `LightBase` and concrete ambient and point lights. `AmbientLight` contributes illumination that appears to come from all directions. `PointLight` occupies a location and radiates outward, and newer JavaFX versions can attenuate its intensity with distance.

Lights are nodes, so they can be added to containers, translated, and moved with a parent transformation. Their color, enabled state, and scope determine which objects they affect. Lighting becomes visible through the way a surface material reacts, particularly the diffuse and specular behavior defined by [[JavaFX Phong Materials and Texture Maps]]. The result is evaluated together with the viewpoint in [[JavaFX 3D Cameras]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
