2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]]

# NVIDIA Multi-Instance GPU

NVIDIA Multi-Instance GPU partitions supported physical hardware into independent instances with dedicated memory and compute slices. Kubernetes can advertise named MIG profiles as extended resources and schedule pods against a profile that matches their required partition.

MIG provides stronger isolation and more predictable performance than software-only sharing, but the available shapes are constrained by the GPU model and active partition layout. Reconfiguration and scheduling must consider how profiles consume the device's finite slices.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

