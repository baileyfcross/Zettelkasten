2026-10-03 17:11

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# Real User Observability Signal

A real user observability signal captures how a person actually experiences a digital service, such as opening an application, loading a page, changing orientation, or completing a transaction. It complements server-side evidence by showing performance and failure at the consumer boundary.

Real-user evidence can reveal that an impact is limited to a browser, region, customer segment, or routing path. It should be collected with privacy-aware context so operators can identify the affected cohort without retaining personal data that is unnecessary for remediation.

The current source connects a browser session and user action to backend tracing. A frontend can create a session identifier, propagate trace context with its request, and correlate user-facing measures with the API path that handled the action. This is particularly useful when server health appears normal but a specific client flow, route, or transaction remains slow.

# References

[[observabilityintheai-nativeera.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
