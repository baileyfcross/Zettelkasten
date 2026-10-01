2026-09-30 23:37

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Domain Controller

A domain controller is a Windows server that hosts Active Directory Domain Services and participates in authenticating domain users and computers. Promoting the first controller creates a new forest and root domain; later controllers can add redundancy to an existing domain or introduce another domain into the forest. DNS is commonly installed with the role because clients use DNS records to locate directory services.

Before promotion, the server should have its final hostname, a static address, and DNS settings appropriate to the domain. Multiple controllers reduce the chance that authentication and directory-dependent services fail with one host. Removal should use a supported demotion while the controller is available; forced removal of a failed controller requires cleanup of directory, site, DNS, and operations-master remnants.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
