2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Information Fusion]]

# Conditional Sensor Dependence

Conditional sensor dependence remains when two readings share influences even after the primary hidden state is known. Treating those readings as independent can count related evidence more than once and make the fused distribution too confident.

A model can retain a joint factor for a dependent sensor group or introduce another hidden variable explaining their correlation. The richer structure increases parameter and inference cost but better represents the information sources.

# References

[[bayesianprogramming.pdf]]
