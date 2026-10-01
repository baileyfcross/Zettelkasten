2026-09-05 16:28

Status: #baby

Tags: [[Speech and Acoustic Modeling]] [[Recursive Bayesian Estimation]] [[Large Language Model Foundations]]

# Hidden Markov Model

A hidden Markov model represents a sequence as transitions among unobserved states that probabilistically emit observable evidence. In speech recognition, the hidden states can represent stages of a speech sound while feature vectors provide the observations.

The model captures duration and order without requiring exact time alignment. It was central to traditional [[Acoustic Model|acoustic modeling]] before end-to-end neural systems became dominant.

As a recursive Bayesian model, a hidden Markov model combines a state transition distribution with an observation distribution. The same decomposition supports filtering of the current state, prediction of later states, and smoothing of past states when later evidence is available.

For language sequences, an HMM represents unobserved states connected by transition probabilities and observed tokens produced through emission probabilities. Unlike an [[N-Gram Language Model]], it can infer a hidden sequence structure, but its independence assumptions and fixed state design limit flexible contextual representation.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[aiassistants.epub]]

[[bayesianprogramming.pdf]]
