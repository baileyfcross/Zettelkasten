2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender BLI Stack

`BLI_Stack` is a generic stack in the [[Blender BLI API]] that stores fixed-size elements in linked chunks. Its public operations create and free a stack, push or pop values, inspect the top, clear or discard entries, count elements, and test whether the stack is empty.

Popping copies the last element to caller-provided storage and then discards that position without necessarily releasing the allocated memory. The [[Blender BLI Stack Chunk]] organization allows storage to be reused and avoids a separate allocation for every pushed item.

# References

[[coreblenderdevelopment.pdf]]

