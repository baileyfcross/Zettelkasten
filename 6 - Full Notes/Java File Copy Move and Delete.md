2026-10-30 15:57

Status: #baby

Tags: [[Java File IO Serialization and Persistence]]

# Java File Copy Move and Delete

The Files API copies and moves entries between Paths and deletes them with explicit failure reporting. Options determine whether an existing target is replaced, attributes are copied, or a move should be attempted atomically.

Deleting a nonempty directory is not a recursive operation, and cross-filesystem moves may not support atomicity. A safe bulk operation therefore walks and validates its intended tree, chooses link behavior, and handles partial failure rather than assuming one call provides a transaction over many paths.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
