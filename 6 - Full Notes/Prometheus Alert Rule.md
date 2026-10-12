2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native Observability]]

# Prometheus Alert Rule

A Prometheus alert rule evaluates a PromQL expression and declares an alert when the condition remains true for a specified duration. Requiring persistence prevents a short transient from paging an operator for a problem that corrected itself before intervention was possible.

The rule should name the affected service, severity, and useful context rather than merely expose a raw threshold. Prometheus detects the condition, while [[Alertmanager Notification Routing]] deduplicates, groups, and sends the resulting alert. The threshold should correspond to user impact or an operational objective so it produces an actionable signal instead of alert noise.

# References

[[clouddevopsengineersguide.pdf]]

