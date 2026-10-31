2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Onion Architecture Dependency Direction

Onion architecture directs coupling inward: outer layers depend on inner layers, while inner layers remain unaware of the outer layers. Infrastructure and delivery mechanisms occupy the outside; application services, domain services, and entities become progressively more central.

This direction preserves an independent object model at the center. A database or web framework can be replaced because it depends on inner contracts, whereas the domain does not import the outer technology that currently realizes them.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

