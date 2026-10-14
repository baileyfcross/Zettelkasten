2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# Active Directory Integrated DNS Zone

An Active Directory-integrated DNS zone stores its records in the directory rather than in a conventional zone file on one primary server. Directory replication distributes the zone among DNS-enabled domain controllers, allowing more than one server to accept updates and answer from a current copy. Secure dynamic updates can use domain identity to limit who changes records.

Integration removes the single writable-primary pattern but makes zone health dependent on both DNS and Active Directory replication. The replication scope should match where the data is needed, and stale records or replication failures should be investigated rather than hidden by adding servers. AD integration is particularly appropriate for the domain namespace because clients and controllers already depend on closely coupled directory and name-resolution availability.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
