2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Manifest

A Kubernetes manifest is a YAML or JSON document that declares an API object's kind, metadata, and desired specification. Applying the manifest submits that declaration to the [[Kubernetes API Server]], after which controllers and node agents work asynchronously to realize it.

The manifest is valuable as reviewable intent, not merely as a command wrapper. Version control, schema validation, policy checks, and environment-specific configuration make changes reproducible; imperative edits that are not reflected in the source of truth create drift and weaken recovery.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

