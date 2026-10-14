2026-10-11 21:26

Status: #baby

Tags: [[Docker Container Security]]

# Falco Runtime Detection

Falco observes kernel events through eBPF probes or a kernel module and evaluates them against rules describing suspicious runtime behavior. Examples include a shell appearing in a container, writes to protected system paths, or unexpected network activity from a process.

Alerts can include container and image metadata and flow to logs, webhooks, or response systems. Falco complements image scanning and admission controls because those tools decide what may be deployed, while runtime detection asks whether an accepted workload is behaving unexpectedly after execution begins.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
