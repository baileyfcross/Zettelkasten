2026-10-30 17:24

Status: #baby

Tags: [[Helm and Helmfile Application Packaging]]

# Helm Chart Dependency Update

A Helm chart can declare another chart as a dependency in its metadata. Running the dependency update resolves that declaration and places the packaged dependency under the chart so rendering and installation can include it.

The declaration alone does not download the dependency. Version and repository information therefore belong to a reproducible resolution step rather than an assumption that the cluster will find the chart during installation.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

