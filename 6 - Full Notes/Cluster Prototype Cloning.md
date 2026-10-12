2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Design Patterns]]

# Cluster Prototype Cloning

The Prototype pattern creates an object by cloning an existing representative rather than selecting its concrete class explicitly. A virtual clone operation delegates copying to the runtime type, preserving derived schema or component behavior.

Cloning is useful when algorithms manipulate polymorphic objects through base pointers. The design must specify whether referenced data are copied deeply or shared, because an unintended shallow copy can couple centers, schemas, or prototypes that should evolve independently.

# References

[[dataclusteringincplusplus.pdf]]

