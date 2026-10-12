2026-09-27 18:58

Status: #baby

Tags: [[AWS Security and Compliance]]

# AWS Encryption at Rest and in Transit

Encryption at rest protects stored data, while encryption in transit protects data moving across a network. AWS services commonly integrate storage encryption with [[AWS Key Management Service]] and use TLS certificates from services such as [[AWS Certificate Manager]] for protected connections.

Encryption reduces exposure when storage media or network traffic is accessed improperly, but its value depends on key control, identity permissions, endpoint validation, and correct service configuration. It complements rather than replaces authorization, logging, backups, and data minimization.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
