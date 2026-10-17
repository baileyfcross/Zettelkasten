2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Binary Assignment Penalty Function

A penalty for one unwanted binary assignment can be built as a product of literals. To select the row $(v_1,\ldots,v_n)$, use $x_i$ when $v_i=1$ and $(1-x_i)$ when $v_i=0$; their product is one on that row and zero on every other binary row.

Multiplying by a positive weight raises only the targeted assignment's objective value. Adding such row penalties constructs a truth-table objective, but direct expansion may introduce cubic or higher-order terms that violate the [[Quadratic Unconstrained Binary Optimization|QUBO]] restriction. The formulation must then use weighted cancellation or auxiliary variables.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

