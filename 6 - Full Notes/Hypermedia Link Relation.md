2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# Hypermedia Link Relation

A hypermedia link relation names the meaning of a link from the current representation, such as retrieving the current resource or invoking an update. The link also supplies the target URI and, in an API representation, may state the relevant HTTP method.

Clients should interpret the relation instead of depending only on a hard-coded target. Stable relation semantics allow the server to change routing details while continuing to advertise the same available transition.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
