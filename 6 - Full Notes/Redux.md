2026-09-06 20:52

Status: #baby

Tags: [[Redux State Management]]

# Redux

Redux is a library for coordinating application state through a single store and a constrained update process. Components read selected state and request changes by dispatching actions rather than modifying shared values directly.

Its predictable data flow helps when state must be shared across distant React components. The added structure is most useful when local component state no longer expresses the application's relationships clearly.

The source presents Redux as Flux-like but simpler: it removes the central Flux dispatcher, keeps one immutable state object, and introduces pure reducers. A dispatched action passes through the store and reducers so the next state can be traced to an explicit event rather than an unobserved component mutation.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
