2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Web API Development]]

# HTTP PATCH

HTTP PATCH requests a partial modification of an existing resource rather than replacing its complete representation. It is useful when the client intends to change selected fields without resending every property.

The patch document and supported operations are part of the endpoint contract. The server must validate the requested changes against the current resource and return an appropriate failure when the target or operation is invalid.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
