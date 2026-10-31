2026-10-30 17:24

Status: #baby

Tags: [[Spring Microservice Application Architecture]]

# Spring GraphQL Schema Mapping

A Spring GraphQL application places its schema files in the configured resources location and maps schema fields to controller methods. A query-mapping method resolves a root query, while schema-mapping methods fetch fields of a complex type and arguments bind query parameters.

The runtime invokes a field resolver only when the client requests that field. This preserves the inner service and entity model while adding GraphQL as another driving adapter beside an existing REST controller.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

