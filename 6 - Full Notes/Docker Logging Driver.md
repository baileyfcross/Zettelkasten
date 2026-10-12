2026-10-11 21:26

Status: #baby

Tags: [[Docker Observability Operations]]

# Docker Logging Driver

A Docker logging driver determines where the standard output and standard error streams of a container are delivered. Drivers can retain JSON files locally or forward events to facilities such as journald, syslog, or an external log system, and the choice can be set as a daemon default or overridden for one container.

Changing the driver affects collection, retrieval, failure behavior, and available metadata. The application should still emit structured events to standard streams, while the platform defines rotation, retention, forwarding, and access so instance replacement does not erase the only evidence of a failure.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
