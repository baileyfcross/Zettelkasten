2026-09-06 22:42

Status: #baby

Tags: [[In-Memory Data Processing]]

# Distributed Software Transactional Memory

Distributed software transactional memory coordinates reads and writes to shared objects as optimistic transactions spanning multiple machines. An operation records its accesses, then commits atomically if concurrent work has not invalidated them.

The model can reduce explicit lock management and its deadlock, livelock, convoying, and composability problems. Conflicts can still waste work, which motivates a [[Transactional Scheduler]].

# References

[[bigdatamanagementandprocessing.pdf]]
