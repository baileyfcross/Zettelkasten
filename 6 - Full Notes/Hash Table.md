2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Hash Table

A hash table stores key-value records in an array location computed from the key. A hash function aims to distribute keys across the available buckets so lookup, insertion, and deletion require near-constant average time.

Different keys can map to the same location, so every hash table needs a collision policy. [[Chaining Hash Table]] stores colliding entries together, while [[Linear Probing Hash Table]] searches other array positions according to a probe sequence.

Performance depends on the key hash distribution and the table's load. Java `HashMap` may resize and redistribute entries as it grows, while [[Java HashMap Bucket Treeification]] limits heavily concentrated buckets by replacing a long chain with a balanced tree under implementation-specific conditions.

# References

[[statisticalcomputingincplusplusandr.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
