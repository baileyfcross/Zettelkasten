2026-09-27 22:21

Status: #baby

Tags: [[Terraform Infrastructure as Code]]

# Terraform Provider

A Terraform provider is a plugin that understands the API of a platform and exposes that platform's objects as Terraform resource types. Providers let the same configuration language manage services such as AWS, Azure, Google Cloud, GitHub, and Docker without embedding every external API in Terraform itself.

The configuration declares the required provider and an acceptable version. `terraform init` then downloads the plugin before planning or applying changes. Provider configuration can also select details such as a cloud region, while authentication should come from an appropriate credential mechanism rather than hardcoded secrets.

# References

[[clouddevopsengineersguide.pdf]]

