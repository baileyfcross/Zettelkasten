2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]] [[GitOps Deployment Operations]]

# Helm Chart

A Helm chart is a versioned package of related Kubernetes resource templates and default configuration. It replaces a loose collection of Deployment, Service, ConfigMap, Secret, ingress, and storage manifests with one defined application package.

When installed, Helm combines the templates with a [[Helm Values File]] to generate concrete Kubernetes manifests. A chart can be shared through a repository and reused across environments, but standardization is valuable only when the templates preserve the controls and resource requirements the application actually needs.

Helm's packaging and templating simplify repeated installation, but generated output should still be inspected and versioned through an auditable delivery path. Environment values must remain explicit, and secrets should not be hidden in ordinary values files simply because the chart makes them easy to interpolate.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[clouddevopsengineersguide.pdf]]

