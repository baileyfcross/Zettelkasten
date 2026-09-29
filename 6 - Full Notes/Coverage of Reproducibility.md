2026-09-28 21:33

Status: #baby

Tags: [[Computational Reproducibility Concepts]]

# Coverage of Reproducibility

Coverage of reproducibility identifies how much of an experiment can be repeated. Full coverage includes the complete path from inputs through every transformation to the reported results; partial coverage preserves only selected stages or components.

Coverage is especially important when proprietary data, specialized instruments, or rare hardware prevent an end-to-end rerun. A project can still expose downstream analysis or a scaled component as [[Partial Computational Reproducibility]]. Explicitly naming the covered boundary prevents a successful subworkflow from being mistaken for reproduction of the whole experiment.

# References

[[implementingreproducableresearch.pdf]]
