2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Security and PKI]]

# Active Directory Certificate Services

Active Directory Certificate Services is the Windows Server role for building a certificate authority and related enrollment services. The Certification Authority role service supplies the issuing engine; optional web enrollment and policy services support browser-based or non-domain enrollment, Network Device Enrollment serves compatible network equipment, and an online responder can provide certificate-status responses.

An enterprise CA integrates with Active Directory, templates, and domain permissions, while a standalone CA can operate outside the domain and is suitable for an offline root. The server's final hostname and domain status should be settled before CA installation because changing them afterward is not a normal supported operation. A CA is durable trust infrastructure, so role-service selection, hierarchy, key protection, backup, revocation, and recovery must be designed before issuance begins.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
