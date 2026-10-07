2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Chaining Hash Table

A chaining hash table resolves collisions by associating each array bucket with a collection of entries that share its hash location. Lookup first computes the bucket and then searches only that bucket's chain.

The chains are commonly implemented with linked containers. Performance remains close to constant average time when hashing distributes entries evenly and the number of entries per bucket stays small, but a poor distribution can reduce lookup to a linear search through a long chain.

# References

[[statisticalcomputingincplusplusandr.pdf]]
