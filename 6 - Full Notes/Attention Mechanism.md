2026-09-05 16:28

Status: #baby

Tags: [[Machine Learning and Neural Networks]]

# Attention Mechanism

An attention mechanism lets a neural model assign different importance to different parts of its input while producing an output. Instead of forcing all information through one fixed summary, it builds a context weighted toward what is currently relevant.

In an [[Encoder-Decoder Network]], attention helps align an output word or symbol with the input positions that support it. The weights are learned with the rest of the network.

Kelleher presents attention-centered transformer models as an alternative to relying on one fixed sentence vector: the model can dynamically focus on selected input parts while generating an output. He also describes BERT's use of an unlabeled-data pretraining stage followed by smaller task-specific supervised tuning. These were developments discussed in the book's 2019 outlook, not a claim about which architecture currently leads every task.

# References

[[aiassistants.epub]]

[[deeplearning_mit.epub]]
