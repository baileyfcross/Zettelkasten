2026-09-18 17:13

Status: #baby

Tags: [[Game Network Transport and Serialization]] [[.NET Network Requests Sockets and Streams]]

# Network Port

A network port is a numeric transport-layer endpoint that directs incoming traffic on a host to the intended application or service. An IP address identifies the host interface, while the port distinguishes processes or logical services on that host.

Servers bind a [[Game Network Socket]] to an address and port so clients know where to send traffic. Firewalls and address translation may need explicit rules for the selected transport and port range.

Ports from 0 through 1023 are conventionally reserved for system services, 1024 through 49151 are registered user ports, and 49152 through 65535 are dynamic ports. A TCP listening port identifies the service, while an accepted connection receives its own connected socket endpoint so the server can maintain many clients concurrently.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[multiplayergameprogramming.pdf]]
