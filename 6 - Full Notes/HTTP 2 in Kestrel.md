2026-09-27 11:15

Status: #baby

Tags: [[ASP.NET Core API Security and Caching]]

# HTTP 2 in Kestrel

Kestrel can serve HTTP/2 when its endpoint and TLS configuration support protocol negotiation. HTTP/2 carries multiple concurrent streams over one connection and compresses headers, reducing some overhead associated with repeated HTTP/1.1 requests.

Enabling the protocol is a hosting concern rather than a change to REST resource semantics. Clients still exchange HTTP methods, status codes, headers, and representations through the same API contract.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
