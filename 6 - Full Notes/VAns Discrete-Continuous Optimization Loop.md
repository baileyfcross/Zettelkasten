2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# VAns Discrete-Continuous Optimization Loop

VAns nests two kinds of optimization. Its outer loop changes discrete architecture variables such as gate type and placement, while its inner loop holds that structure fixed and optimizes continuous rotation parameters until convergence.

After insertion, simplification, and parameter retraining, an architecture whose optimized cost is equal to or lower than the previous cost is accepted. A cost-increasing change can also be accepted with an exponentially decreasing probability controlled by a temperature parameter, giving the structural search a Metropolis-Hastings-like escape from local choices.

The loops stop when a user-supplied termination condition is met, such as reaching a target cost, exhausting a maximum number of architecture iterations, or satisfying another condition involving the cost and circuit structure. This separation lets [[VAns Stochastic Identity Block Insertion]] propose layouts without assuming that their initial parameter values reveal their eventual performance.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
