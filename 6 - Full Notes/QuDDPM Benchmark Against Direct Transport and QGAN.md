2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Benchmark Against Direct Transport and QGAN

The paper compares QuDDPM with quantum direct transport and a generalized QuGAN on the same two-qubit clustered-state ensemble. Each generator receives 720 variational parameters and the same total number of training steps; the QuGAN also has a 96-parameter discriminator.

QuDDPM reaches center-state fidelities near $0.95$ on training and test samples. Direct transport reaches about $0.57$ and $0.47$, while QuGAN reaches about $0.57$ and $0.44$. Their MMD distances also remain roughly two orders of magnitude above QuDDPM's converged value.

The proposed explanation is optimization structure: direct transport is prone to a difficult local minimum, while adversarial training can encounter saddle points and mode collapse. The result supports staged denoising on this small simulation, but the baselines were extended by the authors to a new ensemble-generation task and do not constitute a broad quantum-advantage comparison.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

