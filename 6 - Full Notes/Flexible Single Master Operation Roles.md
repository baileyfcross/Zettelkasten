2026-09-30 23:37

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Flexible Single Master Operation Roles

Flexible Single Master Operation roles assign directory changes that cannot safely use ordinary multi-master behavior to one domain controller at a time. The schema master and domain naming master are forest-wide. The RID master, PDC emulator, and infrastructure master exist in each domain and coordinate identifier allocation, time and password-sensitive behavior, and cross-domain object references.

The role holder is not necessarily the only domain controller serving users, but an unavailable holder can block its specialized operations. Planned maintenance uses a transfer to an online controller. Permanent loss may require seizure after confirming the old holder will not return in its former role. Before demoting a controller, administrators should locate and move any roles it owns rather than discovering the dependency during removal.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
