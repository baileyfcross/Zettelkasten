2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# EC2 Auto Scaling Group

An EC2 Auto Scaling group maintains a collection of EC2 instances between configured minimum, desired, and maximum capacities. It launches instances from an [[EC2 Launch Template]], replaces unhealthy members, and can distribute capacity across multiple [[AWS Availability Zone|Availability Zones]].

The group provides both availability and elasticity. Health replacement restores the desired fleet after failure, while scaling policies change desired capacity as demand changes. Pairing the group with [[Elastic Load Balancing]] lets new healthy instances receive traffic automatically.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
