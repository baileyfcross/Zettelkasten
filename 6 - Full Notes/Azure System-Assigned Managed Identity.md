2026-09-27 21:45

Status: #baby

Tags: [[Azure Cloud-Native Application Architecture]] [[Microsoft Foundry Enterprise Agent Integrations]]

# Azure System-Assigned Managed Identity

An Azure system-assigned managed identity belongs to one Azure resource and shares its lifecycle. Enabling it creates an Entra service principal; deleting the resource deletes the identity. The tight relationship simplifies ownership for a single workload and prevents reuse elsewhere. Role assignments must nevertheless be removed or reviewed with the resource because the identity’s convenience does not justify broad permissions.

For a published Microsoft Foundry agent, a system-assigned managed identity can replace development-time credentials when invoking supported Azure or external integrations. The downstream system must still trust that identity and grant only the required permissions. Publishing creates an operational identity boundary; it does not automatically authorize every tool or data source configured during development.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
[[microsoftfoundryinaction.pdf]]
