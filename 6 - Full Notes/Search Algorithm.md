2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]]

# Search Algorithm

A search algorithm locates a target within a collection or determines that no acceptable target is present. The available structure determines what strategy is possible: an unordered collection may require [[Linear Search]], while ordered data enables [[Binary Search]].

Search problems also differ in what counts as success. Exact search requires a match, [[Approximate Search]] accepts sufficiently similar items, and an [[Optimal Stopping Problem]] requires a choice before later candidates are known.

Other requirements imply different operations: [[Prefix Search]] returns strings sharing an initial sequence, a range query returns ordered values within bounds, and a membership test asks only whether an item exists. Translating the requirement into that operation should precede selecting a hash map, ordered index, trie, database index, or full-text engine.

# References

[[algorithms.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
