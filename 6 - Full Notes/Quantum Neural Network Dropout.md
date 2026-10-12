2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Quantum Neural Network Dropout

Quantum neural network dropout is a training-time regularizer that randomly replaces selected parameterized unitary operations, or structured groups of operations, with identities. The full circuit remains available after training. Repeatedly changing the active subcircuit discourages the optimization from depending too strongly on a particular operation and can reduce the gap between training and test performance associated with [[Overfitting]].

The approach is designed for deep, data-reuploading quantum neural networks whose many trainable gates can make them highly expressive and overparameterized. Unlike classical dropout, removing a one-qubit rotation does not isolate a computational unit: entanglement can propagate its effect, and the same qubit participates at multiple circuit times. The paper therefore defines several explicitly quantum strategies rather than treating gates as exact neuron-and-connection counterparts.

In the reported noiseless simulations, useful effective drop probabilities were modest and depended on the circuit architecture and task. [[Overparameterization-Aware Quantum Dropout Rate]] supplies an upper-bound heuristic, while [[Quantum Dropout Expressibility and Entanglement]] shows that successful regularization need not work by making the circuit less expressive or less entangling.

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
