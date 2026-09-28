2026-09-28 03:43

Status: #baby

Tags: [[Neural Network Hardware Acceleration]]

# Neural Network Weight Compression

Neural network weight compression reduces the storage and transfer required for model parameters through sparsity, quantization, or encoded representations. If the compressed model fits in on-chip SRAM, many costly DRAM accesses can disappear.

Hardware must avoid spending more work decoding or load-balancing the compressed form than it saves. Sparse matrices also create irregular work, so [[Neural Network Accelerator Pruning]] and the execution architecture should be designed together.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

