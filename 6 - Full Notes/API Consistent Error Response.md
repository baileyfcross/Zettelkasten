2026-10-31 21:16

Status: #baby

Tags: [[REST Resource Contracts and Data Handling]]

# API Consistent Error Response

An API consistent error response gives failures a predictable status code and body shape across endpoints. A client can then distinguish invalid input, missing resources, unauthenticated requests, forbidden operations, and server failures without parsing unrelated message formats.

The book pairs status codes such as 400, 401, 403, 404, and 500 with useful messages and recommends a uniform structure. Feedback should identify what a legitimate client can correct while avoiding stack traces, secrets, or internal implementation details.

# References

[[masteringrestapis.epub]]
