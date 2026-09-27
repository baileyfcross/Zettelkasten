2026-09-06 20:52

Status: #baby

Tags: [[Web Performance and Scalability]] [[Cloud Computing Foundations]] [[Software Quality Attributes and Architecture Tradeoffs]]

# Scalability

Scalability is an application's ability to continue serving useful work as demand increases. It depends on how requests consume constrained resources such as server threads, database round trips, memory, and network transfer.

Paging, asynchronous I/O, caching, and fewer queries address different constraints. Load testing shows whether a chosen change improves the behavior that matters rather than merely relocating the bottleneck.

Scaling can be [[Horizontal Scalability|horizontal]], by changing the number of resource instances, or [[Vertical Scalability|vertical]], by increasing the capacity of an individual resource. Cloud [[Rapid Elasticity|elasticity]] automates horizontal scaling in and out so that capacity can follow demand.

As a quality requirement, scalability must identify the growing load and the service levels that remain acceptable; otherwise adding resources may simply move an unmeasured bottleneck.

# References

[[aspnetcore3andreact.pdf]]

[[cloudcomputing_mit.epub]]
[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
