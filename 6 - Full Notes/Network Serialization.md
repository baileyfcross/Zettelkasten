2026-10-02 22:40

Status: #baby

Tags: [[Game Network Transport and Serialization]]

# Network Serialization

Network serialization converts a structured in-memory value into a linear representation that another host can interpret. The receiver deserializes the stream according to the same field order, sizes, encodings, and object rules rather than assuming that its local memory layout matches the sender's.

Copying an object with a raw memory operation is unsafe when it contains pointers, padding, compiler-dependent layout, or multibyte values stored with a different [[Network Byte Order|byte order]]. A deliberate format can also reduce bandwidth through [[Bit Stream Serialization]], sparse representation, bounded numeric ranges, or selective fields. The format is part of the application protocol and should remain understandable as game classes evolve.

# References

[[multiplayergameprogramming.pdf]]
