2026-09-27 11:51

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Cosmos DB Consistency Level

A Cosmos DB consistency level selects the visibility guarantee for replicated data, ranging from strong consistency through bounded staleness, session, consistent prefix, and eventual consistency. The choice affects latency, availability, and how quickly a client observes writes across regions.

The level is an application contract, not merely a performance switch. A team should choose it from the ordering and freshness its business operations require.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
