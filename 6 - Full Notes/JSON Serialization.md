2026-09-06 20:31

Status: #baby

Tags: [[HTTP API Integration]] [[.NET Files Streams and Serialization]]

# JSON Serialization

JSON serialization converts application data into a language-independent text representation that can be placed in an [[HTTP Response]]. Deserialization performs the reverse transformation so a typed client or server object can represent the received values.

An ASP.NET Core endpoint can serialize health or entity results, and an Angular client can consume the same structure through [[Angular HttpClient]]. Naming conventions must agree across the boundary or be configured explicitly.

The Azure projects serialize work items, queue messages, cognitive-service responses, and bot configuration at system boundaries. The bot chapter also uses the .NET Core 3 `JsonDocument` API to select an intent's response array from an embedded JSON resource without constructing a larger object model.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
