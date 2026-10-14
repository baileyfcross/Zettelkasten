2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# DNS over HTTPS

DNS over HTTPS carries resolver queries inside encrypted HTTPS traffic. Encryption prevents an observer on the path from reading or casually modifying the DNS exchange between a client and its selected DoH resolver. Windows can associate known resolver addresses with DoH templates and apply encrypted-resolution behavior through system or policy configuration.

DoH protects transport, not the truth of every answer or the endpoint reached afterward. Enterprise deployment must preserve resolution of private zones and Active Directory records, decide which resolver is trusted, and account for monitoring or filtering that previously observed plain DNS. Sending corporate names to an unrelated public resolver can leak internal naming and break domain behavior, so encrypted DNS should be designed as part of the resolver architecture rather than enabled in isolation.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
