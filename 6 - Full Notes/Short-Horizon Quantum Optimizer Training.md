2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Short-Horizon Quantum Optimizer Training

The learned quantum optimizers are trained and evaluated for a horizon of only ten circuit queries. This keeps the unrolled recurrent graph small enough to train while reducing the vanishing-gradient, exploding-gradient, and memory problems associated with long [[Backpropagation Through Time|backpropagation-through-time]] sequences.

The short horizon defines the optimizer's role. It is expected to make a few global, problem-informed moves and return a useful initialization, not to perform hundreds of fine-tuning steps by itself.

Running the recurrent network for longer than its training horizon is possible in principle but creates a distribution shift in sequence length. The study instead stops the LSTM after ten proposals and delegates local convergence to another optimizer.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

