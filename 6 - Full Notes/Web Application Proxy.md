2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Networking and Remote Access]]

# Web Application Proxy

Web Application Proxy is a Remote Access role service that publishes selected internal web applications through an external-facing reverse proxy. The proxy receives the client's HTTPS request and forwards approved traffic to the internal application, so the backend server does not need to be directly exposed to the internet.

Publishing requires externally resolvable names, trusted certificates, reachable backend URLs, and authentication behavior compatible with the application. Preauthentication can place an identity decision before the request reaches the backend, while pass-through leaves authentication to the application. The proxy narrows access to specific web services rather than providing general network reach, but it still sits at a trust boundary and needs hardening, monitoring, certificate maintenance, and a redundant design when the published application is critical.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
