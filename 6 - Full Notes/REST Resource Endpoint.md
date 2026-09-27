2026-09-06 20:52

Status: #baby

Tags: [[HTTP API Integration]] [[REST Architectural Constraints and Hypermedia]]

# REST Resource Endpoint

A REST resource endpoint combines a resource-oriented URI with an HTTP method to express an operation. Collection and item routes provide stable addresses, while GET, POST, PUT, and DELETE communicate the broad request intent.

The endpoint contract includes more than a route: request fields, validation, response representation, status codes, authentication, and error behavior must agree with the consuming client.

Resource-oriented routes distinguish a collection from an individual member and combine that identity with standard HTTP method semantics. The design avoids embedding implementation method names in the public URI.

# References

[[aspnetcore3andreact.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
