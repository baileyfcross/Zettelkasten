2026-11-06 13:25

Status: #baby

Tags: [[Search Algorithms]]

# Prefix Search

Prefix search finds strings whose beginning matches a supplied character sequence. It supports autocomplete and incremental lookup, where a user expects useful candidates before entering a complete name or query.

Scanning every stored string makes each request depend on the number of records and becomes costly when many users search a large catalog. A [[Trie]] instead follows the prefix characters through shared paths; once the prefix node is reached, matching strings are collected from its subtree.

Exact-key hashing and prefix search answer different questions. A hash map can quickly test whether one complete string exists, while it offers little direct help in enumerating all strings that start with the same partial key.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
