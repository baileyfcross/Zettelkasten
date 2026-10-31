2026-10-30 17:24

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Skaffold Artifact Build Configuration

Skaffold artifact build configuration names the container images produced from source and selects how each image is built. The book configures a Maven-based Jib build, allowing Skaffold to insert image construction into the development and delivery loop.

Local settings can keep the image in the local Docker daemon instead of pushing it to a registry. The declared artifact identity then connects the build output to the Kubernetes manifests that Skaffold deploys.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

