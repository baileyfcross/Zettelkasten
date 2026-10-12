2026-09-30 00:32

Status: #baby

Tags: [[Redux State Management]]

# Redux Middleware

Redux middleware is a sequence of higher-order functions placed in the store's dispatch path. Each middleware receives access to the store, the next operation in the chain, and the current action, so it can perform work before forwarding the action and inspect the updated state after forwarding it.

Calling `next(action)` preserves the chain and eventually reaches the reducers. The source builds logging and persistence middleware, then applies them when a store is created; [[Redux Thunk]] is another middleware that accepts functions so asynchronous action creators can delay or repeat dispatch.

# References

[[learningreact1.pdf]]
