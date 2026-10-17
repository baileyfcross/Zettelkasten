2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Riemannian Natural Gradient

Ordinary [[Gradient Descent]] treats equal coordinate changes as equal distances. On a parameter manifold with local metric tensor $g(\theta)$, an infinitesimal displacement instead has squared length $g_{ij}d\theta_i d\theta_j$, so the coordinate gradient need not point along the steepest decrease at fixed intrinsic distance.

The natural gradient corrects the direction by the inverse metric:

$$\nabla_\theta L=g^{-1}\partial_\theta L,$$

and updates $\theta_{t+1}=\theta_t-\eta_t g^{-1}\partial_\theta L_t$. The metric is local and can change from point to point, so the update adapts to how the parametrization stretches or compresses nearby model states.

This correction does not supply global information about the loss landscape. It replaces a coordinate-dependent local direction with one measured in the geometry chosen for the model.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

