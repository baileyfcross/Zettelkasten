2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Foundations and Hardware Portability]]

# Data-Level Parallelism

Data-level parallelism performs the same operation on several independent data elements at once. SIMD hardware realizes it by placing primitive values in vector lanes and applying one instruction across those lanes, as exposed in Java by [[SIMD Vector Computation in Java]].

It differs from [[Instruction-Level Parallelism]], which overlaps distinct machine instructions within one core. A kernel can use both: vector lanes process multiple elements while the processor schedules independent vector instructions concurrently. Regular arrays and uniform arithmetic expose data parallelism naturally; recurrences and divergent branches require algorithm changes first.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
