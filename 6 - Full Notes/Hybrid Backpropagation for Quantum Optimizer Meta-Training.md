2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Hybrid Backpropagation for Quantum Optimizer Meta-Training

Training a recurrent quantum-circuit optimizer requires gradients of the meta-loss to pass backward through the repeated LSTM states and through the parameterized quantum cost evaluations. The unrolled CPU-QPU loop is therefore treated as one differentiable hybrid graph during meta-training.

This use of [[Backpropagation Through Time]] is confined to training the optimizer network. Once trained, the LSTM interacts with a new circuit through parameter proposals and returned expectation values, so inference remains black-box even though the learned update rule was obtained with circuit derivatives.

The separation matters for near-term use. It permits expensive derivative-aware training on small classically simulated instances, followed by derivative-free proposals on a larger circuit for which gradients would be costly to estimate.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

