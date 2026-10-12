2026-10-07 17:18

Status: #baby

Tags: [[Statistical Computing Workflows]]

# Two-Pass Variance Algorithm

The two-pass variance algorithm first computes the sample mean and then makes a second pass to accumulate squared deviations from that mean. The sample variance is the resulting sum divided by one less than the sample size.

Centering each observation before squaring avoids subtracting two very large, nearly equal accumulated quantities. Its cost is the need to retain or reread the data, which can be undesirable for a stream; [[West Online Variance Algorithm]] trades the second pass for a stable recursive update.

# References

[[statisticalcomputingincplusplusandr.pdf]]
