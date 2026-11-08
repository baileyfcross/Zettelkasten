2026-11-06 13:52

Status: #baby

Tags: [[Microservice Testing Deployment and Scaling]]

# Availability Nines

Availability nines express the proportion of time a service is expected to be operational during a year. Each added nine sharply reduces the allowed downtime: 99.9% permits roughly 8 hours 46 minutes annually, 99.99% about 52.5 minutes, and 99.999% about 5 minutes 16 seconds.

The percentage is an end-to-end property rather than a label that can be assigned to one server. DNS, network paths, gateways, service instances, brokers, and data stores all participate in the request chain, so redundancy at only one layer cannot establish the target. The chosen number should come from the business impact of interruption because each additional nine requires more isolation, failover capacity, testing, and operational cost.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
