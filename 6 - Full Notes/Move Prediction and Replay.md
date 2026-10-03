2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Move Prediction and Replay

Move prediction and replay gives a local player immediate response while preserving server authority. The client simulates each input at once, records the resulting move with an identifier or timestamp, and sends it to the server.

When an authoritative state returns, it identifies the most recent move the server processed. The client discards acknowledged moves, restores the server state, and reapplies the remaining local moves in order. Most frames then reproduce the predicted position; an unexpected server-side event creates a correction that the client can smooth rather than hiding the disagreement.

# References

[[multiplayergameprogramming.pdf]]
