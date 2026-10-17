2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum Batch GAN

A quantum batch GAN uses parameterized quantum circuits for both the generator and discriminator. An index register labels examples in a coherent minibatch, while a feature register carries their latent or image states. The quantum discriminator reduces its output to a real-versus-fake measurement from which averaged adversarial loss information can be estimated.

Unlike the patch architecture, the batch design assumes enough qubits to represent the image features and additional indices. [[Quantum Batch GAN Register Partitioning]] allocates those qubits among index, feature, and ancillary roles, and [[Quantum Batch Gradient Superposition]] describes the proposed training benefit of manipulating the indexed examples together.

The hardware demonstration generates the same $2\times2$ gray-scale bars with a nine-parameter generator and a twelve-parameter quantum discriminator, obtaining scores similar to the patch model. However, it sets the index-register size to zero, giving batch size one. The experiment validates the all-quantum generator-discriminator path but does not experimentally test coherent minibatch acceleration.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
