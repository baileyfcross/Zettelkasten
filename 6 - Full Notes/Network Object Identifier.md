2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Network Object Identifier

A network object identifier is a session-wide value that lets different hosts refer to the same replicated game object. Local memory addresses cannot serve this purpose because the corresponding object occupies unrelated addresses in separate processes.

The sender includes the identifier with replicated data, and the receiver uses a lookup table to find the local object that should receive the update. Creation and destruction must add and remove mappings consistently so an old identifier is not accidentally applied to a later object. The identifier is distinct from a class identifier, which selects the type to construct during [[Object Replication]].

# References

[[multiplayergameprogramming.pdf]]
