2026-09-06 20:37

Status: #baby

Tags: [[Web Application Testing]] [[ASP.NET Core API Integration Testing]] [[Test-Driven Development and Unit Test Design]]

# Moq

Moq is a .NET mocking library used to create controlled substitutes for interfaces and classes in unit tests. A test configures the result a dependency should return, then injects the generated object into the subject.

In ASP.NET Core controller tests, Moq can isolate controller behavior from a production [[Database Context]] or related query dependency.

The book uses configured interface substitutes to return controlled values and keep a unit test focused on the subject's behavior; setups should avoid recreating the full production dependency inside the test.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
