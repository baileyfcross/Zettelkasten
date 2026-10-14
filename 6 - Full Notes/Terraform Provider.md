2026-09-27 22:21

Status: #baby

Tags: [[Terraform Core Workflow and State]]

# Terraform Provider

A Terraform provider is a plugin that understands the API of a platform and exposes that platform's objects as Terraform resource types. Providers let the same configuration language manage services such as AWS, Azure, Google Cloud, GitHub, and Docker without embedding every external API in Terraform itself.

The configuration declares the required provider and an acceptable version. `terraform init` then downloads the plugin before planning or applying changes. Provider configuration can also select details such as a cloud region, while authentication should come from an appropriate credential mechanism rather than hardcoded secrets.

Aliased provider configurations let one root module target multiple regions, accounts, or subscriptions, and a module can receive the appropriate instance explicitly. Providers also define practical control-plane boundaries: a Kubernetes provider cannot plan workload resources until the cluster that supplies its endpoint and credentials exists.

# References

[[clouddevopsengineersguide.pdf]]
[[masteringterraform.pdf]]
