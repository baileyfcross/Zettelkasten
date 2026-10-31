2026-10-30 17:24

Status: #baby

Tags: [[Docker Networking and Compose]]

# Docker Host Service Connectivity

Docker host service connectivity lets a container reach a database or other process running on the container host rather than in another container. The connection address must name the host as visible from the container network, not assume that container-local `localhost` refers to the host.

This topology can be convenient during migration or development, but it couples the container to host-specific addressing and service lifecycle. Containerizing the dependency or using an external managed endpoint creates a different, more explicit boundary.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

