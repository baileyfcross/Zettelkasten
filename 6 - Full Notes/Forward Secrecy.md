2026-09-22 23:34

Status: #baby

Tags: [[TLS Authentication and Secure Remote Access]]

# Forward Secrecy

Forward secrecy prevents later compromise of a server's long-term private key from automatically revealing earlier recorded sessions. Each session uses ephemeral secret material that is not recoverable from the long-term key alone.

The session key must be destroyed after the session ends. Persisting it beyond that lifetime would preserve the missing information an attacker needs to decrypt captured traffic.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
