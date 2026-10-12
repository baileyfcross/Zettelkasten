2026-09-15 02:16

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# Recurrent Hidden State

A recurrent network carries a vector of hidden-layer activations from one sequence step into the next. At the current step, the hidden layer receives both the new input and this stored context. Its output is used to produce the current result and to update the state for the following step.

The memory buffer in Kelleher's [[Recurrent Neural Network]] diagram stores activations without transforming them; weighted connections from the buffer to the hidden units perform the next transformation. This feedback lets a later input be processed in the context of earlier inputs, although basic recurrence can struggle to retain long-range information during training.

# References

[[deeplearning_mit.epub]]
