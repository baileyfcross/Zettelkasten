2026-10-04 22:20

Status: #baby

Tags: [[R Statistical Testing and Model Validation]]

# R Multiple Testing Correction

R multiple testing correction transforms a family of p-values to control an error criterion across the set of hypotheses. Bonferroni-type procedures target family-wise error, while false-discovery-rate procedures permit some false positives in exchange for greater power across many tests.

The family of tests and the chosen error criterion must be defined before selecting a method. Adjusting p-values does not repair biased hypotheses or dependent analyses, and the adjusted values should be interpreted with the corresponding procedure rather than as ordinary single-test probabilities.

# References

[[rprimer.pdf]]
