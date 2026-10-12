2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]] [[Modern Software Delivery Foundations]]

# Graceful Degradation

Graceful degradation lets a system continue providing useful service when one component or dependency fails. A failure should be contained so unrelated operations can continue, perhaps with reduced capability or delayed work. The book relates this property to availability and describes isolating traffic into pools and buffering requests as ways to prevent a local overload from disabling the whole application.

Service degradation may be activated proactively for an anticipated surge or automatically after timeouts, repeated failures, or errors. It intentionally sacrifices lower-priority functions or user experiences to free resources and protect the system's critical work.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
