2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# IdentityServer Signing Credential

An IdentityServer signing credential signs issued tokens so a protected API can verify that they came from the trusted authorization server and were not altered. A development credential is convenient for local setup but is not the intended production identity of the server.

The project replaces its temporary credential with a certificate selected from the Windows certificate store by thumbprint. Key deployment and trust must be planned separately from application code; a self-signed demonstration certificate is not presented as production assurance.

# References

[[c8andnetcore30projectsusingazure.pdf]]
