2026-10-19 22:48

Status: #baby

Tags: [[Helidon Platform Models and Project Tooling]]

# Helidon SE Programming Model

Helidon SE is the smaller Helidon programming model for building Java microservices with functional-style APIs. Its core WebServer, Config, and Security components can run without an application server, and WebClient completes the minimal set for issuing HTTP requests.

The model avoids annotations, dependency injection, and enterprise Java standards. Releases 1 through 3 used reactive, nonblocking APIs over Netty, while Helidon 4 moved the server and client model to blocking code backed by virtual threads through [[Helidon Nima Virtual-Thread Runtime]].

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
