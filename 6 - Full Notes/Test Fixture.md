2026-09-06 20:37

Status: #baby

Tags: [[Web Application Testing]] [[Test-Driven Development and Unit Test Design]]

# Test Fixture

A test fixture is the prepared environment and state used to exercise a unit. It includes the subject, its configured dependencies, and any data needed before the action occurs.

In Angular testing, a component fixture gives the test access to both the component instance and its rendered element. TestBed creates that environment from a testing module configuration.

In xUnit, fixture lifetimes can share costly initialization across tests or classes, but the fixture must not introduce mutable state that makes cases depend on execution order.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
