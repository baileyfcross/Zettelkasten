2026-09-15 02:20

Status: #baby

Tags: [[Neural Network Training]]

# Vanishing Gradient Problem

A gradient vanishes when the error signal becomes very small as it is propagated backward through many neural transformations. Repeated multiplication by small activation derivatives or recurrent weights can leave early layers or early sequence steps with little effective training signal.

Kelleher shows why saturated sigmoid units aggravate this problem and why [[Recurrent Weight Sharing Across Time]] can repeat the same shrinking factor over many steps. Better [[Glorot Weight Initialization|initialization]], rectifying activations, and gated [[Long Short-Term Memory|sequence memory]] are among the responses discussed in the book. The obstacle is practical rather than proof that deep or recurrent networks are impossible to train.

# References

[[deeplearning_mit.epub]]
