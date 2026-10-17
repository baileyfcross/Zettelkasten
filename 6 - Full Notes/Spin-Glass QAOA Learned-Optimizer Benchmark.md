2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Spin-Glass QAOA Learned-Optimizer Benchmark

The Sherrington-Kirkpatrick benchmark applies depth-$3$ QAOA to fully connected Ising Hamiltonians. Couplings and local fields are sampled independently from zero-mean, unit-variance Gaussian distributions, producing a family of dense random optimization landscapes.

The specialist LSTM is trained on 10,000 instances with six to eight qubits and tested on fifty instances with nine to eleven qubits. Its ten-query proposals substantially reduce relative error compared with the alternative initializations, and LSTM-seeded Nelder-Mead supplies the strongest final results in both noiseless and Gaussian-noise tests.

This task shows that learned initialization is not limited to sparse MaxCut graphs. It still relies on the shared depth-$3$ parameterization and on train and test Hamiltonians coming from the same random spin-glass distribution.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

