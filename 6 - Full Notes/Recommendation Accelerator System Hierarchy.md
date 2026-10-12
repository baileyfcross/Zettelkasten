2026-09-28 03:43

Status: #baby

Tags: [[Recommendation Hardware Acceleration]]

# Recommendation Accelerator System Hierarchy

A recommendation accelerator system hierarchy separates hardware, kernel, and user-space responsibilities. The hardware layer contains training and prediction units plus DMA; kernel drivers wrap registers and memory; a runtime library presents simpler calls to applications.

This layering keeps application code from manipulating every device register directly. It also clarifies where overhead occurs: model logic in the application, control transitions through the runtime and driver, and bulk data movement through DMA.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

