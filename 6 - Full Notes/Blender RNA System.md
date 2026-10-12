2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender RNA System

Blender RNA is the descriptive interface wrapped around persistent DNA records. It gives structures and properties identifiers, types, ranges, defaults, accessors, update callbacks, display text, and relationships that higher layers can inspect without manipulating raw C fields directly.

The [[Blender makesrna Module]] builds this layer from repository definitions and generated source. Operators use [[Blender Operator RNA Properties]], the Python interface crosses through the [[Blender Python RNA Bridge]], and the runtime [[Blender RNA Access API]] ultimately reads or changes the underlying [[Blender DNA System]].

# References

[[coreblenderdevelopment.pdf]]

