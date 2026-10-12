2026-09-08 22:09

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Load Balancing

Kubernetes load balancing distributes available work or traffic among replicated workload instances. In the order-processing example, the shared queue lets whichever worker is available claim the next message rather than binding work to a specific pod.

Adding replicas increases potential consumption capacity, while removing one leaves remaining workers able to continue. Effective balancing therefore depends on both the orchestrator and an application input mechanism designed for competing consumers.

The Azure architecture map distinguishes internal Kubernetes service balancing from ingress that accepts traffic at the cluster boundary. An AKS ingress design may use an in-cluster controller or an Azure-managed application gateway, with tradeoffs in Layer 7 routing, Web Application Firewall integration, private exposure, certificate handling, scale, and operational ownership. The external entry path must also align with DNS and network topology rather than being selected in isolation.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
