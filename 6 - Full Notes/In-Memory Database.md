2026-09-06 22:42

Status: #baby

Tags: [[In-Memory Data Processing]]

# In-Memory Database

An in-memory database treats main memory as the primary location for database operations. Its indexes, layouts, and query paths can avoid assumptions inherited from slower block storage.

Durability still requires a strategy such as logging, replication, or periodic snapshots. The performance gain therefore comes from keeping the common execution path in memory, not from pretending failures cannot occur.

# References

[[bigdatamanagementandprocessing.pdf]]
