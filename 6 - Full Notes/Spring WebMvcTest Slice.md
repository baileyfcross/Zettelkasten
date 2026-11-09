2026-11-08 16:45

Status: #baby

Tags: [[Spring Application Testing]]

# Spring WebMvcTest Slice

`@WebMvcTest` loads the Spring MVC layer needed to test controller mappings, validation, argument resolution, and serialization without starting the full application or connecting to its database. Collaborating services can be supplied as test bean overrides so the test remains focused on HTTP behavior.

The slice is useful for verifying status codes, headers, request validation, and the shape of a controller response. It does not prove that the persistence or remote-client adapters work with the controller; that belongs in narrower adapter tests or a smaller number of full-context integration tests.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
