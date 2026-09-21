2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Binary Mesh File

A binary mesh file stores vertex, index, and related mesh data in a compact byte layout designed for direct runtime loading. It avoids the parsing and character-conversion cost of a text representation and typically occupies less disk space.

The efficiency comes from a stricter contract. Writer and reader must agree on the [[Binary File Header]], field order, numeric sizes, counts, and the exact vertex format expected by the renderer.

# References

[[gameprogrammingincplusplus.pdf]]
