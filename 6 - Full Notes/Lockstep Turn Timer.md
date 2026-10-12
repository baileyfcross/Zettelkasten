2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Lockstep Turn Timer

A lockstep turn timer groups local commands into fixed simulation turns and schedules them for execution after a defined delay. Each peer sends its turn data to the others, but no peer advances into a turn until it has the required data from every participant.

Scheduling commands one or more turns ahead gives packets time to cross the network while preserving the common execution order required by [[Deterministic Lockstep]]. The turn length and delay trade responsiveness against tolerance for slow peers; a peer that fails to deliver can stall the group unless the protocol supplies timeout, removal, or recovery behavior.

# References

[[multiplayergameprogramming.pdf]]
