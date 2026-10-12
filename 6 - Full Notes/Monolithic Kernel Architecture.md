2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Monolithic Kernel Architecture

Linux uses a monolithic kernel architecture in which core services, filesystems, networking, and most device drivers execute in one privileged address space. Direct in-kernel calls make subsystem interaction efficient, but a faulty component can corrupt shared kernel state.

The architecture is modular rather than immutable: a [[Loadable Kernel Module]] can add or remove kernel functionality at runtime. Modules still execute with kernel privilege, so modular loading changes deployment and extensibility rather than providing process-style fault isolation.

# References

[[linuxkernelprogramming_secondedition.pdf]]
