2026-10-02 18:09

Status: #baby

Tags: [[Blender Constraint Systems]]

# Blender Constraint Stack

A Blender constraint stack combines several target-driven rules on one object or bone. Each constraint can affect location, rotation, scale, tracking, or a relationship, and its influence determines how strongly its result contributes. The combined behavior depends on stack order because later constraints receive an already constrained transform.

Stacks can create sophisticated motion without directly keying every resulting value, but they also create interaction risk. Owners, targets, coordinate spaces, affected axes, offsets, and influence values should be understood one constraint at a time before rules are layered. A red or otherwise invalid constraint often indicates that a required target or compatible context is missing.

# References

[[modelingandanimationusingblender.pdf]]
