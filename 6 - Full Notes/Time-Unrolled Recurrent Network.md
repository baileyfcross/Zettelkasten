2026-09-15 02:16

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# Time-Unrolled Recurrent Network

Unrolling a [[Recurrent Neural Network]] through time draws its repeated computation as a sequence of hidden and output layers, one set for each input step. The hidden state produced at one step becomes part of the input to the next. This drawing exposes the dependency chain that the compact recurrent loop conceals.

The apparent many-layer network does not learn independent parameters for every drawn step: the recurrent connections reuse the same weights. Unrolling makes [[Backpropagation Through Time]] easier to understand because an error at a later output must travel backward through the earlier states that influenced it.

# References

[[deeplearning_mit.epub]]
