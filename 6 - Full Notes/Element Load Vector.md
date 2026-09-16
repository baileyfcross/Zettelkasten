2026-09-16 08:45

Status: #baby

Tags: [[Finite Element Method Foundations]]

# Element Load Vector

An element load vector collects the external influences assigned to an element's nodes. It can represent concentrated nodal forces, equivalent loads from a distributed source, thermal loading, or another problem-specific excitation.

Distributed effects are converted through the element interpolation so they are work-equivalent to nodal quantities. During assembly, element load contributions sharing a global degree of freedom are summed.

# References

[[finiteelementanalysis_aprimer.pdf]]
