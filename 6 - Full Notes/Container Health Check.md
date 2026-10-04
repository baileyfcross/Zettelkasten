2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Container Health Check

A container health check periodically runs a command that tests whether the application inside a running container is functioning. Interval, timeout, retries, start period, and startup checks control when results become healthy or unhealthy and keep slow initialization from being mistaken immediately for failure.

The probe should test a meaningful service behavior with low cost and deterministic exit status. Podman can report the state and optionally act on failure, but a health command does not repair the application or prove every dependency is correct. It supplies one operational signal to combine with [[Container Log Capture]] and external monitoring.

# References

[[podmanfordevopssecondedition.pdf]]
