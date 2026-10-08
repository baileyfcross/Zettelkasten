2026-09-07 23:25

Status: #baby

Tags: [[Blender Mesh Modeling and Modifiers]]

# Blender Mirror Modifier

The Mirror modifier copies mesh data and flips it across one or more local axes. Vertices near the center seam can merge, making the generated half appear continuous with the modeled half.

Because the reflection remains procedural, an artist can build one side of a symmetrical object and see the other update immediately. Options can also mirror corresponding vertex-group assignments and UV coordinates.

The aircraft exercise demonstrates the common preparation sequence: disable front-only selection, delete the entire half on one side of the intended center plane, then add the modifier. Edits to the surviving vertices are reflected live across the axis, preserving bilateral symmetry while the form is developed.

# References

[[blenderfordummies4thedition.pdf]]

[[introductiontoblender30.pdf]]

[[testdriveblender.pdf]]
