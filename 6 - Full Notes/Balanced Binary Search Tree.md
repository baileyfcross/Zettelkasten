2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Balanced Binary Search Tree

A balanced binary search tree maintains a height proportional to the logarithm of its number of nodes. It restores structural constraints after updates so a valid [[Binary Search Tree]] cannot degenerate into a long chain.

Balancing spends extra work and metadata during insertion or deletion to protect future operations. Different schemes impose different local constraints, but their common purpose is to keep lookup, insertion, and deletion logarithmic in the worst case or under a stated amortized guarantee.

This guarantee also explains Java `HashMap` bucket treeification: when too many colliding entries remain in a sufficiently large table, a red-black tree can replace a linear bucket chain so operations within that bucket approach logarithmic rather than linear time.

# References

[[statisticalcomputingincplusplusandr.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
