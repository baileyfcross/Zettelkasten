2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Binary File Header

A binary file header places identifying and structural metadata before a binary payload. A mesh header can record a signature, version, vertex format, vertex count, index count, and offsets or sizes needed to interpret following bytes.

Validation prevents the loader from treating an unrelated, truncated, or incompatible file as trusted geometry. Because binary data is not self-describing, the header carries the minimum information required to enforce the format contract.

# References

[[gameprogrammingincplusplus.pdf]]
