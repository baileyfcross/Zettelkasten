2026-09-15 02:16

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# LSTM Forget Gate

An LSTM forget gate decides how much of the previous [[LSTM Cell State|cell state]] to retain at a new sequence step. It processes the current input together with the prior hidden output using sigmoid units, producing a vector of values between zero and one.

Multiplying the old cell state elementwise by this vector suppresses entries with gate values near zero and retains entries with values near one. The gate's role is selective memory removal, distinct from adding new information through the [[LSTM Input Gate]] or deciding what to reveal through the [[LSTM Output Gate]].

# References

[[deeplearning_mit.epub]]
