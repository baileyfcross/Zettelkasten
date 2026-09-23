2026-09-22 23:34

Status: #baby

Tags: [[TLS Authentication and Secure Remote Access]]

# Basic Authentication

Basic authentication places a username and password in the HTTP `Authorization` header after applying a transport-safe text encoding. The encoding is reversible and provides no cryptographic confidentiality.

The scheme is simple to implement but exposes reusable credentials whenever the transport is not protected. It should therefore be used only through an encrypted channel and with careful credential handling.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
