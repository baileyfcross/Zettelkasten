2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Noise Robustness of Learned Quantum Optimization

The optimizer was tested both with exact simulated expectations and with independent Gaussian noise of variance $0.05$ added to every cost estimate. Across all three problem classes, the LSTM still found a strong approximate minimum within ten queries, and its seed generally improved the consistency of later local search.

This is evidence of robustness to noisy scalar readout, not a full hardware-noise demonstration. The circuits themselves were simulated without gate errors or a physical readout channel, and the Gaussian perturbation does not reproduce temporal drift, bias, correlations, or parameter-dependent device noise.

The distinction prevents a useful numerical stress test from being read as proof of hardware readiness. In particular, the noisy Hubbard case shows that even when initialization remains good, conventional local refinement can stall on imprecise cost values.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

