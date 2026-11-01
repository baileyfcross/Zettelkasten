2026-10-07 17:18

Status: #baby

Tags: [[Numerical Error and Conditioning]] [[SIMD Numerical Accuracy and Statistics]]

# Catastrophic Cancellation

Catastrophic cancellation occurs when floating-point subtraction removes the leading digits of two nearly equal approximations, leaving a result dominated by their earlier representation errors. The subtraction does not create those input errors, but it exposes and greatly magnifies their relative importance.

The computational identity for sample variance can suffer this problem because it subtracts a term based on the squared sum from a sum of squares. Centered or recursively updated formulations such as [[Two-Pass Variance Algorithm]] and [[West Online Variance Algorithm]] avoid that difference of large, close quantities.

The book's single-pass mean and standard-deviation kernel accumulates $S_1=\sum x_i$ and $S_2=\sum x_i^2$, then forms $S_2/N-(S_1/N)^2$. Although this reduces memory passes and vectorizes readily, the final subtraction can discard significant digits when the two terms are close. More throughput therefore does not establish an adequate numerical result.

# References

[[statisticalcomputingincplusplusandr.pdf]]

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
