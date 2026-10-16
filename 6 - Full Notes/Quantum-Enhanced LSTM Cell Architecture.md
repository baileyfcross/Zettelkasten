2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# Quantum-Enhanced LSTM Cell Architecture

A quantum-enhanced long short-term memory cell preserves the recurrent structure of a classical LSTM while replacing its internal neural subnetworks with quantum neural networks. At time $t$, the cell combines the current input $x_t$ with the previous hidden state $h_{t-1}$ and carries a separate cell state $c_{t-1}$ for long-term memory.

Quantum subnetworks control the forget operation, the amount and content of the cell-state update, and the output gate. Additional subnetworks postprocess the gated state so the next hidden state $h_t$ and the externally reported output $y_t$ can differ.

This is a hybrid substitution, not a wholly quantum recurrent computer: the LSTM's state flow, sigmoid and hyperbolic-tangent nonlinearities, element-wise arithmetic, and training loop remain classical around parameterized quantum circuits. [[QLSTM Variational Subnetwork Ansatz]] records the particular circuit used in the finance experiment.

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
