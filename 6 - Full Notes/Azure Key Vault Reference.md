2026-09-27 21:45

Status: #baby

Tags: [[Azure Cloud-Native Application Architecture]]

# Azure Key Vault Reference

An Azure Key Vault reference lets a supported platform setting point to a Key Vault secret while the application reads it as ordinary configuration. Azure resolves the reference using the workload’s identity, so code need not fetch or store the credential directly. The feature reduces secret-handling logic, but access policy, refresh behavior, supported secret types, startup failure, and rotation timing remain operational concerns.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

