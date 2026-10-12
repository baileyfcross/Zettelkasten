2026-09-27 11:11

Status: #baby

Tags: [[.NET Microservice Communication and Workers]]

# Mediator Pattern

The mediator pattern routes a request or notification through a central abstraction instead of making senders call receivers directly. A web controller can submit a command to a mediator while a handler owns the application operation, leaving the controller unaware of the handler's collaborators.

Mediation reduces direct coupling and supports pipeline behaviors, but it does not remove dependencies; it relocates their coordination. Message contracts and handler boundaries should therefore remain explicit and cohesive.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
