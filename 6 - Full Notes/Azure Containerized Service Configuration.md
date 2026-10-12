2026-09-27 11:23

Status: #baby

Tags: [[Cloud Application Deployment]]

# Azure Containerized Service Configuration

Azure containerized service configuration supplies settings to a deployed image without changing its filesystem layers. Service URLs, connection strings, environment names, and feature settings are bound into the .NET configuration system when the hosted container starts.

Separating configuration from the image lets one tested artifact move across environments. Sensitive values should use managed secret facilities and access controls rather than ordinary committed settings.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
