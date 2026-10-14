2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Linux Capability

A Linux capability is one independently assignable unit of authority split from the traditional all-powerful root privilege. Capabilities govern actions such as changing file ownership, administering networks, or overriding selected permission checks and can be attached to processes or executables under the kernel's transition rules.

Container runtimes use this model to provide a bounded default privilege set rather than granting every root capability. Capabilities are still powerful and should be added only for a demonstrated operation; a namespace changes the scope in which some authority applies but does not make an unnecessary capability harmless.

# References

[[podmanfordevopssecondedition.pdf]]
