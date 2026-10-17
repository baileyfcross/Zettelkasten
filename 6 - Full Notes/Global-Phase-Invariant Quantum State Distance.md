2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Global-Phase-Invariant Quantum State Distance

Two normalized state vectors that differ only by a global phase describe the same physical quantum state. The Euclidean norm $\lVert|\psi\rangle-|\phi\rangle\rVert$ does not respect this equivalence and can assign a nonzero distance to physically identical rays.

The local distance derived from one minus fidelity avoids that problem:

$$ds^2=1-|\langle\psi_\theta|\psi_{\theta+d\theta}\rangle|^2.$$

Expanding this expression to second order produces the [[Fubini-Study Metric for Variational Quantum States]]. This construction explains why the metric subtracts the component of a state derivative parallel to the current state.

Global-phase invariance is therefore not a cosmetic property of the loss. It determines which parameter-space directions correspond to genuine physical changes and which are only changes of representation.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

