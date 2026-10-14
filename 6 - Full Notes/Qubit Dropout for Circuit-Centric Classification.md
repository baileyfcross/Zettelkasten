2026-10-14 09:10

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Qubit Dropout for Circuit-Centric Classification

Qubit dropout temporarily removes an entire qubit from a circuit-centric classifier during training. A qubit is randomly selected, measured, and set aside for a fixed number of parameter-update epochs; it is then restored and another qubit, or no qubit, is selected for the next interval.

For an amplitude-encoded state, dropping one qubit prevents half of the amplitudes from influencing the stochastic gradient during that interval. In the paper's neural-network analogy, this resembles removing half of a hidden layer rather than deleting one conventional neuron. The model alternates among these reduced views while retaining one shared parameter set.

The procedure raises training error but can lower holdout error when the slim classifier still overfits small datasets. It is an early whole-register regularizer and differs from later [[Quantum Neural Network Dropout]], which usually substitutes identities for selected rotations or entangling gates without measuring and removing a qubit.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]
