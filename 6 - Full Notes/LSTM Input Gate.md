2026-09-15 02:16

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# LSTM Input Gate

The input gate controls what new information enters an [[LSTM Cell State|LSTM cell state]]. One sigmoid layer selects which state entries should be updated, while a tanh layer proposes candidate values that can raise or lower those entries. Both process the current input and the prior hidden output.

The selection vector multiplies the candidate vector elementwise, and the result is added to the state left after the [[LSTM Forget Gate]] has filtered it. This separates the question of *where to write* from *what to write*, enabling the recurrent model to update some memory components while leaving others alone.

# References

[[deeplearning_mit.epub]]
