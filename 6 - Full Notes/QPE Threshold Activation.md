2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# QPE Threshold Activation

Quantum phase estimation can implement a binary neuron's threshold after its integer preactivation has been encoded as a Hamiltonian eigenvalue. With the phase scaled so that all possible counts fit in an ancilla register, phase estimation writes the preactivation into binary form.

The most significant ancilla bit states whether the count exceeds half of the possible inputs. Reading that bit therefore applies the paper's step activation without separately reconstructing the whole integer. Repeating the procedure for each output neuron implements a probabilistic binary layer.

The method operates on the eigenstates of the [[Quantum-Deformed Binary Preactivation Hamiltonian]]. Conjugating the phase-estimation unitary by the learned deformation changes those eigenstates and produces a [[Quantum-Deformed Neural Network]], but the reliance on phase estimation also places the full architecture beyond the noisy intermediate-scale hardware assumed by the paper.

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
