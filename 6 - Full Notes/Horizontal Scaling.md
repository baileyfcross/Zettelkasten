2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]]

# Horizontal Scaling

Horizontal scaling changes the number of application instances rather than the size of one instance. A load balancer distributes requests among several servers, increasing aggregate capacity and allowing one node to fail without necessarily ending the service. The application must handle session state and shared data deliberately; requests tied to one server through sticky sessions limit how evenly load can be spread.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

