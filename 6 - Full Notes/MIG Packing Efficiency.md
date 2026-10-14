2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Sharing and Fleet Management]]

# MIG Packing Efficiency

MIG packing efficiency describes how well the selected set of [[MIG Profile|MIG profiles]] fills the finite compute and memory slices of a physical GPU. Several small profiles can increase service density, while larger profiles give each workload more capacity but leave fewer placement combinations.

The best geometry follows the service catalog and observed demand rather than the goal of creating the most instances. A profile too small fails the workload, while a poor mixture can strand slices that no pending request can use even though the device is not fully allocated.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

