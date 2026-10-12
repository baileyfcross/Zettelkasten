2026-09-28 03:43

Status: #baby

Tags: [[Neural Network Hardware Acceleration]]

# Input-Major Neural Layer Mapping

Input-major neural layer mapping organizes a fully connected computation so input values remain the dominant reusable data while weights stream through the engine. It can map batches and kernel dimensions into a convolution representation that matches an input-stationary datapath.

The benefit depends on layer dimensions and buffer organization. A mapping that maximizes input reuse may increase weight traffic, so it should be compared with [[Weight-Major Neural Layer Mapping]] for the actual network.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

