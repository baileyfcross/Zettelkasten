2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native DevSecOps Controls]]

# Repository Secret Scanning

Repository secret scanning looks for credentials, tokens, private keys, and other sensitive values in commits and proposed changes. Prevention at commit or pull-request time is important because deleting a secret in a later commit does not remove it from prior Git history or existing clones.

A positive match requires both removal from the repository and revocation or rotation of the exposed credential. Secrets used by automation should instead be injected from a managed store, with access constrained to the required job. [[Automatic Secret Rotation]] and [[Dynamic Secret|short-lived credentials]] reduce the exposure window if prevention fails.

# References

[[clouddevopsengineersguide.pdf]]
