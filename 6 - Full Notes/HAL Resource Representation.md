2026-10-30 17:24

Status: #baby

Tags: [[Spring Microservice Application Architecture]]

# HAL Resource Representation

Hypertext Application Language represents a resource's ordinary state together with links and embedded resources in JSON or XML. Each link has a target URI and a relation name, with optional metadata for concerns such as content negotiation or deprecation.

HAL gives a HATEOAS response a predictable shape rather than inventing a different link convention for every API. The resource state remains distinct from the hypermedia controls that describe related resources and possible transitions.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

