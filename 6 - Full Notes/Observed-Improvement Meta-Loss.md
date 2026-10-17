2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Observed-Improvement Meta-Loss

The observed-improvement meta-loss rewards a learned optimizer only when a proposal beats the best cost it has previously observed:

$$\mathcal L(\phi)=\mathbb E_{f,y}\left[\sum_{t=1}^{T}\min\left\{f(\theta_t)-\min_{j<t}f(\theta_j),0\right\}\right].$$

A step that does not set a new historical best contributes zero. A temporary increase is therefore not punished if it enables a later proposal whose improvement exceeds the previous best, giving the optimizer room to explore instead of demanding monotone descent.

The objective is denser than using only the final cost but less conservative than cumulative regret. Cumulative regret rewards reaching a merely adequate point quickly and remaining there, whereas observed improvement keeps rewarding deeper discoveries anywhere in the short query history.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

