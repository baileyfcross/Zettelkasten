2026-09-06 22:09

Status: #baby

Tags: [[Scalable Social Data Processing]]

# Iterative Data Processing

Iterative data processing repeats a computation until a convergence rule or iteration limit is reached. Clustering, graph ranking, linear algebra, and expectation-maximization often reuse the same large inputs during every round.

Launching separate MapReduce jobs for each round adds disk and process overhead. Loop-aware runtimes can cache invariant data, keep workers alive, and exchange only the partial results needed for the next update.

# References

[[bigdataincomplexandsocialnetworks.pdf]]
