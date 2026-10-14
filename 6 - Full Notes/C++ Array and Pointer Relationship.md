2026-10-07 17:18

Status: #baby

Tags: [[C++ Scientific Programming]]

# C++ Array and Pointer Relationship

In many C++ expressions, an array name converts to a [[Pointer]] to its first element. Indexing `a[i]` is consequently related to pointer arithmetic on the base address, with the element type determining how far the address advances.

This relationship enables compact traversal and dynamic arrays, but a pointer does not retain the array's length. Functions receiving a raw pointer must obtain valid bounds separately, and arithmetic outside the allocated block produces invalid access rather than automatic resizing.

# References

[[statisticalcomputingincplusplusandr.pdf]]
