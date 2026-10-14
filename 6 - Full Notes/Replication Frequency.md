2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Scalability and Security]]

# Replication Frequency

Replication frequency controls how often an object or property is considered for a network update. Frequently changing or player-critical state can use a short period, while slow background objects can be updated less often.

Lower frequency conserves bandwidth but increases the age of the state a client receives and may demand more interpolation or prediction. A scheduler can combine time since the last update with [[Replication Priority]] so important objects remain responsive while low-priority objects eventually receive service.

# References

[[multiplayergameprogramming.pdf]]
