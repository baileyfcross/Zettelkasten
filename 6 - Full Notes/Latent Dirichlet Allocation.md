2026-10-11 12:45

Status: #baby

Tags: [[Probabilistic Topic Modeling]]

# Latent Dirichlet Allocation

Latent Dirichlet allocation is a generative topic model in which each document is a mixture of latent topics and each topic is a probability distribution over words. The observed tokens are explained through unobserved topic assignments rather than by giving every document one exclusive category.

The model reduces a high-dimensional corpus to document-topic and topic-term distributions. Because the latent variables are not directly observed, an inference procedure such as [[Gibbs-Sampled Topic Model|Gibbs sampling]] or a [[Variational Topic Model|variational method]] must estimate them.

# References

[[textminingandvisualization.pdf]]
