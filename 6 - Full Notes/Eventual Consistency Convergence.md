2026-10-30 17:24

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Eventual Consistency Convergence

Eventual consistency allows service-owned data to be temporarily inconsistent while independent local operations and messages progress toward an agreed business state. A booking can be recorded before the inventory service consumes the corresponding event and updates its own store.

Convergence is an operational promise rather than permission to ignore failures. The system needs a way to detect missing work and bring the participating records back into agreement after delays or service outages.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

