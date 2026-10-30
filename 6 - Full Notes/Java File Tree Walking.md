2026-10-30 15:57

Status: #baby

Tags: [[Java File IO Serialization and Persistence]]

# Java File Tree Walking

`Files.walk` returns a lazy stream of paths in a directory tree, while `Files.walkFileTree` drives a visitor through entry, directory, failure, and exit callbacks. Both support bounded depth and configurable symbolic-link behavior.

The stream form composes naturally with filters and terminal operations but must be closed. The visitor form gives finer control over skipping subtrees, continuing after errors, or terminating early. Following links requires cycle awareness because a graph of directories is not necessarily a tree.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
