2026-09-18 17:13

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Peer-to-Peer Game Topology

A peer-to-peer game topology has participating machines exchange state or commands without one separate authoritative server. Real-time strategy games can use this model by sending player commands while each peer runs the same deterministic simulation.

The approach reduces centralized hosting needs but makes synchronization, late joining, disconnection, trust, and cheating harder. A slow or divergent peer can affect the entire shared session.

In a fully connected group, each participant needs direct communication with every other participant, so connection and upload requirements grow faster than in a client-server design. A master or rendezvous service can help peers find the session without becoming the simulation authority. [[Deterministic Lockstep]] reduces state bandwidth by sharing commands, but it makes every peer wait for complete turn data.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[multiplayergameprogramming.pdf]]
