2026-10-07 17:18

Status: #baby

Tags: [[Statistical Computing Workflows]] [[SIMD Numerical Accuracy and Statistics]]

# Two-Pass Variance Algorithm

The two-pass variance algorithm first computes the sample mean and then makes a second pass to accumulate squared deviations from that mean. The sample variance is the resulting sum divided by one less than the sample size.

Centering each observation before squaring avoids subtracting two very large, nearly equal accumulated quantities. Its cost is the need to retain or reread the data, which can be undesirable for a stream; [[West Online Variance Algorithm]] trades the second pass for a stable recursive update.

For a population standard deviation, the same centered second pass divides by $N$ rather than $N-1$ and takes the square root. The book traverses the first pass backward and the second forward so the end of the first traversal leaves the beginning of a large array warm for the next one, a cache-oblivious improvement that does not require knowing the cache size.

# References

[[statisticalcomputingincplusplusandr.pdf]]

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
