2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Governance and Protection]]

# Microsoft Entra ID Migration

Microsoft Entra ID migration is the staged transformation from an on-premises Active Directory control plane to cloud-native identity. Organizations commonly move through cloud-attached, hybrid, cloud-first, minimized-AD, and cloud-only states rather than attempting one irreversible cutover.

Planning begins with users, groups, applications, service accounts, trusts, policies, devices, and protocol dependencies. Phased migration and hybrid coexistence reduce risk; lift-and-shift can preserve legacy domain services in Azure; a greenfield organization can begin cloud-only. Applications using modern protocols can move to Entra SSO, while LDAP, Kerberos, or NTLM workloads require modernization or explicit bridges. Domain controllers should be decommissioned only after authentication, devices, DNS, certificates, files, policies, and automation no longer depend on them.

# References

[[masteringmicrosoftentraid.pdf]]
