2026-10-18 15:54

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Bounded Context to Microservice Mapping

Bounded context to microservice mapping uses a domain boundary as a candidate deployment boundary. Within a [[Bounded Context]], one model and language remain consistent; a microservice can own that model, the behavior built from it, and the data that records it.

The mapping is a design guide rather than a rule that every context must immediately become one process. The team must still consider communication frequency, ownership, scale, and operational cost. When models with different meanings are forced into one service, changes become coupled; when one coherent model is scattered across many services, ordinary behavior becomes a distributed workflow. A successful mapping keeps translations explicit at the service interface and preserves [[Microservice Data Ownership]].

# References

[[artofdecodingmicroservices.epub]]
