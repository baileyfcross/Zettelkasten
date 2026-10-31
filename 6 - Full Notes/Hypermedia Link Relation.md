2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# Hypermedia Link Relation

A hypermedia link relation names the meaning of a link from the current representation, such as retrieving the current resource or invoking an update. The link also supplies the target URI and, in an API representation, may state the relevant HTTP method.

Clients should interpret the relation instead of depending only on a hard-coded target. Stable relation semantics allow the server to change routing details while continuing to advertise the same available transition.

HAL formalizes the link as a target URI plus a `rel` name and optional properties for concerns such as content negotiation or deprecation. A representation can also contain embedded resources, keeping resource state distinct from the controls that connect it to related application states.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[javamicroservicesandcontainersinthecloud.epub]]
