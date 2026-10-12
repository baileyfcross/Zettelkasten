2026-09-27 22:21

Status: #baby

Tags: [[Terraform Core Workflow and State]]

# Terraform Resource

A Terraform resource block declares an infrastructure object that should exist. Its resource type comes from a [[Terraform Provider]], while its local name gives other configuration in the same project a stable way to refer to that object and its attributes.

The block contains arguments describing desired properties, such as an object name, region-dependent settings, or tags. Terraform maps the declaration to a real object through [[Terraform State]], allowing later plans to distinguish creation from modification or destruction rather than treating every run as a new provisioning request.

When one resource argument references another resource's attribute, Terraform adds an edge to its [[Terraform Dependency Graph]]. Stable resource addresses are operationally important: changing an address without a `moved` block can make an existing object appear deleted at the old location and newly required at the new one.

# References

[[clouddevopsengineersguide.pdf]]
[[masteringterraform.pdf]]
