2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# SELinux Security Context

An SELinux security context labels a process or object with identity, role, type, and sensitivity information used by mandatory access-control policy. In the targeted policy used for common services, type enforcement is especially important: a service process type may be allowed to access one file type and denied another even when Unix ownership and modes permit both.

Moving content into a service directory does not always give it the directory's expected label. Administrators should compare the current context with the policy default and use persistent labeling tools and `restorecon` rather than treating an arbitrary relabel or disabled enforcement as the solution.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
