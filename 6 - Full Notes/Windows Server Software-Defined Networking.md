2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Networking and Remote Access]]

# Windows Server Software-Defined Networking

Windows Server software-defined networking separates network policy and control from individual physical devices. A centralized network controller can program virtual networks, addressing, access rules, gateways, and software load balancing across hosts. Hyper-V Network Virtualization overlays tenant or workload networks on the provider's physical fabric, allowing virtual addresses and policy to move with the workload.

SDN increases elasticity but adds a control plane that must itself be available and secured. Network Security Groups express traffic policy, gateways connect virtual and external networks, and encapsulation carries overlay traffic across the physical underlay. Operators must troubleshoot both layers: a virtual rule can block traffic even when switches and routes are healthy, while an underlay fault can affect many apparently isolated virtual networks at once.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
