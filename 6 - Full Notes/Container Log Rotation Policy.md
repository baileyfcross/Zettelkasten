2026-10-11 21:26

Status: #baby

Tags: [[Docker Observability Operations]]

# Container Log Rotation Policy

A container log rotation policy limits the size and number or age of local log files retained by the Docker logging driver. It prevents an otherwise healthy workload from exhausting host storage through unbounded standard-output capture.

Local rotation is a capacity safeguard rather than a complete retention strategy. Events needed for investigation, compliance, or long-term analysis should be shipped to durable centralized storage before old files are removed, and the policy should be tested against peak log volume so useful incident context is not rotated away too quickly.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
