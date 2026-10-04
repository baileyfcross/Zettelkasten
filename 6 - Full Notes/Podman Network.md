2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Podman Network

A Podman network is a named configuration that connects container network namespaces through a shared subnet and associated gateway, DNS, routing, and port-forwarding behavior. Containers on the same network can communicate directly, while containers on different networks need a route through an attached network path.

Podman can create, inspect, connect, disconnect, remove, and prune networks, with [[Netavark]] applying the host configuration. Removing a network that still has associated containers fails until those attachments are removed, which protects live and stopped workloads from silently losing their declared connectivity.

# References

[[podmanfordevopssecondedition.pdf]]
