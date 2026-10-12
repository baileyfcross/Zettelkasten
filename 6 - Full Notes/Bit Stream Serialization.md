2026-10-02 22:40

Status: #baby

Tags: [[Game Network Transport and Serialization]]

# Bit Stream Serialization

Bit stream serialization writes and reads fields at single-bit precision instead of requiring every value to occupy a whole number of bytes. It is useful when a Boolean needs one bit or when a bounded enumeration or integer can be represented by fewer bits than its ordinary machine type.

The stream tracks both a byte buffer and a bit position, copying a requested number of bits across byte boundaries when necessary. This packing reduces the size of frequent [[Network Packet|network packets]], but both endpoints must agree exactly on field widths and order. Saving a few bits is worthwhile only when the resulting protocol remains testable and maintainable.

# References

[[multiplayergameprogramming.pdf]]
