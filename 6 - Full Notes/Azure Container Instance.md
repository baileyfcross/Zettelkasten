2026-09-27 11:23

Status: #baby

Tags: [[Cloud Application Deployment]]

# Azure Container Instance

Azure Container Instances runs a container image without requiring the user to manage a virtual machine or container orchestrator. A deployment specifies the image, resource allocation, networking, and environment configuration needed to start the container group.

It offers a direct path for isolated or modest container workloads. Applications that need complex service discovery, rolling orchestration, or extensive multi-container coordination may require a broader hosting platform.

The Azure architecture map places Azure Container Instances near the infrastructure-oriented end of the container-service spectrum. It removes virtual-machine management and starts containers quickly, but supplies fewer application-platform capabilities than Azure Container Apps or AKS. It therefore fits burst, batch, build, or isolated execution better than a microservice estate that depends on rich routing, revision management, service discovery, and coordinated operations.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
