2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# Range Partitioning

Range partitioning divides an indexed source into contiguous intervals and assigns each interval as a unit of parallel work. It has little per-element coordination overhead and suits collections with known size and roughly uniform processing cost.

Fixed ranges can become imbalanced when some intervals contain more expensive elements. A worker that finishes early may sit idle while another completes a disproportionately heavy range, so uniform element counts do not guarantee uniform workloads.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
