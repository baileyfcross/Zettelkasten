2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Clustered-State Benchmark

The central QuDDPM benchmark generates a distribution of two-qubit states concentrated near $|0,0\rangle$. It uses 20 diffusion steps, one ancilla, depth-six reverse circuits per step, 100 training states, and 720 variational parameters.

The target ensemble has mean center-state fidelity $0.977\pm0.014$. Generated training and test ensembles reach approximately $0.947\pm0.070$ and $0.948\pm0.061$, while the final MMD distance is about $0.002$. Training traces follow the forward-diffusion trajectory, with temporary spikes when each newly initialized reverse circuit is introduced.

The result shows successful ensemble reconstruction and held-out agreement in a noiseless two-qubit simulation. It does not establish performance on hardware or on high-dimensional state distributions.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

