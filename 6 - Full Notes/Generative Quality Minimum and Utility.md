2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Generative Quality Minimum and Utility

For the set $G_{sol}$ of valid, unseen generated samples, the minimum value $MV=\min_{x\in G_{sol}}c(x)$ records the best objective value discovered. Averaging this metric across independent runs reduces sensitivity to a particular initialization but does not remove the chance effect within each generated batch.

Utility addresses that weakness by averaging the costs of the lowest-cost 5% of $G_{sol}$. A low utility therefore requires a useful tail of solutions rather than one exceptional sample. The exact five-percent cutoff is a benchmark convention and should be adapted if an application values a different number of candidates.

Minimum value and utility are meaningful only under a declared query or evaluation budget. Otherwise, a model allowed more samples has more opportunities to obtain an extreme minimum, making the comparison inseparable from [[Generative Model Advantage Race Design]].

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

