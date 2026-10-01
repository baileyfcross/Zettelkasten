2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra External and Network Access]]

# Verified ID Face Check

Verified ID Face Check adds a privacy-conscious facial comparison to a credential presentation. A verifier requests a face check against the trusted photo claim in a supported [[Verifiable Credential]], and the holder captures a live image through the wallet experience.

The service returns a confidence-based match result rather than sending the verifier the underlying credential photograph. This can strengthen assurance that the person presenting a credential is its subject while limiting unnecessary biometric disclosure. The relying application must still choose an appropriate confidence threshold, provide an alternative path for failed or inaccessible checks, and treat the result as one signal rather than proof of every identity claim.

# References

[[masteringmicrosoftentraid.pdf]]
