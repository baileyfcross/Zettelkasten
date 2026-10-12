2026-09-16 22:54

Status: #baby

Tags: [[Regular Languages and Finite Automata]]

# Pumping Lemma for Regular Languages

The pumping lemma states that every regular language has a threshold n such that each accepted string w of length at least n can be written w = xyz with |xy| ≤ n, |y| > 0, and xyᵏz in the language for every k ≥ 0.

The repeated segment y arises because a finite automaton processing a sufficiently long string must revisit a state. The lemma is used contrapositively: if every proposed threshold admits a long string that cannot be pumped, the language is not regular.

# References

[[FoundationsOfComputation_2.3.2.pdf]]
