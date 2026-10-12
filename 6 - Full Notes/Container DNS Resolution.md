2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]] [[Docker Networking and Compose]]

# Container DNS Resolution

Container DNS resolution combines generated resolver configuration with network-scoped records and upstream DNS service. Podman mounts a suitable `resolv.conf` into the container, and [[Aardvark DNS]] can resolve names and aliases for peers on a managed [[Podman Network]] before forwarding other queries.

A failed application connection should distinguish resolution from reachability. An NXDOMAIN answer indicates that no name was found, while a correct address followed by failure points toward routes, listening sockets, port mappings, or filtering. This sequence keeps [[Container Namespace Troubleshooting]] evidence-driven.

User-defined Docker networks provide embedded DNS so containers can resolve peers by stable service or container names instead of transient IP addresses. Name-based discovery keeps application configuration valid as containers are recreated and addresses change.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[podmanfordevopssecondedition.pdf]]
