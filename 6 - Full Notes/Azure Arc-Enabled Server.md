2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Deployment and Administration]]

# Azure Arc-Enabled Server

An Azure Arc-enabled server is an on-premises or non-Azure machine registered as a manageable resource in the Azure control plane. Registration installs a connected-machine agent through a generated script or installer, associates the host with a subscription, resource group, and region, and uses an encrypted outbound connection to Azure. Tags can then organize the server alongside native Azure resources.

Arc extends hybrid governance and management without moving the workload itself. For Windows Server 2025, it can support services such as pay-as-you-go licensing and hotpatching when prerequisites and licensing permit. Because registration crosses an administrative boundary, teams should decide who owns the Azure resource, which policies apply, and whether public endpoint connectivity or a more private network path is appropriate before onboarding production servers.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
