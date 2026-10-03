2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Predictor-Corrector Method

A predictor-corrector method first estimates the next solution value with an explicit formula, then substitutes that estimate into a more accurate correcting formula. Correction may be repeated until successive values agree.

The separation provides both an efficient first guess and a way to gauge local error from the correction size. Multistep examples such as [[Milne Method]] and [[Adams-Bashforth Method]] require several prior values and therefore are not self-starting.

# References

[[numericalmethodsinengineeringandscience.pdf]]

