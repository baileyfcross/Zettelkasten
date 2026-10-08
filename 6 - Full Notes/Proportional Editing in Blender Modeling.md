2026-09-14 01:18

Status: #baby

Tags: [[Blender Mesh Shaping Tools]]

# Proportional Editing in Blender Modeling

Proportional editing extends a transform beyond the directly selected components through a distance-based falloff. Nearby vertices move strongly and distant vertices move less, creating a smooth regional deformation from a compact selection.

Falloff shape and influence radius determine the character of the change, while connected-only behavior can prevent influence from crossing separate geometry. The technique supports terrain and organic shaping without manually selecting every affected vertex.

In the project exercise, one selected vertex is raised while the mouse wheel adjusts the influence circle and Random falloff varies the neighboring response. Repeating the operation across a subdivided plane creates hills and depressions without selecting every affected vertex directly.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

[[introductiontoblender30.pdf]]

[[testdriveblender.pdf]]
