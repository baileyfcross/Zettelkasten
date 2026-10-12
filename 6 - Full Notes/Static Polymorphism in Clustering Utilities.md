2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Object Model]]

# Static Polymorphism in Clustering Utilities

Static polymorphism uses templates and overloaded operators to adapt one implementation to several types at compile time. ClusLib container and double-key map utilities are parameterized so records, clusters, nodes, or numeric values can reuse the same operations.

Template specialization avoids virtual dispatch and preserves type information, but it generates a separate instantiation for each type and exposes implementation in headers. It is best suited to structural operations whose behavior is known during compilation.

# References

[[dataclusteringincplusplus.pdf]]

