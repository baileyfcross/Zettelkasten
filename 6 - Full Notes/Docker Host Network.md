2026-11-11 19:33

Status: #baby

Tags: [[Docker Networking and Compose]]

# Docker Host Network

The Docker host network driver places a containerized process in the host's network namespace instead of giving it an isolated container network. A service therefore binds directly to host interfaces and ports, without a separate Docker port-publication step.

This mode removes the network boundary between the container and host and makes host-port conflicts part of container startup. The source presents it as a Linux-specific choice for workloads that deliberately need the host network rather than the isolation supplied by a [[Docker Bridge Network]].

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
