2026-10-07 17:18

Status: #baby

Tags: [[R Programming Environment]]

# R Apply Function Family

The R apply function family evaluates one function across parts of a structured object. apply works across selected margins of an array, lapply returns one list element per input element, and sapply attempts to simplify those results into a vector or array.

The family can express independent repeated calculations without explicit loop bookkeeping. It does not automatically make an inefficient function fast, and simplification must be checked because irregular results may remain a list or be coerced into a shape different from what downstream code expects.

# References

[[statisticalcomputingincplusplusandr.pdf]]
