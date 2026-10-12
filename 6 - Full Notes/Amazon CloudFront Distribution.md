2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# Amazon CloudFront Distribution

An Amazon CloudFront distribution delivers content through AWS edge locations and caches eligible responses close to viewers. Its origin can be an S3 bucket, load balancer, web server, or another HTTP endpoint, while cache behaviors determine routing, protocols, and caching rules.

CloudFront reduces origin load and improves content-delivery latency, but cached data needs a deliberate expiration or invalidation strategy. It is a content delivery network, whereas [[AWS Global Accelerator]] improves the network path to regional endpoints without acting as a general-purpose content cache.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
