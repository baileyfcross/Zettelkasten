2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# AWS Auto Scaling Policy

An Auto Scaling policy defines when and how an [[EC2 Auto Scaling Group]] changes its desired capacity. A policy can react to monitored demand, maintain a target metric, make stepped adjustments after thresholds are crossed, or schedule known capacity changes.

Effective policies balance responsiveness against stability. Scaling too slowly can harm availability, while scaling too aggressively can add cost or cause oscillation. Minimum and maximum capacities bound the policy's choices, and cooldown or warmup behavior gives new instances time to become useful.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
