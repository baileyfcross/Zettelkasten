2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Relative Resolvability of Mitigated Cost Values

Relative resolvability compares the shots required to distinguish two points on a noisy cost landscape with and without error mitigation. If $N_{\mathrm{EM}}$ and $N_{\mathrm{noisy}}$ are the required shot counts, the paper defines

$$
\chi=\frac{N_{\mathrm{noisy}}}{N_{\mathrm{EM}}}
=\frac{1}{\gamma}\left(\frac{\Delta C_m}{\Delta\widetilde C}\right)^2,
$$

where $\gamma$ is the [[Error-Mitigation Variance Cost]].

A value $\chi>1$ means mitigation makes the pair easier to resolve, while $\chi<1$ means that variance grows faster than the recovered separation and mitigation is counterproductive for this task. The measure directly matches the repeated comparison primitive used by both gradient-based and gradient-free optimizers.

Improved resolvability is necessary but not sufficient for improved training. It does not require the mitigated landscape to match the ideal landscape, and it does not detect spurious minima or other forms of [[Noise-Driven Cost Landscape Corruption]].

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
