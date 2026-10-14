2026-10-03 22:25

Status: #baby

Tags: [[Developer Self-Service and Platform Experience]]

# Platform and Software Lifecycle Separation

Platform and software lifecycles overlap but have different users, release risks, and operating responsibilities. An application directly serves an end user, while the platform provides the services through which many application teams build, deliver, and operate their products.

A platform change can affect every tenant and may coordinate many components, so its rollout, compatibility, and support window cannot be treated like a single application deployment. The platform team owns the reliability and serviceability of shared capabilities; application teams own the behavior of their workloads within those contracts. Clear separation prevents either side from assuming the other will manage its lifecycle obligations.

# References

[[platformengineeringforarchitects.pdf]]
