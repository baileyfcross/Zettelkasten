2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring Boot Health Indicator

A Spring Boot health indicator contributes one named status and optional diagnostic details to the aggregate Actuator health endpoint. Boot auto-configures indicators for recognized dependencies, while an application can implement a blocking or reactive indicator for a domain-specific dependency such as an external API or warmed cache.

Health is consumed by operators, load balancers, and orchestrators, so the indicator should answer an actionable availability question rather than expose arbitrary internal data. Disabling an irrelevant dependency check can prevent false alarms, but hiding a required dependency produces false health. Sensitive details should remain protected even when the overall status is public.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
