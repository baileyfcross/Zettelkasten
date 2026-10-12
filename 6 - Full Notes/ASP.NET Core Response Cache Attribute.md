2026-09-27 11:15

Status: #baby

Tags: [[ASP.NET Core API Security and Caching]]

# ASP.NET Core Response Cache Attribute

The ASP.NET Core `ResponseCache` attribute declares cache-related response metadata for a controller or action. Its settings can establish duration, location, variation, or no-store behavior that ASP.NET Core translates into HTTP cache headers.

The attribute expresses policy at the endpoint, but consumers and intermediary caches still decide how to apply valid HTTP directives. It should reflect the sensitivity and change rate of the returned representation.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
