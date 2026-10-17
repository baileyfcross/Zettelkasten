2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# LSTM-Seeded Nelder-Mead Quantum Optimization

The hybrid optimization strategy runs a trained LSTM for ten cost queries and uses its final parameters to initialize Nelder-Mead. The two stages divide the search: the recurrent model selects a promising basin, and the derivative-free simplex method performs local refinement.

Across the noiseless and noisy MaxCut QAOA, spin-glass QAOA, and Hubbard VQE tests, this combination tended to reach the best final cost with lower variance than Nelder-Mead initialized by random guesses or application-specific heuristics. The gain came from the starting point rather than from changing the local optimizer.

The noisy Hubbard result exposes the boundary of the composition. Nelder-Mead sometimes failed to improve the LSTM seed when the cost estimates were noisy, so a better initializer does not by itself solve robust high-precision fine-tuning.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

