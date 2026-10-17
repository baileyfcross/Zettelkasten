2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# QUBO Cubic-Term Cancellation

Truth-table penalties for a three-variable relation often expand to terms containing $x_0x_1x_2$, which cannot be sent directly to a quadratic optimizer. When several invalid rows are being penalized, each row penalty can be multiplied by a positive weight without changing which rows it penalizes.

Choosing those weights so the positive and negative cubic coefficients sum to zero removes the third-order term while leaving every invalid row above the valid rows. The NASA lecture uses this construction for OR and AND relations. The technique is relation-specific; if cancellation is impossible or poorly conditioned, auxiliary-variable quadratization is needed instead.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

