2026-09-27 11:51

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Data Consistency

Data consistency describes the guarantees governing which values a read may observe after writes and across replicas. In a distributed store, stronger guarantees typically require more coordination, while weaker models can improve availability, latency, or geographic write capacity.

The correct guarantee depends on business meaning. A temporary delay in a catalog view may be acceptable, while accepting a reservation against stale capacity can violate a critical invariant.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
