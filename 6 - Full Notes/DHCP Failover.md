2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# DHCP Failover

Windows DHCP failover pairs two servers for an IPv4 scope and replicates lease information between them. If one partner becomes unavailable, the other can continue issuing and renewing addresses without treating the active lease database as unknown. The relationship is configured per scope and does not arise merely because DHCP happens to run on redundant domain controllers.

Hot standby mode assigns primary responsibility to one server and keeps the other ready for failure, which suits a remote site backed by a central server. Load-balance mode lets both partners serve clients and assumes a reliable connection between them. Only two servers participate in one relationship, and Windows DHCP failover does not provide the same mechanism for IPv6 scopes. The maximum client lead time bounds how far one partner can extend leases without confirmation from the other.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
