2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# Tensor-Network Error Mitigation

Tensor-network error mitigation (TEM) leaves the noisy circuit unchanged and instead constructs a Heisenberg-picture map that applies the inverses of characterized noise layers to the measured observable. The map is built iteratively from the circuit unitaries and inverse-noise channels, each represented as a matrix-product operator.

Exact multiplication makes the bond dimension grow exponentially with depth. TEM therefore compresses the matrix-product operator back to a chosen dimension $\chi$ after each iteration, trading classical contraction cost for [[TEM Bond-Dimension Compression Bias]]. Once the map is contracted with an observable, noisy measurement data are rescaled to estimate the ideal expectation value without sampling altered circuit variants.

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

