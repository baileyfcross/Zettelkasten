2026-10-30 17:24

Status: #baby

Tags: [[Helm and Helmfile Application Packaging]]

# Helm Chart Structure

A Helm chart groups chart metadata, default values, Kubernetes templates, and optional packaged dependencies into one application package. `Chart.yaml` describes the chart, `values.yaml` supplies defaults, and the templates directory produces the manifests installed into the cluster.

The structure replaces a growing set of copied environment-specific YAML files with one versioned template boundary. Environment differences should enter through the chart's declared values rather than through manual edits to rendered resources.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

