2026-09-30 23:37

Status: #baby

Tags: [[Windows File Services and High Availability]]

# Storage Spaces Direct

Storage Spaces Direct pools locally attached drives from several Windows Server cluster nodes into software-defined shared storage. The cluster combines capacity, creates resilient virtual disks or volumes, and can use fast devices as cache while keeping data available across drive or node failures. This supports hyper-converged designs in which the same nodes provide compute and storage.

Resilience is a property of the whole validated cluster, not of a single disk. Node count, drive type, network bandwidth, failure-domain awareness, and repair capacity determine how the pool behaves under loss. Administrators should use supported hardware and high-speed redundant networking, monitor health and remaining capacity, and maintain headroom for repair. Storage Spaces Direct is a Datacenter-class capability and should be selected as an architectural platform rather than added casually to unrelated servers.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
