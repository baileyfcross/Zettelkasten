2026-09-30 17:53

Status: #baby

Tags: [[Large Language Model Foundations]]

# Multi-Head Attention

Multi-head attention performs several learned attention projections in parallel. Each head can emphasize different token relationships or representation subspaces, after which the head outputs are concatenated and transformed into one result.

Dividing attention into heads provides several simultaneous views of the same sequence without requiring a separate model for each relationship. The surrounding [[Transformer Architecture]] combines this operation with feedforward layers, residual connections, and normalization.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
