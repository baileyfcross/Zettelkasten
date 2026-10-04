2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]]

# Container Engine

A container engine is the user-facing management layer that coordinates images, registries, storage, networking, and container lifecycle operations. It translates commands such as run, pull, inspect, and stop into lower-level work performed by image libraries, Linux isolation mechanisms, and an [[OCI Container Runtime]].

The engine is distinct from the runtime. The runtime creates and starts the isolated process described by an OCI bundle, whereas the engine manages the surrounding workflow and durable metadata. Docker commonly places this coordination behind a long-running daemon; [[Podman Daemonless Architecture]] performs it through ordinary processes and libraries.

# References

[[podmanfordevopssecondedition.pdf]]
