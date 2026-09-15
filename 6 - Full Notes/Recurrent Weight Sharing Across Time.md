2026-09-15 02:16

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# Recurrent Weight Sharing Across Time

An [[Recurrent Neural Network]] applies the same recurrent connection weights at each step of a sequence. When the network is [[Time-Unrolled Recurrent Network|unrolled]], the arrows between successive hidden states depict repeated uses of one parameter set, not new parameters for each time position.

This allows a sequence-processing rule to be reused regardless of the step being processed. It also creates a training difficulty: a gradient traveling through many steps repeatedly passes through transformations involving the same weights. The book explains that repeated multiplication by factors below one can make an early-step gradient shrink sharply.

# References

[[deeplearning_mit.epub]]
