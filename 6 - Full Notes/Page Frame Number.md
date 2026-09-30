2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Page Frame Number

A page frame number identifies a page-sized unit of physical memory by dividing its physical address by the system page size. Linux uses PFNs to connect hardware addresses with the metadata structures that describe physical pages.

The inverse conversion combines a PFN with an offset to locate a byte in physical memory. Not every numerically possible PFN is necessarily backed by usable RAM, particularly on systems with holes or the [[Sparse Memory Model]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
