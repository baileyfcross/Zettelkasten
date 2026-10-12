2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Microsoft Entra Administrative Unit

A Microsoft Entra administrative unit is a directory scope that groups users, groups, or devices for delegated administration. It lets a large organization give a regional, departmental, or service-desk administrator authority over a bounded population without granting the same authority across the entire tenant.

Only roles and permissions that support administrative-unit scope inherit that boundary, and some sensitive operations remain restricted when the target is another administrator. Restricted-management administrative units add stronger protection around high-value identities by limiting which administrators can modify them. An administrative unit is therefore a delegation boundary within the tenant, not a separate tenant or a general replacement for resource-level [[Authorization]].

# References

[[masteringmicrosoftentraid.pdf]]
