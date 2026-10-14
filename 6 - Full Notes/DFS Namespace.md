2026-09-30 23:37

Status: #baby

Tags: [[Windows File Services and High Availability]]

# DFS Namespace

A DFS namespace presents shared folders through one logical path even when the targets reside on different file servers. A domain-based namespace can use a stable path tied to the directory namespace, letting administrators move or replace backend shares while preserving the location users and applications reference.

Folder targets can provide more than one destination for a namespace path, and referrals direct clients toward an appropriate target. The namespace itself does not keep target data synchronized; [[DFS Replication]] or another data mechanism must provide consistent copies where required. Administrators should design names around durable business functions, verify target permissions, and ensure namespace servers are redundant so the abstraction does not become a new point of failure.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
