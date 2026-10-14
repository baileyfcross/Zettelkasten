2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Governance and Protection]]

# Microsoft Entra Backup and Recovery

Microsoft Entra backup and recovery combines native soft deletion with independent records of tenant configuration. Selected objects—including users, groups, applications, administrative units, Conditional Access policies, and named locations—retain recoverable state for a limited window, after which deletion becomes permanent.

Native recovery does not cover every object or every relationship. A resilient plan regularly exports configuration through Microsoft Graph, Entra Exporter, Microsoft 365 Desired State Configuration, Conditional Access APIs, or equivalent documented snapshots, then tests how dependencies will be reconstructed. [[Emergency Access Account|Emergency access]] preserves an administrative path, while audit and sign-in logs explain what changed. Recovery readiness therefore depends on both recoverable objects and a current model of the tenant's intended state.

# References

[[masteringmicrosoftentraid.pdf]]
