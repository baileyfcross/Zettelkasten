2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Deployment Stage

A deployment stage applies a selected build artifact and environment configuration to a target. Stages let a release pipeline model destinations such as staging and production as ordered steps with separate variables and conditions.

The stage should deploy an existing artifact rather than silently compile a new one. This preserves the evidence gathered earlier in the pipeline as the release advances.

# References

[[aspnetcore3andreact.pdf]]
