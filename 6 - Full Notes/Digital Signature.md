2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]]

# Digital Signature

A digital signature uses a private key to sign data and a corresponding public key to verify the result. Verification provides evidence that the signed content has not changed and that the signer possessed the private key.

Practical signature APIs usually hash the message and apply an asymmetric algorithm such as RSA to the digest using a defined padding scheme. Trust in the signature still depends on securely associating the public key with the claimed identity.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
