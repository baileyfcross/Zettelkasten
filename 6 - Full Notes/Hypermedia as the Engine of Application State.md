2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# Hypermedia as the Engine of Application State

Hypermedia as the Engine of Application State means a response includes links or controls that describe operations available from the represented state. A client follows those advertised transitions instead of constructing every future URI from out-of-band knowledge.

The server can expose a relation, target, and method for actions such as retrieving, updating, or deleting a resource. The relation carries semantic meaning; the target can evolve while a client continues to navigate through the representation.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
