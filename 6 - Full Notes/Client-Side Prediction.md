2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Client-Side Prediction

Client-side prediction estimates a more current game state than the latest state received from the server. Since an arriving update is already delayed, the client advances it using known motion or locally available input, often across an interval related to half the measured [[Round-Trip Time]].

Prediction reduces perceived lag but can be wrong when input changes or an unseen event affects motion. The client must reconcile the authoritative correction by snapping, interpolating, or gradually adjusting higher-order motion. [[Dead Reckoning]] predicts remote actors from their last state, while [[Move Prediction and Replay]] handles unacknowledged local input.

# References

[[multiplayergameprogramming.pdf]]
