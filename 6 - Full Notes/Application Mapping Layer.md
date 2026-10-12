2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Service Layers and Mapping]]

# Application Mapping Layer

An application mapping layer converts between persistence or domain entities and the request and response models used at the service boundary. It makes field selection, renaming, nesting, and relationship projection explicit rather than allowing serialization to reveal the entity shape directly.

Mapping can be handwritten or delegated to a configured library. Either form needs tests because a valid object conversion can still omit a required public value or expose a field that should remain internal.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
