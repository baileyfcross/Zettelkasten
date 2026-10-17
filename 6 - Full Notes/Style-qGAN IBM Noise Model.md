2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN IBM Noise Model

The appendix simulates the hardware circuit with an IBM calibration-derived noise model containing readout error, energy relaxation, dephasing, gate errors, and gate durations. The model is applied to the same one-layer style-qGAN used on `ibmq_santiago`, without noise mitigation.

For $10^5$ generated events, the noisy simulation produces KL divergences of $1.379$, $0.339$, and $0.172$ for $s$, $t$, and $y$. It reproduces much of the qualitative hardware degradation and many two-dimensional density ratios remain near one, but individual observables differ substantially from both noiseless simulation and device data.

The result shows that a simplified local noise model can explain broad loss of fidelity while remaining an imperfect predictor of a week-long hardware run whose calibration may drift. It is a diagnostic comparison, not a validation that calibration metrics fully capture circuit-level behavior.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

