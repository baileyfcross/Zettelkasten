2026-09-28 03:19

Status: #baby

Tags: [[Health Data Privacy and Integration]]

# Perturbed Gibbs Sampler

The Perturbed Gibbs Sampler, or PeGS, generates synthetic records from conditional statistical models while injecting controlled randomness into those models. It disintegrates the original data into conditional building blocks, perturbs them, and synthesizes new combinations.

The privacy parameter governs how strongly the output distribution can depend on any one record, connecting the procedure to differential privacy. More perturbation reduces disclosure risk but can weaken relationships needed for analysis. The released data should therefore be compared with the original through both privacy measures and model-specific utility checks.

# References

[[healthcaredataanalytics.pdf]]
