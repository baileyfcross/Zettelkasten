2026-09-30 17:53

Status: #baby

Tags: [[Large Language Model Foundations]]

# Positional Encoding

Positional encoding adds information about token order to embeddings before transformer attention. Without it, the same set of token vectors would not by itself distinguish different arrangements because attention has no recurrent step that inherently records sequence position.

The position signal can be fixed or learned and is combined with the [[Word Embedding]] representation. Attention layers can then use both content and relative placement when forming contextual representations.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
