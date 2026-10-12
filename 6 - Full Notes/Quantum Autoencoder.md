2026-10-12 01:15

Status: #baby

Tags: [[Quantum Autoencoding and State Compression]]

# Quantum Autoencoder

A quantum autoencoder is a variational quantum circuit that learns to compress a family of quantum states into a smaller latent register. The encoder applies a parameterized unitary to an input state on (N) qubits and separates the result into (K) latent qubits and (N-K) disposable qubits. Training seeks parameters that make the disposable subsystem approach a fixed reference state, usually the all-zero state.

After successful training, the disposable qubits can be removed while the latent register retains the information needed for the intended reconstruction or analysis. A decoder applies the inverse of the learned encoder to the latent state together with a freshly prepared reference subsystem. This makes the architecture a quantum analogue of an [[Autoencoder]], but its encoder and decoder are unitary transformations and its encoded object is a quantum state rather than a classical feature vector.

The useful compression depends on the input family having sufficiently low effective rank and on the circuit finding a suitable optimum. These conditions connect the basic architecture to the [[Quantum Autoencoder Latent Rank Condition]] and the guarantees described by [[Quantum Autoencoder Spectral Preservation]].

# References

[[2021 - On exploring practical potentials of quantum auto-encoder with advantages.pdf]]
