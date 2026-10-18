2026-10-18 15:54

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Backend for Frontend Pattern

The backend for frontend pattern gives each client type a dedicated backend that adapts microservice capabilities to that client's needs. A web application, mobile application, and external partner can receive different payload shapes, aggregation, authentication flow, and latency tradeoffs without forcing one general gateway to encode every presentation concern.

The dedicated backend can reduce client round trips and shield the client from internal service topology. It also creates more deployable components and can duplicate logic across frontends. Shared business rules should remain in the owning services, while the BFF concentrates on client-specific orchestration and transformation. The pattern is a specialization of [[Microservice API Gateway]], not a license to move domain ownership to the edge.

# References

[[artofdecodingmicroservices.epub]]
