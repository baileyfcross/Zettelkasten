2026-09-27 11:15

Status: #baby

Tags: [[ASP.NET Core API Security and Caching]]

# IDistributedCache Abstraction

`IDistributedCache` is ASP.NET Core's key-based abstraction for a cache shared across application instances. It supports storing, retrieving, refreshing, and removing byte or string values while allowing the configured provider to be changed independently of most application code.

The abstraction does not define application-level serialization or invalidation. Callers must design stable keys, encode values, choose expirations, and handle a missing or unavailable cache without corrupting the source of truth.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
