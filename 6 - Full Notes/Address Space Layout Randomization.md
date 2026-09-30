2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Address Space Layout Randomization

Address space layout randomization varies the virtual locations of user-space components such as executables, shared libraries, heap, mappings, and stacks between executions. The uncertainty makes attacks that depend on fixed code or data addresses less reliable.

ASLR is a mitigation rather than an isolation boundary, and its effectiveness depends on available entropy, position-independent code, and resistance to address disclosure. The related [[Kernel Address Space Layout Randomization]] applies the principle to privileged kernel regions.

# References

[[linuxkernelprogramming_secondedition.pdf]]
