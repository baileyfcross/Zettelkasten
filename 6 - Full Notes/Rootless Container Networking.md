2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Rootless Container Networking

Rootless container networking connects an unprivileged user's network namespace to the host without requiring that user to create ordinary privileged bridge and firewall state. Podman can use user-mode mechanisms such as pasta to forward traffic and map selected ports into the isolated namespace.

This changes several assumptions of rootful networking. Privileged host ports are unavailable by default, source addresses and reachability can differ, and `ping` may depend on host policy because raw-socket operations are restricted. Tests should cover outbound access, DNS, host access, and [[Container Port Publishing]] under the actual rootless configuration.

# References

[[podmanfordevopssecondedition.pdf]]
