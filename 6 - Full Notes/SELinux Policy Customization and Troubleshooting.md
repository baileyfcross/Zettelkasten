2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# SELinux Policy Customization and Troubleshooting

SELinux troubleshooting begins with the denied operation and its audit evidence, then compares process type, object type, requested permission, and expected service behavior. Common fixes include restoring a default label, defining a persistent file or port mapping with `semanage`, or enabling a policy boolean designed for the required behavior.

The goal is to represent legitimate access without granting unrelated authority. A generated allow rule based on one denial may conceal a wrong path or unsafe service design, and a temporary manual label can vanish during relabeling. Persistent customization should be documented, retested in enforcing mode, and limited to the intended resource.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
