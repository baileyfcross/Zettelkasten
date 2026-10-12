2026-09-28 03:43

Status: #baby

Tags: [[Neural Network Hardware Acceleration]]

# Neural Network Accelerator Data Locality

Neural network accelerator data locality keeps weights, activations, or partial sums near the processing elements that reuse them. Because moving data can cost more energy than the arithmetic itself, a mapping that reduces off-chip and on-chip transfers may outperform one with more nominal multipliers.

Loop order, tiling, stationary dataflow, buffer size, and layer shape determine which value should remain local. Locality must therefore be co-optimized with parallelism rather than added after the compute array is designed.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

