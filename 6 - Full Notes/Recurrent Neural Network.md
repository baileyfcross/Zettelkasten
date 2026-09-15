2026-09-05 16:28

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# Recurrent Neural Network

A recurrent neural network processes a sequence while carrying information from earlier steps into later ones. Its recurrent connections make the current output depend on both the present input and a representation of prior inputs.

This structure fits speech and language, where word or sound interpretation depends on surrounding sequence context. [[Long Short-Term Memory]] units were developed to preserve relevant information across longer spans.

Kelleher depicts the network's [[Recurrent Hidden State|hidden state]] as a memory buffer whose activations are fed into the next step along with its new input. [[Time-Unrolled Recurrent Network|Unrolling]] the loop shows how one set of [[Recurrent Weight Sharing Across Time|shared recurrent weights]] is reused through a sequence. Training with [[Backpropagation Through Time]] then has to propagate error through those steps, which can make long-range dependencies difficult to learn.

# References

[[aiassistants.epub]]

[[deeplearning_mit.epub]]
