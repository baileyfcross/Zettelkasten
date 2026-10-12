2026-09-30 17:53

Status: #baby

Tags: [[LLM-Assisted Software Testing]]

# LLM-Assisted Regression Testing

LLM-assisted regression testing analyzes a change, affected code, requirements, and prior failures to recommend which existing tests to run and which new cases may be needed. This can focus limited test time on behavior most likely to have changed.

Selection remains a risk decision and should be checked against deterministic dependency and coverage information. The model must not silently remove mandatory suites, and every generated regression case requires execution and stable expected outcomes.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
