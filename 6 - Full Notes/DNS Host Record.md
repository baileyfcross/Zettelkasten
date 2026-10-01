2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# DNS Host Record

A DNS host record maps a hostname to an IP address. An A record supplies an IPv4 address, while an AAAA record supplies an IPv6 address. These records let clients use stable names even when the numeric addressing beneath a service changes, and Active Directory relies on related DNS records to help clients locate domain services.

The record should identify the system or service that actually owns the address, use an appropriate time to live, and be removed when the target is retired. A host record provides forward resolution only; a corresponding pointer in a reverse lookup zone is separately required when software or troubleshooting must translate the address back to a name. DNS records and IP documentation should be updated together to avoid plausible but stale answers.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
