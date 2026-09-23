2026-09-22 23:04

Status: #baby

Tags: [[Mobile Data Synchronization and Notifications]]

# Client Cache-Aside Pattern

Client cache-aside makes the mobile application check a local cache before requesting an entity from a remote service. A cache miss triggers the network request and stores the returned value for later reads.

The pattern can keep screens responsive and permit limited offline use, but application code owns freshness and invalidation. A cached result should be presented with an explicit understanding of when it was obtained and how it will be reconciled with server data.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
