2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Hyper-V Container

A Hyper-V container runs a container image inside a lightweight, purpose-built virtual machine. The application retains the image and deployment model of a Windows container, but it receives a kernel boundary separate from the host and other containers. This strengthens isolation and relaxes some exact host-to-image kernel compatibility constraints.

The additional virtualized boundary consumes more memory and startup time than process isolation, though less operational machinery than a conventional general-purpose VM. Hyper-V isolation is useful for untrusted or multi-tenant workloads and when the image cannot safely share the host kernel. It does not remove container responsibilities: persistent state, image provenance, network policy, resource limits, and rebuild-based patching still need explicit design.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
