2026-09-17 09:48

Status: #baby

Tags: [[Recommender System Evolution]]

# Alternating Least Squares

Alternating least squares fits a matrix-factorization model by repeatedly optimizing one factor matrix while holding the other fixed, then switching roles. Each subproblem becomes a least-squares calculation even though the joint problem is not solved in one step.

The separation supports parallel and distributed computation because many user or item updates can be calculated independently during each phase. Iteration continues until improvement or another stopping criterion is reached.

# References

[[frontiersofdatascience.pdf]]
