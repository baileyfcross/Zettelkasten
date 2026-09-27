2026-09-27 11:11

Status: #baby

Tags: [[.NET Microservice Communication and Workers]]

# Event Publisher

An event publisher converts an application fact into a message and sends it to the configured event bus. The publisher hides broker-specific connection and serialization mechanics from the service operation that decides an event should be emitted.

Publishing successfully is distinct from completing the local database transaction. A reliable design must define what happens if one succeeds and the other fails rather than assuming the two resources commit atomically.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
