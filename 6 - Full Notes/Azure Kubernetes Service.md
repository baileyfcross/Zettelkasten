2026-09-08 22:09

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Azure Kubernetes Service

Azure Kubernetes Service is Microsoft's managed environment for running Kubernetes clusters. It gives an application control over Kubernetes deployment and scaling while Azure operates much of the cluster infrastructure.

The 2019 project creates an AKS cluster, grants it access to an Azure container registry, and applies a deployment that runs the sales-order image. The workload remains containerized and is presented as portable in principle to another Kubernetes provider.

The book positions Azure Kubernetes Service as an orchestration option for containerized microservices, managing clusters, replicas, service exposure, and deployment while the application team retains responsibility for service boundaries, data, and message behavior.

The newer Azure architecture map emphasizes that AKS is managed Kubernetes, not a fully managed application platform. Azure operates the control plane, while the platform team still designs node pools, networking, ingress, identity, policy, upgrades, observability, scaling, disruption handling, and workload isolation. This broad control makes AKS suitable when Kubernetes portability or extensibility is a requirement, but it also creates more operational responsibility than serverless container choices.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[c8andnetcore30projectsusingazure.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
