2026-09-06 20:52

Status: #baby

Tags: [[Web Identity and Access Control]]

# Authenticated User

An authenticated user is the identity established after the server validates the credentials or token attached to a request. ASP.NET Core makes that principal and its claims available to controller code.

For a write operation, the server can derive authorship from this validated identity rather than trusting a user identifier supplied in the request body. That binds persisted ownership to authentication evidence.

# References

[[aspnetcore3andreact.pdf]]
