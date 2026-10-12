2026-09-28 03:43

Status: #baby

Tags: [[Genome Sequencing Acceleration]]

# BWA Hardware Accelerator

A BWA hardware accelerator implements indexed sequence search in programmable logic. The host prepares or supplies the reference index and query data, while the circuit performs the repeated rank and interval updates required by the search.

The design can pipeline independent queries and use custom memory interfaces, but index-access behavior may become the bottleneck. Performance depends on query length, memory organization, and the amount of work left in software.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

