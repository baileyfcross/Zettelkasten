2026-09-27 21:45

Status: #baby

Tags: [[Azure Cloud-Native Application Architecture]] [[Microsoft Entra Governance and Protection]]

# Azure Workload Identity Federation

Azure workload identity federation establishes trust between an external token issuer, such as GitHub or an AKS cluster, and Entra ID. A matching external token can be exchanged for an Entra access token through a user-assigned identity or app registration without storing a long-lived client secret. Issuer, subject, audience, token lifetime, and target permissions form the trust boundary and must be constrained together.

The federated identity credential records the external issuer, audience, and workload subject that Entra will accept. At runtime the workload presents its external token; Entra compares the claims with that trust record and, on a match, returns an access token for the protected resource. Flexible credentials can consolidate subjects with restricted matching expressions, but the exchange still needs tight claim constraints and least-privilege authorization.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[masteringmicrosoftentraid.pdf]]
