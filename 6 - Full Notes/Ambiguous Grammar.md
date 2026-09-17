2026-09-16 22:54

Status: #baby

Tags: [[Context-Free Languages and Parsing]]

# Ambiguous Grammar

A context-free grammar is ambiguous when at least one generated string has more than one left derivation, equivalently more than one [[Parse Tree]]. The alternatives can assign genuinely different structures and meanings to the same terminal sequence.

Arithmetic grammars avoid ambiguity by separating expressions, terms, and factors so that precedence and grouping are encoded in the grammar. Removing ambiguity is important for compilers because a parser must choose a definite program structure.

# References

[[FoundationsOfComputation_2.3.2.pdf]]
