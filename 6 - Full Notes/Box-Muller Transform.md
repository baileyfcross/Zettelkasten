2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Box-Muller Transform

The Box-Muller transform converts two independent uniform values $U_1,U_2$ into two independent standard normal values:

$$Z_1=\sqrt{-2\ln U_1}\cos(2\pi U_2),\qquad Z_2=\sqrt{-2\ln U_1}\sin(2\pi U_2).$$

The transformation produces normal values in pairs. Its polar reformulation, [[Polar Method for Normal Random Variates]], replaces the trigonometric evaluations with an acceptance test inside the unit disk.

# References

[[statisticalcomputingincplusplusandr.pdf]]
