2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Reweighted Evens Distribution Benchmark

The benchmark solution space contains 20-bit strings with an even number of ones, giving $|S|=2^{19}$ valid configurations. Training subsets use either $\epsilon=0.01$ with 5,242 examples or $\epsilon=0.001$ with 524 examples, and both subsets are selected to have the same minimum cost of $-12$.

Each training example is reweighted by $P_{train}(x)\propto\exp[-\beta c(x)]$, with the inverse-temperature scale derived from the training-set cost variation. The reweighting encourages every model to allocate probability toward lower-cost examples in the hope of extrapolating to unseen configurations that improve on them.

This synthetic parity constraint makes validity unambiguous and the full search space conceptually clear, but it is not a realistic application dataset. It demonstrates the comparison framework under controlled conditions rather than establishing commercial relevance by itself.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

