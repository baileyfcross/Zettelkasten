2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Adversarial Update Scheduling

A qGAN discriminator is trained on asymmetrical inputs: it receives a batch of individually embedded real events but compares them with one generator state intended to represent the entire generated distribution. Alternating the generator and discriminator once each can therefore bias the adversarial game or allow one side to improve faster than the other.

The A-qGAN implementation compensates by updating the discriminator several times before each generator update. Its three-feature experiment uses five discriminator updates per generator step, while the seven-feature experiment uses ten. Training data are shuffled into batches of ten, and parameter-shift gradients feed an AMSGRAD optimizer.

The schedule is a stability heuristic rather than a universal ratio. A discriminator that becomes too accurate can starve the generator of useful gradients, while a weak discriminator provides little learning signal. Suitable update frequency depends on batch size, circuit capacity, noise, and learning rate. The large variability across repeated benchmark runs shows that scheduling reduces but does not eliminate the intrinsic volatility of adversarial training.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
