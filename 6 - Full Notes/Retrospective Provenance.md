2026-09-28 21:33

Status: #baby

Tags: [[Scientific Workflow Provenance]]

# Retrospective Provenance

Retrospective provenance records what happened during a particular execution. It can include the modules invoked, concrete input and output artifacts, timing, errors, system details, and the path actually taken through a workflow.

The record distinguishes an executed run from the intended design represented by [[Prospective Provenance]]. It supports diagnosis when two runs differ and supplies evidence for [[Provenance Query and Comparison]]. Because runtime behavior can depart from a plan, reproducibility benefits from preserving both representations rather than assuming the workflow definition alone tells the whole story.

# References

[[implementingreproducableresearch.pdf]]
