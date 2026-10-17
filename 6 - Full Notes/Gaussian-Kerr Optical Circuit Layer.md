2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Gaussian-Kerr Optical Circuit Layer

The state-preparation ansatz alternates a generic single-mode Gaussian transformation with a non-Gaussian Kerr interaction. One layer has the form

$$K(\kappa)G(\gamma,\phi,\zeta)=K(\kappa)D(\gamma)R(\phi)S(\zeta),$$

where $S$ squeezes, $R$ rotates phase, $D$ displaces, and $K$ applies a photon-number-dependent nonlinear phase.

The squeezing amplitude $\zeta$ and displacement amplitude $\gamma$ are complex, while the phase $\phi$ and Kerr strength $\kappa$ are real. Counting real and imaginary parts separately gives six real degrees of freedom per single-mode layer.

Gaussian operations provide affine-like transformations of continuous-variable states, whereas the Kerr gate supplies non-Gaussian nonlinearity. The mixed parameter types are the direct reason that the optimizer requires a complex natural-gradient formalism.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

