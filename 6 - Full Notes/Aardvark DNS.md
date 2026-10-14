2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Aardvark DNS

Aardvark DNS is the DNS service used with Podman's Netavark backend to resolve container names and aliases on managed networks. It maintains records that reflect network membership so cooperating containers can address stable names instead of discovering changing container IP addresses.

Name resolution is scoped by network connectivity: two containers must share an appropriate [[Podman Network]] before a local name is useful. Debugging therefore separates a missing or wrong DNS answer from routing, port listening, and host-firewall problems rather than treating every failed connection as one networking issue.

# References

[[podmanfordevopssecondedition.pdf]]
