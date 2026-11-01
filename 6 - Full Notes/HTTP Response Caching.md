2026-09-27 11:15

Status: #baby

Tags: [[ASP.NET Core API Security and Caching]] [[REST API Performance Scaling and Observability]]

# HTTP Response Caching

HTTP response caching allows a client or intermediary to reuse a previously transferred representation when the response's cache directives permit it. This can remove application work and network transfer without changing the resource's public address.

Caching is safe only when freshness, variation, and privacy are described correctly. Personalized or rapidly changing responses need restrictive directives, while stable public responses can usually tolerate broader reuse.

The book places caches at several layers: clients and proxies can obey HTTP directives, application code can cache frequent data in Redis or Memcached, and a gateway can cache repeated upstream responses. Each location reduces different work, so invalidation and the sensitivity of the cached representation must match that layer.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[masteringrestapis.epub]]
