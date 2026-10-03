2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA AI Inference Stack]]

# Inference Latency-Throughput Tradeoff

The inference latency-throughput tradeoff balances the response time of an individual request against the amount of work completed per unit time. Batching can keep a GPU busier and amortize fixed overhead, but waiting to collect requests can increase latency.

Configuration should follow the service-level objective and real arrival pattern. Dynamic batch delay, preferred sizes, model concurrency, request preprocessing, GPU partition size, and network behavior can all shift the balance, so aggregate throughput cannot substitute for tail-latency measurement.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

