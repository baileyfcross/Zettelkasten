2026-09-27 21:45

Status: #baby

Tags: [[Azure Security Architecture and Operations]]

# Azure Bring Your Own Key

Azure Bring Your Own Key lets an organization supply and control a key used by a supported Azure service for encryption. The key is commonly held in Azure Key Vault or Managed HSM while the service performs encryption operations under granted permissions. BYOK can support rotation, revocation, separation of duties, and regulatory evidence, but it also transfers availability and lifecycle responsibilities to the customer: disabling, deleting, or misconfiguring the key can make protected data unavailable.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
