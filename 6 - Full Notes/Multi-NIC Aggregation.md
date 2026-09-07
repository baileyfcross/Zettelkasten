2026-09-06 22:42

Status: #baby

Tags: [[Data Center Storage Networking]]

# Multi-NIC Aggregation

Multi-NIC aggregation uses several network interface cards as one larger communication resource. Storage channels or requests can be distributed across interfaces to increase throughput and avoid a single-link bottleneck.

Effective aggregation must account for unequal paths, packet ordering, failure of one interface, CPU and NUMA placement, and how flows are balanced over time.

# References

[[bigdatamanagementandprocessing.pdf]]
