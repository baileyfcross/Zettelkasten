2026-10-02 18:09

Status: #baby

Tags: [[Blender Constraint Systems]]

# Blender Child Of Constraint

The Blender Child Of constraint creates a parent-like relationship while retaining constraint controls. Separate switches determine whether the target affects the owner's location, rotation, and scale on each axis, and the Influence value allows the relationship to be blended or animated.

Set Inverse preserves the owner's apparent transform when the relationship is established, while Clear Inverse removes that compensation. Unlike ordinary parenting, the relationship can occupy a position in the [[Blender Constraint Stack]] and can be faded without restructuring the object hierarchy. This makes it useful for temporary attachment, handoffs between controls, and selective inheritance.

# References

[[modelingandanimationusingblender.pdf]]
