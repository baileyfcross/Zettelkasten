2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]] [[Public-Key Cryptosystems and Digital Identity]]

# Digital Signature

A digital signature uses a private key to sign data and a corresponding public key to verify the result. Verification provides evidence that the signed content has not changed and that the signer possessed the private key.

Practical signature APIs usually hash the message and apply an asymmetric algorithm such as RSA to the digest using a defined padding scheme. Trust in the signature still depends on securely associating the public key with the claimed identity.

Digital signatures support [[Nonrepudiation]] by giving a recipient verifiable evidence that the holder of a private key signed particular content. The public key checks that evidence, while a certificate or other trusted association is still needed to connect the key to a claimed sender.

The message digest makes verification sensitive to any content change without requiring the asymmetric operation to process the whole message directly. Signing applies the private-key operation to that digest, and verification recomputes the digest before checking it with the public key.

A signature scheme separates key generation, signing, and verification. Signing consumes the private key and message, while verification consumes the message, signature, and public key and returns acceptance or rejection. The Java examples implement `SHA256withRSA` and an ElGamal signature, emphasizing that practical implementations normally sign a [[Cryptographic Hash Function|digest]] rather than applying the public-key operation directly to an arbitrarily long message.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[cybersecurity.epub]]

[[programmingincexam70-483mcsdguide.pdf]]

[[cryptographyandcryptanalysisinjava.epub]]
