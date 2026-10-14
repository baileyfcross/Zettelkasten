2026-09-30 23:37

Status: #baby

Tags: [[Windows File Services and High Availability]]

# Windows SMB File Share

A Windows SMB file share exposes a server folder through a Universal Naming Convention path such as `\\server\share`. Separating shared data from the operating-system volume simplifies capacity planning, recovery, and future server replacement. A share name ending in `$` is hidden from casual browsing but does not provide access control.

Stable service-oriented names and drive mappings can reduce user dependence on a particular server name. Availability, permissions, quotas, backups, and offline or remote access should be designed before data accumulates. Sharing a folder creates a network entry point; it does not replace NTFS security or automatically reorganize inherited permissions beneath the folder. A clear top-level structure is easier to administer than many overlapping shares cut into arbitrary subfolders.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
