2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra External and Network Access]]

# Cross-Tenant Synchronization

Cross-tenant synchronization automatically provisions selected users from one Microsoft Entra tenant into another as B2B identities. It is configured as an organization-specific inbound capability and is most appropriate between tenants under a shared organizational relationship.

Synchronization improves predictable account creation and attribute maintenance compared with individual invitations, but it does not merge the tenants or transfer authority over the source identity. Scoping rules decide which users and groups participate, mappings determine which attributes flow, and deletion behavior must remove access when a person falls out of scope. The synchronized object remains subject to the destination tenant's [[Cross-Tenant Access Settings]], assignments, reviews, and Conditional Access policies.

# References

[[masteringmicrosoftentraid.pdf]]
