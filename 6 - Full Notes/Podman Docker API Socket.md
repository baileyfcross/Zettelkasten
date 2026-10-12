2026-10-04 08:37

Status: #baby

Tags: [[Podman Workload Integration and Desktop]]

# Podman Docker API Socket

The Podman Docker API socket exposes a compatibility service that lets Docker-oriented clients send REST requests to Podman. Systemd socket activation can start the service only when a client connects, preserving [[Podman Daemonless Architecture]] for ordinary CLI use.

The socket carries control authority over the user's or system's containers and should be protected like an administrative interface. Its path and ownership differ between rootless and rootful services. API compatibility is broad enough for tools such as [[Docker Compose]], but callers still need testing for behavior that depends on Docker's daemon or unsupported endpoints.

# References

[[podmanfordevopssecondedition.pdf]]
