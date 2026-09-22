2026-09-21 22:12

Status: #baby

Tags: [[Cloud Messaging Caching and Operations Patterns]]

# Static Content Hosting Pattern

Static content hosting serves files such as images, scripts, and video from infrastructure specialized for distributing unchanged bytes, rather than making an application server deliver each file. A content delivery network can place copies near users, and a browser can fetch those assets directly while requesting dynamic pages from the application. This reduces application traffic and improves retrieval latency when asset versioning and cache invalidation are managed clearly.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

