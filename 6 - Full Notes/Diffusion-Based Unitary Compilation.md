2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Diffusion-Based Unitary Compilation

Diffusion-based unitary compilation conditions circuit generation on both a target unitary and a text-specified gate set. A learned unitary encoder supplies the operation condition, while the text condition tells the denoiser which gates may appear, allowing the same operation to be sampled under several native vocabularies.

The benchmark uses previously unseen three-qubit unitaries known to have at least one exact implementation within the allowed gates. From 1,024 generated candidates for each of 3,100 targets, the model finds at least one exact circuit for 92.6 percent of the unitaries and often finds multiple distinct exact implementations. Failed targets still tend to have lower Frobenius distance than random-circuit candidates.

Multiple valid outputs allow later selection for length, gate availability, or another deployment preference, and failed samples can seed a separate refinement method. The result is limited to short, synthetically generated three-qubit circuits; the exponentially growing unitary condition prevents treating it as evidence of large-scale compilation performance.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
