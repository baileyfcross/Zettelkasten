2026-09-06 20:52

Status: #baby

Tags: [[Redux State Management]]

# Redux Reducer

A Redux reducer is a pure function that receives the current state and an action and returns the next state. It expresses how each recognized event transforms the store without mutating the existing state object.

Keeping reducers deterministic makes state changes easier to reason about and test. An unrecognized action returns the current state, preserving the store when no transition applies.

# References

[[aspnetcore3andreact.pdf]]
