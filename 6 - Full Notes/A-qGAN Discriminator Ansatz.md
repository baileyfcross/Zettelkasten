2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Discriminator Ansatz

The A-qGAN discriminator begins with Hadamard gates and repeats blocks of parameterized $R_Z$, $R_Y$, and $R_Z$ rotations followed by controlled-$Z$ entanglers. A fan-in series of CNOT gates then couples the register to the final qubit, where additional $R_X$, $R_Y$, and $R_Z$ rotations prepare a single-qubit readout.

For $n$ qubits and $k_D$ repeated blocks, the circuit has $3(k_Dn+1)$ trainable rotations. Its label is obtained from the Pauli-$Z$ expectation on the last qubit, so the measured cost is local even though preceding entanglers allow that qubit to summarize information distributed across the register.

The local readout is significant for trainability because shallow circuits with local cost functions are less exposed to cost-induced barren plateaus than deep circuits measured by global observables. That does not remove adversarial instability or hardware noise, and the CNOT fan-in still makes topology and compilation relevant. [[A-qGAN Adversarial Update Scheduling]] balances this discriminator against the generator during training.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
