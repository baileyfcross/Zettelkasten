2026-10-30 17:24

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring HATEOAS Representation

A Spring HATEOAS representation combines resource state with links that identify available next actions. A client discovers transitions from the response rather than relying entirely on out-of-band route knowledge.

The set of links can vary with resource state; for example, a purchase link can disappear when stock is unavailable. Spring HATEOAS supplies representation and link-building support so the controller can expose this hypermedia contract deliberately.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

