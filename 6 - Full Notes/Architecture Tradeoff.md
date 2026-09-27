2026-09-27 11:39

Status: #baby

Tags: [[Software Quality Attributes and Architecture Tradeoffs]]

# Architecture Tradeoff

An architecture tradeoff is an explicit choice that improves one valued property while accepting cost or limitation elsewhere. Horizontal scaling can increase capacity but demand stateless behavior; stronger consistency can simplify reasoning but reduce write distribution; additional security can add latency and interaction.

A responsible tradeoff records the context, alternatives, evidence, and consequence. Without that rationale, a later team may preserve an obsolete constraint or undo a decision whose risk is still present.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
