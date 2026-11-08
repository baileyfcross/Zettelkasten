2026-09-05 15:58

Status: #baby

Tags: [[Live Game Operations]] [[Modern Software Delivery Foundations]]

# Canary Deployment

A canary deployment exposes a new version or feature to a limited portion of the live population before wider release. Operational and player metrics from that group reveal failures or harmful effects while the potential impact remains bounded.

The release expands only when evidence meets predefined expectations. The method requires observability and a fast way to stop or reverse exposure.

Platform and SRE practices use a canary release as a low-risk production change mechanism: a limited audience receives the new version while telemetry is compared with the established version. Promotion or rollback depends on predefined health and business criteria rather than elapsed time alone.

In Kubernetes, ingress or another routing layer can assign a small traffic weight to the candidate while the stable deployment serves the remainder. A canary for a stateful Jakarta EE application may also require coordination with session handling, database changes, and application-server behavior; traffic percentage alone is not an isolation boundary.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[agilegamedevelopment2e.pdf]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
