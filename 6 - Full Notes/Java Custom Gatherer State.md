2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Custom Gatherer State

A custom Java gatherer can maintain processing state between input elements. Its initializer creates the state, its integrator updates state and emits values, an optional combiner merges parallel states, and an optional finisher publishes work after the input ends.

State enables operations such as emitting every second element multiple times, resetting a running total at a boundary, or distinctness by a derived key. `Gatherer.of` and `ofSequential` compose these functions without an anonymous class; sequential construction omits the combiner because no parallel states need merging.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
