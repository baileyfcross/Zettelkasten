2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Fidelity-Loss Quantum Classification

Fidelity-loss classification trains a quantum circuit by comparing its output state with the label state assigned to each example. For a training pair $(x,c)$, the desired quantity is $|\langle\phi_c|\psi(x,\Theta)\rangle|^2=1$, and the paper minimizes the dataset average of the squared deviation from one.

At inference time, the circuit is compared with every candidate [[Bloch-Sphere Label States for Quantum Classification|label state]], and the class with maximum squared overlap is returned. The loss therefore shapes a geometric embedding of samples into the qubit state space rather than directly fitting a scalar decision threshold.

The objective can be evaluated in an exact simulator or estimated on hardware through repeated label-state projections. Simulation provides a smooth training signal, while hardware estimates inherit the sampling and calibration effects summarized by [[Quantum Classifier Sampling and Systematic Error]].

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
