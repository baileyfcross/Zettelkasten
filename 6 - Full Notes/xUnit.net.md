2026-09-06 20:37

Status: #baby

Tags: [[Web Application Testing]] [[C Sharp Functions Diagnostics and Testing]]

# xUnit.net

xUnit.net is a testing framework used to define and execute .NET unit tests. An ASP.NET Core solution can place tests in a separate project that references the application project and its required test dependencies.

The tests arrange controlled data, invoke controller or service behavior, and assert the result. They can be executed from the command line or through an IDE test explorer.

The web-research project uses xUnit facts to arrange an EF Core in-memory context, act through an ASP.NET Core controller, and assert either the returned model or a not-found result. A uniquely named store keeps repeated test runs from sharing unintended state.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
