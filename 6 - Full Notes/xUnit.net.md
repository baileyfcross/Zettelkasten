2026-09-06 20:37

Status: #baby

Tags: [[Web Application Testing]] [[C Sharp Functions Diagnostics and Testing]] [[ASP.NET Core API Integration Testing]] [[Test-Driven Development and Unit Test Design]]

# xUnit.net

xUnit.net is a testing framework used to define and execute .NET unit tests. An ASP.NET Core solution can place tests in a separate project that references the application project and its required test dependencies.

The tests arrange controlled data, invoke controller or service behavior, and assert the result. They can be executed from the command line or through an IDE test explorer.

The web-research project uses xUnit facts to arrange an EF Core in-memory context, act through an ASP.NET Core controller, and assert either the returned model or a not-found result. A uniquely named store keeps repeated test runs from sharing unintended state.

The framework also supplies constructor-based setup, disposal, class and collection fixtures, facts for single cases, and theories for data-driven cases, allowing test lifetime to be made explicit.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
