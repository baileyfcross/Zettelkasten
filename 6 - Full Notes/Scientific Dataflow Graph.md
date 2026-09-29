2026-09-28 21:33

Status: #baby

Tags: [[Scientific Workflow Provenance]]

# Scientific Dataflow Graph

A scientific dataflow graph represents a computation as modules connected by the data they consume and produce. When represented as a directed acyclic graph, an edge makes a dependency explicit and the structure shows which upstream results must exist before downstream work can run.

The graph turns an implicit script sequence into an inspectable experimental design. Modules can be grouped through [[Workflow Abstraction]], and the same structure can be instantiated with different parameters for a [[Workflow Parameter Sweep]]. Capturing the graph as [[Prospective Provenance]] supports rerunning and comparing the analysis.

# References

[[implementingreproducableresearch.pdf]]
