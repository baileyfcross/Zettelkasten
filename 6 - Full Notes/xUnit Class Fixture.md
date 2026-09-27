2026-09-27 11:46

Status: #baby

Tags: [[Test-Driven Development and Unit Test Design]]

# xUnit Class Fixture

An xUnit class fixture creates one shared fixture instance for the tests in a class and injects it through the test-class constructor. It is useful when preparing a resource is costly and the cases can safely use the same initialized object.

Shared lifetime introduces a state boundary. Tests must not make fixture mutations that create ordering dependence, and cleanup belongs in the fixture's disposal behavior when it owns resources.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
