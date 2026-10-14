2026-09-30 00:32

Status: #baby

Tags: [[Redux State Management]]

# Redux Reducer Composition

Redux reducer composition divides a state tree among focused reducer functions and combines them into the reducer used by the store. A leaf reducer can calculate one record, an array reducer can locate or remove records, and a root reducer can join those branch results into the complete next state.

Several reducers may respond to the same action because each interprets the event for its own portion of the tree. Composition is recommended rather than required, but it preserves functional modularity and avoids one switch statement becoming responsible for every application transition.

# References

[[learningreact1.pdf]]
