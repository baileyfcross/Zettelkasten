2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Container Port Publishing

Container port publishing maps a host address and port to a port inside a container or pod network namespace. It creates an inbound path to a service that would otherwise be reachable only through the container network, and it is separate from Dockerfile `EXPOSE` metadata.

The application must listen on the expected container address and port, the mapping must target that port, and the host firewall must permit the traffic. Rootless users normally cannot bind privileged host ports below 1024, so [[Rootless Container Networking]] may require a higher host port or deliberate host configuration.

# References

[[podmanfordevopssecondedition.pdf]]
