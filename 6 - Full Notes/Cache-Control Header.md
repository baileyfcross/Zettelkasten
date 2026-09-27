2026-09-27 11:15

Status: #baby

Tags: [[ASP.NET Core API Security and Caching]]

# Cache-Control Header

The HTTP `Cache-Control` header carries directives that describe whether and for how long a response may be reused. Directives can distinguish shared from private storage, set freshness lifetimes, require revalidation, or prohibit storage.

These directives are part of the API's observable semantics. An overly broad policy can disclose user-specific data or serve stale state, while an unnecessarily restrictive policy forfeits useful caching.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
