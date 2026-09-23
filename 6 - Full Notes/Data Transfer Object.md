2026-09-06 20:37

Status: #baby

Tags: [[Front-End Service Design]] [[ASP.NET Core Web API Development]] [[Application Commands and Service Boundaries]]

# Data Transfer Object

A data transfer object is a class shaped specifically for data sent across an application boundary. It can include values required by the client while omitting entity properties that should not be serialized or exposed.

Using a DTO preserves [[Separation of Concerns]] between persistence and presentation. It also gives tests a named, typed result, whereas a quick projection to an anonymous type is less reusable outside the method that created it.

In a domain-centered application, request DTOs form the [[Public API Contract]] rather than becoming domain objects. They favor serialization-friendly primitive values and carry data across the transport boundary; the [[Application Layer]] converts them into an [[Application Command]] or domain-specific values before invoking behavior. This prevents HTTP and serializer requirements from leaking into the [[Domain Model]].

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-ondomain-drivendesignwithnetcore.pdf]]
