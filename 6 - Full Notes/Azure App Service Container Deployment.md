2026-09-27 11:23

Status: #baby

Tags: [[Cloud Application Deployment]]

# Azure App Service Container Deployment

Azure App Service container deployment runs a web application from an image stored in a registry. The hosting service manages the public web endpoint and process lifecycle while application settings provide environment-specific configuration to the container.

The image remains the release artifact, so a deployment should identify a deliberate version rather than depend indefinitely on an ambiguous mutable tag. Runtime logs and configuration belong in managed facilities outside the image.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
