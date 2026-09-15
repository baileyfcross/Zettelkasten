2026-09-14 02:44

Status: #baby

Tags: [[Operating System Security and Access Control]]

# Hardware Memory Segmentation

Hardware memory segmentation maps processes to controlled memory regions and uses processor support to restrict which addresses an execution context may reach. This supplies a stronger enforcement layer than a convention implemented only by application code.

An attempted access outside the assigned segment can be trapped instead of silently modifying another process. Segmentation therefore reinforces [[Process Isolation]] within the host's [[Memory Protection]] system.

# References

[[cybersecurity.epub]]
