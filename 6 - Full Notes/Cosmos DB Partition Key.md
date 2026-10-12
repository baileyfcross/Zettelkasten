2026-09-27 11:51

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Cosmos DB Partition Key

A Cosmos DB partition key selects the value used to distribute documents and requests among logical partitions. A good key spreads storage and throughput while keeping common operations within a useful partition boundary.

Poor distribution can create a hot partition that limits scale despite abundant total capacity. Because changing the key later is disruptive, selection should follow expected access and growth patterns rather than a convenient field name.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
