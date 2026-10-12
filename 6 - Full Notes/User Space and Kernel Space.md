2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# User Space and Kernel Space

User space is the restricted execution environment in which applications run, while kernel space is the privileged environment that manages hardware and system-wide resources. A controlled transition such as a system call, exception, or interrupt transfers execution into the kernel.

The separation protects the operating system from direct application access to privileged instructions and kernel memory. Kernel code must therefore validate user pointers and copy data through safe interfaces rather than treating user addresses as trusted kernel addresses.

# References

[[linuxkernelprogramming_secondedition.pdf]]
