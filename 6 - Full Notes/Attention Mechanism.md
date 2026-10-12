2026-09-05 16:28

Status: #baby

Tags: [[Large Language Model Foundations]] · [[Machine Translation Architectures]]

# Attention Mechanism

An attention mechanism lets a neural model assign different importance to different parts of its input while producing an output. Instead of forcing all information through one fixed summary, it builds a context weighted toward what is currently relevant.

In an [[Encoder-Decoder Network]], attention helps align an output word or symbol with the input positions that support it. The weights are learned with the rest of the network.

Kelleher presents attention-centered transformer models as an alternative to relying on one fixed sentence vector: the model can dynamically focus on selected input parts while generating an output. He also describes BERT's use of an unlabeled-data pretraining stage followed by smaller task-specific supervised tuning. These were developments discussed in the book's 2019 outlook, not a claim about which architecture currently leads every task.

Transformer attention learns query, key, and value projections so a token can weight information from other positions according to the current context. [[Scaled Dot-Product Attention]] supplies the core calculation, while [[Multi-Head Attention]] learns several relationship spaces in parallel.

Machine translation makes the alignment role concrete. While generating a target word, the decoder can raise the weight of the source words most relevant to that decision rather than treating the entire encoded sentence equally. This is especially useful for long inputs and language pairs with different word order, where the source position needed for agreement or meaning may be far from the decoder's current step.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[aiassistants.epub]]

[[deeplearning_mit.epub]]

[[machinetranslation.epub]]
