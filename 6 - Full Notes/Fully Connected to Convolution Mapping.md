2026-09-28 03:43

Status: #baby

Tags: [[Neural Network Hardware Acceleration]]

# Fully Connected to Convolution Mapping

Fully connected to convolution mapping reformulates a dense neural layer as a convolution-like operation so one accelerator datapath can support both layer types. Inputs, weights, and batch elements are reshaped into the dimensions expected by the convolution engine.

The mapping increases hardware reuse but its efficiency depends on layout. [[Input-Major Neural Layer Mapping]] and [[Weight-Major Neural Layer Mapping]] organize the same dense computation around different reuse opportunities.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

