2026-09-30 23:37

Status: #baby

Tags: [[Windows File Services and High Availability]]

# SMB over QUIC

SMB over QUIC carries Server Message Block traffic through an encrypted QUIC connection, commonly over UDP 443. It enables approved clients to reach file shares across an untrusted network without exposing traditional SMB ports or first creating a general-purpose VPN tunnel. Certificates authenticate the server and participate in protecting the transport.

The feature changes the path, not the file authorization model: share and NTFS permissions still determine access after the connection is established. Deployment must coordinate a supported server edition, client capability, DNS name, trusted certificate, firewall path, and certificate renewal. Because the entry point is internet-reachable, operators should restrict which shares and identities are usable, monitor connections, and preserve another administrative path if QUIC connectivity fails.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
