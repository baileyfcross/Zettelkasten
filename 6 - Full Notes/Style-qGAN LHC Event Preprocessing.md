2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN LHC Event Preprocessing

The collider observables have very different scales and strongly skewed tails, whereas the generator's expectation-value outputs lie in $[-1,1]$. The pipeline first applies a power transform to each physical feature and then linearly rescales the transformed values into the circuit's output interval.

After generation, the linear scaling and power transform are inverted to recover $s$, $t$, and $y$ in physical coordinates. This classical preprocessing is part of the learned model: it makes the compact circuit's task easier but also means that fidelity depends on how well the transform represents tails and remains invertible over generated values.

Reported KL divergences and correlation plots are computed after returning to the physical variables. Any practical comparison with a classical generator should include the same preprocessing assumptions and the cost of fitting and applying them.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

