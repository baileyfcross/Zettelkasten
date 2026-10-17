2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# Quantum State Ensemble Generation

Quantum state ensemble generation aims to produce new individual states distributed like samples from an unknown ensemble. This is stronger than reproducing only the ensemble's average density operator: many distinct distributions of pure states can share the same average state.

For example, generating a Haar-random state or a state drawn from a structured ring requires matching sample-to-sample variation, not merely outputting the maximally mixed average associated with the Haar ensemble. A loss must therefore compare distributions over state vectors rather than only expectation values of the mean state.

QuDDPM addresses this task by learning a map from a noisy random-state ensemble to the structured target ensemble. Its benchmarks also modify quantum direct transport and QuGAN baselines because prior versions generally targeted one state or a classical distribution rather than a distribution of quantum states.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

