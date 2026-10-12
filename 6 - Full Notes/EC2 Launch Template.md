2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# EC2 Launch Template

An EC2 launch template is a reusable, versioned specification for launching instances. It can name an [[Amazon Machine Image]], instance type, security groups, storage mappings, key pair, IAM role, and startup data.

An [[EC2 Auto Scaling Group]] uses the template to create consistent replacement and scale-out capacity. Versioning makes changes deliberate: a revised configuration can be tested and then selected without erasing the earlier launch definition.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
