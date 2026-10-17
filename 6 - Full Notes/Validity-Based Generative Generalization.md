2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Validity-Based Generative Generalization

Validity-based generalization measures whether novel generated samples satisfy the task constraints. If $G_{sol}$ is the set of generated queries that are both unseen and valid, the generalization rate is $R=|G_{sol}|/Q$ and can be normalized by the unobserved fraction as $\widetilde R=R/(1-\epsilon)$.

Generalization fidelity, $F=|G_{sol}|/|G_{new}|$, asks what fraction of all novel outputs are valid. Generalization coverage instead measures how many distinct valid unseen solutions are reached relative to the unobserved solution space, so it captures diversity rather than probability mass alone.

On the parity-constrained benchmark, the QCBM balances validity and quality more evenly than the VAE and WGAN, which obtain strong quality scores but sacrifice validity and coverage. The QCBM is broadly competitive with the autoregressive RNN and Transformer on these validity measures.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

