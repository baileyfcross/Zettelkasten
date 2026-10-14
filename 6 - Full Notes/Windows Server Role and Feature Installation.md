2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Deployment and Administration]]

# Windows Server Role and Feature Installation

A Windows Server role gives a server its main network purpose, such as directory services, DNS, file sharing, web hosting, or remote access. A feature is a supporting operating-system capability that may stand alone or enable a role. The Add Roles and Features wizard in Server Manager resolves required components, while PowerShell provides the same operation through repeatable commands such as `Install-WindowsFeature`.

Role installation should follow workload design rather than convenience. Combining unrelated services can increase the failure and security impact of one host, and some roles impose permanent constraints on naming or domain membership. Administrators should decide placement first, install management tools where appropriate, and verify the role's post-installation configuration instead of assuming that adding its binaries creates a production-ready service.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
