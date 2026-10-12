2026-09-28 21:33

Status: #baby

Tags: [[Scientific Workflow Provenance]]

# Workflow Abstraction

Workflow abstraction groups several low-level modules into a higher-level operation. It lets a reader see the conceptual stages of a [[Scientific Dataflow Graph]] without losing the ability to expand a stage and inspect its internal transformations.

The grouping is useful for large experiments whose complete graphs would otherwise overwhelm interpretation. It also supports reuse: a validated subworkflow can become a component in another analysis. Good abstraction hides incidental complexity while preserving inputs, outputs, and dependencies needed for [[Prospective Provenance]] and later reproduction.

# References

[[implementingreproducableresearch.pdf]]
