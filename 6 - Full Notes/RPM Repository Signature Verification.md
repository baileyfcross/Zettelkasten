2026-10-07 18:14

Status: #baby

Tags: [[SLES Software Lifecycle Management]]

# RPM Repository Signature Verification

RPM repository signature verification uses trusted signing keys to detect metadata or packages that were changed or did not originate from an accepted signer. Verification establishes a cryptographic relationship to a key; it does not prove that every signed package is defect-free or suitable for the system.

Importing a new key changes the local trust boundary and should follow verification of the key's source and fingerprint. Disabling checks to pass one installation converts a diagnosable provenance failure into an unaudited software change. Repository transport and entitlement complement signatures but do not replace them.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
