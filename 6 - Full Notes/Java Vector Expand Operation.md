2026-10-31 22:04

Status: #baby

Tags: [[Java Vector Masks and Data Movement]]

# Java Vector Expand Operation

The Java vector expand operation is the masked inverse of [[Java Vector Compress Operation|compress]]. It consumes packed input values in order and places them into result lanes whose mask positions are true.

Expand supports dynamic lane refill. In the book's work-piling algorithm, completed Collatz lanes form a mask, new starting values are expanded into those holes, and lanes still in flight retain their state. This raises utilization but also adds packing, bookkeeping, and irregular memory costs.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
