2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Scoring and Graph Structure]]

# Graph Signal Smoothness

Graph signal smoothness measures how little a value assigned to each vertex changes across strongly weighted edges. For a signal $f$ and [[Graph Laplacian]] $L$, the quadratic form $f^TLf$ equals a weighted sum of squared differences $(f_i-f_j)^2$ across connected vertices.

A small value means neighboring vertices tend to receive similar values. In feature selection, a feature vector is treated as a signal over a sample graph; smooth features are considered consistent with the sample relationships. Scale and degree effects must be normalized before comparing different features.

# References

[[spectralfeatureselectionfordatamining.pdf]]

