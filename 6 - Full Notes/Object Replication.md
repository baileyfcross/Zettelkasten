2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Object Replication

Object replication reconstructs and updates a game object on another host. The packet must identify the replication operation, the particular object through a [[Network Object Identifier]], and enough class information or registered construction behavior to create the right type when it does not yet exist.

Sending every object in every packet is simple but becomes too expensive as the world grows. A replication manager therefore sends create, update, or destroy actions, often as a [[World State Delta]], and can limit an update to the properties that changed. Replication carries authoritative state; it does not by itself decide which host is authoritative or how lost updates recover.

# References

[[multiplayergameprogramming.pdf]]
