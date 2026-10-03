2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Wave Equation Difference Scheme

Centered differences for $u_{tt}=c^2u_{xx}$ give a three-level recurrence:

$$u_{i,j+1}=2(1-r^2)u_{i,j}+r^2(u_{i-1,j}+u_{i+1,j})-u_{i,j-1},$$

where $r=ck/h$. Two initial time levels are obtained from the initial displacement and velocity. The scheme is stable only when the time step is sufficiently small relative to the spatial step; at $r=1$ it simplifies substantially.

# References

[[numericalmethodsinengineeringandscience.pdf]]

