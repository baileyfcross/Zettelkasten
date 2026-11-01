2026-10-31 22:04

Status: #baby

Tags: [[Java Vector Masks and Data Movement]]

# Java Vector Slice Operation

The Java vector slice operation conceptually concatenates two vectors and extracts a vector-length window beginning at a specified lane offset. It can shift values while carrying elements across the boundary between a previous and current vector.

In the book's sorted-duplicate removal, slice aligns every element with its predecessor, including the first lane's predecessor from the prior block. The alternative is an overlapping memory load starting one element earlier. Slice avoids that extra access, but its relative cost depends on the processor and must be benchmarked.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
