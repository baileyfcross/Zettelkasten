2026-09-28 21:33

Status: #baby

Tags: [[Computational Reproducibility Concepts]]

# Partial Computational Reproducibility

Partial computational reproducibility makes a bounded part of an otherwise unreproducible experiment available for rerunning. A project that depends on a unique instrument, confidential source data, or an enormous computation may still permit reproduction of preprocessing, a smaller-scale test, or the downstream analysis.

The value depends on an explicit boundary. The released component should state its inputs, outputs, and relationship to the unavailable stages so readers can judge what it tests. This approach improves [[Coverage of Reproducibility]] without pretending that the full experiment has been reproduced.

# References

[[implementingreproducableresearch.pdf]]
