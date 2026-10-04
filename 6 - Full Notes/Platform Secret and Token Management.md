2026-10-03 22:25

Status: #baby

Tags: [[Platform Security and Software Supply Chain]]

# Platform Secret and Token Management

Platform secret and token management keeps credentials out of source repositories and ordinary deployment artifacts, restricts who and what may retrieve them, and supports rotation without rebuilding application images. A dedicated source of truth can store the secret while an operator synchronizes references into the environments that need it.

The retrieval mechanism has a bootstrap credential of its own, so the trust chain must be explicit. Permissions should be tenant-scoped, audit activity should record access without exposing values, and rotation should propagate predictably. The selected pattern must protect certificates, passwords, and tokens through creation, distribution, use, replacement, and revocation.

# References

[[platformengineeringforarchitects.pdf]]
