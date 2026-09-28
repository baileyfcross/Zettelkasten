2026-09-27 21:45

Status: #baby

Tags: [[Azure Cloud-Native Application Architecture]]

# Azure Workload Identity Federation

Azure workload identity federation establishes trust between an external token issuer, such as GitHub or an AKS cluster, and Entra ID. A matching external token can be exchanged for an Entra access token through a user-assigned identity or app registration without storing a long-lived client secret. Issuer, subject, audience, token lifetime, and target permissions form the trust boundary and must be constrained together.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

