2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Deterministic Lockstep

Deterministic lockstep synchronizes a multiplayer simulation by exchanging player commands rather than continuously replicating every object's state. Each peer applies the same commands at the same logical time, so identical starting state and deterministic execution should produce the same world on every machine.

Peers delay command execution through a [[Lockstep Turn Timer]] until all required turn data has arrived. The method saves bandwidth for games with many simulated units, but any nondeterministic calculation, missed command, or differing random sequence can cause [[Multiplayer Desynchronization]]. Checksums and synchronized pseudo-random generation help detect or prevent divergence.

# References

[[multiplayergameprogramming.pdf]]
