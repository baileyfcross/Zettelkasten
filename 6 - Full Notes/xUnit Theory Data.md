2026-09-27 11:07

Status: #baby

Tags: [[ASP.NET Core API Integration Testing]]

# xUnit Theory Data

An xUnit theory runs the same test logic for multiple supplied data rows. Each row becomes a separate case, allowing an API rule to be checked across valid, missing, malformed, or boundary inputs without duplicating the request and assertion structure.

Theory data is most useful when every row tests one coherent behavior. If rows require unrelated setup or assertions, separate tests communicate the contract more clearly.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
