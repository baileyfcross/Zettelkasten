2026-09-16 22:54

Status: #baby

Tags: [[Regular Languages and Finite Automata]]

# Deterministic Finite-State Automaton

A deterministic finite-state automaton is a five-part machine (Q, Σ, q₀, δ, F): a finite state set, input alphabet, start state, total transition function, and set of accepting states. Every state-symbol pair selects exactly one next state.

The machine accepts a [[String]] when consuming the entire string from q₀ ends in F. Its states summarize only the finite information about the processed prefix that is relevant to future acceptance.

# References

[[FoundationsOfComputation_2.3.2.pdf]]
