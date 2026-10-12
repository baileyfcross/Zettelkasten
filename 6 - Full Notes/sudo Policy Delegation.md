2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]] [[Shell Script Security and Reliability]]

# sudo Policy Delegation

Sudo evaluates policy to decide whether a user may execute a specified command as another identity. A rule can constrain the invoking user or group, target identity, host, command, environment, and authentication behavior, allowing administrative capability to be delegated without distributing the root password.

Least privilege depends on the command boundary being meaningful. Permission to edit a root-executed script, choose an unrestricted argument, or launch a general shell may be equivalent to unrestricted root access. Sudoers changes should be validated with the appropriate syntax-aware tool and reviewed as security policy.

For shell automation, the script itself becomes part of the delegated boundary. A sudo rule is unsafe if a less-trusted user can modify the script, influence its command search path, or control arguments that it reinterprets as code. Ownership, fixed command resolution, and narrow accepted inputs must support the policy expressed in sudoers.

# References

[[ultimatelinuxshellscriptingguide.pdf]]

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
