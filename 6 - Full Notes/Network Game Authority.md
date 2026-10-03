2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Network Game Authority

Network game authority identifies the game instance allowed to decide the accepted state of an object or action. In a [[Client-Server Game Topology]], the server usually owns the shared truth and treats client messages as requests or input rather than unquestioned state.

Authority determines who may create objects, resolve collisions, award damage, and correct disagreement. Clients can predict results for responsiveness, but an authoritative update can replace that prediction. Concentrating authority simplifies conflict resolution and validation, while distributing it reduces central dependence but requires stronger synchronization and trust rules.

# References

[[multiplayergameprogramming.pdf]]
