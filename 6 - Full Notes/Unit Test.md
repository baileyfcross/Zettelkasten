2026-09-05 15:58

Status: #baby

Tags: [[Agile Engineering and Quality]] [[Web Application Testing]] [[C Sharp Functions Diagnostics and Testing]] [[ASP.NET Core API Integration Testing]] [[Test-Driven Development and Unit Test Design]] [[Reproducible Scientific Software]] [[R Software Testing]]

# Unit Test

A unit test is a fast automated check of a small piece of software behavior in controlled conditions. It gives developers immediate evidence about local correctness and supports safe refactoring.

Its narrow scope should isolate external collaborators, arrange deterministic state, and express a specific expectation. Unit tests can be wrong, but independently written tests and implementation are unlikely to reproduce exactly the same error.

Many unit tests form the fast base of a [[Testing Pyramid]], but they cannot prove that assets, systems, platforms, and player-facing behavior work together. Broader integration and playthrough tests supply that evidence.

In a full-stack web application, unit tests can isolate ASP.NET Core controller behavior with [[Moq]] and an [[In-Memory Database Provider]], or isolate Angular components with [[Angular TestBed]], [[Jasmine]], and a [[Test Double]]. [[Arrange-Act-Assert]] keeps setup, execution, and verification distinct.

The web-research chapter emphasizes that test code has a maintenance cost and should prove a useful behavior. Its controller/database example spans multiple components and is therefore described cautiously rather than being labeled a pure single-unit test.

For research software, writing a small test as a scientific component is developed localizes defects near their introduction. Automated execution across supported systems then distinguishes failures caused by a proposed change from failures caused by platform differences, strengthening confidence in the software used to produce scientific results.

In R, testthat gives a unit test a descriptive behavior statement and one or more [[R testthat Expectation|expectations]]. A common value test declares the expected result, computes the actual result, and compares them; error cases should also verify that the intended error occurred. Keeping these tests in files or package test directories makes it easy to rerun them after every function change, turning previously discovered edge cases into regression protection.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[agilegamedevelopment2e.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[implementingreproducableresearch.pdf]]

[[testingrcode.pdf]]
