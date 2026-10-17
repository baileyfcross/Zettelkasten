2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum Patch GAN Convergence Guarantee

The quantum patch GAN uses the same adversarial loss as the original classical GAN after treating the concatenated patch outputs as one generator map $G(z)$. For a fixed generator, its optimal discriminator is therefore $D^*(x)=P_{data}(x)/(P_g(x)+P_{data}(x))$, the same expression obtained for a classical GAN.

Under the ideal assumptions that the generator and discriminator have enough capacity, the discriminator reaches its optimum at every iteration, and each generator update improves the prescribed criterion, the generated distribution converges to the data distribution. The equilibrium occurs when $P_g=P_{data}$ and the discriminator cannot distinguish the two distributions.

This is an inherited ideal convergence statement, not a guarantee for finite circuits, finite shots, alternating gradient descent, or noisy hardware. It establishes that patch concatenation does not change the formal target of adversarial learning; it does not rule out mode collapse, saddle points, or [[Barren Plateau Gradient Scaling|barren plateaus]] in an implemented qGAN.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
