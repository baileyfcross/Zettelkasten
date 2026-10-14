2026-09-18 17:13

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Client-Server Game Topology

A client-server game topology gives a server authoritative responsibility for shared game state while clients send input and receive results. Central authority simplifies validation and resolves disagreements among participants.

A dedicated server runs separately from players, while a listen server also hosts a local player. Server capacity, latency, and failure become central constraints, but clients need not trust one another's claims directly.

With `n` clients, each client needs only its connection to the server while the server maintains one connection per client and enough bandwidth to receive and redistribute their traffic. The extra hop can increase peer-to-peer communication latency, but the central [[Network Game Authority]] gives replication, validation, and late joining a single coordinating point.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[multiplayergameprogramming.pdf]]
