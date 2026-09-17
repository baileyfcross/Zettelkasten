2026-09-06 00:13

Status: #baby

Tags: [[Algorithm Foundations]] · [[Wartime Computing and Early Electronic Machines]] · [[Turing Machines and Computability]]

# Turing Machine

A Turing machine is an idealized computational machine consisting of an unbounded tape divided into cells, a movable read-write head, a finite set of states, and an instruction table. Each instruction uses the current state and scanned symbol to choose a new state, write a symbol, and move the head one cell left or right.

Its operations are deliberately elementary, yet a properly constructed Turing machine can implement any [[Algorithm]]. This makes it a formal model for reasoning about what computation can accomplish, independent of the speed or physical construction of a particular computer.

Formally, its transition function maps the current non-halting state and scanned symbol to a written symbol, a one-cell left or right move, and a new state. A computation may reach its halt state or continue forever, allowing the model to distinguish [[Turing-Decidable Language|decision]] from [[Turing-Acceptable Language|acceptance]].

# References

[[algorithms.epub]]
[[computing.epub]]

[[FoundationsOfComputation_2.3.2.pdf]]
