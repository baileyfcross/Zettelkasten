2026-09-14 21:00

Status: #baby

Tags: [[Sequence and Network Classification]]

# Relational Feature Construction

Relational feature construction summarizes a node's neighborhood into predictors such as label proportions, attribute aggregates, link counts, or weighted neighbor statistics. These features let an ordinary classifier consume network context.

When neighboring labels are unknown, their current estimates can supply provisional relational features during iterative classification. Leakage must be avoided so that evaluation does not use true test labels indirectly through the graph.

# References

[[dataclassification.pdf]]
