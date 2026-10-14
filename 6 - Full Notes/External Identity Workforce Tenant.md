2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra External and Network Access]]

# External Identity Workforce Tenant

An External Identity workforce tenant uses the organization's ordinary Microsoft Entra tenant for B2B collaboration. External guests or members authenticate with a home Entra directory, social provider, federated identity provider, Microsoft account, or email one-time passcode while a local object represents their relationship to the resource tenant.

The resource tenant controls application access, guest restrictions, Conditional Access, invitations, sponsors, and governance. [[Cross-Tenant Access Settings]] define inbound and outbound trust with partner tenants, while access packages, lifecycle workflows, and access reviews prevent guest access from persisting after the relationship ends. The home tenant proves the external identity; the resource tenant remains responsible for what that identity may access locally.

# References

[[masteringmicrosoftentraid.pdf]]
