2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# Atomic Bitwise Operations

Atomic bitwise operations set, clear, toggle, or test individual bits without losing concurrent changes to other bits in the same machine word. Linux uses them for compact state flags and bitmaps that can be updated from multiple execution contexts.

Test-and-modify forms return the prior bit value and can coordinate ownership transitions. Atomicity covers the chosen word operation, not a larger invariant across multiple fields, and required ordering around published state may still need an explicit barrier or a stronger synchronization primitive.

# References

[[linuxkernelprogramming_secondedition.pdf]]
