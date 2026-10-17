2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum GAN State-Preparation Bottleneck

The batch qGAN's coherent-minibatch proposal requires oracles that prepare indexed superpositions of latent vectors and real examples. For a batch of $2^{N_I}$ records with $M$ features, generic amplitude encoding does not make data access free: the stated preparation complexity is broadly comparable to reading the same data classically and may require many multi-controlled gates.

Those gates are hostile to near-term hardware because their decomposition increases depth and noise exposure. The paper therefore suggests using pretrained approximate state-preparation oracles. This shifts work out of the adversarial loop, but the cost and error of learning or executing those oracles must still be included in an end-to-end comparison.

The bottleneck limits the claim made by [[Quantum Batch Gradient Superposition]]. A compact quantum representation can reduce qubit storage relative to classical bits, yet storage width alone is not runtime advantage. Useful coherent batching requires a structured dataset or preparation procedure whose total cost does not erase the gain from shared quantum processing.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
