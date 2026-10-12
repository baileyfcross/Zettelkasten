2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Scalability and Security]]

# Replication Priority

Replication priority ranks objects or messages when a server cannot fit every eligible update into the available bandwidth. High-impact state is serialized first, while less important state waits until capacity remains.

A fixed low priority can starve an object forever. Practical schedulers therefore raise priority as time since the last update grows or combine base importance with [[Replication Frequency]]. The same policy can apply to remote procedure calls when some events may be dropped without changing authoritative state.

# References

[[multiplayergameprogramming.pdf]]
