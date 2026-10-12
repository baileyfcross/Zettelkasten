2026-09-30 23:37

Status: #baby

Tags: [[Windows Remote Desktop Services]]

# Remote Desktop Gateway

Remote Desktop Gateway tunnels Remote Desktop Protocol through HTTPS so authorized users can reach internal RDS resources without exposing the ordinary RDP port directly to the internet or first establishing a broad VPN. The gateway terminates the external connection and applies policy before forwarding approved traffic toward internal targets.

Connection authorization policies decide who may connect and under which conditions, while resource authorization policies define which internal computers they may reach. A trusted public certificate and externally resolvable name are essential for client validation. The gateway is an internet-facing security boundary, so it requires patching, multifactor-capable authentication where available, logging, restricted policy, and redundancy. Allowing every approved user to reach every internal server would defeat the narrowing that the gateway is meant to provide.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
