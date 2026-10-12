2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Microsoft Entra Domain Services

Microsoft Entra Domain Services supplies a managed domain for applications that still require LDAP, Kerberos, NTLM, domain join, or Group Policy. Microsoft operates the domain controllers, patching, backups, and core availability, while an organization deploys replica sets into selected virtual networks and manages supported directory objects and policies.

Identity data synchronizes one way from Entra ID into the managed domain, so the service is not a fully writable replacement for self-managed Active Directory. Custom organizational units and resource forests can isolate legacy workloads, and trusts can support selected scenarios. Security still requires disabling obsolete cryptography where possible, enforcing LDAP protections, monitoring audit events, and treating the managed domain as a compatibility bridge on the path toward modern authentication.

# References

[[masteringmicrosoftentraid.pdf]]
