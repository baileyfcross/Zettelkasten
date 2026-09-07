2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Information Fusion]]

# Naive Bayes Sensor Fusion

Naive Bayes sensor fusion estimates a hidden state from several readings by assuming the sensors are conditionally independent once that state is known. The joint model factors into a state prior multiplied by one sensor model for each reading.

This sharply reduces dimensionality and makes additional sensors easy to incorporate. The assumption is only an approximation when unmodeled causes correlate the readings, so its computational benefit must be weighed against the quality required by the task.

# References

[[bayesianprogramming.pdf]]
