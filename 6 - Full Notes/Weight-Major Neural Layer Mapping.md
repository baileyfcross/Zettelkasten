2026-09-28 03:43

Status: #baby

Tags: [[Neural Network Hardware Acceleration]]

# Weight-Major Neural Layer Mapping

Weight-major neural layer mapping keeps or repeatedly reuses weight values while activations move through the accelerator. It is useful when model parameters dominate traffic or the same weights serve many input examples.

Weight reuse is not free if output accumulation or activation delivery becomes the new bottleneck. The mapping should be chosen from the network's batch size, layer dimensions, and available on-chip buffers.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

