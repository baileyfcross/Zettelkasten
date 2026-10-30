2026-10-30 15:57

Status: #baby

Tags: [[Java File IO Serialization and Persistence]]

# Java Directory and Temporary File Operations

Java can list a directory through legacy File arrays or through NIO directory streams and `Files.list`. NIO creation distinguishes one directory from a complete missing parent chain, and listing results hold resources that must be closed.

Temporary-file factories create uniquely named files or directories in a selected location or the system temporary area. `deleteOnExit` is a last-resort process-exit request rather than prompt cleanup; explicit deletion in a controlled lifecycle is more predictable for long-running applications and large temporary data.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
