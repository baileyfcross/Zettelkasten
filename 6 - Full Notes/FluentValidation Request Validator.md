2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Service Layers and Mapping]]

# FluentValidation Request Validator

A FluentValidation request validator expresses rules for a transport model through a dedicated validator type. Rules can check individual fields and compose more involved conditions without placing validation logic inside the controller action.

The validator is part of the input boundary and should report failures before application work changes durable state. Domain invariants still belong in the domain behavior because a request validator cannot protect every non-HTTP caller.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
