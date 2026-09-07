2026-09-06 19:44

Status: #baby

Tags: [[Numerical Eigenvalue Methods]]

# Shifted Inverse Power Method

The shifted inverse power method applies inverse iteration to $A-qI$. Its dominant reciprocal corresponds to the eigenvalue of $A$ nearest the chosen shift $q$.

Each step solves $(A-qI)y=x$ and normalizes the result. A good shift targets an interior eigenvalue much more directly than the ordinary [[Power Method]].

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

