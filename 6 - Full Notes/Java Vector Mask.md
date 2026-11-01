2026-10-31 22:04

Status: #baby

Tags: [[Java Vector Masks and Data Movement]]

# Java Vector Mask

A Java vector mask contains one Boolean value per [[Vector Lane]]. It describes which lanes satisfy a comparison, fall inside an array boundary, or should participate in a subsequent operation.

Masks turn many per-element conditions into data. They can be combined with Boolean operations, counted with `trueCount`, tested with `anyTrue` or `allTrue`, and passed to loads, stores, arithmetic, comparisons, or [[Java Vector Blend Operation|blends]]. An `indexInRange` mask is especially important for safely processing the final partial vector.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
