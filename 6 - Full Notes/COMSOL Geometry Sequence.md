2026-09-21 00:45

Status: #baby

Tags: [[COMSOL Geometry Operations]]

# COMSOL Geometry Sequence

A COMSOL geometry sequence is the ordered set of primitives, imports, transforms, Boolean operations, partitions, conversions, and cleanup features that produces the finalized geometry. Each node consumes the state created by earlier nodes.

Keeping the sequence explicit makes the construction reproducible and debuggable. Features can be edited, disabled, reordered, or rebuilt to locate the operation that introduced an invalid entity or unintended domain.

# References

[[geometrycreationandimport.pdf]]
