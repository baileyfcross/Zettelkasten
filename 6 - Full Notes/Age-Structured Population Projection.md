2026-10-04 22:56

Status: #baby

Tags: [[R Matrix Systems and Scientific Models]]

# Age-Structured Population Projection

An age-structured population projection represents the numbers in each age class as a state vector and uses a matrix of survival and reproduction rates to advance that vector one time step. Each output class is a dot product between one matrix row and the current population.

Repeated matrix multiplication generates a projected trajectory and exposes how vital rates couple the age classes. The projection is conditional on rates remaining appropriate; it is a model of population structure, not a guarantee about future abundance.

# References

[[rstudentcompanion.pdf]]
