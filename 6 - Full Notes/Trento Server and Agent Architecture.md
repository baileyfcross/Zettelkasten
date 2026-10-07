2026-10-07 18:14

Status: #baby

Tags: [[SLES Container and SAP Workload Operations]]

# Trento Server and Agent Architecture

Trento is a SUSE administration and monitoring solution for SAP infrastructure built from a central server and an agent on each monitored host. Agents discover local system information and report it, while the server presents the web interface and coordinates configuration checks, monitoring, documentation, and recommended remediations.

The server includes cooperating components for control, check execution, persistence, messaging, and metrics, so its own health must be operated as a distributed application. A silent host may indicate agent or communication failure rather than a healthy SAP system; heartbeat and agent logs are therefore part of the evidence.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
