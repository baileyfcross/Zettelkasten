2026-11-08 14:08

Status: #baby

Tags: [[Microservice Architecture Adoption]]

# Strangler Fig Pattern

The Strangler Fig pattern replaces a legacy application's capabilities incrementally rather than through one complete cutover. A routing boundary directs selected functions or requests to a new service while the remaining behavior continues through the existing system; the old implementation contracts as each replacement becomes trustworthy.

This migration limits the blast radius of each step and allows operational learning before the next extraction. It still requires deliberate handling of shared data, traffic routing, observability, security, team ownership, and rollback. Branch by abstraction can place old and new implementations behind one interface, while a parallel run can compare their results before traffic depends on the replacement.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
