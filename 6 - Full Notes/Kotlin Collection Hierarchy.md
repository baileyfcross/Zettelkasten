2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Collections Standard Library and File I-O]]

# Kotlin Collection Hierarchy

Kotlin collections group values behind common traversal and size operations, with lists, sets, and maps adding different structural promises. Read-only interfaces expose observation, while mutable variants add operations that change the stored contents.

The distinction is expressed by the reference's interface rather than a guarantee that no mutable implementation exists anywhere. Depending on the narrow read-only view prevents that caller from changing the collection through that reference and makes mutation an explicit capability.

# References

[[masteringkotlinforjavadevelopers.epub]]
