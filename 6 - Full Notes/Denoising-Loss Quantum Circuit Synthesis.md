2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Denoising-Loss Quantum Circuit Synthesis

Denoising-loss quantum circuit synthesis trains on valid circuit tensors corrupted by Gaussian noise. At a randomly selected diffusion step, the model predicts the added noise and minimizes squared error between the true and predicted noise, allowing the clean circuit representation to be recovered progressively.

The objective does not compare a generated circuit's output state or unitary with the requested quantum result. It therefore avoids repeatedly simulating quantum dynamics inside the training loss, which is the paper's main computational distinction from methods trained directly on circuit fidelity or target-state error.

The saving is limited to training-time evaluation. [[Quantum Circuit Diffusion Dataset Curation]] must still compute the entanglement label or unitary condition for each source circuit, and generated candidates may still require simulation for verification. The reported models use a 1,000-step DDPM training process, conditional dropout for classifier-free guidance, input perturbation, and reduced-step sampling after training.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
