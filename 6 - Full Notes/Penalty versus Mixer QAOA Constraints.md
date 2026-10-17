2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# Penalty versus Mixer QAOA Constraints

Penalty-based QAOA adds energy terms that make infeasible bit strings unattractive while retaining a simple bit-flip mixer. The evolution can still enter the infeasible space, and performance depends on a penalty weight large enough to separate invalid optima without distorting the useful landscape excessively.

Mixer-based enforcement instead begins with a valid state and uses a [[Feasible-Subspace QAOA Mixer]] that cannot violate the constraint. This can shrink the explored space exponentially, but the required mixer may be deeper, more connected, and harder to compile than the standard transverse-field operation.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

