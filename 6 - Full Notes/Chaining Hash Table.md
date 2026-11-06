2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Chaining Hash Table

A chaining hash table resolves collisions by associating each array bucket with a collection of entries that share its hash location. Lookup first computes the bucket and then searches only that bucket's chain.

The chains are commonly implemented with linked containers. Performance remains close to constant average time when hashing distributes entries evenly and the number of entries per bucket stays small, but a poor distribution can reduce lookup to a linear search through a long chain.

Java `HashMap` begins collision handling with this chained-bucket idea but can treeify a sufficiently populated bucket once the backing table is also large enough. Resizing is preferred for a small table because more buckets may remove the concentration without paying for a tree.

# References

[[statisticalcomputingincplusplusandr.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
