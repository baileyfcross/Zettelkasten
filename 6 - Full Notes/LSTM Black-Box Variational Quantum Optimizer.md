2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# LSTM Black-Box Variational Quantum Optimizer

An LSTM can act as the classical optimizer inside a variational quantum algorithm. At iteration $t$, it receives the current circuit parameters $\theta_t$, their estimated cost $y_t$, and its hidden state $h_t$, then produces both a new proposal and an updated memory:

$$h_{t+1},\theta_{t+1}=\operatorname{RNN}_{\phi}(h_t,\theta_t,y_t).$$

The hidden state lets the optimizer condition each move on its query history rather than on the latest cost alone. During inference it needs neither an analytical gradient nor direct access to the circuit internals; the circuit is a black-box function whose noisy values guide the sequence.

This is different from a [[Neural Network Optimizer]] that updates the weights of the same model it belongs to. Here a separately trained recurrent network proposes the parameters of a quantum circuit.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

