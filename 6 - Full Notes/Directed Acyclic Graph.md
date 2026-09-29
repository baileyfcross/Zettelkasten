2026-09-06 00:13

Status: #baby

Tags: [[Graph Structures]] · [[High-Dimensional Graphical Models]]

# Directed Acyclic Graph

A directed acyclic graph is a [[Directed Graph]] containing no [[Graph Cycle]]. It is commonly abbreviated DAG.

DAGs represent relationships that proceed in one direction without eventually returning to their starting point. Task priorities, prerequisites, and dependencies fit this structure when following the directed relationships can never lead back to an earlier item.

In a directed graphical model, each variable is conditionally independent of its nondescendants given its parents, and a positive joint density factors into one conditional density per node. Different arrow orientations can encode the same conditional independences, so observational data do not generally identify a unique minimal DAG or causal direction without additional assumptions.

# References

[[algorithms.epub]]

[[introductiontohigh-dimensionalstatistics.pdf]]
