2026-09-30 23:37

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Group Policy Scope and Processing Order

Group Policy normally processes from local policy through site, domain, and increasingly specific organizational units. Later applicable settings can override conflicting earlier ones, so the directory path of a user or computer is part of its effective configuration. Link order, enforced links, inheritance blocking, security filtering, and WMI conditions modify that basic sequence.

Loopback processing changes user-policy evaluation to follow the computer's location, which is useful for kiosks and Remote Desktop Session Hosts that must present a controlled environment regardless of the person signing in. Policy results should be verified on a representative target with tools such as `gpresult`, since the existence of a link does not prove it survived filtering or precedence. Design becomes clearer when broad baselines are linked high and exceptions are introduced deliberately lower in the hierarchy.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
