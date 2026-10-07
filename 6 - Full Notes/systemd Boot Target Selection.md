2026-10-07 18:14

Status: #baby

Tags: [[SLES Boot and Recovery Administration]]

# systemd Boot Target Selection

After the kernel and early user space reach the real root filesystem, systemd activates the default target and its dependency graph. The target represents the intended operating state, while ordering and requirement relationships determine which services, mounts, sockets, and other units must participate.

A temporary boot target can be selected for diagnosis without permanently changing the normal default. This makes it possible to enter a reduced environment when the multi-user graph fails. [[SLES Rescue and Emergency Targets]] provide different levels of that reduced operation.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
