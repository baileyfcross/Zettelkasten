2026-10-02 18:09

Status: #baby

Tags: [[Blender Constraint Systems]]

# Blender Transform Limit Constraints

Blender transform limit constraints bound an owner's location, rotation, scale, or distance from a target. Per-axis minimum and maximum values define admissible translation, rotation, or scale, while Limit Distance can keep an object inside, outside, or on the surface of a sphere centered on its target.

The selected coordinate space determines how the bounds are evaluated. The For Transform option can also restrict the displayed transform properties rather than only the evaluated result. Limits are useful for mechanical travel, rig controls, and spatial safety zones, but negative scale requires particular care because the scale constraint expects positive boundary behavior.

# References

[[modelingandanimationusingblender.pdf]]
