2026-09-27 11:07

Status: #baby

Tags: [[ASP.NET Core API Integration Testing]]

# Custom WebApplicationFactory

A custom `WebApplicationFactory` changes the service collection used by an ASP.NET Core test host. It can remove a production registration and replace it with an in-memory database, fake repository, or another controlled dependency before the server begins handling test requests.

Centralizing these substitutions makes the test environment repeatable. Individual tests can focus on observable API behavior while the factory owns infrastructure setup and teardown.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
