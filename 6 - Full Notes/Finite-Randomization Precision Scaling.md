2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# Finite-Randomization Precision Scaling

Randomized compiling estimates a tailored-noise expectation value by averaging results from a finite ensemble of logically equivalent circuits. The residual statistical spread of that estimate decreases in proportion to $1/\sqrt{N_{\mathrm{rand}}}$, where $N_{\mathrm{rand}}$ is the number of randomized compilations.

Fixed-parameter simulations under over-rotation, $XI$-rotation, and $IZ$-rotation noise reproduce this scaling. The paper uses 20 randomized circuits for its main finite-ensemble experiments because that count is sufficient to reveal the intended Pauli-stochastic behavior in the simulated cases, not because 20 is a universal hardware optimum.

Increasing the ensemble improves precision but multiplies circuit executions at every noise scale and optimizer step. This is a concrete component of [[Error-Mitigation Variance Cost]] and helps explain [[Optimizer Sensitivity under Finite Randomization]].

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
