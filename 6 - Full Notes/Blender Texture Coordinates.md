2026-09-07 23:25

Status: #baby

Tags: [[Blender Materials and Textures]] · [[Blender UV Mapping and UDIM]]

# Blender Texture Coordinates

Texture coordinates tell Blender where points in a texture belong on an object's surface. The Texture Coordinate and Mapping nodes expose and transform those positions explicitly inside a material network.

Different coordinate sources behave differently under object transforms and deformation. Making the source visible in the node graph can be clearer than hiding mapping adjustments in a Sidebar panel, especially when a material will be revisited or shared.

UV coordinates are a deliberately authored coordinate source that flatten mesh faces into image space. Projection, seam, island, scale, and tile decisions determine how much texture resolution each part receives and where distortion or overlap can occur.

# References

[[blenderfordummies4thedition.pdf]]

[[creatinggameenvironmentsinblender3d.pdf]]
