2026-09-30 23:37

Status: #baby

Tags: [[Windows Remote Desktop Services]]

# FSLogix Profile Container

An FSLogix profile container stores a user's Windows profile in a virtual disk on shared storage and attaches that disk at sign-in. To Windows and applications, the attached content behaves like a local profile, while the user can receive the same environment on different Session Hosts. This is particularly useful for large or complex profiles and Microsoft 365 application data.

The profile follows the availability and performance of its file path. Share permissions, NTFS permissions, capacity, backup, antivirus treatment, and network latency must therefore support many concurrent mount and I/O operations. A profile disk should not be treated as the only copy of business data, and simultaneous-session behavior needs deliberate configuration. FSLogix improves profile consistency but cannot correct an overloaded Session Host or an application that is unsafe for multi-user execution.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
