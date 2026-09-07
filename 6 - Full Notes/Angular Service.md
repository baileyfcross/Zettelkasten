2026-09-06 20:37

Status: #baby

Tags: [[Front-End Service Design]]

# Angular Service

An Angular service is an injectable class that provides reusable behavior outside a component's presentation logic. Services commonly centralize HTTP access, error handling, retry behavior, or shared state.

A component receives the service through [[Dependency Injection]] rather than constructing it. This makes the component smaller and allows a [[Mock Object|mock service]] to replace network behavior during a unit test.

# References

[[aspnetcore3andangular9_3ed.pdf]]
