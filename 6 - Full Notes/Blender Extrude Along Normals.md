2026-09-14 01:18

Status: #baby

Tags: [[Blender Mesh Modeling and Modifiers]]

# Blender Extrude Along Normals

Extrude Along Normals creates new connected faces and moves them in the direction of their surface normals. It is suited to thickening or extending a region while respecting its local orientation rather than one global axis.

The operation combines topology creation with normal-relative movement. Adjacent selected faces remain connected, distinguishing it from [[Blender Individual Face Extrusion|individual extrusion]], which gives each face its own separate outward result.

Blender 2.80 exposes offset size, orientation, normal flipping, and proportional-editing controls after the operation. Flipping normals changes the local extrusion direction, while proportional falloff can spread the transformation beyond the selected components. These settings make the tool useful on surfaces whose faces do not share a single global direction.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

[[modelingandanimationusingblender.pdf]]
