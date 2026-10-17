2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]] · [[Quantum Generative Architecture Performance]]

# Cross-Architecture Parameter Count Limitation

The selected QCBM has 256 trainable parameters, compared with 3,456 for the RNN, 25,538 for the Transformer, 87,828 for the VAE, and either 573 or 54,933 for the WGAN depending on the data regime. This makes the quantum model parameter-efficient by a raw count in most comparisons.

Raw parameter count is not a controlled measure of computational cost across fundamentally different models. A quantum rotation, a recurrent weight, an attention parameter, and an adversarial parameter participate in different evaluation graphs and require different optimization, sampling, memory, and hardware resources.

The smaller QCBM count is therefore a descriptive result rather than evidence of quantum advantage. A practical comparison must combine representational quality with training evaluations, circuit shots, classical simulation or hardware time, inference cost, and the resource limits defined by [[Generative Model Advantage Race Design]].

A second performance study reports a similarly striking but still conditional example: a 54-parameter discrete copula QGAN fits the three-dimensional X distribution with KL $0.029$, compared with KL $0.089$ for a 9,475-parameter classical GAN. The quantum and classical parameter counts arise from different circuit blocks, hidden layers, training rules, and runtime costs, while every quantum result is obtained in noiseless state-vector simulation. Parameter efficiency is therefore an empirical architecture property, not a controlled resource advantage.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

[[2023 - A performance characterization of quantum generative models.pdf]]

