2026-09-27 18:58

Status: #baby

Tags: [[AWS Compute and Serverless Services]]

# EC2 Spot Instance

An EC2 Spot Instance uses spare AWS capacity at a large discount but can be interrupted when AWS needs the capacity back. It suits distributed, resumable, stateless, or otherwise interruption-tolerant workloads.

The application should checkpoint work, diversify capacity choices, and handle termination notices. A low price does not make Spot suitable for an irreplaceable database or a single critical server whose interruption cannot be absorbed.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
