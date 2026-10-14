2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Hyper-V Checkpoint

A Hyper-V checkpoint records a virtual machine's configuration and virtual-disk state so the VM can later return to that point. Production checkpoints use guest-aware backup mechanisms to create a data-consistent recovery state, while standard checkpoints can also capture memory and device state for a more exact lab rollback.

Checkpoints are temporary change-control tools, not backups. Their differencing disks depend on the parent chain, consume growing storage, and can create significant merge work when deleted. Long-lived checkpoints increase operational risk and do not protect against loss of the host or storage containing the chain. Before a risky update, administrators should prefer a production checkpoint where supported, monitor capacity, validate the application afterward, and merge the checkpoint promptly once rollback is no longer needed.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
