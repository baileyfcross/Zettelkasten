2026-09-27 11:11

Status: #baby

Tags: [[.NET Microservice Communication and Workers]]

# Integration Event

An integration event is a message published after a fact becomes relevant outside one service boundary. It carries the stable data other services need to react without exposing the producer's internal entities or database model.

Because publishers and consumers can deploy independently, the event is a versioned interservice contract. Its name should describe something that happened, and its schema should evolve with compatibility and duplicate delivery in mind.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
