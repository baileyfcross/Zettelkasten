2026-09-27 18:58

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# AWS Storage Modality Selection

AWS storage modality selection begins with how an application accesses data. Block storage presents addressable volumes to one host, file storage exposes a shared hierarchical filesystem, and object storage stores named objects with metadata through an API.

The modalities are not interchangeable performance tiers. A boot volume needs block semantics, several servers may need a shared filesystem, and durable media or backups may fit object storage. Access pattern, sharing, latency, lifecycle, and recovery determine the service choice.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
