2026-09-28 21:33

Status: #baby

Tags: [[Computational Environment Portability]]

# Semipermeable Reproducibility Sandbox

A semipermeable reproducibility sandbox packages most execution dependencies while deliberately leaving selected resources outside. Very large shared datasets, machine-specific pseudo-files, or locally managed storage can remain external while code and ordinary dependencies are redirected into the captured environment.

The boundary reduces package size and avoids copying inappropriate system state, but it must be explicit. External resources become requirements that a reproducer must supply. The design is therefore a controlled compromise between complete encapsulation and practical distribution of a [[Lightweight Execution Environment Package]].

# References

[[implementingreproducableresearch.pdf]]
