2026-09-29 19:17

Status: #baby

Tags: [[Support Vector Classification]]

# Convex Surrogate Classification Loss

A convex surrogate classification loss replaces discontinuous zero–one misclassification loss with a convex function of the signed score. The relaxation makes optimization tractable while still encouraging scores with the correct sign.

Surrogates trade computational feasibility against how faithfully their risk reflects classification error. The [[Hinge Loss]] produces support vector machines, while an exponential surrogate leads to AdaBoost-style weighting. Statistical analysis compares surrogate excess risk with true classification excess risk rather than assuming that easier optimization automatically preserves the original objective.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
