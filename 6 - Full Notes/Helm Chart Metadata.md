2026-10-30 17:24

Status: #baby

Tags: [[Helm and Helmfile Application Packaging]]

# Helm Chart Metadata

Helm chart metadata identifies the package, its chart version, application version, description, and dependency declarations. It gives the templates and values a versioned package identity that Helm can validate and install.

Changing an application or chart should update the appropriate version before an upgrade. Dependency entries describe required charts, but the dependency artifacts still need to be resolved and placed into the chart's dependency directory.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

