2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Web API Development]]

# Related Resource Endpoint

A related-resource endpoint exposes a relationship through a route such as a parent resource followed by the related collection or member. The route makes the relationship visible in the HTTP interface instead of requiring the client to infer database joins.

The service layer and repository must enforce that the parent exists and that returned children actually belong to it. Response models can then represent the related data without exposing the persistence model directly.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
