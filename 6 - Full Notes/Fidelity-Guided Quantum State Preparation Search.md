2026-10-12 18:49

Status: #baby

Tags: [[Genetic Quantum Circuit Optimization]]

# Fidelity-Guided Quantum State Preparation Search

Fidelity-guided state-preparation search evolves a circuit whose output state is close to a specified target state. The candidate's fitness is the fidelity between its prepared state and the target, so selection progressively favors circuit structures and parameters that reproduce the target more closely.

The objective can include additional preferences rather than fidelity alone. Circuit depth can penalize unnecessarily long candidates, [[Hardware Gate-Set-Constrained Circuit Evolution|the gate alphabet can be restricted]] to operations supported by a device, and a hardware noise model can be incorporated so the selected circuit is optimized for noisy execution.

In the paper's experiments, target statevectors come from randomly generated four-qubit circuits of depth 20. The search therefore demonstrates synthesis toward known simulated targets; it does not test state preparation on hardware, under noise, or at a scale beyond four qubits.

# References

[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
