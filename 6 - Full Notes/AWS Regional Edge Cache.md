2026-09-27 18:58

Status: #baby

Tags: [[AWS Global Infrastructure and Support]]

# AWS Regional Edge Cache

An AWS regional edge cache is an intermediate CloudFront caching layer between many edge locations and an origin. Content absent from a local edge can be found in the larger regional cache, reducing how often the request reaches the origin.

This hierarchy gives less frequently requested objects a longer useful cache life than a small edge cache alone. Cache policy and time to live still govern freshness, so the layer reduces origin traffic without becoming the authoritative data store.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
