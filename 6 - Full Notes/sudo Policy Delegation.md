2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]]

# sudo Policy Delegation

Sudo evaluates policy to decide whether a user may execute a specified command as another identity. A rule can constrain the invoking user or group, target identity, host, command, environment, and authentication behavior, allowing administrative capability to be delegated without distributing the root password.

Least privilege depends on the command boundary being meaningful. Permission to edit a root-executed script, choose an unrestricted argument, or launch a general shell may be equivalent to unrestricted root access. Sudoers changes should be validated with the appropriate syntax-aware tool and reviewed as security policy.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
