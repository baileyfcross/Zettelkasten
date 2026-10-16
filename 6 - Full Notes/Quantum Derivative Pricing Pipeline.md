2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Quantum Derivative Pricing Pipeline

Derivative pricing estimates the discounted expectation of a contract's payoff over possible future paths of its underlying assets. A quantum pricing circuit separates this into probability loading, payoff encoding, and expectation estimation.

A preparation operator $P$ creates $\sum_\omega\sqrt{p(\omega)}|\omega\rangle$. A payoff operator $F$ then makes a designated ancilla's good-state probability equal to the normalized payoff $f(\omega)$ for each path. The composite operator $A=FP$ therefore produces a total good-state probability $\sum_\omega p(\omega)f(\omega)=\mathbb{E}[f]$.

Quantum amplitude estimation estimates that probability, providing the proposed quadratic sampling improvement over classical [[Monte Carlo Integration]]. The main engineering question is how to implement $P$ and $F$ cheaply enough for this asymptotic advantage to survive; [[Quantum Arithmetic Bottleneck in Derivative Pricing]] identifies the payoff-side obstacle targeted by QSP.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
