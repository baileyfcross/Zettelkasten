2026-09-30 23:37

Status: #baby

Tags: [[Windows File Services and High Availability]]

# Storage Replica

Storage Replica copies blocks between Windows Server volumes so a second location maintains a recoverable replica. Synchronous replication waits for both sides and targets low or zero data loss across a sufficiently fast, low-latency link. Asynchronous replication acknowledges local writes first and can span longer or slower links at the cost of possible recent-data loss during a failure.

The destination volume is not an ordinary second writable file share while replication is active; the design protects volume state rather than merging concurrent file edits. Administrators must provide separate log volumes, compatible storage, adequate throughput, and a planned direction for failover and reversal. Replication improves site or server continuity, but accidental deletion or corruption can also be copied, so independent backups and recovery testing remain necessary.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
