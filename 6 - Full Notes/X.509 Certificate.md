2026-09-22 23:34

Status: #baby

Tags: [[TLS Authentication and Secure Remote Access]]

# X.509 Certificate

An X.509 certificate binds an asserted identity to a public key and includes a digital signature from its issuer. A TLS client validates the signature and certificate chain to decide whether the server's presented key belongs to the named endpoint.

The certificate exposes a public key rather than the server's private key. Trust therefore depends on the issuing authority, validity constraints, hostname relationship, and protection of the corresponding private key.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
