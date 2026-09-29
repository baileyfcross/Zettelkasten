2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Gauss-Lasso

Gauss-Lasso is a two-stage estimator that uses Lasso to select a support and then refits least squares within the selected model. The second stage projects the response onto the span of the chosen variables instead of retaining the penalized coefficient magnitudes.

Refitting removes the direct [[Lasso Shrinkage Bias]] and can restore the amplitude of strong signals. It does not undo a mistaken support: omitted variables remain absent and false inclusions are still fitted. The method separates the selection role of the $\ell_1$ penalty from the final coefficient estimation step.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
