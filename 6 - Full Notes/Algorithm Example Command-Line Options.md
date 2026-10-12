2026-09-14 22:06

Status: #baby

Tags: [[C++ Partitional and Fuzzy Clustering]]

# Algorithm Example Command-Line Options

ClusLib examples use Boost program options to expose data files, cluster counts, seeds, iteration limits, run counts, and algorithm-specific thresholds. Default values support quick experiments, while help output documents the executable contract.

Parsing options outside the algorithm keeps the reusable class independent of command-line policy. The example transfers parsed values through Arguments and lets setup validation reject incompatible combinations.

# References

[[dataclusteringincplusplus.pdf]]

