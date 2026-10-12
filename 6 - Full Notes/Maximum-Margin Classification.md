2026-09-14 21:00

Status: #baby

Tags: [[Support Vector Classification]]

# Maximum-Margin Classification

Maximum-margin classification chooses a separating hyperplane that maximizes the distance to the nearest training observations from either class. Those closest cases define the attainable margin.

A larger margin provides a geometric form of regularization because many separating boundaries may classify the training data perfectly but differ in robustness. The hard-margin formulation requires separability; overlapping data require penalties for violations.

Support vector machines implement this idea through regularized [[Hinge Loss]]. The learned score lies in the span of kernel evaluations at the training observations, and only cases with active margin constraints receive nonzero coefficients. This links the geometric margin to the [[Support Vector Perspective]].

# References

[[dataclassification.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
