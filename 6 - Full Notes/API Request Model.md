2026-09-06 20:52

Status: #baby

Tags: [[HTTP API Integration]] [[REST Resource Contracts and Data Handling]]

# API Request Model

An API request model defines the fields accepted by one HTTP operation. It gives model binding and validation a transport-specific target instead of accepting a persistence entity as an unrestricted request body.

A focused request model makes writable fields explicit and can carry validation rules suited to that operation. Separate models may be appropriate when create and update requests have different requirements.

ASP.NET Core binds the request payload into this transport model before application logic runs. Custom and fluent validation can reject an invalid model while leaving persistence entities protected from unrestricted client assignment.

Across the book's frameworks, the accepted request shape is paired with parsing and validation before persistence or business behavior. Treating that shape as an operation-specific contract makes required fields, supported media types, and invalid-input feedback visible to API consumers.

# References

[[aspnetcore3andreact.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[masteringrestapis.epub]]
