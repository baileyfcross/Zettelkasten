2026-09-28 03:43

Status: #baby

Tags: [[Neural Network Hardware Acceleration]]

# Multi-FPGA Neural Network Partitioning

Multi-FPGA neural network partitioning distributes inference across several programmable devices. Division between layers assigns different layers to devices and can pipeline successive inputs; division inside a layer splits one layer's data and later combines partial results.

Between-layer division reduces coordination within a layer but follows the network's sequential depth. Inside-layer division exposes more parallelism for a large layer but requires scatter, gather, and reduction through a control FPGA or interconnect.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

