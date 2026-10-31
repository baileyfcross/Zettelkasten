2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Onion and Hexagonal Architecture Complementarity

Hexagonal and onion architecture describe complementary views of the same separation. Hexagonal architecture emphasizes ports and adapters at multiple system boundaries, while onion architecture emphasizes concentric layers and inward dependency direction.

Driving and driven adapters sit at the outer onion boundary and connect through application services to domain services and entities. A REST or GraphQL port can change at the edge while the same inner services and domain objects continue to serve both interfaces.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

