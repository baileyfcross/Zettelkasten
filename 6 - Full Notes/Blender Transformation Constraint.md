2026-10-02 18:09

Status: #baby

Tags: [[Blender Constraint Systems]]

# Blender Transformation Constraint

The Blender Transformation constraint maps one target transform channel into an owner transform channel. A target's location, rotation, or scale over a chosen input range can drive the same or a different property on the owner, and source axes can be remapped to different destination axes.

Input and output minimums and maximums normally bound the relationship. With extrapolation enabled, those values become reference markers for a proportional linear mapping beyond the range rather than hard clips. This makes the constraint useful for mechanical linkages and control rigs where, for example, a target's translation should produce a controlled rotation elsewhere.

# References

[[modelingandanimationusingblender.pdf]]
