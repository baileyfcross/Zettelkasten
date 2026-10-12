2026-09-27 12:11

Status: #baby

Tags: [[Multi-Agent Incident Response]]

# Specialist Prompt Contracts

Specialist prompt contracts give each incident agent one responsibility and one structured result. A deployment analyst focuses on pipeline evidence, an application-health analyst focuses on runtime symptoms, and a runbook agent recommends only actions supported by the supplied runbook.

Each contract treats operational text as untrusted, forbids destructive instructions, and requires JSON fields suited to the role. This prevents specialists from competing to solve the whole incident and makes their outputs easier to validate, compare, and combine during final synthesis.

# References

[[agenticaifordevopsengineers.pdf]]
