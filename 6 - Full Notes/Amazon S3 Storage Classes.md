2026-09-27 18:58

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# Amazon S3 Storage Classes

Amazon S3 storage classes trade storage price, retrieval price, minimum duration, access latency, and availability placement. Standard serves frequent access; Standard-IA and One Zone-IA reduce storage cost for less frequent access; Glacier classes serve archival access with different retrieval times.

Class selection should follow recovery and access requirements rather than age alone. One Zone-IA deliberately stores within one availability zone, while archive classes may impose retrieval delay. Lifecycle rules can move objects when their pattern changes.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
