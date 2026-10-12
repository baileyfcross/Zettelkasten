2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# Policy-Gradient Compilation Generalization

The paper measures whether a circuit trained with [[Ancilla-Free Sampled Unitary Fidelity]] also reverses inputs outside its training set. Ten-qubit circuits are trained on between one and 1,000 local product states, using 2,000 circuit executions per rollout.

Evaluation includes the all-zero state, 100 unseen random product states, and 100 random state vectors that are generally nonlocal. Test fidelity rises as the training set expands, including on the nonlocal set, supporting the use of a sub-tomographic training ensemble for these simulated circuits.

Larger training sets require tighter learning-rate control and longer optimization: the reported maximum rises from a few hundred iterations for one training state to 5,000 iterations for 1,000 states. The experiment demonstrates an empirical sample-performance tradeoff rather than proving that a fixed small training set will characterize arbitrary unitaries.

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
