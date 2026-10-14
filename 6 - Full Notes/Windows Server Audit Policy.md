2026-10-14 00:45

Status: #baby

Tags: [[Windows Server Security and PKI]]

# Windows Server Audit Policy

A Windows Server audit policy selects which security-relevant activities generate event records. Useful categories include successful and failed logons, account logons, policy changes, system events, object access, and administrative changes. Capturing both success and failure can reveal ordinary behavior, repeated unauthorized attempts, and the sequence of changes preceding an incident.

Audit value depends on deliberate scope. Logging too little leaves investigative gaps, while indiscriminate collection creates noise and storage pressure that can hide important events. Policies should follow the sensitivity of each server role, send high-value events into a protected monitoring workflow, define retention, and be tested by generating known events. Review then turns the log from a compliance artifact into evidence for detection and response.

# References

[[windowsserver2025administrationfundamentals_fourthedition.pdf]]
