2026-09-30 00:32

Status: #baby

Tags: [[Universal React Applications]]

# Universal Redux Store

A universal Redux store uses the same reducers and store-construction logic in server and browser environments while allowing environment-specific middleware and initial state. The source's store factory chooses a server or client logger and creates each store from the state appropriate to that runtime.

The long-lived server store is the authoritative source for its example, while a request creates a client-shaped store from the server's current snapshot for rendering. Reusing the transition logic keeps actions meaningful on both sides without requiring the store instances themselves to be the same object.

# References

[[learningreact1.pdf]]
