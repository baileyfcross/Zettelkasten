2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Container DNS Resolution

Container DNS resolution combines generated resolver configuration with network-scoped records and upstream DNS service. Podman mounts a suitable `resolv.conf` into the container, and [[Aardvark DNS]] can resolve names and aliases for peers on a managed [[Podman Network]] before forwarding other queries.

A failed application connection should distinguish resolution from reachability. An NXDOMAIN answer indicates that no name was found, while a correct address followed by failure points toward routes, listening sockets, port mappings, or filtering. This sequence keeps [[Container Namespace Troubleshooting]] evidence-driven.

# References

[[podmanfordevopssecondedition.pdf]]
