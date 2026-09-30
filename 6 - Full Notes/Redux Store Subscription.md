2026-09-30 00:32

Status: #baby

Tags: [[Redux State Management]]

# Redux Store Subscription

A Redux store subscription registers a listener that runs after the store finishes dispatching an action. The listener can read the new state to trigger rendering, log a transition, or persist a snapshot without being embedded in the reducer itself.

`subscribe` returns an unsubscribe function, giving the caller explicit ownership of the listener's lifetime. The source also uses a subscription to serialize state into browser storage after each dispatch, then restores that value as the next store's initial state.

# References

[[learningreact1.pdf]]
