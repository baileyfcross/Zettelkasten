2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Security and PKI]]

# Certificate Signing Request

A certificate signing request contains a public key and requested identity information for submission to a certificate authority. The corresponding private key is generated and retained by the requester; the CA validates the request according to its policy and returns a signed certificate that binds the approved identity to that public key.

For a public TLS certificate, the requested names must include every hostname clients are expected to validate, and proof of control may be required by the external authority. When the signed certificate returns, it must be installed on the system that holds the matching private key. A certificate and private key that do not match cannot establish the intended identity. Exporting that identity for transfer normally requires a protected PFX rather than copying only the public certificate.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
