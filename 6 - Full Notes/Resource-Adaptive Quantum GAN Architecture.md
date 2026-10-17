2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Resource-Adaptive Quantum GAN Architecture

A resource-adaptive quantum GAN selects its organization according to the relationship between available qubits and output dimension. When the register is too small to represent a whole image conveniently, a [[Quantum Patch GAN]] assembles the output from several circuit-generated probability vectors. When additional qubits are available, a [[Quantum Batch GAN]] assigns some of them to an index register intended to process several examples coherently.

Both designs retain the adversarial game between a generator and a discriminator, but they place the quantum boundary differently. The patch design uses quantum sub-generators with a classical discriminator, whereas the batch design makes both generator and discriminator quantum. Classical optimization still alternates their parameter updates from measured loss information.

Resource adaptation is an architectural proposal rather than a demonstrated scaling advantage. The image experiment validates patchwise generation on at most six adjacent superconducting qubits, while the batch experiment uses no index qubits and therefore a batch size of one. The claimed coherent-batch benefit depends on state-preparation assumptions examined in [[Quantum GAN State-Preparation Bottleneck]].

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
