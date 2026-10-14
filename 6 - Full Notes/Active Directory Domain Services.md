2026-09-30 23:37

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Active Directory Domain Services

Active Directory Domain Services is a replicated directory for identities, computers, groups, policies, and service-related configuration in a Windows domain. It provides a common authentication system so a user can receive a security token and use authorized resources throughout the domain without maintaining a separate local identity on every server.

AD DS is both a data model and a dependency network. Domain controllers store the directory, DNS locates its services, sites guide replication and authentication traffic, and Group Policy turns directory placement into configuration. Because so many services depend on it, a production domain should have multiple domain controllers and functioning name resolution rather than concentrating identity on one machine.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
