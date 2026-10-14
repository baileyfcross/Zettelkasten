2026-09-06 20:52

Status: #baby

Tags: [[Redux State Management]]

# Redux Store

A Redux store holds the application's shared state tree and coordinates access to it. It exposes the current state, accepts dispatched actions, and notifies subscribers after the reducer has produced a new state.

The store is the meeting point between action-producing code and state-consuming UI. React components normally receive it through a provider instead of importing a mutable global value.

A store is created from the root reducer and optional initial state. Its `getState`, `dispatch`, and [[Redux Store Subscription|subscription]] operations form the public coordination boundary: callers read snapshots, submit events, and react after transitions without mutating the store's data directly.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
