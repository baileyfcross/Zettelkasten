2026-09-06 22:42

Status: #baby

Tags: [[Hadoop and SQL Analytics]]

# NewSQL

NewSQL describes database systems that seek distributed scalability while retaining relational interfaces and transactional guarantees associated with traditional SQL systems. They redesign execution, concurrency, and partitioning rather than simply placing an unchanged database on more machines.

The category is broad; a system's actual consistency, failure behavior, workload assumptions, and scaling limits matter more than the label.

The Spring Boot source uses CockroachDB as a concrete NewSQL system: it speaks the PostgreSQL wire protocol, distributes ordered key ranges across nodes, replicates data across regions, and enforces serializable isolation. Random or time-ordered UUIDs avoid a sequential-key write hotspot, while follower reads trade bounded freshness for local latency and changefeeds carry committed changes to external consumers.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[bigdatamanagementandprocessing.pdf]]
