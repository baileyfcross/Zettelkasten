2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender RNA Typed Property

An RNA typed property extends the common [[Blender PropertyRNA]] layout with operations and metadata for a particular value kind. Boolean, integer, float, enum, pointer, collection, string, and other variants can supply scalar or array accessors, defaults, ranges, units, and update callbacks.

Generated property objects connect those descriptors to DNA fields through getter and setter functions. This makes the [[Blender RNA Access API]] type-safe at its boundary and lets the same property drive operator settings, interface controls, and Python attributes.

# References

[[coreblenderdevelopment.pdf]]

