2026-09-14 02:44

Status: #baby

Tags: [[Applied Cryptography and PKI]] [[TLS Authentication and Secure Remote Access]] [[Windows Server Security and PKI]]

# Public Key Infrastructure

Public key infrastructure manages the creation, distribution, use, storage, and revocation of digital certificates and their keys. It associates an online identity with a public key so another party can decide whether to trust a presented credential.

PKI supports encrypted sessions, identity checks, signatures, and secure key exchange. [[Certificate Authority|Certificate authorities]] issue or validate the bindings, while private-key protection remains the responsibility of the identified holder.

A Windows PKI can be organized as a hierarchy: a root authority establishes the trust anchor, and subordinate issuing authorities enroll users, computers, services, or network devices. Templates define what a certificate may contain, who may enroll, and how long it remains valid. Deployment planning must therefore cover authority placement, key custody, enrollment paths, renewal, revocation, and recovery rather than treating certificate issuance as a one-time server role installation.

# References

[[cybersecurity.epub]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[masteringwindowsserver2025_fifthedition.pdf]]
