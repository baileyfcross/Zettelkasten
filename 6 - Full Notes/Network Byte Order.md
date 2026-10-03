2026-10-02 22:40

Status: #baby

Tags: [[Game Network Transport and Serialization]]

# Network Byte Order

Network byte order is the agreed ordering of bytes for multibyte values in a serialized stream. A little-endian processor places the low-order byte at the lowest address, while a big-endian processor places the high-order byte there; sending native memory without conversion can therefore change the value on a host with the opposite convention.

A serializer compares platform endianness with the stream convention and swaps the bytes of affected primitive values when they differ. Single-byte values do not need swapping, and an array of single-byte characters must not be reversed as though the entire string were one integer. Explicit conversion makes [[Network Serialization]] portable across processor architectures.

# References

[[multiplayergameprogramming.pdf]]
