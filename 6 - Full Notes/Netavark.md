2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Netavark

Netavark is Podman's network configuration backend. It creates and removes the interfaces, addresses, routes, port-forwarding rules, and related host networking state needed to attach a container or pod to one or more [[Podman Network]] objects.

The backend consumes network definitions and performs the privileged configuration work, while [[Aardvark DNS]] supplies container-aware name resolution. Separating these responsibilities makes it easier to reason about whether a failure comes from network construction, DNS records, host filtering, or the application itself.

# References

[[podmanfordevopssecondedition.pdf]]
