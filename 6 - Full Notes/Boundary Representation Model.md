2026-10-01 00:39

Status: #baby

Tags: [[3D Game Rendering]]

# Boundary Representation Model

A boundary representation, or B-rep, defines a solid by the surfaces that enclose it. It stores geometric descriptions of faces and edges together with topology describing how vertices, edges, loops, and faces are connected.

Orientation is essential: ordered boundary vertices and outward-pointing face normals distinguish the interior from the exterior. Only the boundary surfaces need to be stored, while volumetric properties can be derived from them. Polyhedral validity can be checked with Euler-style relationships among faces, edges, vertices, loops, bodies, and holes. B-rep extends a [[Wireframe Geometric Model]] by adding explicit face and enclosure information.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
