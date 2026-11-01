2026-10-31 22:04

Status: #baby

Tags: [[Java Vector Masks and Data Movement]]

# Java Vector Compress Operation

The Java vector compress operation keeps lanes selected by a mask and packs their values contiguously at the beginning of the result vector while preserving order. The mask's true count gives the number of meaningful packed values.

Compress turns filtering into bulk data movement. The book uses it to write unique values from a sorted array and to pack accepted pseudorandom candidates after rejection sampling. Its speed depends strongly on native instruction support: processors without an efficient compress instruction can lose to scalar code.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
