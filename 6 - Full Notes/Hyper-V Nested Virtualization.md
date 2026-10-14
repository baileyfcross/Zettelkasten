2026-10-14 00:45

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Hyper-V Nested Virtualization

Hyper-V nested virtualization exposes processor virtualization extensions to a virtual machine so that the guest can run [[Hyper-V Role|Hyper-V]] and create another layer of virtual machines. It is useful for isolated labs, training, development, and testing configurations that would otherwise require several physical hosts.

The outer VM must be configured to expose its virtualization extensions before the inner hypervisor can start. Networking may also require MAC-address spoofing on the outer VM's virtual adapter so traffic from nested guests can traverse the surrounding virtual network. A nested design should be treated as a deliberate topology because every inner workload still depends on the compute, memory, storage, and network limits of the physical host and outer VM.

# References

[[windowsserver2025administrationfundamentals_fourthedition.pdf]]
