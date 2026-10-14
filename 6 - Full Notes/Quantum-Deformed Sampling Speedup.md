2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# Quantum-Deformed Sampling Speedup

Some quantum-deformed layers can sample their correlated activation-weight distribution efficiently on a quantum computer even when classical sampling is believed to require exponential time. The paper points to deformation circuits drawn from random-circuit or quantum-time-evolution families whose output distributions underpin quantum-supremacy arguments.

This is a conditional sampling advantage, not an established learning advantage. The proposed network still requires quantum phase estimation and is intended for error-corrected hardware, and the authors did not execute its unrestricted form on a quantum computer. They explicitly leave open whether faster access to these distributions improves performance on learning tasks.

The experiments instead use [[Low-Entanglement Classical QDNN Simulation]], which deliberately limits entanglement so the model can run classically. Their modest accuracy changes therefore provide evidence about a quantum-inspired architecture, not evidence for the claimed exponential sampling separation.

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
