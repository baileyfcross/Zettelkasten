2026-10-31 21:16

Status: #baby

Tags: [[REST API Performance Scaling and Observability]]

# API Load Balancing

API load balancing distributes incoming requests across several service instances. It improves capacity and availability by preventing one instance from receiving all traffic and by routing around an instance that is unavailable.

The book associates load balancing with horizontal scaling and gateway operation. Stateless requests simplify distribution because no hidden session selects one server, while health checks and an appropriate balancing policy determine which instances should receive new work.

# References

[[masteringrestapis.epub]]
