2026-10-03 22:06

Status: #baby

Tags: [[Transportation and Transshipment Optimization]]

# Initial Basic Feasible Transportation Solution

An initial basic feasible transportation solution satisfies every supply and demand requirement before optimality is tested. For a balanced $m$-origin, $n$-destination model, it should contain $m+n-1$ independent basic cells, allowing zero basic allocations when degeneracy requires them.

Construction rules differ in how much cost information they use. The [[Northwest Corner Method]] ignores cost, row and column minima use local costs, and the [[Vogel Approximation Method]] uses penalties to seek a stronger starting plan.

# References

[[optimizationusinglinearprogramming.pdf]]

