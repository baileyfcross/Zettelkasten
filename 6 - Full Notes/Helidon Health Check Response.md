2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Health Check Response

A Helidon health-check response names a procedure, reports it as `UP` or `DOWN`, and can attach diagnostic data. A builder can set status from a boolean and add key-value fields before producing the immutable response.

For a simpler decision, static `up(name)` and `down(name)` forms create a named result directly. Both construction styles feed the same aggregate health JSON; the difference is how much contextual detail the check supplies.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
