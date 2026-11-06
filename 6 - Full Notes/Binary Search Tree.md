2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Binary Search Tree

A binary search tree stores keys so every key in a node's left subtree precedes the node's key and every key in its right subtree follows it. Lookup and insertion compare a target with successive nodes to choose one branch at each step.

Its running time is proportional to tree height. A well-shaped tree provides logarithmic search, while ordered insertion can create a chain with linear behavior; a [[Balanced Binary Search Tree]] controls height by restructuring the tree.

An in-order traversal visits the keys in sorted order, while pre-order and post-order traversals change when the node is processed relative to its subtrees. The search-order invariant applies recursively to every subtree, which is why one comparison selects the only branch that can contain a target.

# References

[[statisticalcomputingincplusplusandr.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
