2026-09-28 03:43

Status: #baby

Tags: [[FPGA Accelerator Co-Design]]

# Fixed-Point Accelerator Datapath

A fixed-point accelerator datapath represents numerical values with a predetermined scale and bit width instead of general floating point. This can reduce logic, latency, and power, allowing more parallel units within the same FPGA.

The representation must still cover the algorithm's range and accumulated error. Quantization choices should be verified against software results, especially when repeated reductions amplify rounding.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

