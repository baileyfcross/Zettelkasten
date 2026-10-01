2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform TLS Provider

The Terraform TLS provider can generate private keys, certificate requests, and self-signed or locally signed certificates as managed values. It is useful for bootstrapping SSH access, development certificates, or inputs to an external certificate authority when those artifacts are integral to provisioning.

Private material generated this way is stored in [[Terraform State]], so a protected [[Terraform Remote Backend]] becomes part of the key-management boundary. Production public-key infrastructure often requires rotation, audit, hardware protection, and established trust processes beyond the provider's scope. Terraform can orchestrate enrollment, but it should not silently replace an organization's certificate authority.

# References

[[masteringterraform.pdf]]

