2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Platform Architecture]]

# Microsoft Foundry Supporting Azure Services

Microsoft Foundry relies on supporting Azure services rather than containing every platform function itself. Storage accounts hold documents and other project data, Key Vault protects secrets and connections, Azure AI Search supplies indexed retrieval, and Application Insights with Log Analytics stores telemetry and traces.

Container Registry supports custom deployment images, while virtual networks and Private Link constrain connectivity. Some services are mandatory and others depend on the workload's production, security, retrieval, or observability requirements. The architecture should treat these services as one dependency graph, because removing a project connection or omitting a telemetry component can break a deployment or leave it unauditable.

# References

[[microsoftfoundryinaction.pdf]]
