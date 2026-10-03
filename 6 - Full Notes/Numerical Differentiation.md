2026-10-03 16:11

Status: #baby

Tags: [[Finite Difference Methods]]

# Numerical Differentiation

Numerical differentiation estimates a derivative from tabulated values by first replacing the unknown function with an interpolating polynomial and then differentiating that polynomial.

Forward formulas suit points near the beginning of an equally spaced table, backward formulas suit the end, and central formulas suit the middle. The process can amplify data error, especially for high derivatives, because close values are subtracted and the result is divided by powers of the step size.

# References

[[numericalmethodsinengineeringandscience.pdf]]

