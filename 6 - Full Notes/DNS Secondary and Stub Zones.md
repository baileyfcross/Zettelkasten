2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# DNS Secondary and Stub Zones

A secondary DNS zone is a read-only copy transferred from an authoritative primary and can answer with the zone's full replicated record set. A stub zone keeps only the records needed to locate authoritative servers for another zone, directing queries to the current authorities without copying all of its data.

The two models solve different problems. A secondary provides answer redundancy and local access to the full zone, but transfer permissions and refresh behavior must be maintained. A stub preserves delegation awareness with less data and is useful when another namespace remains independently administered. Neither should be chosen merely because two organizations need name resolution; conditional forwarding may be simpler when queries only need to be sent to known resolvers.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
