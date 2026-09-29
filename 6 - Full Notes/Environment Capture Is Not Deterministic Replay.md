2026-09-28 21:33

Status: #baby

Tags: [[Computational Environment Portability]]

# Environment Capture Is Not Deterministic Replay

Capturing an execution environment does not guarantee that a later run will reproduce every bit of output. Random inputs, thread schedules, external network state, floating-point differences, and sensitive numerical branches may vary even when the code and packaged dependencies are unchanged.

Environment capture preserves influential context and narrows the search for differences; deterministic replay would also have to control nondeterministic events and external state. For chaotic computations, an appropriate target may instead be [[Ensemble Reproducibility for Chaotic Computation|similar aggregate behavior]] within stated tolerances.

# References

[[implementingreproducableresearch.pdf]]
