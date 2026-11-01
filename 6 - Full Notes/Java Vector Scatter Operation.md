2026-10-31 22:04

Status: #baby

Tags: [[Java Vector Masks and Data Movement]]

# Java Vector Scatter Operation

A Java vector scatter stores lanes to memory positions supplied by an index map. It can place ranked elements directly into their merged positions or cache results whose destinations are not contiguous.

Scatter should be used cautiously. Some indices may leave output holes, repeated indices create write conflicts with an unspecified winner, and arbitrary addresses lose the efficiency of sequential stores. The book's merge benchmarks show indexed writes can be dramatically slower than scalar merging even when the placement calculation is vectorized.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
