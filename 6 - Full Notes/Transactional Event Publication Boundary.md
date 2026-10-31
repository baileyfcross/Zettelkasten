2026-10-30 17:24

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Transactional Event Publication Boundary

A transactional event publication boundary attempts to keep a service's local state change and its publication of the corresponding business event in one reliable unit. In the booking example, the event and booking record should not diverge if one succeeds and the other fails.

The book identifies the need without prescribing a particular implementation. The essential boundary is that downstream services must not depend on an event that can silently disappear after the producer commits its local work.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

