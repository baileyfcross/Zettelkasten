2026-10-19 22:48

Status: #baby

Tags: [[Helidon Platform Models and Project Tooling]]

# Helidon Nima Virtual-Thread Runtime

Helidon Níma is the ground-up web-server implementation introduced in Helidon 4.0. It replaced the Netty-based reactive server used by Helidon versions 1 through 3 with a blocking programming model implemented on Java virtual threads.

The architecture places both Helidon SE components and Helidon MP facilities above this shared virtual-thread server. Because virtual threads arrived with JDK 21, Helidon 4 establishes JDK 21 as its minimum Java version while older release trains retain the earlier reactive design.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
