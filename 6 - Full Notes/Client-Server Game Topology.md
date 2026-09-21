2026-09-18 17:13

Status: #baby

Tags: [[Networked Game Programming]]

# Client-Server Game Topology

A client-server game topology gives a server authoritative responsibility for shared game state while clients send input and receive results. Central authority simplifies validation and resolves disagreements among participants.

A dedicated server runs separately from players, while a listen server also hosts a local player. Server capacity, latency, and failure become central constraints, but clients need not trust one another's claims directly.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
