2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Networking and Remote Access]]

# Always On VPN

Always On VPN is a Windows remote-access design in which policy causes a managed client to establish VPN connectivity automatically. A device tunnel can connect before user sign-in for machine management and domain-related services, while a user tunnel supplies access associated with the signed-in identity. Profiles define triggers, routes, names, and the VPN endpoint.

The design builds on standard VPN infrastructure and can use certificates for scalable authentication. Device and user tunnels should expose only the networks required for their purpose, especially because pre-logon machine access has different trust implications from an interactive user session. DNS behavior, split or forced tunneling, high availability, and certificate enrollment must be tested together so automatic connectivity does not conceal a route or identity failure.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
