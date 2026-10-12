2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender BLI Stack Chunk

A `StackChunk` is a linked allocation unit used by [[Blender BLI Stack]]. The stack tracks a current chunk, a pool of free chunks, the current element index, element size, capacity per chunk, and optionally the total number of stored elements.

Chunking targets substantial blocks of memory and a minimum number of elements, reducing repeated allocator overhead. When values are removed, storage can remain available through the free-chunk list, making the container suitable for repeated push-and-pop workloads in the Blender codebase.

# References

[[coreblenderdevelopment.pdf]]

