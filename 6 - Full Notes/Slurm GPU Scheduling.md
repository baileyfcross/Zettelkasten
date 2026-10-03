2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Sharing and Fleet Management]]

# Slurm GPU Scheduling

Slurm GPU scheduling places queued batch, research, and high-performance-computing jobs on nodes that satisfy requested accelerator resources and constraints. Policies can control priority, fairness, reservations, limits, and access to full GPUs or configured MIG resources.

Interactive work can be launched with `srun`, batch work with `sbatch`, and queue state inspected with `squeue`, subject to site configuration. Slurm complements DCGM telemetry by making allocation decisions for queued jobs, whereas Kubernetes commonly schedules long-running container services and cloud-native workflows.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

