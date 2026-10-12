2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Deployment and Administration]]

# PowerShell Remoting

PowerShell remoting executes commands or opens interactive sessions on another Windows computer through Windows Remote Management. It turns administration into an object-based remote workflow: commands run near the target resource, and structured results return to the operator for filtering, formatting, or further automation. One-to-one sessions aid investigation, while one-to-many invocation applies the same task across a server set.

Remoting is central to managing [[Windows Server Core]] and large fleets without repeated graphical logons. It should be enabled and authorized deliberately, with trusted authentication, firewall access, and administrative endpoints that match the network's security model. Scripts should distinguish connection failures from command failures and preserve enough output to identify which target produced each result.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
