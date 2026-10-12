2026-09-14 02:44

Status: #baby

Tags: [[Operating System Security and Access Control]] [[Linux Virtual Memory Internals]]

# Memory Protection

Memory protection prevents one process from reading or corrupting memory assigned to another process. It is necessary in multitasking and multiuser systems because several programs execute on the same hardware without being permitted to interfere.

The source identifies [[Process Isolation]], [[Hardware Memory Segmentation]], and [[Virtual Memory Protection]] as complementary mechanisms. Their combined boundary protects application behavior and the confidentiality, integrity, and availability of in-memory data.

Linux enforces the boundary through per-mapping read, write, execute, and user-access permissions encoded in [[Page Table|page tables]]. The [[User Space and Kernel Space|user/kernel privilege boundary]] prevents an application from directly using kernel mappings even though controlled system calls can operate on its behalf.

# References

[[cybersecurity.epub]]
[[linuxkernelprogramming_secondedition.pdf]]
