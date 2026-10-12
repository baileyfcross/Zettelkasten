2026-09-22 23:34

Status: #baby

Tags: [[TLS Authentication and Secure Remote Access]]

# TLS Handshake

A TLS handshake establishes a protected session before ordinary application data is exchanged. The client and server identify supported cryptographic choices, the server presents identity evidence, and the endpoints derive session keys for encrypted communication.

Identity verification and key negotiation are separate responsibilities within the exchange. A connection is not trustworthy merely because encryption was selected; the client must also validate that the certificate identifies the intended server.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
