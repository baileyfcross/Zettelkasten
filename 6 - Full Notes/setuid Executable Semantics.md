2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]]

# setuid Executable Semantics

The setuid bit on an executable causes a launched process to receive the file owner's effective user identity in addition to the caller's identity. It supports narrowly designed programs that must perform a privileged operation for ordinary users without granting them a general privileged shell.

Because program inputs are now processed with the owner's authority, a defect can become a privilege-escalation path. Setuid should be limited to reviewed executables with controlled ownership and write access; setting the bit on a script or user-modifiable program is not a safe substitute for [[sudo Policy Delegation]].

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
