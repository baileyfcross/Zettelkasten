2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# Lazy Initialization Overhead

Lazy initialization adds a state check to access and may add locking, factory allocation, exception storage, or per-thread state. For cheap values that are almost always used, eager construction can be simpler and faster.

Deferral is most valuable when construction is expensive, access is uncertain, or startup resource pressure matters. Measuring both the initialization path and repeated access avoids treating laziness as a performance improvement independent of workload.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
