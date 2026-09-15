2026-09-15 02:16

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# Backpropagation Through Time

Backpropagation through time applies [[Backpropagation]] to the [[Time-Unrolled Recurrent Network|unrolled]] chain of a recurrent network. A later output may depend on many earlier hidden states, so its error must be propagated backward through those time steps to assign credit to the reused connection weights.

Long chains create a training problem. Repeated multiplication by recurrent weights and activation derivatives can make gradients for early inputs very small. [[Long Short-Term Memory]] units are designed to preserve a more useful path for information and gradients across sequence steps, rather than relying only on an ordinary recurrent hidden state.

# References

[[deeplearning_mit.epub]]
