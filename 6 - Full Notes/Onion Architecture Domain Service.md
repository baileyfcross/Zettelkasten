2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Onion Architecture Domain Service

An onion-architecture domain service holds reusable business logic that spans multiple entities and does not naturally belong to one entity. It receives domain objects, performs the operation, and can coordinate other domain services while remaining inside the technical application boundary.

The service differs from an application service that translates protocols or formats. Domain services express business behavior; application services connect outer adapters to that behavior.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

