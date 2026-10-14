2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Multiplayer Desynchronization

Multiplayer desynchronization occurs when participants that should represent the same game state instead produce different results. In [[Deterministic Lockstep]], a missed turn, different command order, inconsistent floating-point behavior, or unequal pseudo-random calls can make the divergence grow even though later inputs match.

Regular [[Game State Checksum|state checksums]] can expose the first disagreeing turn, while structured logs record the commands and important state that produced it. Recovery may remove the divergent peer or transmit a known-good state, but a full resynchronization can be impractical for a large world. Prevention depends on deterministic code and an exact turn protocol.

# References

[[multiplayergameprogramming.pdf]]
