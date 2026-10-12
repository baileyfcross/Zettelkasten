2026-09-27 18:58

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# Amazon S3 Encryption

Amazon S3 encryption protects stored objects with server-side or client-side approaches. Server-side options include S3-managed keys, KMS keys with additional control and auditability, customer-provided keys, and dual-layer KMS encryption for requirements that call for two cryptographic layers.

Transport should also use TLS. Encryption does not replace access control: a principal authorized to read an object may receive decrypted data, while KMS-based protection additionally requires permission to use the key.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
