2026-09-27 18:58

Status: #baby

Tags: [[AWS Security and Compliance]]

# AWS Key Management Service

AWS Key Management Service creates and controls cryptographic keys used by integrated AWS services and applications. Key policies and identity permissions determine who may administer a key and who may use it for operations such as encrypting, decrypting, or generating data keys.

KMS centralizes key lifecycle controls and records API activity through CloudTrail. The key policy is a critical authorization boundary: encrypted data remains exposed to principals that are allowed to decrypt it, so storage permissions and key permissions must be designed together.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
