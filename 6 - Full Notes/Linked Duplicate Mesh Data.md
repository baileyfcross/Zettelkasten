2026-09-28 20:13

Status: #baby

Tags: [[Blender Efficient Modeling and Retopology]]

# Linked Duplicate Mesh Data

A linked duplicate creates another object that shares the original object's mesh datablock. Each object can have its own transform, but editing their shared mesh propagates the topology change to every linked instance.

This reduces memory and keeps repeated forms synchronized. It is appropriate for repeated assets that should remain geometrically identical; an ordinary independent duplicate is preferable when a copy must later acquire unique topology.

# References

[[howtocheatinblender27x.pdf]]
