2026-09-09 00:00

Status: #baby

Tags: [[Cloud Security Monitoring and Resilience]] [[Applied Cryptography and PKI]] [[TLS Authentication and Secure Remote Access]] [[Windows Server Security and PKI]]

# Certificate Authority

A certificate authority is a trusted party that signs digital certificates used to associate an identity with a public cryptographic key. A communicating endpoint can use that signature when deciding whether the presented certificate belongs to a party it should trust.

Certificates help establish an [[Encrypted Communication Channel]], but trust also depends on correct names, validity periods, protected private keys, and an accepted authority chain. A certificate does not authorize every action by the identified party.

Within [[Public Key Infrastructure]], a certificate authority supports the creation, distribution, management, and revocation of certificates that bind identities to public keys. A client authenticates a presented certificate before relying on it during secure-session establishment.

In a Windows enterprise, the root CA anchors the certification path with a self-signed certificate. Subordinate or issuing CAs receive certificates from that root and perform routine enrollment. A small environment may combine those responsibilities in one enterprise root CA, while a larger design can keep a standalone root offline and use domain-integrated issuing CAs for day-to-day work. The CA name and hierarchy are durable design choices because issued certificates preserve the issuer identity.

# References

[[cloudcomputing_mit.epub]]

[[cybersecurity.epub]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[masteringwindowsserver2025_fifthedition.pdf]]
