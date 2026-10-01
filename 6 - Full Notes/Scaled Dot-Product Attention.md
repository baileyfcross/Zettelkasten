2026-09-30 17:53

Status: #baby

Tags: [[Large Language Model Foundations]]

# Scaled Dot-Product Attention

Scaled dot-product attention compares query and key vectors with dot products, divides the scores by the square root of the key dimension, applies any mask, and normalizes them with softmax. The normalized weights produce a weighted sum of value vectors.

Scaling prevents large vector dimensions from driving softmax into extremely peaked regions with poor gradients. The calculation is the basic attention operation repeated within [[Multi-Head Attention]].

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
