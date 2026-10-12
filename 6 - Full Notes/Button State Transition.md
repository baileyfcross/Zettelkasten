2026-09-18 17:13

Status: #baby

Tags: [[Game Input Systems]]

# Button State Transition

A button state transition is a change between released and pressed states across input updates. Just pressed occurs when the previous state was off and the current state is on; just released is the inverse transition.

Transitions let a game trigger one event per activation while still supporting held-state behavior for continuous actions. They require retaining at least the previous sampled state of the control.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
