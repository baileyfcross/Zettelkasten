2026-10-18 15:54

Status: #baby

Tags: [[Microservice Architecture Adoption]]

# Microservice Service Granularity

Microservice service granularity is the choice of how much cohesive business behavior belongs behind one service boundary. A useful service is small enough to own one capability and change independently, but large enough that routine work does not require a long chain of remote calls.

There is no useful target based only on code size. A boundary should instead be evaluated by its business responsibility, data ownership, team ownership, communication frequency, and deployment needs. Splitting too far creates [[Microservice Boundary Over-Segmentation]]; grouping unrelated responsibilities creates [[Microservice Boundary Under-Segmentation]]. Granularity should be revised as the domain becomes better understood rather than fixed by an early enthusiasm for smaller services.

The source distinguishes packaging milestones along that continuum. A macroservice can place separate JAR modules inside one deployable archive, while a mini service can create several deployables that still share a node or dependencies. Full microservice granularity requires independent development, deployment, release, and data ownership rather than merely more files.

The practical architecture source treats granularity as an explicit quality trade-off rather than a rule that smaller is always better. A boundary may improve selective scaling or fault isolation while increasing remote calls and outer-architecture work. A [[Domain-Centric Microservice Partition]] is therefore stronger evidence for a split than a target line count or a desire to maximize service quantity.

# References

[[artofdecodingmicroservices.epub]]
[[javamicroservicesandcontainersinthecloud.epub]]
[[practicalmicroservicesarchitecturalpatterns.epub]]
