2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Multimodal Conditioning for Quantum Circuit Diffusion

Quantum circuit diffusion can combine textual and numerical conditions in one cross-attention context. A frozen CLIP encoder converts prompts such as a desired Schmidt-rank vector or permitted gate set into token embeddings, while a separately trained unitary encoder represents a target unitary matrix.

For compilation, the unitary's real and imaginary parts enter two channels, receive two-dimensional positional encoding, and pass through convolutional and global self-attention blocks. Its flattened output is concatenated with the text tokens and supplied to the denoising U-Net's cross-attention layers. The unitary encoder is trained jointly with the denoiser, while CLIP remains frozen.

This separation lets the text describe how a circuit may be built and the numerical condition describe what operation it must implement. It also creates the exponential input-size limitation discussed in [[Quantum Circuit Diffusion Scalability Limits]], because an n-qubit unitary contains exponentially many entries.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
