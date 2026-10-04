2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Container Network Namespace

A container network namespace supplies a private network stack with its own interfaces, addresses, routes, port space, and firewall view. Virtual interfaces and host-side routing connect that isolated stack to Podman networks and external destinations without making every container share the host's network state.

This boundary makes identical internal ports possible across containers and gives diagnostics a clear scope. An address or route visible on the host may not exist inside the namespace, so [[Container Namespace Troubleshooting]] must examine name resolution, interfaces, routes, sockets, and filtering from the workload's actual network context.

# References

[[podmanfordevopssecondedition.pdf]]
