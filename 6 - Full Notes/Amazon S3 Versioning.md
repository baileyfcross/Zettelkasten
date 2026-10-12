2026-09-27 18:58

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# Amazon S3 Versioning

Amazon S3 versioning preserves multiple states of an object under the same key. Updating an object creates a new version, while an ordinary delete creates a delete marker rather than immediately erasing older versions.

Versioning protects against accidental overwrite and deletion, but retained versions consume storage and need lifecycle management. It also supports replication behavior, because source and destination can identify the exact object version being copied.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
