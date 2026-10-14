2026-09-14 02:44

Status: #baby

Tags: [[Applied Cryptography and PKI]]

# Asymmetric Encryption

Asymmetric encryption uses a mathematically related public and private key pair. Data encrypted for a recipient with the public key can be recovered with the corresponding private key, allowing secure exchange without first sharing one secret key.

It is slower than [[Symmetric Encryption]] and is therefore suited to small values such as session keys or signature operations. Secure protocols combine its key-management advantage with symmetric bulk-data performance.

The inverse key roles support [[Digital Signature|digital signatures]] as well as confidentiality: the private key produces evidence that the public key can verify. RSA is a representative .NET asymmetric algorithm, but its small-input and performance constraints reinforce the hybrid design rather than making it a bulk-data cipher.

# References

[[cybersecurity.epub]]

[[programmingincexam70-483mcsdguide.pdf]]
