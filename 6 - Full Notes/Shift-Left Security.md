2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native DevSecOps Controls]]

# Shift-Left Security

Shift-left security moves security feedback into planning, coding, and continuous integration instead of waiting for a final pre-production review. The goal is not to make developers solely responsible for security, but to make common defects inexpensive to find while the change and its context are still fresh.

A practical pipeline combines [[Static Application Security Testing]], dependency checks, secret scanning, container and infrastructure scans, and an explicit [[CI Security Quality Gate]]. Runtime testing and monitoring remain necessary because early analysis cannot observe every behavior or production condition.

# References

[[clouddevopsengineersguide.pdf]]
