2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# User Namespace UID Mapping

User namespace UID mapping translates user and group identifiers seen inside a container into different identifiers on the host. A process can appear as UID 0 within its namespace while mapping to an unprivileged account or subordinate ID outside it.

This translation permits ownership checks and privileged-looking container operations without granting equivalent host authority. It also explains common mount failures: a host file owned by an unmapped ID may be inaccessible even when the process believes it is root. [[Subordinate UID and GID Range]] defines the additional host identities available for these mappings.

# References

[[podmanfordevopssecondedition.pdf]]
