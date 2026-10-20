2026-10-19 22:48

Status: #baby

Tags: [[Helidon Metrics Instrumentation]]

# Helidon Base Metrics Endpoint

The Helidon `/metrics/base` endpoint exposes optional MicroProfile base metrics supplied by the runtime. These describe JVM and operating-system state such as heap use and commitment, garbage-collection count and time, uptime, thread counts, loaded classes, available processors, system load, and process CPU activity.

Base measurements are implementation-maintained rather than declared by application resource methods. Their output identifies `mp_scope="base"`, while custom measurements normally appear under the separate application endpoint.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
