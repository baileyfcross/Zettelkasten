2026-10-11 21:26

Status: #baby

Tags: [[Docker Container Security]]

# Docker Runtime Secret Injection

Docker runtime secret injection supplies a credential or key when a service starts instead of storing it in the image or ordinary committed configuration. Swarm secrets and Compose secret declarations can expose selected values to only the services that request them, commonly as mounted files.

This separation supports rotation without rebuilding application layers and reduces leakage through image history. The source secret store, file permissions, service authorization, audit trail, and application reload behavior still determine the strength of the mechanism; injection is delivery, not complete secret governance.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
