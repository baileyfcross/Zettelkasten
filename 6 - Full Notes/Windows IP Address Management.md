2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# Windows IP Address Management

Windows IP Address Management discovers and inventories supported DNS, DHCP, domain, and address-space information so administrators can manage the relationships from a central server. It records address utilization, server status, scopes, zones, and configuration history rather than leaving IP ownership scattered among spreadsheets and individual consoles.

IPAM can use Group Policy-based provisioning to grant its server the access required to manage discovered infrastructure. It should be placed on a dedicated member server rather than casually combined with a domain controller or DHCP server. Central visibility is most valuable when administrators keep discovery and access current; IPAM does not prevent address conflicts if changes occur outside its managed process or if stale records are never reconciled.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
