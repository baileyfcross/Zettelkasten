2026-11-06 13:25

Status: #baby

Tags: [[Abstract Data Structures]]

# Trie

A trie is a tree-shaped string index that stores common prefixes as shared paths. Each node represents a prefix position, references possible next characters, and may mark that a complete word ends at that point.

Inserting or checking a key follows one edge per character, so the work depends primarily on key length rather than the total number of stored strings. Finding whether a prefix exists has the same property, but returning every completion also requires traversing the corresponding subtree and therefore depends on the number of matches.

This structure is designed for [[Prefix Search]] rather than only exact-key membership. Its speed is purchased with memory for many nodes and child references, so production systems may use compressed variants such as radix or Patricia tries when a classical trie is too large.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
