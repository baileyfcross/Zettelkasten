2026-10-11 21:26

Status: #baby

Tags: [[Docker Networking and Compose]]

# Docker Compose Service Scaling

Docker Compose service scaling creates several containers from one service definition on a single Docker host. The replicas share the declared image, networks, environment, and mounts, while Docker assigns separate instance names and the service name remains the logical application role.

A fixed host-port mapping cannot be owned by every replica. Omitting the fixed host side lets Docker allocate distinct ephemeral ports, or a reverse proxy can provide one stable entry point and balance among instances. Compose scaling is useful for development and testing but does not supply multi-node placement or failure recovery.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
