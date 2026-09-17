2026-09-16 22:54

Status: #baby

Tags: [[Context-Free Languages and Parsing]]

# Deterministic Context-Free Language

A deterministic context-free language L is one for which a deterministic [[Pushdown Automaton]] accepts the strings of L followed by a distinct end marker. The marker lets the machine distinguish an actual end of input from a point where more symbols might still arrive.

Nondeterminism adds genuine recognition power to pushdown automata, so some context-free languages are not deterministic context-free. Deterministic context-free languages support efficient parsing methods such as [[LL(1) Parsing]] and [[LR(1) Parsing]].

# References

[[FoundationsOfComputation_2.3.2.pdf]]
