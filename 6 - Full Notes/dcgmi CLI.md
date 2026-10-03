2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Sharing and Fleet Management]]

# dcgmi CLI

The `dcgmi` CLI is the command-line client for NVIDIA Data Center GPU Manager. It can discover visible devices, inspect health and statistics, run diagnostics, and support scripted operational checks against the [[DCGM Host Engine]].

Command flags vary across DCGM releases, so a safe runbook first consults the help installed with the environment, such as discovery and health-help commands, before targeting production groups or devices. Scripts should record results and treat remediation as an explicit policy decision.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

