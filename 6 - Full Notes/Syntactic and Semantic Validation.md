2026-09-28 21:33

Status: #baby

Tags: [[Semantic Scientific Computation]]

# Syntactic and Semantic Validation

Syntactic validation checks that data conform to a formal structure; semantic validation checks that the contained values, references, units, and domain relationships make scientific sense. A file can be grammatically readable yet still refer to a missing entity or express an impossible quantity.

Validation should occur before, during, and after computation. Invalid inputs should stop rather than produce plausible-looking output, and results can be compared with expected values within stated numerical tolerances. Embedded assertions make these checks part of a [[Semantic Scientific Document]] instead of an informal promise in external documentation.

# References

[[implementingreproducableresearch.pdf]]
