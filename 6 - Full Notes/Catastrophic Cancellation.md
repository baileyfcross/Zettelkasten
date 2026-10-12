2026-10-07 17:18

Status: #baby

Tags: [[Numerical Error and Conditioning]]

# Catastrophic Cancellation

Catastrophic cancellation occurs when floating-point subtraction removes the leading digits of two nearly equal approximations, leaving a result dominated by their earlier representation errors. The subtraction does not create those input errors, but it exposes and greatly magnifies their relative importance.

The computational identity for sample variance can suffer this problem because it subtracts a term based on the squared sum from a sum of squares. Centered or recursively updated formulations such as [[Two-Pass Variance Algorithm]] and [[West Online Variance Algorithm]] avoid that difference of large, close quantities.

# References

[[statisticalcomputingincplusplusandr.pdf]]
