2026-09-06 19:44

Status: #baby

Tags: [[Iterative Linear System Methods]]

# Successive Over-Relaxation

Successive over-relaxation modifies the [[Gauss-Seidel Method]] by blending the old component with its newly computed value using a relaxation factor $\omega$.

When $1<\omega<2$, over-relaxation may accelerate an already convergent system. Values $0<\omega<1$ under-relax the update and can stabilize some systems that otherwise diverge.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

