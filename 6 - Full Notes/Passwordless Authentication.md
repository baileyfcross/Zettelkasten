2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Passwordless Authentication

Passwordless authentication proves identity with a device-bound or cryptographic method instead of a memorized shared secret. Microsoft Entra supports methods such as passkeys, certificate-based authentication, Windows Hello for Business, and the Microsoft Authenticator app.

The security gain comes from removing a reusable password that can be guessed, phished, sprayed, or replayed. Enrollment and recovery remain part of the trust boundary: a user may receive a short-lived [[Temporary Access Pass]] to register a strong method, while policy can require an authentication strength appropriate to the resource. Passwordless is therefore a credential-lifecycle design, not merely the absence of a password box.

# References

[[masteringmicrosoftentraid.pdf]]
