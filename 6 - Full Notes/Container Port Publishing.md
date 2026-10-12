2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]] [[Docker Networking and Compose]]

# Container Port Publishing

Container port publishing maps a host address and port to a port inside a container or pod network namespace. It creates an inbound path to a service that would otherwise be reachable only through the container network, and it is separate from Dockerfile `EXPOSE` metadata.

The application must listen on the expected container address and port, the mapping must target that port, and the host firewall must permit the traffic. Rootless users normally cannot bind privileged host ports below 1024, so [[Rootless Container Networking]] may require a higher host port or deliberate host configuration.

Docker port publishing creates an explicit host-to-container ingress path; merely exposing or listening on a container port does not publish it externally. Fixed host ports also constrain local service scaling because only one container can bind a given host address and port combination.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[podmanfordevopssecondedition.pdf]]
