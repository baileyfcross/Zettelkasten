2026-10-31 21:16

Status: #baby

Tags: [[REST Resource Contracts and Data Handling]]

# REST Composite Resource

A REST composite resource returns related data from several underlying sources as one cohesive representation. The book's example combines a user profile with recent posts so the client can obtain an immediately useful view in one request.

Composition reduces round trips and client-side joining, but it transfers assembly work to the server and can produce oversized responses. A useful composite groups data that clients commonly need together while keeping optional or unbounded relationships outside the default payload.

# References

[[masteringrestapis.epub]]
