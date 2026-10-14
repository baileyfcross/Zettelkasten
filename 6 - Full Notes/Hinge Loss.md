2026-09-29 19:17

Status: #baby

Tags: [[Support Vector Classification]]

# Hinge Loss

Hinge loss for a labeled score is $(1-yf(x))_+$. It is zero when the observation is classified correctly with margin at least one, increases linearly inside the margin, and remains convex in the score.

Regularized empirical hinge-loss minimization defines a support vector machine. Only observations on or inside the margin contribute to the active penalty, which leads to the [[Support Vector Perspective]]. Hinge loss is a [[Convex Surrogate Classification Loss]], so its computational advantages are paired with a statistical comparison to zero–one classification risk.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
