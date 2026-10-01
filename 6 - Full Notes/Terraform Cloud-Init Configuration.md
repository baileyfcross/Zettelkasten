2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform Cloud-Init Configuration

Terraform can assemble multipart cloud-init user data containing shell scripts, cloud-config documents, and other startup parts for a newly created virtual machine. Resource outputs and [[Terraform Input Variable|inputs]] can be rendered into this configuration before the compute instance boots.

Cloud-init is well suited to lightweight first-boot wiring, such as installing an agent or supplying an endpoint. Extensive machine construction is usually more predictable in an [[Immutable Machine Image Pipeline]], where configuration is tested before launch. User data also reaches provider APIs and often state, so secret distribution should use a dedicated secret service rather than embedding long-lived credentials in the rendered payload.

# References

[[masteringterraform.pdf]]

