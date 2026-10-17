2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# Superconducting-Qubit Noise Strength and Susceptibility

Decoherence depends on both the environment's fluctuations and the qubit's response to them. Noise strength describes the fluctuation spectrum of a physical parameter, while susceptibility describes how strongly the qubit Hamiltonian changes when that parameter changes.

The distinction explains why identical environmental noise can affect two devices differently. For slow fluctuations in a control variable $\lambda$, dephasing is set by the product of the noise amplitude and the frequency derivative $\partial\omega_q/\partial\lambda$. At a sweet spot this first-order susceptibility vanishes, even though the environmental noise itself remains.

Noise mitigation can therefore attack either side of the product. Better materials, fabrication, filtering, shielding, and thermalization reduce the source. Circuit design and bias selection reduce susceptibility. Pulse sequences such as [[Dynamical Decoupling Filter Functions]] reshape temporal sensitivity. Treating these as separate levers prevents an observed coherence improvement from being misattributed solely to a quieter environment.

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
