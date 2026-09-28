2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native Observability]]

# Alertmanager Notification Routing

Alertmanager receives alerts from Prometheus and determines how they should reach people or systems. It can deduplicate repeated instances, group related alerts, and route them by attributes such as service or severity to email, chat, or an on-call platform.

This separates detection from notification policy. A [[Prometheus Alert Rule]] states what condition matters; Alertmanager states who should know and through which channel. Grouping prevents one underlying failure from producing a flood of independent messages, while routing ensures a critical production symptom reaches the responsible responder rather than every team.

# References

[[clouddevopsengineersguide.pdf]]

