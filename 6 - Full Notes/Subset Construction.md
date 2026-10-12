2026-09-16 22:54

Status: #baby

Tags: [[Regular Languages and Finite Automata]]

# Subset Construction

Subset construction converts a [[Nondeterministic Finite-State Automaton]] into a deterministic one by making each DFA state represent a set of NFA states reachable after the same input. Transitions collect every state reachable from the represented set, including those reached through ε-transitions.

The DFA start state is the NFA start state's ε-closure, and a set-state is accepting when it contains any NFA accepting state. The construction proves that nondeterministic and [[Deterministic Finite-State Automaton|deterministic finite automata]] recognize the same languages.

# References

[[FoundationsOfComputation_2.3.2.pdf]]
