2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Startup Check

A Helidon startup check reports whether initialization has progressed far enough for liveness and readiness results to be meaningful. A startup result of `DOWN` normally indicates that the service is still initializing and can later become `UP` if startup succeeds.

A custom startup procedure uses `@Startup`. The book's example examines CPU load, attaches diagnostic data, and reports through `/health/started`, keeping initialization state distinct from ongoing readiness and fatal liveness.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
