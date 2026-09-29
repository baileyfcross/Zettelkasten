2026-09-28 04:01

Status: #baby

Tags: [[Digital Image Representation and Quality]]

# Predictive and Entropy Image Coding

Prediction estimates a sample or transformed value from information already decoded, then stores the smaller residual between the prediction and the actual value. Accurate prediction concentrates residuals around zero and makes them easier to compress.

Entropy coding assigns compact representations to common symbols and longer representations to rare ones without changing their values. These techniques are complementary: prediction reshapes the data distribution, and entropy coding exploits that distribution. PNG filters and WebP block prediction are format-specific examples. See [[PNG Scanline Filters]] and [[WebP Block Prediction]].

# References

[[highperformanceimages.pdf]]
