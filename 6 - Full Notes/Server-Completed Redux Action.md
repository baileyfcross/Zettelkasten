2026-09-30 00:32

Status: #baby

Tags: [[Universal React Applications]]

# Server-Completed Redux Action

A server-completed Redux action begins with a client intent but receives authoritative fields and final action construction on the server. The server dispatches that action to its own store and returns the action object, after which the client dispatches the same event to its local store.

In the source's color API, a POST supplies user-entered values while the server adds an identifier and timestamp. Sharing the completed action keeps both stores aligned around one recorded transition and prevents each side from independently inventing fields for what should be the same event.

# References

[[learningreact1.pdf]]
