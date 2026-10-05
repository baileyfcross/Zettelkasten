2026-10-04 22:20

Status: #baby

Tags: [[R Data Transformation and Reshaping]]

# R Factor Reference Level

An R factor reference level is the baseline category against which other levels are represented in a treatment-coded model. Releveling changes coefficient interpretation without changing the observations themselves, so the baseline should be selected for scientific and communicative meaning rather than left to an accidental ordering.

The reference choice should be made after [[Factor Level Normalization]]. Otherwise spelling variants or unused levels can become part of the model matrix and obscure the intended comparison.

# References

[[rprimer.pdf]]
