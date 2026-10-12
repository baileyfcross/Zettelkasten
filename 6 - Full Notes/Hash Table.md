2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Hash Table

A hash table stores key-value records in an array location computed from the key. A hash function aims to distribute keys across the available buckets so lookup, insertion, and deletion require near-constant average time.

Different keys can map to the same location, so every hash table needs a collision policy. [[Chaining Hash Table]] stores colliding entries together, while [[Linear Probing Hash Table]] searches other array positions according to a probe sequence.

# References

[[statisticalcomputingincplusplusandr.pdf]]
