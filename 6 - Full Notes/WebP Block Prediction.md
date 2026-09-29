2026-09-28 04:01

Status: #baby

Tags: [[Modern Web Image Formats]]

# WebP Block Prediction

Lossy WebP predicts each block from already available neighboring pixels using one of several prediction modes. It then transforms and encodes the difference between the prediction and the actual block.

A good prediction leaves small residual values with many zeros, which compress more efficiently than the raw samples. WebP uses smaller transform blocks than JPEG and can choose prediction behavior according to local structure. This is a concrete instance of [[Predictive and Entropy Image Coding]].

# References

[[highperformanceimages.pdf]]
