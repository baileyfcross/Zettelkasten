2026-09-06 22:42

Status: #baby

Tags: [[In-Memory Data Processing]] [[Entity Framework Core Data Access]]

# In-Memory Database

An in-memory database treats main memory as the primary location for database operations. Its indexes, layouts, and query paths can avoid assumptions inherited from slower block storage.

Durability still requires a strategy such as logging, replication, or periodic snapshots. The performance gain therefore comes from keeping the common execution path in memory, not from pretending failures cannot occur.

EF Core's testing provider supplies a disposable in-process database whose changing state can be isolated for each automated test. The book distinguishes this convenient application test from a narrow unit test and notes that real database operations are otherwise slow and difficult to repeat.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[bigdatamanagementandprocessing.pdf]]
