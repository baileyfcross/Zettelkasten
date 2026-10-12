2026-09-30 23:37

Status: #baby

Tags: [[Windows File Services and High Availability]]

# Share and NTFS Permission Layers

Remote access to a Windows file passes through both share permissions and NTFS permissions. The effective result is constrained by both layers: permission granted at the share cannot overcome a denial or missing right on the file system, and restrictive share permissions can block an action that NTFS would otherwise allow.

A manageable pattern is to keep the share layer broad enough for intended users and express granular business access through NTFS groups. This avoids maintaining two competing fine-grained models, but it does not mean granting universal access without thought. Administrators should assign permissions to groups rather than individual users, test from the network path, and distinguish remote behavior from local access, which does not traverse the SMB share layer.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
