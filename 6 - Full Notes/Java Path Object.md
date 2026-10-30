2026-10-30 15:57

Status: #baby

Tags: [[Java File IO Serialization and Persistence]]

# Java Path Object

`java.nio.file.Path` is an immutable representation of a filesystem path. It exposes roots, names, parents, resolution, relativization, normalization, and conversion to absolute or real paths without implying that the named entry currently exists.

Relative paths are interpreted against a context such as the process working directory, while a real path asks the filesystem to resolve actual entries and links. Path separates pathname manipulation from I/O; the [[Java Files Utility]] performs reads, writes, copies, metadata checks, and directory operations on it.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
