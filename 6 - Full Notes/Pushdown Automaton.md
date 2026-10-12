2026-09-16 22:54

Status: #baby

Tags: [[Context-Free Languages and Parsing]]

# Pushdown Automaton

A pushdown automaton is a finite-state machine augmented by a stack. A transition may consume an input symbol or ε, pop a string from the stack, push a replacement string, and change state.

The stack supplies unbounded last-in-first-out memory for nested structure. Pushdown automata accept exactly the [[Context-Free Language|context-free languages]], and a grammar can be simulated by pushing its start symbol, expanding nonterminals, and matching terminals against the input.

# References

[[FoundationsOfComputation_2.3.2.pdf]]
