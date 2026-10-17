2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Quantum Learned-Optimizer Meta-Training Cost

Each specialist LSTM is trained on 10,000 problem instances for at most 1,000 epochs with a ten-step horizon. The stated upper bound is one million simulated quantum-neural-network inference executions per optimizer network, in addition to backpropagation through the temporal hybrid graph.

The reported objective-query curves exclude this meta-training overhead. Their advantage therefore describes the cost of reusing a trained optimizer on a new instance, not the end-to-end cost of learning and applying the optimizer once.

The investment can be worthwhile only when it is amortized across enough related instances or when classical training on small systems enables expensive larger-system queries to be avoided. Early stopping reduced the actual training below the stated maximum in most runs, but the paper does not provide a complete hardware-equivalent training budget.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

