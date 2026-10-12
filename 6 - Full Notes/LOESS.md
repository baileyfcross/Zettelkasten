2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]]

# LOESS

LOESS estimates a smooth relationship by fitting a low-degree polynomial to a weighted neighborhood around each target predictor value. Nearby observations receive more influence, allowing the fitted curve to follow gradual nonlinear structure without specifying one global formula.

The span controls the neighborhood size and therefore the bias-variance tradeoff. Compared with [[Bin Smoothing]], local lines or parabolas permit larger neighborhoods while retaining curvature and producing a smoother estimate.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
