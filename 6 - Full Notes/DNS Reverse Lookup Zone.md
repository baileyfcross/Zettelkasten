2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# DNS Reverse Lookup Zone

A DNS reverse lookup zone maps addresses back to names with PTR records. IPv4 reverse zones are organized beneath `in-addr.arpa` according to the relevant network, while IPv6 uses its own reverse namespace. Reverse lookup complements, rather than automatically mirrors, the A or AAAA record used for forward resolution.

Reverse records assist diagnostics, logging, and services that inspect the apparent name of a connecting address. They should agree with the intended forward identity, but a successful reverse lookup is not authentication because zone owners control their own mappings. In Windows environments, DHCP can participate in dynamic record registration, so ownership and scavenging rules must be clear to prevent abandoned PTR entries from outliving their leases.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
