2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Generative Pre-Generalization Exploration

Pre-generalization asks only whether a generative model produces samples outside its training set. For $Q$ generated queries and the subset $G_{new}$ that was not present during training, exploration is $E=|G_{new}|/Q$.

A high exploration score rules out pure memorization but does not establish useful generalization. Novel samples may violate the problem constraints, repeat a narrow invalid pattern, or have poor objective values. Exploration is therefore a prerequisite that must be interpreted alongside [[Validity-Based Generative Generalization]] and [[Quality-Based Generative Generalization]].

In the 20-bit benchmark, the QCBM remains competitive with the RNN and Transformer on exploration across both training-set sizes. The VAE and WGAN explore less as training proceeds, consistent with their stronger concentration and weaker validity metrics in this setup.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

