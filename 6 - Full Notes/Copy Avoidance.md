2026-09-06 22:42

Status: #baby

Tags: [[Data Center Storage Networking]]

# Copy Avoidance

Copy avoidance designs an I/O path so data does not repeatedly move between application, protocol, and device buffers. Each eliminated copy saves memory bandwidth and CPU time and can reduce latency.

The technique often requires careful buffer ownership, lifetime management, alignment, and protection because shared or directly registered memory crosses subsystem boundaries.

# References

[[bigdatamanagementandprocessing.pdf]]
