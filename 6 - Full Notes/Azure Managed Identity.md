2026-09-27 21:45

Status: #baby

Tags: [[Azure Cloud-Native Application Architecture]] [[Microsoft Entra Governance and Protection]]

# Azure Managed Identity

An Azure managed identity gives an Azure resource an Entra identity whose credentials are created, rotated, and protected by the platform. Application code obtains a token for an Azure resource and authorizes through Azure role-based access control instead of storing a client secret. Managed identity removes credential handling, not permission design: the target role, scope, token audience, and resource’s support for the mechanism still matter.

A system-assigned identity follows the lifecycle of one Azure resource and disappears with it. A user-assigned identity is created independently, can be attached to several supported resources, and persists until explicitly removed. Both appear in Entra as managed-identity service principals; choosing between them is therefore a lifecycle and sharing decision, not a difference in token semantics.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[masteringmicrosoftentraid.pdf]]
