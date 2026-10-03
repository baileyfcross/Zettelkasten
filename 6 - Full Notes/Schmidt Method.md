2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Schmidt Method

The Schmidt method is an explicit finite-difference scheme for the one-dimensional heat equation $u_t=c^2u_{xx}$. With $\alpha=kc^2/h^2$,

$$u_{i,j+1}=\alpha u_{i-1,j}+(1-2\alpha)u_{i,j}+\alpha u_{i+1,j}.$$

Every value on the new time level comes directly from three values on the preceding level. The simplicity is paired with a stability restriction on the ratio of time step to spatial step.

# References

[[numericalmethodsinengineeringandscience.pdf]]

