2026-10-14 00:45

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Active Directory 32K Database Pages

Windows Server 2025 expands the Active Directory database engine page size from 8 KB to 32 KB. The larger page can hold bigger directory objects and as many as 3,200 values in a multi-valued attribute. It also reduces page splitting and fragmentation when a large directory changes frequently, which lowers database-management overhead and improves scalability.

The transition is a forest-level change rather than an isolated tuning choice for one [[Domain Controller]]. Mixed environments retain legacy 8 KB compatibility while the forest is upgraded in a controlled sequence. Because the change is critical and described as irreversible, administrators should take a complete directory backup, test the transition outside production, verify that backup tooling supports the new structure, and confirm the resulting database mode through Directory Service events.

# References

[[windowsserver2025administrationfundamentals_fourthedition.pdf]]
