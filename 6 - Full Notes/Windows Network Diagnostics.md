2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Networking and Remote Access]]

# Windows Network Diagnostics

Windows network diagnosis works outward from local state. `ipconfig` reveals addresses, gateways, DNS servers, and lease information; `ping` tests basic reachability when ICMP is permitted; `tracert` exposes the routed path; and `nslookup` or `Resolve-DnsName` separates name-resolution failure from transport failure. `Test-NetConnection` can test a specific TCP port, while `netstat` and TCPView show listeners and active conversations.

No single result is conclusive. A failed ping can reflect firewall policy while the application port remains reachable, and a successful DNS answer can still point to the wrong server. Effective troubleshooting tests the local interface, same-subnet peer, gateway, remote address, DNS name, and required port in sequence. Recording the exact source, destination, protocol, and time makes packet flow and event data comparable rather than relying on the vague claim that the network is down.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
