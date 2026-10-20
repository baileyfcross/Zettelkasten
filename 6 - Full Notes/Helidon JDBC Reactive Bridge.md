2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon JDBC Reactive Bridge

Helidon DB Client adapts an ordinary blocking JDBC driver to its reactive, nonblocking database API by running JDBC work through an executor service. The application therefore uses the common client contract even though the underlying relational driver was not designed as reactive.

This bridge preserves access to the JDBC ecosystem while separating its blocking implementation from the subscriber-facing flow. The related [[Helidon DB Client Backpressure]] controls how result rows are delivered instead of forcing the whole result set on a consumer at once.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
