2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA Data Center GPU Selection]]

# GPU Memory Capacity

GPU memory capacity is the amount of model data and runtime state that can reside on a device or assigned partition. A workable allocation must hold more than weights: training can require gradients, optimizer state, activations, and batches, while inference can require workspace, activations, request state, and a key-value cache.

Capacity determines whether the workload can run, whereas [[GPU Memory Bandwidth]] and [[GPU Compute Throughput]] influence how quickly it runs. Operational headroom is necessary because larger batches, longer context, concurrency, or temporary workspace can trigger out-of-memory failures even when the static model fits.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

