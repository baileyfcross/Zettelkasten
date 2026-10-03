2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Dead Reckoning

Dead reckoning predicts a remote object's future state from its last known position, velocity, orientation, or other motion data. It optimistically assumes the motion continues until a newer authoritative update proves otherwise.

The method works best when remote motion changes gradually and exact local input is unavailable. A wrong estimate creates a divergence that must be corrected by an immediate update, interpolation over several frames, or a gentler acceleration-based adjustment. The correction policy should depend on the error magnitude and the movement style of the game.

# References

[[multiplayergameprogramming.pdf]]
