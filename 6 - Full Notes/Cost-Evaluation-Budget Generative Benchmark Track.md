2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Cost-Evaluation-Budget Generative Benchmark Track

Track T2 fixes the number of unique, valid, unseen solutions whose costs may be evaluated. A model can sample repeatedly until it obtains at most $Q_u$ qualifying solutions, so duplicate, invalid, and memorized outputs do not consume the scarce objective-evaluation budget.

The paper sets $Q_u=100$ and uses this track as a proxy for molecule or drug-design problems in which validating a distinct candidate may require an expensive experiment. If a model suffers severe mode collapse and never reaches the target, its metrics are computed using the smaller number it actually produces.

This rule favors models that can concentrate on useful candidates even if they require many raw draws. It therefore answers a different question from [[Sampling-Budget Generative Benchmark Track]], and the winning classical or quantum architecture can change when the bottleneck changes.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

