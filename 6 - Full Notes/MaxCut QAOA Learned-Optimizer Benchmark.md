2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# MaxCut QAOA Learned-Optimizer Benchmark

The MaxCut benchmark uses depth-$2$ QAOA, giving the learned optimizer four circuit parameters independent of graph size. Training contains 10,000 random Erdos-Renyi graphs with six through nine vertices; each graph first samples an expected degree between three and $n-1$ and then sets the edge probability to that degree divided by $n$.

Testing uses fifty twelve-vertex graphs, strictly larger than any training instance. The raw LSTM reaches a low relative error in ten objective queries, and Nelder-Mead seeded by those proposals improves further while outperforming random and mean-training-parameter initializations.

The benchmark demonstrates within-distribution size transfer under a fixed-depth ansatz. It does not establish that the same optimizer would transfer to another graph distribution, another QAOA depth, or a different combinatorial problem.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

