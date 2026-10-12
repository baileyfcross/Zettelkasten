2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Networking and Remote Access]]

# DirectAccess

DirectAccess gives domain-joined Windows clients automatic connectivity to internal resources without asking the user to start a conventional VPN session. It establishes machine-oriented connectivity that can also let administrators reach and manage a remote computer. The deployment depends on domain policy, certificates in stronger designs, DNS behavior, and an external entry point provided by Remote Access servers.

A Network Location Server helps a client decide whether it is already inside the corporate network; misidentifying that state can prevent the expected tunnel. DirectAccess is therefore tightly coupled to Active Directory and managed Windows clients. Always On VPN offers a newer and more flexible path for many deployments, but existing DirectAccess environments still require careful treatment of name resolution, IPv6 transition, certificates, load balancing, and client policy.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
