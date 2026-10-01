2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Passkey Authentication

Passkey authentication uses a FIDO2 public-key credential bound to a user account. The private key remains with an authenticator such as a security key or supported device, while the service stores a public key and verifies a signed challenge during sign-in.

Because the signature is scoped to the legitimate service and no shared password crosses the network, a passkey is resistant to ordinary credential phishing and password replay. Microsoft Entra can allow device-bound or synced passkeys according to policy and can require them through an authentication strength. Registration may be bootstrapped with a [[Temporary Access Pass]], after which lifecycle controls must cover loss, replacement, and revocation of the authenticator.

# References

[[masteringmicrosoftentraid.pdf]]
