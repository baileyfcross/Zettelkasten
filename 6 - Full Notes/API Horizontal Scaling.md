2026-10-31 21:16

Status: #baby

Tags: [[REST API Performance Scaling and Observability]]

# API Horizontal Scaling

API horizontal scaling adds more service instances and distributes traffic among them. It contrasts with vertical scaling, which increases the processor, memory, or storage capacity of one machine.

The book favors horizontal scaling for dynamic demand and high availability. The application must externalize shared durable state, coordinate access to dependencies, and make deployments compatible across instances; adding replicas does not by itself remove a database or gateway bottleneck.

# References

[[masteringrestapis.epub]]
