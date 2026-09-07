2026-09-06 20:41

Status: #baby

Tags: [[Web Application Deployment]]

# Self-Signed TLS Certificate

A self-signed TLS certificate is signed by its own key rather than by a certificate authority already trusted by clients. It can encrypt a test connection and demonstrate HTTPS configuration, but browsers cannot establish public trust automatically.

The deployment examples use self-signed certificates with local host mapping to test Windows and Linux hosting without purchasing a domain or certificate. A public production service requires an appropriately trusted certificate.

# References

[[aspnetcore3andangular9_3ed.pdf]]
