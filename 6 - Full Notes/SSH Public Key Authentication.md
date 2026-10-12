2026-09-22 23:34

Status: #baby

Tags: [[TLS Authentication and Secure Remote Access]], [[SLES Service Logging and Remote Operations]]

# SSH Public Key Authentication

SSH public key authentication proves that a client controls a private key corresponding to an authorized public key. The client signs authentication data, and the server verifies the signature without receiving the private key.

The server must associate the public key with an allowed account, while the client must protect its private key. The method avoids sending a reusable password but does not eliminate key lifecycle and authorization management.

An SLES administrator can store an authorized public key for the target account and keep the corresponding private key encrypted on the client. An SSH agent can hold a decrypted key for a bounded session, reducing repeated passphrase entry without turning the private key into server-side data.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
