2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# No-Go Theorem for One-Sided Parameter-Shift Rules

No universal exact parameter-shift rule can recover $f'(\theta)$ from only the two values $f(\theta)$ and $f(\theta+\gamma)$ for every two-eigenvalue circuit expectation value and every admissible parameter point. The same impossibility applies to a backward rule.

The proof constructs two valid quantum cost functions that agree at both supplied evaluation points but have different derivatives at the unshifted point. Any function receiving only those identical pairs would have to return the same answer for both costs, so it cannot be exact for both.

An exact one-sided rule would have reduced a full $n$-parameter gradient from the $2n$ evaluations of the [[Centered Parameter-Shift Rule]] to $n+1$ by reusing the unshifted cost. The theorem shows that this saving is unavailable without extra assumptions, evaluations, or information about the particular cost function.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

