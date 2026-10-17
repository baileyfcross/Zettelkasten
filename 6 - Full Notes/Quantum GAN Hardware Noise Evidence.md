2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum GAN Hardware Noise Evidence

The experimental qGAN runs on adjacent qubits chosen from a twelve-transmon linear processor. Across the six characterized qubits, average single-qubit gate fidelity is about $0.9994$, average controlled-$Z$ fidelity about $0.985$, energy-relaxation times about 30-39 microseconds, and readout fidelity is lower for prepared $|1\rangle$ states than for $|0\rangle$ states.

Experimental handwritten digits and gray-scale bars resemble noiseless simulation results, and the gray-scale benchmark yields comparable Frechet Distance distributions. Readout was recalibrated hourly, while gate operations were not recalibrated over four training days. This provides evidence that the small variational circuits and optimizer can tolerate the device's operating drift and noise at the tested scale.

It is not a general robustness result. The study does not present a controlled sweep over noise strength, larger circuits, or matched error-mitigated baselines, and the patch strategy deliberately keeps each circuit small. The evidence supports feasibility on this processor, while scaling remains exposed to deeper state preparation, lower postselection probability, and barren plateaus.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
