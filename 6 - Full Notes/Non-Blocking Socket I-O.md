2026-10-02 22:40

Status: #baby

Tags: [[Game Network Transport and Serialization]]

# Non-Blocking Socket I-O

Non-blocking socket I/O makes a network operation return immediately when it cannot yet send, receive, connect, or accept. The game can then continue its real-time update instead of allowing one slow endpoint to suspend the thread that advances simulation or rendering.

The program must treat a would-block result as temporary rather than as a failed connection. It can poll readiness with socket-selection facilities, integrate networking into an event loop, or move blocking work to a separate thread. Non-blocking mode prevents an accidental stall, but it also requires explicit buffering and partial-operation handling around the [[Game Network Socket]].

# References

[[multiplayergameprogramming.pdf]]
