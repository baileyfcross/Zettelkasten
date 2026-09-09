2026-09-05 15:58

Status: #baby

Tags: [[Agile Engineering and Quality]] [[Web Application Testing]] [[C Sharp Functions Diagnostics and Testing]]

# Unit Test

A unit test is a fast automated check of a small piece of software behavior in controlled conditions. It gives developers immediate evidence about local correctness and supports safe refactoring.

Many unit tests form the fast base of a [[Testing Pyramid]], but they cannot prove that assets, systems, platforms, and player-facing behavior work together. Broader integration and playthrough tests supply that evidence.

In a full-stack web application, unit tests can isolate ASP.NET Core controller behavior with [[Moq]] and an [[In-Memory Database Provider]], or isolate Angular components with [[Angular TestBed]], [[Jasmine]], and a [[Test Double]]. [[Arrange-Act-Assert]] keeps setup, execution, and verification distinct.

The web-research chapter emphasizes that test code has a maintenance cost and should prove a useful behavior. Its controller/database example spans multiple components and is therefore described cautiously rather than being labeled a pure single-unit test.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[agilegamedevelopment2e.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
