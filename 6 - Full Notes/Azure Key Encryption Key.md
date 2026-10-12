2026-09-27 21:45

Status: #baby

Tags: [[Azure Security Architecture and Operations]]

# Azure Key Encryption Key

An Azure key encryption key protects another key, usually a data encryption key, instead of encrypting the application data directly. Envelope encryption lets data be processed efficiently with symmetric data keys while a separately governed key encrypts or wraps those keys. Rotating a key encryption key can therefore protect large datasets without re-encrypting every data block, although architects must still design versioning, recovery, access policy, auditing, and deletion safeguards.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
