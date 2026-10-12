2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Operator Type Registry

Blender stores registered operator types in a global hash keyed by each type's unique identifier. Completing [[Blender Operator Type Registration]] inserts the populated record, and lookup functions retrieve it when an event, interface button, or Python call requests the operation.

Hash lookup provides average constant-time access, which suits the timing demands of event processing. The identifier conventions described by [[Blender Operator Naming Convention]] make the key both unique and visibly associated with the module or editor that owns the operation.

# References

[[coreblenderdevelopment.pdf]]

