2026-09-27 18:58

Status: #baby

Tags: [[AWS Security and Compliance]]

# AWS Secrets Manager

AWS Secrets Manager stores and retrieves sensitive application values such as database credentials and API keys. Access is controlled through IAM, values can be encrypted with [[AWS Key Management Service]], and supported secrets can be rotated automatically.

Retrieving a secret at runtime avoids embedding it in source code or a machine image, but applications must protect the returned value in memory and logs. Rotation is effective only when both the target system and every consumer can transition to the new credential safely.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
