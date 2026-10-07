2026-10-07 17:18

Status: #baby

Tags: [[Numerical Error and Conditioning]]

# West Online Variance Algorithm

West's online variance algorithm updates a running mean and a centered sum of squares when each observation arrives. For observation $x_k$, it first updates the mean and then adds the product of the old and new deviations to the accumulated squared-deviation term.

The sample variance after $n$ observations is the accumulated term divided by $n-1$. The algorithm requires constant storage and one pass, yet avoids the severe [[Catastrophic Cancellation]] of subtracting a squared total from a sum of squares.

# References

[[statisticalcomputingincplusplusandr.pdf]]
