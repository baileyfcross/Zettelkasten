2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Passkey Authentication

Passkey authentication uses a FIDO2 public-key credential bound to a user account. The private key remains with an authenticator such as a security key or supported device, while the service stores a public key and verifies a signed challenge during sign-in.

Because the signature is scoped to the legitimate service and no shared password crosses the network, a passkey is resistant to ordinary credential phishing and password replay. Microsoft Entra can allow device-bound or synced passkeys according to policy and can require them through an authentication strength. Registration may be bootstrapped with a [[Temporary Access Pass]], after which lifecycle controls must cover loss, replacement, and revocation of the authenticator.

The enterprise-social source describes the same WebAuthn foundation: registration creates a key pair for a relying party, the service retains the public key, and the private key remains under the authenticator's control. A later challenge is signed only after local user verification such as a PIN or biometric. Because the credential is bound to the relying party, a convincing imitation site cannot use the signature for the legitimate site's origin.

# References

[[masteringmicrosoftentraid.pdf]]

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
