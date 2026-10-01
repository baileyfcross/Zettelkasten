2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Governance and Protection]]

# Microsoft Entra Service Principal

A Microsoft Entra service principal is the tenant-local security identity through which an application or managed identity receives assignments and accesses resources. It defines how the software operates in one tenant, including its permissions, user assignments, and applicable access policies.

An application object is the global definition or master configuration created by app registration; each tenant that uses the application has a corresponding service principal. Managed identities are represented by a special service-principal type whose credentials Azure controls, and legacy principals may lack an associated app registration. Separating application definition from tenant instance makes multitenant use possible, but every local principal still needs an owner, constrained credentials, reviewed permissions, and a deletion lifecycle.

# References

[[masteringmicrosoftentraid.pdf]]
