2026-09-27 18:58

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# Amazon S3 Transfer Acceleration

Amazon S3 Transfer Acceleration routes uploads and downloads through nearby AWS edge locations and the AWS backbone toward the destination bucket. It can improve long-distance transfer performance when clients are geographically far from the bucket region.

The feature uses an accelerated endpoint and adds cost, so performance should be measured for the actual path and object sizes. Nearby clients or already efficient routes may receive little benefit.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
