2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# NVIDIA Nsight Systems

NVIDIA Nsight Systems profiles the application-wide timeline across CPU activity, GPU kernels, memory transfers, synchronization, and idle gaps. It answers where time is being spent and can reveal that low GPU utilization originates in data loading, host work, transfers, or coordination.

A practical workflow begins with this broad view, then uses [[NVIDIA Nsight Compute]] after a particular slow kernel is identified. Nsight Systems complements fleet telemetry because it explains behavior inside one node and one application run rather than long-term device health.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

