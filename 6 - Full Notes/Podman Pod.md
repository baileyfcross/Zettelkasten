2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Podman Pod

A Podman pod groups containers so they can share selected Linux namespaces, especially one network namespace. Containers in the pod can use the same IP address and communicate over loopback while retaining separate images, processes, and writable filesystems.

The shared boundary resembles a Kubernetes Pod and makes tightly coupled helper processes possible, but it also fixes the group to one host and one scheduling unit. Components that need independent placement or scaling should not be combined merely for convenient connectivity; an ordinary [[Podman Network]] preserves looser coupling.

# References

[[podmanfordevopssecondedition.pdf]]
