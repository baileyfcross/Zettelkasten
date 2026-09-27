2026-09-27 11:23

Status: #baby

Tags: [[Cloud Application Deployment]]

# Azure Container Registry Image Push

An Azure Container Registry image push tags a locally built container image with the registry's qualified repository name and uploads its layers to the managed registry. Azure hosting services can then pull that identified artifact for deployment.

Authentication permits the transfer, while repository names and tags communicate which service and version the image represents. A successful push publishes an artifact; it does not by itself update a running application.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
