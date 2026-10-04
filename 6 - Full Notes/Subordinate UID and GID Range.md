2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Subordinate UID and GID Range

A subordinate UID and GID range allocates extra host identifiers that an ordinary user may map into a user namespace. The `/etc/subuid` and `/etc/subgid` files associate these ranges with the account so rootless containers can represent many internal users without giving them matching privileged host identities.

The range must be present, large enough, and non-overlapping for reliable [[User Namespace UID Mapping]]. Changing it after containers have created storage can make existing file ownership appear incorrect, so identity allocation and migration are storage concerns as well as account configuration.

# References

[[podmanfordevopssecondedition.pdf]]
