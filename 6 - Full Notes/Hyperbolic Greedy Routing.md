2026-09-06 22:09

Status: #baby

Tags: [[Hyperbolic Network Analytics]]

# Hyperbolic Greedy Routing

Hyperbolic greedy routing forwards a message to the neighbor whose coordinate is closest in [[Hyperbolic Distance]] to the destination. Each node needs only its neighbors' coordinates and the destination coordinate rather than a global routing table.

The method is highly successful in networks whose topology fits a hidden hyperbolic geometry, and its routes can approach shortest paths. It fails at a local minimum when no neighbor is closer, unless the embedding or forwarding rule supplies a recovery mechanism.

# References

[[bigdataincomplexandsocialnetworks.pdf]]
