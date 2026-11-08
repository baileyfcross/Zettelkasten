2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Web API Development]]

# JSON API Error Response

A JSON API error response gives clients a structured body alongside the HTTP status code. It can name the failure, provide a message, and carry details needed to diagnose an invalid identifier or request without returning an HTML error page.

The format should remain consistent across controllers and avoid leaking implementation internals. A filter or shared result type can centralize serialization while each action still chooses the status and safe client-facing context.

For a consumer, the server is otherwise a black box, so the error contract is also a usage and troubleshooting interface. The source groups outcomes into success, client error, and server error, then recommends preserving the corresponding HTTP status while returning a stable code, message, and safe link or detail when more explanation is needed.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]

[[prorestfulapiswithmicronaut.epub]]
