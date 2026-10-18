2026-10-18 15:54

Status: #baby

Tags: [[Microservice Testing Deployment and Scaling]]

# Microservice Horizontal Pod Autoscaling

Microservice horizontal pod autoscaling changes the desired number of Kubernetes pod replicas from observed load, such as CPU use or another configured metric. It applies [[Horizontal Scaling]] to one independently deployed service so capacity can grow and contract with that service's demand.

The threshold and replica limits must reflect the workload rather than merely react to any metric spike. New pods take time to start and become ready, while downstream databases, queues, or services may remain fixed bottlenecks. Readiness checks prevent traffic from reaching an initializing replica, and resource requests give the scheduler and utilization calculation a meaningful basis. Autoscaling is a feedback controller, not a substitute for capacity planning or stateless design.

# References

[[artofdecodingmicroservices.epub]]
