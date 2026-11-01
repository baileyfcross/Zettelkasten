2026-10-31 22:04

Status: #baby

Tags: [[SIMD Algorithm Reformulation Patterns]]

# Structure of Arrays for SIMD

A structure-of-arrays layout stores each field of many logical records in its own contiguous array. Corresponding fields from adjacent records can then be loaded into one vector without strided address calculation or [[Java Vector Gather Operation|gather]].

An array of structures instead interleaves fields record by record, which scatters one field through memory. The book represents batches of small recurrence matrices as four component vectors for this reason. The layout is less object-oriented but lets [[Matrix Recurrence Vectorization]] apply the same arithmetic to many matrices lane-wise.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
