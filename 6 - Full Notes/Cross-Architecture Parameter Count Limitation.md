2026-10-16 23:13

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]] · [[Quantum Generative Architecture Performance]]

# Cross-Architecture Parameter Count Limitation

The selected QCBM has 256 trainable parameters, compared with 3,456 for the RNN, 25,538 for the Transformer, 87,828 for the VAE, and either 573 or 54,933 for the WGAN depending on the data regime. This makes the quantum model parameter-efficient by a raw count in most comparisons.

Raw parameter count is not a controlled measure of computational cost across fundamentally different models. A quantum rotation, a recurrent weight, an attention parameter, and an adversarial parameter participate in different evaluation graphs and require different optimization, sampling, memory, and hardware resources.

The smaller QCBM count is therefore a descriptive result rather than evidence of quantum advantage. A practical comparison must combine representational quality with training evaluations, circuit shots, classical simulation or hardware time, inference cost, and the resource limits defined by [[Generative Model Advantage Race Design]].

A second performance study reports a similarly striking but still conditional example: a 54-parameter discrete copula QGAN fits the three-dimensional X distribution with KL $0.029$, compared with KL $0.089$ for a 9,475-parameter classical GAN. The quantum and classical parameter counts arise from different circuit blocks, hidden layers, training rules, and runtime costs, while every quantum result is obtained in noiseless state-vector simulation. Parameter efficiency is therefore an empirical architecture property, not a controlled resource advantage.

A quantum invertible neural network supplies a third example. Its roughly 2,000 parameters outperform an equal-sized spline INN and are reported as comparable to classical models with about 6,000 to 16,000 parameters on a five-dimensional collider task. Yet about 1,700 of the QINN parameters belong to a classical inverse-state-preparation network, the comparison uses different model structures, and all quantum results are simulated without hardware measurement costs. The result supports compact hybrid model capacity, not an end-to-end quantum resource advantage.

A QuDDPM comparison controls the generator circuits more tightly: QuDDPM, quantum direct transport, and the QuGAN generator each receive 720 variational parameters and the same total training-step budget on a two-qubit state-ensemble task. QuDDPM performs much better, but its parameters are distributed across 20 sequential denoising circuits, the QuGAN has an additional discriminator, and the models require different measurement and optimization workflows. Equalized raw counts improve the comparison without making computational cost identical, especially in a noiseless simulation.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

[[2023 - A performance characterization of quantum generative models.pdf]]

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

