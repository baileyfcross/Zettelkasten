2026-09-06 20:41

Status: #baby

Tags: [[Web Application Deployment]] [[Windows Server Security and PKI]]

# Self-Signed TLS Certificate

A self-signed TLS certificate is signed by its own key rather than by a certificate authority already trusted by clients. It can encrypt a test connection and demonstrate HTTPS configuration, but browsers cannot establish public trust automatically.

The deployment examples use self-signed certificates with local host mapping to test Windows and Linux hosting without purchasing a domain or certificate. A public production service requires an appropriately trusted certificate.

Self-signing is also how a root certificate authority establishes the top of a certificate hierarchy. That controlled PKI use differs from assigning an arbitrary self-signed server certificate to a production website: clients must explicitly trust the root, while a public-facing endpoint normally needs a chain to an authority already present in client trust stores. Windows Admin Center may be installed with a self-signed certificate for a lab, but a production deployment should replace it with an appropriately trusted certificate.

# References

[[aspnetcore3andangular9_3ed.pdf]]

[[masteringwindowsserver2025_fifthedition.pdf]]
