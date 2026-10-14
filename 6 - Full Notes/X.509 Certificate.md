2026-09-22 23:34

Status: #baby

Tags: [[TLS Authentication and Secure Remote Access]] [[Windows Server Security and PKI]]

# X.509 Certificate

An X.509 certificate binds an asserted identity to a public key and includes a digital signature from its issuer. A TLS client validates the signature and certificate chain to decide whether the server's presented key belongs to the named endpoint.

The certificate exposes a public key rather than the server's private key. Trust therefore depends on the issuing authority, validity constraints, hostname relationship, and protection of the corresponding private key.

Windows stores machine certificates in the local computer certificate store, commonly under Personal for certificates used by the host. Exporting a certificate with its private key produces a password-protected PFX suitable for controlled transfer or backup; exporting only the public certificate cannot reproduce the endpoint identity. Certificate chains may also require root and intermediate certificates so a relying party can validate the presented leaf back to a trusted authority.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[masteringwindowsserver2025_fifthedition.pdf]]
