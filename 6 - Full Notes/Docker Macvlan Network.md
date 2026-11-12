2026-11-11 19:33

Status: #baby

Tags: [[Docker Networking and Compose]]

# Docker Macvlan Network

A Docker macvlan network assigns a container its own MAC address and connects it directly to the host's physical network. To other devices on that network, the container can appear as a separate physical endpoint rather than as a service reached through a published host port.

The source positions macvlan for workloads, including some legacy applications, that require direct presence on the physical network. This purpose differs from an overlay network's logical communication across multiple container hosts.

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
