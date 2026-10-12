2026-09-30 17:53

Status: #baby

Tags: [[Large Language Model Foundations]]

# Causal Attention Mask

A causal attention mask prevents a generating position from attending to tokens that occur later in the target sequence. Future-position scores are suppressed before softmax, so each prediction depends only on the available prefix.

This constraint lets a decoder train on full sequences while preserving the information boundary used during [[Autoregressive Language Modeling]]. Removing it would allow the training calculation to leak the answer tokens the model is supposed to predict.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
