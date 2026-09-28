2026-09-27 21:45

Status: #baby

Tags: [[Azure Cloud-Native Application Architecture]]

# Azure Managed Identity

An Azure managed identity gives an Azure resource an Entra identity whose credentials are created, rotated, and protected by the platform. Application code obtains a token for an Azure resource and authorizes through Azure role-based access control instead of storing a client secret. Managed identity removes credential handling, not permission design: the target role, scope, token audience, and resource’s support for the mechanism still matter.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

