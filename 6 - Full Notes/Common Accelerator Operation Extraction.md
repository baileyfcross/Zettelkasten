2026-09-28 03:43

Status: #baby

Tags: [[FPGA Accelerator Co-Design]]

# Common Accelerator Operation Extraction

Common accelerator operation extraction identifies arithmetic and data-access kernels shared by several algorithms. A clustering accelerator, for example, can reuse vector distance, minimum search, accumulation, and memory-transfer structures across k-means, PAM, SLINK, and DBSCAN.

Factoring common operators produces a more versatile accelerator than duplicating four complete algorithms. It also forces a tradeoff between generality and the extra multiplexing or control logic needed to support several behaviors.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

