2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Game State Checksum

A game state checksum condenses selected deterministic state into a value that peers can compare. Matching values do not prove that every hidden detail is identical, but a mismatch reveals that the simulations no longer agree.

The checksum must be computed from the same ordered, canonical fields on every machine; pointer values, unordered iteration, or platform-dependent bytes can create false differences. Logging the checksum with turn numbers and important object state makes [[Multiplayer Desynchronization]] reproducible and helps locate the first divergent turn rather than only the later visible symptom.

# References

[[multiplayergameprogramming.pdf]]
