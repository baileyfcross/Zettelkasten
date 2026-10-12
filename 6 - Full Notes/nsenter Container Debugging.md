2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# nsenter Container Debugging

`nsenter` container debugging starts a host command inside one or more namespaces of a target container process. Using the container's host PID, an operator can enter just the network namespace for focused tests or all namespaces for a view similar to [[Container Exec]].

The important advantage is that the executable comes from the host, not the container image. Tools such as `ip`, `ss`, `dig`, or a shell can therefore diagnose a minimal image that intentionally omits them. Namespace entry is powerful host access and should be limited to authorized troubleshooting rather than installed as an application feature.

# References

[[podmanfordevopssecondedition.pdf]]
