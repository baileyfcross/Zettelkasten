2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Bendre-Schmidt Recurrence

The Bendre-Schmidt recurrence is the special [[Schmidt Method]] obtained when $\alpha=1/2$. The central coefficient vanishes and the heat-equation update becomes

$$u_{i,j+1}=\frac12(u_{i-1,j}+u_{i+1,j}).$$

Thus each new value is the average of its two spatial neighbors at the preceding time level. The simplification fixes the time step through $kc^2/h^2=1/2$.

# References

[[numericalmethodsinengineeringandscience.pdf]]

