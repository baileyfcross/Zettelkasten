2026-09-06 20:52

Status: #baby

Tags: [[Redux State Management]]

# Redux Action Creator

A Redux action creator is a function that constructs an action. Centralizing this construction gives calling code a stable operation and keeps action types and payload shapes from being repeated throughout components.

A synchronous action creator returns an action immediately. With middleware such as Redux Thunk, an action creator can instead coordinate asynchronous work and dispatch later actions as that work progresses.

# References

[[aspnetcore3andreact.pdf]]
