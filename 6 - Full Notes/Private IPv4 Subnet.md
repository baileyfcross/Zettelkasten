2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Networking and Remote Access]]

# Private IPv4 Subnet

A private IPv4 subnet uses address space reserved for internal networks: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`. The prefix length or subnet mask separates network bits from host bits and determines which addresses a host considers directly reachable. Traffic for a different subnet normally goes to a router through the default gateway.

Subnet design affects capacity, broadcast scope, routing, and remote connectivity. Common home ranges such as `192.168.0.0/24` and `192.168.1.0/24` often overlap with VPN clients' local networks, producing ambiguous routes, so business networks should plan less collision-prone space. Public addresses should not be improvised inside a private network because internal routes can make their legitimate internet destinations unreachable.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
