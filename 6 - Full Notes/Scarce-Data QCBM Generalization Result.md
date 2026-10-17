2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Scarce-Data QCBM Generalization Result

With only 524 training strings ($\epsilon=0.001$), the QCBM wins the fixed-query T1 comparison: its best utility is $-17.30(8)$, its minimum value reaches $-19$, and its quality coverage is approximately $7\times10^{-4}$. It also leads T2 quality coverage at $0.04$ while matching the VAE closely on minimum value and utility.

The outcome is regime dependent. With 5,242 training examples ($\epsilon=0.01$), the VAE wins T1 and the WGAN wins T2, so the QCBM's relative strength appears specifically when both data and post-training queries are scarce rather than across all tested conditions.

This is evidence for a potential advantage hypothesis, not a demonstrated PQA. The QCBM is simulated with exact probabilities on a synthetic parity task, training cost is omitted, the classical model set is not exhaustive, and no scaling or hardware-noise study shows that the ranking persists in a practical application.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

