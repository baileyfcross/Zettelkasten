2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Learned Basin Initialization for Variational Quantum Circuits

A short learned optimization sequence is most useful when it places variational parameters inside the basin of attraction of a high-quality optimum. It does not need to finish the optimization; it needs to make the subsequent local search faster, more reliable, and less dependent on a random seed.

This reframes initialization as approximate global optimization. The LSTM uses landscape regularities learned across problem instances to make a few nonlocal proposals, after which a conventional method can exploit the local geometry near the selected point.

The reported evidence supports basin finding rather than exact convergence: the raw LSTM achieves a strong approximate solution after ten queries, while the highest-quality final results generally come from local refinement of its output.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

