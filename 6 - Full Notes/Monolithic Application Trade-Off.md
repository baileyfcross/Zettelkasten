2026-10-18 15:54

Status: #baby

Tags: [[Microservice Architecture Adoption]]

# Monolithic Application Trade-Off

A monolithic application packages its presentation, business logic, and data access into one deployable unit. That arrangement can simplify initial development: calls remain inside one process, one deployment changes the whole application, and related data can share an ordinary transaction. For a small or still-uncertain domain, those properties can make a monolith easier to understand and operate than a distributed design.

The same unity becomes a constraint when parts of the system need different release schedules, scaling profiles, or technologies. The whole application may need to be rebuilt and redeployed for a local change, and a defect or resource bottleneck can affect the entire unit. These pressures motivate [[Thoughtful Monolith-to-Microservices Migration]], but they do not by themselves make decomposition worthwhile; the replacement also incurs [[Microservice Operational Complexity]].

# References

[[artofdecodingmicroservices.epub]]
