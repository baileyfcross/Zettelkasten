2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# TEM Bond-Dimension Compression Bias

TEM repeatedly compresses its matrix-product-operator representation to an affordable bond dimension $\chi$. Compression discards small singular-value components of the inverse-noise map, so the implemented map no longer reproduces every Pauli-string rescaling factor exactly and introduces systematic bias.

Below the threshold dimension, the retained map misses some first-order noise terms and the error decreases rapidly as $\chi$ grows. Above [[TEM Threshold Bond Dimension]], all first-order terms are represented and the remaining bias is second order in the noise rates, approximately $\epsilon^2NL/30$ for the modeled dense circuits. The two regimes make bond dimension a quality-control parameter rather than only a runtime setting.

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

