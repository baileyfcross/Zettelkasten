2026-09-30 23:37

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Read-Only Domain Controller

A read-only domain controller holds a non-writable copy of the Active Directory database for a location where local authentication is useful but physical or administrative security is weaker. Directory changes are made on writable controllers and replicated toward the RODC, preventing a compromised branch server from originating arbitrary updates back into the domain.

Its Password Replication Policy controls which credentials may be cached locally. Explicit denials take precedence, so highly privileged accounts can remain absent even when broader groups are allowed. Caching selected branch-user credentials permits logon during a WAN outage, but it also defines the credentials exposed if the RODC is stolen. Deployment therefore balances offline continuity against the smallest practical cache.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
