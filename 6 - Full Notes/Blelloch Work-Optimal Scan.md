2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# Blelloch Work-Optimal Scan

Blelloch's parallel scan separates accumulation into an upsweep and a downsweep. The upsweep builds partial aggregates along a tree and leaves the total at its root; the downsweep distributes preceding aggregates to fill the cumulative result.

It uses asymptotically optimal total combine work rather than updating every lane at every logarithmic stage. Mapping that tree efficiently to SIMD still requires selecting the participating positions. The book transposes several vectors so each tree level becomes occupied lane-wise work, trading unused arithmetic for shuffle and register costs.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
