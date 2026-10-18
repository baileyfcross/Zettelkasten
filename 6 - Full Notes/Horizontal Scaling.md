2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]] [[Software Quality Attributes and Architecture Tradeoffs]] [[Microservice Testing Deployment and Scaling]]

# Horizontal Scaling

Horizontal scaling changes the number of application instances rather than the size of one instance. A load balancer distributes requests among several servers, increasing aggregate capacity and allowing one node to fail without necessarily ending the service. The application must handle session state and shared data deliberately; requests tied to one server through sticky sessions limit how evenly load can be spread.

Cloud platforms can add replicas dynamically, but the architecture must remove or externalize instance-local state and ensure downstream databases or services can absorb the increased concurrency.

For microservices, horizontal scaling can be applied to one capability rather than the whole application. That selectivity is useful only when a load balancer or queue distributes work among interchangeable instances and service discovery tracks the changing replica set. Scaling callers without measuring downstream saturation can simply transfer the bottleneck to another service or database.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]
[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
[[artofdecodingmicroservices.epub]]
