2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# Step Scaling

Step scaling changes capacity by different amounts according to how far a monitored metric has moved beyond an alarm threshold. A modest breach might add one instance, whereas a severe breach can trigger a larger adjustment.

This gives an operator more explicit control than [[Target Tracking Scaling]], but it also requires carefully chosen thresholds and adjustment sizes. The steps should reflect the workload's response to added capacity and avoid overlapping or contradictory actions.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
