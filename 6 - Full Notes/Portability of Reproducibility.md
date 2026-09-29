2026-09-28 21:33

Status: #baby

Tags: [[Computational Reproducibility Concepts]]

# Portability of Reproducibility

Portability of reproducibility describes how far an experiment can move from its original execution setting. The weakest case reruns only in the original environment; stronger cases work on similar systems and then on materially different systems.

Hard-coded paths, unavailable libraries, operating-system assumptions, and specialized hardware can reduce portability even when the complete code is available. [[Computational Environment Portability]] addresses these constraints with dependency records, packages, and virtual environments. Portability is distinct from [[Depth of Reproducibility]] because a deeply documented experiment may still depend on an irreplaceable platform.

# References

[[implementingreproducableresearch.pdf]]
