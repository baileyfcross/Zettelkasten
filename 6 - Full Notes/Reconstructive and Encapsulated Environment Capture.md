2026-09-28 21:33

Status: #baby

Tags: [[Computational Environment Portability]]

# Reconstructive and Encapsulated Environment Capture

Reconstructive environment capture records enough metadata to rebuild an execution context, while encapsulated capture packages a working context itself. Dependency names, versions, operating-system facts, and configuration support reconstruction; a [[Virtual Machine]] or [[Lightweight Execution Environment Package]] preserves selected installed artifacts directly.

The approaches trade transparency, size, and effort. Reconstructive records are easier to query and understand but may fail when dependencies disappear. Encapsulation lowers the burden of direct rerunning but can be opaque and weak for long-term extension. A hybrid can preserve both a runnable environment and an intelligible account of its contents.

# References

[[implementingreproducableresearch.pdf]]
