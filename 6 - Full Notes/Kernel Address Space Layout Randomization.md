2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Kernel Address Space Layout Randomization

Kernel address space layout randomization changes the virtual placement of the kernel image and selected kernel regions at boot. It raises the cost of exploits that require known privileged code or object addresses.

KASLR complements permission enforcement and other hardening but cannot compensate for an information leak that reveals the randomized layout. Its architecture and boot configuration determine which parts of the [[Kernel Virtual Address Space]] can be randomized and how much entropy is available.

# References

[[linuxkernelprogramming_secondedition.pdf]]
