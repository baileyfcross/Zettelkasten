2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Client-Side Interpolation

Client-side interpolation renders a remote object between two received states instead of immediately snapping to each new update. A local perception filter retains enough history to produce a continuous path over an interpolation period, commonly aligned with the server's packet period.

Because both endpoints are known, interpolation avoids inventing a state and smooths timing variation from [[Network Jitter]]. Its cost is additional visible delay: the rendered world intentionally lags the newest received sample. Local player motion usually needs [[Move Prediction and Replay]] so that this buffering does not make controls feel delayed.

# References

[[multiplayergameprogramming.pdf]]
