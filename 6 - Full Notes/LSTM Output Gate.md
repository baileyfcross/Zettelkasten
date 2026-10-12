2026-09-15 02:16

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# LSTM Output Gate

An LSTM output gate selects which parts of the updated [[LSTM Cell State|cell state]] become the hidden output at the current time step. The cell state is passed through tanh to form a candidate output; a sigmoid gate, computed from the current input and prior hidden output, filters that candidate element by element.

The resulting vector is sent toward the network's output and is also carried as the next step's hidden context. This is different from the [[LSTM Forget Gate]], which filters stored memory, and the [[LSTM Input Gate]], which adds selected information to it.

# References

[[deeplearning_mit.epub]]
