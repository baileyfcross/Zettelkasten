2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Inference Algorithms]]

# Distribution Sampling

Distribution sampling generates values whose frequencies approximate a probability distribution. Samples allow expectations, probabilities, and other summaries to be estimated even when direct integration is difficult.

A valid sampling method must account for any difference between the distribution used to generate candidates and the target distribution. Accuracy improves with effective independent sample count, not merely raw iterations.

A quantum circuit offers a different access pattern when its computational-basis probabilities represent the target distribution: each projective measurement produces one sample without classically integrating and inverting a learned density at draw time. The [[Quantum Chebyshev Transform]] creates this access by mapping a learned polynomial-basis model into computational amplitudes. State preparation, model training, repeated shots, and conversion from bitstrings to the nonuniform Chebyshev grid remain costs, so direct measurement is not by itself proof of end-to-end advantage.

# References

[[bayesianprogramming.pdf]]

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
