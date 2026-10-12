2026-09-22 23:34

Status: #baby

Tags: [[TLS Authentication and Secure Remote Access]]

# HTTP Strict Transport Security

HTTP Strict Transport Security is a response policy that tells a browser to use HTTPS for a host for a defined period. After receiving the policy over a valid secure connection, the browser upgrades later HTTP attempts instead of first sending an insecure request.

HSTS reduces downgrade and first-request exposure after the policy is known. It does not replace a valid TLS certificate or correct server-side HTTPS configuration.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
