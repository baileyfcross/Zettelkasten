2026-10-30 17:24

Status: #baby

Tags: [[Docker Networking and Compose]]

# Legacy Docker Container Link

A legacy Docker container link connects one container to another and exposes connection information under an assigned alias. The book uses links in an early microservice-and-database example before replacing them with an explicit container network.

Links couple startup commands and container identities and are less flexible than user-defined networks with DNS-based service names. They are useful for understanding older examples but should not define a modern multi-service topology.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

