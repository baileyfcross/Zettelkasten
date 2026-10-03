2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Replication and Topologies]]

# Remote Procedure Call

A remote procedure call represents a request for a named operation to run on another host with serialized arguments. In a game protocol, the sender transmits an RPC identifier and parameter data, and the receiver uses a registry to select a wrapper that deserializes the arguments and invokes the permitted local function.

An RPC is useful for discrete events that do not fit ordinary object-state replication, but it is still network input and must be validated. Delivery order, reliability, authority, and duplicate handling determine whether the operation is safe to execute. A replication manager can carry RPC records alongside other [[World State Delta|world-state changes]] without making low-level networking code depend on gameplay functions.

# References

[[multiplayergameprogramming.pdf]]
