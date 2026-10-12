2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# Target Tracking Scaling

Target tracking scaling adjusts an [[EC2 Auto Scaling Group]] to keep a chosen metric near a configured target, such as average CPU utilization. The policy adds capacity when the metric rises above the target and removes capacity when demand subsides.

This resembles a thermostat: the operator declares the desired operating level rather than enumerating every scaling adjustment. The metric should correlate meaningfully with load, and the fleet's warmup time must be considered so newly launched instances are not mistaken for ineffective capacity.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
