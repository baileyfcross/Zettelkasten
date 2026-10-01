2026-09-30 17:53

Status: #baby

Tags: [[Large Language Model Foundations]]

# Autoregressive Language Modeling

Autoregressive language modeling factors a sequence into conditional next-token predictions. During generation, the model samples or selects a token from the current probability distribution, appends it to the context, and repeats the prediction loop.

GPT-style models implement this process with a decoder-only [[Transformer Architecture]] and a [[Causal Attention Mask]]. Longer context and deeper representations extend the same fundamental prediction objective illustrated by an [[N-Gram Language Model]].

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
