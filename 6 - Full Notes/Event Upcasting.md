2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Event Upcasting

Event upcasting enriches a stored event for read-side use by consuming the original event, obtaining additional data, and emitting a new event to a dedicated stream. The upcast event does not replace the aggregate's history; it exists to provide reusable enriched input for one or more [[Projection]]s. Because it adds another subscription and dependency, it is more complex than including stable data in the original event and is justified when several read models need the same enrichment.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
