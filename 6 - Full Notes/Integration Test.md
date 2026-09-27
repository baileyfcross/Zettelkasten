2026-09-06 20:52

Status: #baby

Tags: [[Web Application Testing]] [[ASP.NET Core API Integration Testing]]

# Integration Test

An integration test verifies behavior across a real boundary between cooperating components. In an ASP.NET Core application, it can start the web application in a test host and make HTTP requests through routing, model binding, controllers, and configured services.

The broader path provides confidence that individually correct pieces work together. It is slower and requires more setup than a focused unit test, so the two scopes answer different questions.

The book distinguishes unit isolation from integration and functional evidence: the latter can execute a configured ASP.NET Core server and inspect real HTTP or HTML responses to verify cooperating components against the application specification.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[aspnetcore3andreact.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
