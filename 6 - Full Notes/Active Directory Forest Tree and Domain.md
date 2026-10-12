2026-09-30 23:37

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Active Directory Forest Tree and Domain

An Active Directory domain is a naming, authentication, and policy boundary within a directory. Domains with a contiguous DNS namespace form a tree; one or more trees share a forest. The forest is the broadest directory structure and carries shared schema and configuration, while individual domains can separate administration, naming, and some policy concerns.

Creating extra domains adds controllers, DNS relationships, trusts, and long-term operational work. Organizational units usually provide a lighter way to delegate management and apply policy inside one domain. A new domain or tree is justified when its durable boundary is actually needed, not simply to mirror every department. Forest design is therefore an infrastructure decision whose consequences outlive the installation wizard.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
