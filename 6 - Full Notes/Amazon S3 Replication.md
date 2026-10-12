2026-09-27 18:58

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# Amazon S3 Replication

Amazon S3 replication copies eligible objects from a versioned source bucket to a versioned destination bucket. Same-Region Replication can support account separation or duplicate processing, while Cross-Region Replication supports geographic and compliance needs.

Replication is configured by rules and permissions and is not a retroactive backup of everything by default. The design should specify which prefixes and versions move, whether deletions replicate, and how destination encryption and ownership are handled.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
