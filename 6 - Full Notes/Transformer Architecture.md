2026-09-30 17:53

Status: #baby

Tags: [[Large Language Model Foundations]]

# Transformer Architecture

The transformer architecture processes sequence representations with attention and position-wise feedforward layers rather than recurrently passing one hidden state from token to token. This permits parallel training and creates direct paths between distant positions in a sequence.

The original design contains encoder and decoder stacks connected with residual paths and normalization. Encoder-only models use contextual input representations, decoder-only models such as GPT use causal generation, and encoder-decoder models transform one sequence into another.

The source connects transformer scale to practical inference constraints. Attention and feedforward computation make context length, memory, batching, quantization, and serving hardware application concerns even when a Java framework hides the model's internal tensor operations.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
