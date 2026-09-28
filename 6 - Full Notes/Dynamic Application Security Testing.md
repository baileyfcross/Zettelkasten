2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native DevSecOps Controls]]

# Dynamic Application Security Testing

Dynamic application security testing probes a running application from the outside, looking for exploitable behavior in its exposed interfaces. Because it observes the assembled system, DAST can reveal configuration and integration problems that are invisible to source-only analysis.

DAST requires a deployed test target and therefore usually runs later than [[Static Application Security Testing]]. Its feedback should still enter the delivery pipeline before production promotion. Authenticated coverage, realistic test data, and careful rate limits determine whether the scan reaches meaningful paths without disrupting the environment.

# References

[[clouddevopsengineersguide.pdf]]
