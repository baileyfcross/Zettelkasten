2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Partial Object State Replication

Partial object state replication sends only the properties of an object that need an update. A compact header or bit mask identifies the included fields, after which the receiver deserializes those fields into its existing local object.

The technique reduces bandwidth when large objects change sparsely, but it couples the packet to a well-defined property schema. The sender must also account for loss: if a field is omitted from later packets because it is assumed delivered, the system needs acknowledgment-based recovery; if current packets resend the newest needed value, old lost values can be superseded.

# References

[[multiplayergameprogramming.pdf]]
