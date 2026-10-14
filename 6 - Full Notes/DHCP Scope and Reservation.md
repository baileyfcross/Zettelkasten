2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# DHCP Scope and Reservation

A DHCP scope defines the address range and configuration that a server may lease to clients on one IPv4 subnet. Exclusions remove addresses reserved for static infrastructure, while scope options supply values such as the default gateway, DNS servers, and DNS suffix. The lease duration determines how long a client may use an assignment before renewal.

A reservation binds a client's hardware identifier to a particular address while preserving DHCP-managed configuration. It is useful when a device needs predictability but centralized options and documentation are still desirable. Scopes should be authorized, sized for expected clients, and coordinated with static ranges to avoid duplicate addresses. A rogue or accidental DHCP server can disrupt an entire subnet by supplying conflicting leases or gateways, so server presence must be controlled as carefully as the scope values.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
