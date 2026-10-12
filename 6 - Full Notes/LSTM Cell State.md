2026-09-15 02:16

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# LSTM Cell State

The cell state is the memory vector carried forward inside a [[Long Short-Term Memory]] unit. Its entries preserve activations between sequence steps, while gates determine which old values remain and which new candidate values are added.

The [[LSTM Forget Gate]] filters the prior cell state, and the [[LSTM Input Gate]] selects a candidate update. The [[LSTM Output Gate]] determines which parts of the updated state contribute to the visible hidden output. Separating this carried state from the immediate output gives the recurrent model a controlled route for retaining context across time.

# References

[[deeplearning_mit.epub]]
