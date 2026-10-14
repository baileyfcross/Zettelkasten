2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Topology-Constrained Circuit Diffusion Masking

Topology-constrained circuit diffusion masking prevents the denoiser from placing gates in selected locations of the circuit tensor. A device coupling map can therefore reserve only placements consistent with available qubit connections, reducing the need to repair forbidden long-range operations after generation.

The mask is applied at inference and does not require retraining the generator. Entire qubit rows or time regions can also be masked to constrain width or length, although the paper finds that directly resizing the tensor gives better accuracy when size control alone is needed.

Hard masks can sharply reduce feasibility. In the reported processor-topology experiment, the fraction of structurally invalid circuits rises from below one percent in ordinary entanglement generation to roughly ninety percent under masking, and more samples are required as the restriction tightens. Masking supplies a constraint mechanism, not a guarantee that the conditioned model can satisfy every constrained request.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
